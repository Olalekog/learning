variable "env" {
  description = "Deployment environment (dev, uat, prod)"
  type        = string
  validation {
    condition     = contains(["dev", "uat", "prod"], var.env)
    error_message = "env must be one of: dev, uat, prod."
  }
}

variable "source_dir" {
  description = "Path to the Lambda source directory (../src)"
  type        = string
}

variable "execution_role_arn" {
  description = "Lambda execution role ARN (from the iam module)"
  type        = string
}

variable "raw_docs_bucket_name" {
  type = string
}

variable "raw_docs_bucket_arn" {
  type = string
}

variable "vectors_bucket_name" {
  type = string
}

variable "opensearch_collection_endpoint" {
  type = string
}

variable "bedrock_embed_model" {
  description = "Bedrock embedding model ID used at ingestion time"
  type        = string
}

variable "memory_size" {
  description = "Lambda memory allocation (MB) — tune down in dev, up in prod for larger documents"
  type        = number
  default     = 1024
}

variable "timeout" {
  description = "Lambda timeout (seconds)"
  type        = number
  default     = 120
}
