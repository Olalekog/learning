output "raw_docs_bucket_name" {
  value = aws_s3_bucket.raw_docs.bucket
}

output "raw_docs_bucket_arn" {
  value = aws_s3_bucket.raw_docs.arn
}

output "vectors_bucket_name" {
  value = aws_s3_bucket.vectors.bucket
}

output "vectors_bucket_arn" {
  value = aws_s3_bucket.vectors.arn
}
