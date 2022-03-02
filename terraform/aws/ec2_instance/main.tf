module "ec2_instance" {
  source  = "terraform-aws-modules/ec2-instance/aws"
  version = "~> 2.0"

  name           = var.name
  instance_count = var.instance_count

  ami                         = var.ami
  instance_type               = var.instance_type
  key_name                    = var.key_name
  monitoring                  = var.monitoring
  user_data                   = var.user_data
  vpc_security_group_ids      = var.security_group_ids
  ebs_optimized               = var.ebs_optimized
  subnet_id                   = var.subnet_id
  associate_public_ip_address = var.associate_public_ip_address
  iam_instance_profile        = var.iam_instance_profile
  disable_api_termination     = var.disable_api_termination

  tags = {
    Name = "bombardier"
  }
}
