provider "aws" {
  region = var.aws_region
}

# code
data "aws_ami" "ami_ecs" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-ecs-hvm-2.0*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "architecture"
    values = ["x86_64"]
  }

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }
}

data "template_file" "user_data" {
  template = file("${path.module}/files/user_data.sh")
}

resource "aws_security_group" "security_group" {
  name   = "NoWarDDoS"
  vpc_id = var.vpc_id

  ingress {
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "NoWarDDoS"
  }

}


module "ec2_instance" {
  source = "./ec2_instance"

  env                = "NoWarDDoS"
  name               = "NoWarDDoS"
  instance_count     = var.instance_count
  ami                = data.aws_ami.ami_ecs.id
  instance_type      = var.instance_type
  key_name           = var.key_name
  monitoring         = "false"
  user_data          = data.template_file.user_data.rendered
  security_group_ids = [aws_security_group.security_group.id]
  subnet_id          = var.subnet_id
}
