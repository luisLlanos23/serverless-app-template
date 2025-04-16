FROM python:3.10.16-bookworm AS base
RUN apt-get -y update
RUN apt-get -y upgrade
RUN pip install --upgrade pip
RUN pip install python-dotenv

FROM python:3.10.16-bookworm AS lambda
COPY --from=base . .
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN mv app.lambda.py app.py
ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD ["app.function_handler"]

FROM python:3.10.16-bookworm AS task
COPY --from=base . .
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.task.py"]