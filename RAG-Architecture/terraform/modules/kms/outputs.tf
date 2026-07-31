output "key_arn" {
  value = aws_kms_key.rag.arn
}

output "key_id" {
  value = aws_kms_key.rag.key_id
}
