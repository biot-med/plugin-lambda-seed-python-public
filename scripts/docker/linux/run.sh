read -p "Enter full image name[leave empty for using the latest image built by the build.sh script]: " fullImageName

if [ -z "$fullImageName" ]; then
  fullImageName="docker-image:latest"
fi

docker run --platform linux/amd64 --name plugin-local-run-container -p 9000:8080 "$fullImageName"