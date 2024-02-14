FROM --platform=$BUILDPLATFORM python:3.12-alpine AS builder

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

# CMD ["python", "run.py"]
CMD ["flask", "--app", "app", "run", "-h", "0.0.0.0", "-p", "5000"]
