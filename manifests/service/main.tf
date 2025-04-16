resource "kubernetes_service_v1" "function_ifc_element_extractor_service" {
  metadata {
    name      = "serverless-app-template"
    namespace = "templates"
  }
  spec {
    selector = {
      app = "serverless-app-template"
    }
    type             = "NodePort"
    session_affinity = "None"
    session_affinity_config {
      client_ip {
        timeout_seconds = 10800
      }
    }
    port {
      port      = 8080
      node_port = 30050
      protocol  = "TCP"
    }
  }
}