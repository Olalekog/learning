"""RAG ingestion Lambda: chunk source documents, generate embeddings via
Amazon Bedrock, and dual-write to Amazon OpenSearch (hot path) and S3
Vectors (cold/bulk path). See ../README.md for the full architecture.
"""

import hashlib
import json
import os

import boto3

bedrock = boto3.client("bedrock-runtime")
s3 = boto3.client("s3")

EMBED_MODEL = os.environ["BEDROCK_EMBED_MODEL"]
VECTORS_BUCKET = os.environ["VECTORS_BUCKET"]
OPENSEARCH_ENDPOINT = os.environ["OPENSEARCH_ENDPOINT"]


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """Token-approximate chunking with overlap so a fact near a chunk
    boundary is still retrievable from at least one chunk."""
    words = text.split()
    if not words:
        return []
    step = max(chunk_size - overlap, 1)
    return [" ".join(words[i : i + chunk_size]) for i in range(0, len(words), step)]


def embed(text: str) -> list[float]:
    response = bedrock.invoke_model(
        modelId=EMBED_MODEL,
        body=json.dumps({"inputText": text}),
    )
    return json.loads(response["body"].read())["embedding"]


def index_into_opensearch(record: dict) -> None:
    """Upsert a chunk + its embedding into the OpenSearch vector index.
    Client construction/auth (AWS SigV4 signing against the collection
    endpoint) is omitted here — see the OpenSearch Serverless Python
    client docs for the aoss-signed request setup.
    """
    raise NotImplementedError(
        "Wire up the OpenSearch Serverless client against "
        f"{OPENSEARCH_ENDPOINT} before deploying."
    )


def handler(event, context):
    chunks_processed = 0

    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]

        doc_text = s3.get_object(Bucket=bucket, Key=key)["Body"].read().decode("utf-8")
        chunks = chunk_text(doc_text)

        for idx, chunk in enumerate(chunks):
            chunk_id = hashlib.sha256(f"{key}:{idx}".encode()).hexdigest()
            vector = embed(chunk)
            record_body = {
                "chunk_id": chunk_id,
                "source_key": key,
                "chunk_index": idx,
                "text": chunk,
                "embedding": vector,
                "model": EMBED_MODEL,
            }

            # Hot path — real-time retrieval index
            index_into_opensearch(record_body)

            # Cold/bulk path — durable system of record, used to rebuild
            # the OpenSearch index after a model upgrade without
            # re-calling Bedrock on every source document again
            s3.put_object(
                Bucket=VECTORS_BUCKET,
                Key=f"{key}/chunks/{chunk_id}.json",
                Body=json.dumps(record_body),
            )
            chunks_processed += 1

    return {"statusCode": 200, "chunksProcessed": chunks_processed}
