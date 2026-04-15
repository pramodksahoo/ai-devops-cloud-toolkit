variable "kubeconfig_path" {
  type        = string
  description = "Path to kubeconfig used for the local kind cluster."
  default     = "~/.kube/config"
}

variable "cluster_context" {
  type        = string
  description = "Kubernetes context for the local kind cluster."
  default     = "kind-toolkit-demo"
}

variable "namespace" {
  type        = string
  description = "Namespace used by the demo workload."
  default     = "demo-toolkit"
}

variable "service_account_name" {
  type        = string
  description = "Service account used by the demo workload."
  default     = "toolkit-demo"
}
