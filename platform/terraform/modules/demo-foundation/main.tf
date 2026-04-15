resource "kubernetes_namespace" "demo" {
  metadata {
    name = var.namespace
    labels = {
      "app.kubernetes.io/part-of" = "ai-devops-cloud-toolkit"
      "toolkit.layer"             = "foundation"
    }
  }
}

resource "kubernetes_service_account" "demo" {
  metadata {
    name      = var.service_account_name
    namespace = kubernetes_namespace.demo.metadata[0].name
    labels = {
      "app.kubernetes.io/name" = var.service_account_name
    }
  }
}

resource "kubernetes_role" "demo_read_only" {
  metadata {
    name      = "demo-read-only"
    namespace = kubernetes_namespace.demo.metadata[0].name
  }

  rule {
    api_groups = [""]
    resources  = ["pods", "services", "configmaps"]
    verbs      = ["get", "list", "watch"]
  }

  rule {
    api_groups = ["apps"]
    resources  = ["deployments", "replicasets"]
    verbs      = ["get", "list", "watch"]
  }
}

resource "kubernetes_role_binding" "demo_read_only" {
  metadata {
    name      = "demo-read-only"
    namespace = kubernetes_namespace.demo.metadata[0].name
  }

  role_ref {
    api_group = "rbac.authorization.k8s.io"
    kind      = "Role"
    name      = kubernetes_role.demo_read_only.metadata[0].name
  }

  subject {
    kind      = "ServiceAccount"
    name      = kubernetes_service_account.demo.metadata[0].name
    namespace = kubernetes_namespace.demo.metadata[0].name
  }
}
