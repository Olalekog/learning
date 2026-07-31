# Lambda module — the ingestion function triggered on new documents
# landing in the raw bucket; chunks, embeds (Bedrock), and dual-writes
# to OpenSearch and S3 Vectors (see ../../README.md §4). Execution role
# is injected from the iam module, not created here.

data "archive_file" "ingest" {
  type        = "zip"
  source_dir  = var.source_dir
  output_path = "${path.module}/build/ingest_embeddings.zip"
}

resource "aws_lambda_function" "ingest" {
  function_name    = "rag-ingest-${var.env}"
  role             = var.execution_role_arn
  handler          = "ingest_embeddings.handler"
  runtime          = "python3.12"
  timeout          = var.timeout
  memory_size      = var.memory_size
  filename         = data.archive_file.ingest.output_path
  source_code_hash = data.archive_file.ingest.output_base64sha256

  environment {
    variables = {
      OPENSEARCH_ENDPOINT = var.opensearch_collection_endpoint
      VECTORS_BUCKET      = var.vectors_bucket_name
      BEDROCK_EMBED_MODEL = var.bedrock_embed_model
    }
  }
}

resource "aws_lambda_permission" "allow_s3" {
  statement_id  = "AllowS3Invoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.ingest.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = var.raw_docs_bucket_arn
}

resource "aws_s3_bucket_notification" "raw_docs_trigger" {
  bucket = var.raw_docs_bucket_name
  lambda_function {
    lambda_function_arn = aws_lambda_function.ingest.arn
    events              = ["s3:ObjectCreated:*"]
  }
  depends_on = [aws_lambda_permission.allow_s3]
}
