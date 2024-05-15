set -e

# using the unix time in milliseconds as the image tag (could be any other random string)
unixTimeMs=$(date +%s%N | cut -b1-13)
fullImageName=docker-image:$unixTimeMs

docker build --platform linux/amd64 -t "$fullImageName" .
docker tag "$fullImageName" "docker-image:latest"

echo "fullImageName=$fullImageName"