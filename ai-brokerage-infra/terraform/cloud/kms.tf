resource "aws_kms_key" "storage" {
  description             = "CMK for AI brokerage at-rest encryption"
  deletion_window_in_days = 30
}
