# prod environment — HA re-ranker endpoint (2 instances), longer KMS
# deletion window, production-sized Lambda. See ../../../README.md §9.

locals {
  env = "prod"
}

module "kms" {
  source                  = "../../modules/kms"
  env                     = local.env
  deletion_window_in_days = 30
}

module "s3" {
  source      = "../../modules/s3"
  env         = local.env
  kms_key_arn = module.kms.key_arn
}

module "opensearch" {
  source      = "../../modules/opensearch"
  env         = local.env
  kms_key_arn = module.kms.key_arn
}

module "iam" {
  source = "../../modules/iam"
  env    = local.env

  raw_docs_bucket_arn       = module.s3.raw_docs_bucket_arn
  vectors_bucket_arn        = module.s3.vectors_bucket_arn
  opensearch_collection_arn = module.opensearch.collection_arn
  bedrock_embed_model       = var.bedrock_embed_model
}

module "sagemaker" {
  source = "../../modules/sagemaker"
  env    = local.env

  execution_role_arn             = module.iam.sagemaker_execution_role_arn
  reranker_image_uri             = var.reranker_image_uri
  reranker_model_artifact_s3_uri = var.reranker_model_artifact_s3_uri

  # prod: 2 instances behind the endpoint for HA — a single-instance
  # endpoint has no failover if that instance is unhealthy
  instance_type  = "ml.g5.xlarge"
  instance_count = 2
}

module "lambda" {
  source     = "../../modules/lambda"
  env        = local.env
  source_dir = "${path.module}/../../../src"

  execution_role_arn   = module.iam.lambda_execution_role_arn
  raw_docs_bucket_name = module.s3.raw_docs_bucket_name
  raw_docs_bucket_arn  = module.s3.raw_docs_bucket_arn
  vectors_bucket_name  = module.s3.vectors_bucket_name

  opensearch_collection_endpoint = module.opensearch.collection_endpoint
  bedrock_embed_model            = var.bedrock_embed_model

  memory_size = 1024
  timeout     = 120
}
