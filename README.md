# Technologies
* Python 3.8
* uvicorn 0.13.3 as lightning-fast ASGI server implementation
* Gunicorn 20.0.4 as workers
* Starlette 0.14.2 as lightweight ASGI framework/toolkit

# Run
1. To create docker image
```shell
sudo docker build -t hypercube:latest . -f deploy/Dockerfile
```
2. To run created image and up contained (8002 port)
```shell
sudo docker run --name hypercube -p 8002:8002 --rm hypercube:latest
```
