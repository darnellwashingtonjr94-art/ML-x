terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  # backend "s3" {} # Uncomment to store state remotely
}

provider "aws" {
  region = var.aws_region
}

# Base Network Infrastructure
resource "aws_vpc" "mlx_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "mlx-production-vpc"
  }
}
