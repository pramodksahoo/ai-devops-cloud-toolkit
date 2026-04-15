terraform {
  required_version = ">= 1.6.0"

  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.29"
    }
  }
}

provider "kubernetes" {
  config_path    = var.kubeconfig_path
  config_context = var.cluster_context
}

module "demo_foundation" {
  source               = "../../modules/demo-foundation"
  namespace            = var.namespace
  service_account_name = var.service_account_name
}
