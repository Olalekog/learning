terraform {
  required_version = ">= 1.5"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.4"
    }
  }

  # Separate state per environment — dev's state can never be confused
  # with or accidentally overwritten by uat/prod. See ../../../README.md
  # §9 and ../../../../Terraform/Terraform.md §8 for the S3+DynamoDB
  # backend pattern this points at.
  backend "s3" {
    bucket         = "rag-architecture-tfstate"
    key            = "rag-architecture/dev/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "rag-architecture-tf-locks"
    encrypt        = true
  }
}

provider "aws" {
  region = "us-east-1"
}
