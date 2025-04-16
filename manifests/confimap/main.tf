resource "kubernetes_config_map_v1" "serverless_app_template_config_map" {
  metadata {
    namespace = "templates"
    name      = "serverless-app-template"
  }

  data = {
    TOKEN_SECRET = "${var.env_vars.TOKEN_SECRET}"
    CLOUD_ACCESS = <<EOT
    {
      "AWS_REGION": "${var.env_vars.AWS_REGION}",
      "AWS_ACCESS_KEY_ID": "${var.env_vars.AWS_ACCESS_KEY_ID}",
      "AWS_SECRET_KEY_ID": "${var.env_vars.AWS_SECRET_KEY_ID}"
    }
    EOT
  }
}