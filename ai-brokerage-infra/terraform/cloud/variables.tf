variable "aws_region" {
  type        = string
  description = "AWS region for cloud resources"
  default     = "us-east-1"
}

variable "vpc_cidr" {
  type        = string
  description = "Primary VPC CIDR"
  default     = "10.40.0.0/16"
}
