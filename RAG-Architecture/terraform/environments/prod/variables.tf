variable "reranker_image_uri" {
  description = "ECR image URI for the custom SageMaker re-ranker container"
  type        = string
}

variable "reranker_model_artifact_s3_uri" {
  description = "S3 URI of the trained re-ranker model artifact (model.tar.gz)"
  type        = string
}

variable "bedrock_embed_model" {
  description = "Bedrock embedding model ID used at ingestion time"
  type        = string
  default     = "amazon.titan-embed-text-v2:0"
}
