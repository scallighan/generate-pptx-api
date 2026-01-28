docker build -t generate-pptx-api .
    
docker stop gpa
docker rm gpa

docker run -d --env-file .env -p 8888:80 --name gpa generate-pptx-api
docker logs -f gpa