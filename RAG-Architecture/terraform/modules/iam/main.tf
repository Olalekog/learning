# IAM module — every role/policy in the platform lives here, scoped to
# exactly what each consuming module (lambda, sagemaker) needs. Roles are
# created and exported from this module; the resources that assume them
# (the Lambda function, the SageMaker model) live in their own modules
# and receive the role ARN as an input.

# --- Lambda execution role (least-privilege: embed, index, dual-write) ---

data "aws_iam_policy_document" "lambda_assume" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "ingest_lambda" {
  name               = "rag-ingest-lambda-role-${var.env}"
  assume_role_policy = data.aws_iam_policy_document.lambda_assume.json
}

resource "aws_iam_role_policy" "ingest_permissions" {
  name = "rag-ingest-permissions"
  role = aws_iam_role.ingest_lambda.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = ["bedrock:InvokeModel"]
        Resource = "arn:aws:bedrock:*::foundation-model/${var.bedrock_embed_model}"
      },
      {
        Effect   = "Allow"
        Action   = ["aoss:APIAccessAll"]
        Resource = var.opensearch_collection_arn
      },
      {
        Effect = "Allow"
        Action = ["s3:PutObject", "s3:GetObject"]
        Resource = [
          "${var.vectors_bucket_arn}/*",
          "${var.raw_docs_bucket_arn}/*",
        ]
      },
      {
        Effect   = "Allow"
        Action   = ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"]
        Resource = "arn:aws:logs:*:*:*"
      }
    ]
  })
}

# --- SageMaker execution role (model artifact + inference) ---

data "aws_iam_policy_document" "sagemaker_assume" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["sagemaker.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "sagemaker_exec" {
  name               = "rag-sagemaker-exec-${var.env}"
  assume_role_policy = data.aws_iam_policy_document.sagemaker_assume.json
}

resource "aws_iam_role_policy_attachment" "sagemaker_exec_s3" {
  role       = aws_iam_role.sagemaker_exec.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSageMakerFullAccess"
}
