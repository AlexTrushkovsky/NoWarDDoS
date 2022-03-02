output private_ip {
  value = module.ec2_instance.private_ip
}

output private_dns {
  value = module.ec2_instance.private_dns
}

output public_dns {
  value = module.ec2_instance.public_dns
}

output id {
  value = module.ec2_instance.id
}

output availability_zone {
  value = module.ec2_instance.availability_zone
}
