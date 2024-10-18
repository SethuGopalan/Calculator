variable "aws_key_pair" {
  default = "C:/Users/Sethu/.aws/Ec2-key.pem"

}

locals {

  is_file_path_correct = fileexists(var.aws_key_pair)
}

output "file_path_exists" {

  value = local.is_file_path_correct

}
