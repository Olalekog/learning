# KMS module — the single customer-managed key used to encrypt every
# other service's data at rest (S3 buckets, OpenSearch collection).

resource "aws_kms_key" "rag" {
  description             = "KMS key for RAG platform data at rest (${var.env})"
  deletion_window_in_days = var.deletion_window_in_days
}

resource "aws_kms_alias" "rag" {
  name          = "alias/rag-${var.env}"
  target_key_id = aws_kms_key.rag.key_id
}
