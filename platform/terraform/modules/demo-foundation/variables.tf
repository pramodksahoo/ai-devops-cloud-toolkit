variable "namespace" {
  type        = string
  description = "Namespace for the demo foundation resources."
  default     = "demo-toolkit"
}

variable "service_account_name" {
  type        = string
  description = "Service account used by the demo workload."
  default     = "toolkit-demo"
}
