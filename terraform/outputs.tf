output "vpc_id" {
  description = "The ID of the VPC"
  value       = aws_vpc.mlx_vpc.id
}

output "public_subnet_ids" {
  description = "List of public subnet IDs"
  # Assuming subnets are built out in main.tf
  value       = [] 
}
