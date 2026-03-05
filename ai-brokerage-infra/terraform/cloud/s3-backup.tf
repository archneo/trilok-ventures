resource "aws_s3_bucket" "backup" {
  bucket = "${replace(terraform.workspace, "_", "-")}-ai-brokerage-backup"
}

resource "aws_s3_bucket_versioning" "backup" {
  bucket = aws_s3_bucket.backup.id
  versioning_configuration {
    status = "Enabled"
  }
}
