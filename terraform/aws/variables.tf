# variables
variable "aws_region" {
  default = "eu-central-1"
}

variable "instance_type" {
  default = "c5.large"
}

variable "key_name" {
  default = "qwerty"
}

variable "subnet_id" {
  description = "SHOULD BE PUBLIC !!!"
  #default     = ""
}

variable "vpc_id" {
  description = "vpc_id"
  #default     = ""
}

variable "instance_count" {
  description = "numbder of instances"
  #default     = "10"
}
