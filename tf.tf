resource "aws_instance" "example_resource" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
  subnet_id     = "subnet-abcdef"
}

resource "aws_s3_bucket" "another_resource" {
  bucket_name = "example-bucket"
  acl         = "private"
}
