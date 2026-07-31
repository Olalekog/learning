# OpenSearch module — the "hot path" real-time k-NN vector index (see
# ../../README.md for why this is paired with, not replaced by, S3
# Vectors). Encryption key is injected from the kms module.

resource "aws_opensearchserverless_collection" "vector_store" {
  name = "rag-vector-store-${var.env}"
  type = "VECTORSEARCH"

  depends_on = [
    aws_opensearchserverless_security_policy.encryption,
    aws_opensearchserverless_security_policy.network,
  ]
}

resource "aws_opensearchserverless_security_policy" "encryption" {
  name = "rag-vs-encryption-${var.env}"
  type = "encryption"
  policy = jsonencode({
    Rules = [{
      ResourceType = "collection"
      Resource     = ["collection/rag-vector-store-${var.env}"]
    }]
    AWSOwnedKey = false
    KmsARN      = var.kms_key_arn
  })
}

resource "aws_opensearchserverless_security_policy" "network" {
  name = "rag-vs-network-${var.env}"
  type = "network"
  policy = jsonencode([
    {
      Rules = [{
        ResourceType = "collection"
        Resource     = ["collection/rag-vector-store-${var.env}"]
      }]
      AllowFromPublic = false
    }
  ])
}
