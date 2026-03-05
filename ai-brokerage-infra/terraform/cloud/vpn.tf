resource "aws_vpn_gateway" "main" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "ai-brokerage-vpn-gw"
  }
}
