# SageMaker module — hosts the custom re-ranker (or a custom fine-tuned
# embedding model) for the cases a managed Bedrock foundation model
# doesn't fit (see ../../README.md §6). Execution role is injected from
# the iam module, not created here.

resource "aws_sagemaker_model" "custom_reranker" {
  name               = "rag-custom-reranker-${var.env}"
  execution_role_arn = var.execution_role_arn

  primary_container {
    image          = var.reranker_image_uri
    model_data_url = var.reranker_model_artifact_s3_uri
  }
}

resource "aws_sagemaker_endpoint_configuration" "reranker" {
  name = "rag-reranker-config-${var.env}"
  production_variants {
    variant_name           = "primary"
    model_name             = aws_sagemaker_model.custom_reranker.name
    initial_instance_count = var.instance_count
    instance_type          = var.instance_type
  }
}

resource "aws_sagemaker_endpoint" "reranker" {
  name                 = "rag-reranker-${var.env}"
  endpoint_config_name = aws_sagemaker_endpoint_configuration.reranker.name
}
