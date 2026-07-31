variable "env" {
  description = "Deployment environment (dev, uat, prod)"
  type        = string
  validation {
    condition     = contains(["dev", "uat", "prod"], var.env)
    error_message = "env must be one of: dev, uat, prod."
  }
}

variable "execution_role_arn" {
  description = "SageMaker execution role ARN (from the iam module)"
  type        = string
}

variable "reranker_image_uri" {
  description = "ECR image URI for the custom SageMaker re-ranker container"
  type        = string
}

variable "reranker_model_artifact_s3_uri" {
  description = "S3 URI of the trained re-ranker model artifact (model.tar.gz)"
  type        = string
}

variable "instance_type" {
  description = "Instance type backing the real-time inference endpoint"
  type        = string
  default     = "ml.g5.xlarge"
}

variable "instance_count" {
  description = "Number of instances behind the endpoint"
  type        = number
  default     = 1
}
