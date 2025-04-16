resource "kubernetes_deployment_v1" "serverless_app_template_deployment" {
  timeouts {
    create = "3m"
    update = "3m"
    delete = "3m"
  }
  metadata {
    name      = "serverless-app-template"
    namespace = "templates"
    labels = {
      app = "serverless-app-template"
    }
  }

  spec {
    revision_history_limit = 5
    selector {
      match_labels = {
        app = "serverless-app-template"
      }
    }

    template {
      metadata {
        name = "serverless-app-template"
        labels = {
          app = "serverless-app-template"
        }
      }
      spec {
        init_container {
          name    = "init-aws-lambda-rie"
          image   = "busybox:latest"
          command = ["sh", "-c", "mkdir -p /aws-lambda && wget -O /aws-lambda/aws-lambda-rie https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie && chmod +x /aws-lambda/aws-lambda-rie"]

          volume_mount {
            name       = "aws-lambda-rie"
            mount_path = "/aws-lambda"
          }
        }
        container {
          name              = "serverless-app-template"
          image             = "luisllanos/serverless-app-template:lambda"
          image_pull_policy = "Always"

          command = ["/aws-lambda/aws-lambda-rie"]
          args    = ["/usr/local/bin/python3", "-m", "awslambdaric", "app.function_handler"]

          volume_mount {
            name       = "aws-lambda-rie"
            mount_path = "/aws-lambda"
          }
          env_from {
            config_map_ref {
              name     = "serverless-app-template"
              optional = false
            }
          }
          resources {
            requests = {
              memory = "512Mi"
            }
          }
          port {
            container_port = 9001
          }
        }
        volume {
          name = "aws-lambda-rie"
          empty_dir {}
        }
      }
    }
  }
}