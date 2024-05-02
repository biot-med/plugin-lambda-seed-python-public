@echo off

set "fullImageName=docker-image:latest"
set /p fullImageName=Enter full image name[leave empty for using the latest image built by the build.bat script]:

docker run --platform linux/amd64 --name plugin-local-run-container -p 9000:8080 %fullImageName%