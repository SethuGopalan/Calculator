terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  profile = "terraform"
  region  = "us-east-1"


}
# Get the default VPC
resource "aws_default_vpc" "default" {

}
data "aws_subnet_ids" "default_subnets" {


  vpc_id = aws_default_vpc.default.id


}
resource "aws_security_group" "EC2_Docker_SG" {

  name = "EC2_Docker_SG"
  # vpc_id = "vpc-77b8c011"
  vpc_id = aws_default_vpc.default.id
  # where you wnat to allow trafic from
  # http
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]

  }
  # ssh
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]

  }

  # what kind of things you can do it from this hhtp server
  egress {

    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]

  }

  tags = {
    name = "EC2_Docker_SG"
  }



}
data "aws_ami" "aws_linux" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}


# Find the latest Amazon Linux 2 AMI
# data "aws_ami" "aws_linux" {
#   most_recent = true
#   owners      = ["amazon"]

#   filter {
#     name   = "name"
#     values = ["amzn2-ami-hvm-*-x86_64-gp2"]
#   }
# }
resource "aws_instance" "EC2_Docker_SG" {
  # ami                    = "ami-03a6eaae9938c858c"
  ami                    = data.aws_ami.aws_linux.id
  key_name               = "default-ec2"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.EC2_Docker_SG.id]
  subnet_id              = tolist(data.aws_subnet_ids.default_subnets.ids)[0]

  provisioner "remote-exec" {
    connection {
      type        = "ssh"
      host        = self.public_ip
      user        = "ec2-user"
      private_key = file(var.aws_key_pair)
    }

    inline = [
      "sudo yum update -y",                         # Update the package list
      "sudo amazon-linux-extras install docker -y", # Install Docker on Amazon Linux
      "sudo systemctl start docker",                # Start Docker service
      "sudo systemctl enable docker",               # Enable Docker service at boot
      "sudo usermod -aG docker ec2-user"            # Add ec2-user to Docker group
    ]
  }

  tags = {
    Name = "EC2 Docker Instance"
  }
}
