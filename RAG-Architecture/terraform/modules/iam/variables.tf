variable "env" {
  description = "Deployment environment (dev, uat, prod)"
  type        = string
  validation {
    condition     = contains(["dev", "uat", "prod"], var.env)
    error_message = "env must be one of: dev, uat, prod."
  }
}

variable "raw_docs_bucket_arn" {
  description = "ARN of the raw documents bucket (from the s3 module)"
  type        = string
}

variable "vectors_bucket_arn" {
  description = "ARN of the S3 Vectors bucket (from the s3 module)"
  type        = string
}

variable "opensearch_collection_arn" {
  description = "ARN of the OpenSearch Serverless collection (from the opensearch module)"
  type        = string
}

variable "bedrock_embed_model" {
  description = "Bedrock embedding model ID the ingestion role is scoped to invoke"
  type        = string
}
