variable "env" {
  description = "Deployment environment (dev, uat, prod)"
  type        = string
  validation {
    condition     = contains(["dev", "uat", "prod"], var.env)
    error_message = "env must be one of: dev, uat, prod."
  }
}

variable "deletion_window_in_days" {
  description = "KMS key deletion window — shorter in dev for faster teardown, longer in prod"
  type        = number
  default     = 30
}
