variable "env" {
  description = "env name"
}

variable "security_group_ids" {
  description = "security group ids for resource"
}

variable "name" {
  description = "name for ec2 instance"
}

variable "instance_count" {
  description = "numbder of instances"
  default     = "1"
}

variable "ami" {
  description = "ami for ec2 instance"
}

variable "ebs_optimized" {
  default = false
}

variable "instance_type" {
  description = "instance type"
}

variable "key_name" {
  description = "ssh key pair, should already exist in aws"
}

variable "monitoring" {
  description = "true/false to enable/disable monitoring"
  default     = false
}

variable "user_data" {
  description = "userdata script"
  default     = "null"
}

variable "subnet_id" {
  description = "subnet id"
}

variable "associate_public_ip_address" {
  description = "If true, the EC2 instance will have associated public IP address"
  default     = true
}

variable "iam_instance_profile" {
  description = ""
  default     = ""
}

variable "disable_api_termination" {
  description = "if true, enables ec2 instance termination protection"
  default     = "false"
}
