# S3 module — raw document landing bucket and the S3 Vectors bulk/cold
# storage bucket. Encryption key is injected from the kms module, not
# created here, so this module owns storage only.

resource "aws_s3_bucket" "raw_docs" {
  bucket = "rag-raw-docs-${var.env}"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "raw_docs" {
  bucket = aws_s3_bucket.raw_docs.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = var.kms_key_arn
    }
  }
}

resource "aws_s3_bucket" "vectors" {
  bucket = "rag-s3-vectors-${var.env}"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "vectors" {
  bucket = aws_s3_bucket.vectors.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = var.kms_key_arn
    }
  }
}
