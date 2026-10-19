# 1. Escolhemos onde criar (AWS)
  provider "aws" {
    region = "us-east-1"
  }

  # 2. Pedimos um servidor (Instância EC2)
  resource "aws_instance" "meu_servidor" {
    ami           = "ami-0c7217cdde317cfec" # Sistema operacional (Linux)
    instance_type = "t2.micro"              # Tamanho do computador
  }