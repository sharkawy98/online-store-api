# Online-Store-API
RESTful API for an online store with DRF and Docker.

## How to Run our API 
* It works for any OS contains only Docker.
* You can follow the below instructions, which cover two scenarios.

#### Your first time:
```bash
git clone "https://github.com/sharkawy98/online-store-api.git"
cd online-store-api

# build your Docker Image
docker build -t <image-name> .

# run your Docker Container
docker run -d -p <your-port>:9000 --name <container-name> <image-name>

# stop the container running at <your-port>
docker stop <container-name>
```

#### Runned it before:
```bash
# make your local repo updated with the remote one
git pull

# run your Docker Container
docker start <container-name>

# stop the container running at <your-port>
docker stop <container-name>
```
