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

  backend "s3" {
    bucket         = "rag-architecture-tfstate"
    key            = "rag-architecture/prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "rag-architecture-tf-locks"
    encrypt        = true
  }
}

provider "aws" {
  region = "us-east-1"
}
