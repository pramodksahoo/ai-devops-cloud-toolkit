output "namespace" {
  description = "Demo namespace name."
  value       = kubernetes_namespace.demo.metadata[0].name
}

output "service_account_name" {
  description = "Demo service account name."
  value       = kubernetes_service_account.demo.metadata[0].name
}
