set -e

read -p "Enter repositoryUri: " repositoryUri

# using the unix time in milliseconds as the image tag (could be any other random string)
imageTag=$(date +%s%N | cut -b1-13)

echo "Building an image..."
docker build --platform linux/amd64 -t "docker-image:$imageTag" .
docker tag "docker-image:$imageTag" "docker-image:latest"
docker tag "docker-image:$imageTag" "$repositoryUri:$imageTag"
docker push "$repositoryUri:$imageTag"

echo "provide the following parameter to the plugin API:"
echo "imageTag=$imageTag"