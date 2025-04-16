# Serverless App Template
## Contact
[![Linkedin](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/luis-alfonso-llanos-a64639206/) [![Github](https://img.shields.io/badge/-Github-000?style=flat&logo=Github&logoColor=white)](https://github.com/luisLlanos23)
## Description:
This template provides a foundational structure for building serverless applications using AWS Lambda or background tasks. It includes utilities for secure token handling, cryptographic operations, and environment-based configurations. Designed for scalability and maintainability, this template simplifies the development of serverless workflows and task-based processing.

### Variable configuration
Create .env into application folder file copying the following template:
```
CLOUD_ACCESS={}
TOKEN_SECRET=
```
__Note:__
  - __CLOUD_ACCESS__ When deploying on AWS, you only need to fill in the region. This variable includes the local usage of this resource through the following fields:
    - __AWS_REGION:__ A llows you to access AWS services that are in a specific geographic location
      - __us-east-1__
      - __us-east-2__
      - __us-west-1__
      - __us-west-2__
    - __AWS_ACCESS_KEY_ID:__ Access key used with the AWS SDK to connect to AWS services.
    - __AWS_SECRET_KEY_ID:__ AWS secret access key

    __Example:__ CLOUD_ACCESS={ "AWS_REGION": "us-east-2", "AWS_ACCESS_KEY_ID": "xxxxxxxxxxxx", "AWS_SECRET_KEY_ID": "xxxxxxxxxxxx" }
  - __TOKEN_SECRET:__ key to decrypt and validate access token.
## 📌 Languages and Tools

<img width="15%" src="https://www.vectorlogo.zone/logos/python/python-ar21.svg"><img width="15%" src="https://www.vectorlogo.zone/logos/amazon_aws/amazon_aws-ar21.svg"><img width="15%" src="https://www.vectorlogo.zone/logos/serverless/serverless-ar21.svg"><img width="15%" src="https://www.vectorlogo.zone/logos/terraformio/terraformio-ar21.svg"><img width="15%" src="https://www.vectorlogo.zone/logos/kubernetes/kubernetes-ar21.svg"><img width="15%" src="https://www.vectorlogo.zone/logos/docker/docker-ar21.svg">

