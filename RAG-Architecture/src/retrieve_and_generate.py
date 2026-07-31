"""RAG query-time Lambda: embed the question, retrieve candidate chunks
from Amazon OpenSearch, optionally re-rank via a custom SageMaker
endpoint, then generate the grounded answer via Amazon Bedrock. See
../README.md for the full architecture and sequence diagram.
"""

import json
import os

import boto3

bedrock = boto3.client("bedrock-runtime")
sagemaker_runtime = boto3.client("sagemaker-runtime")

EMBED_MODEL = os.environ["BEDROCK_EMBED_MODEL"]
GEN_MODEL = os.environ["BEDROCK_GEN_MODEL"]
RERANKER_ENDPOINT = os.environ.get("SAGEMAKER_RERANKER_ENDPOINT")


def embed(text: str) -> list[float]:
    response = bedrock.invoke_model(
        modelId=EMBED_MODEL,
        body=json.dumps({"inputText": text}),
    )
    return json.loads(response["body"].read())["embedding"]


def search_opensearch(query_vector: list[float], top_k: int = 20) -> list[dict]:
    """k-NN similarity search against the vector index. Client
    construction/auth omitted here — see ingest_embeddings.py's
    index_into_opensearch docstring for the same note.
    """
    raise NotImplementedError("Wire up the OpenSearch Serverless client before deploying.")


def rerank(question: str, candidates: list[dict], top_k: int = 5) -> list[dict]:
    """Cross-encoder re-ranking on a small candidate set is far more
    precise than raw vector similarity alone — used only for the
    narrowed top-N from search_opensearch, not the whole corpus."""
    if not RERANKER_ENDPOINT:
        return candidates[:top_k]

    payload = {"question": question, "candidates": [c["text"] for c in candidates]}
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=RERANKER_ENDPOINT,
        ContentType="application/json",
        Body=json.dumps(payload),
    )
    scores = json.loads(response["Body"].read())["scores"]
    ranked = sorted(zip(candidates, scores), key=lambda pair: pair[1], reverse=True)
    return [chunk for chunk, _ in ranked[:top_k]]


def generate(question: str, context_chunks: list[dict]) -> str:
    context = "\n\n".join(c["text"] for c in context_chunks)
    prompt = (
        "Answer the question using only the context below. "
        "Cite the source_key for each fact you use. If the context "
        "doesn't contain the answer, say so explicitly rather than "
        "guessing.\n\n"
        f"Context:\n{context}\n\nQuestion: {question}"
    )
    response = bedrock.invoke_model(
        modelId=GEN_MODEL,
        body=json.dumps({"prompt": prompt, "max_tokens": 512}),
    )
    return json.loads(response["body"].read())["completion"]


def handler(event, context):
    question = json.loads(event["body"])["question"]

    query_vector = embed(question)
    candidates = search_opensearch(query_vector, top_k=20)
    top_chunks = rerank(question, candidates, top_k=5)
    answer = generate(question, top_chunks)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "answer": answer,
                "citations": [c["source_key"] for c in top_chunks],
            }
        ),
    }
