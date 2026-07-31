variable "env" {
  description = "Deployment environment (dev, uat, prod)"
  type        = string
  validation {
    condition     = contains(["dev", "uat", "prod"], var.env)
    error_message = "env must be one of: dev, uat, prod."
  }
}

variable "kms_key_arn" {
  description = "KMS key ARN used to encrypt both buckets at rest"
  type        = string
}
