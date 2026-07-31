output "lambda_execution_role_arn" {
  value = aws_iam_role.ingest_lambda.arn
}

output "sagemaker_execution_role_arn" {
  value = aws_iam_role.sagemaker_exec.arn
}
