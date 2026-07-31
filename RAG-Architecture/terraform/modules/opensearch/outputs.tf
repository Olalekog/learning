output "collection_arn" {
  value = aws_opensearchserverless_collection.vector_store.arn
}

output "collection_endpoint" {
  value = aws_opensearchserverless_collection.vector_store.collection_endpoint
}

output "collection_name" {
  value = aws_opensearchserverless_collection.vector_store.name
}
