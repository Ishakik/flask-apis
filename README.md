#### prerequisites:
    
    * docker
    * kubectl

## **Build the docker image**
sudo docker build --tag flask-apis .

## Start the docker container to run the app in local
sudo docker run --name flask-apis -p 9090:9090 flask-apis

## publishing the container image to cloud repo
sudo docker tag flask-apis:latest flask-apis:0.1

## Push the container image to repo
sudo docker push flask-apis

## deploying app to kubernetes
kubectl apply -f deployment.yaml

##API Endpoints
* localhost:6000/api/health - health checking API

`Sample response:
{
    "server health": "GREEN"
}`

* localhost:6000/api/encrypt - encryption API

`Sample response:
{
    "Input": "plain text",
    "Message": "encryption successful",
    "Output": "Encrypted_plain text_String",
    "Status": "success"
}`
* localhost:6000/api/decrypt - decryption API

`Sample response:
{
    "Input": "Encrypted_plain text_String",
    "Message": "decryption successful",
    "Output": "plain text",
    "Status": "success"
}`