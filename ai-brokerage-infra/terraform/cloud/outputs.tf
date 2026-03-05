output "vpc_id" {
  description = "Provisioned VPC ID"
  value       = aws_vpc.main.id
}
