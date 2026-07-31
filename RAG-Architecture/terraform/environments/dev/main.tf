# dev environment — sized for fast iteration, not load or HA. Calls the
# same six shared modules used by uat/prod (../../modules/*); only the
# sizing/tuning inputs differ per environment. See ../../../README.md §9.

locals {
  env = "dev"
}

module "kms" {
  source                  = "../../modules/kms"
  env                     = local.env
  deletion_window_in_days = 7 # short — dev keys get recreated often
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

  # dev: cheapest instance, single copy — no HA requirement
  instance_type  = "ml.m5.large"
  instance_count = 1
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

  # dev: smaller memory/timeout — dev document set is small
  memory_size = 512
  timeout     = 60
}
