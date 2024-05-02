set -e

read -p "Enter repositoryUri: " repositoryUri
read -p "Enter fullImageName (an output from the build.sh script execution): " fullImageName

imageTag=$(echo "$fullImageName" | awk -F[:] '{print $2}')

docker tag "$fullImageName" "$repositoryUri:$imageTag"
docker push "$repositoryUri:$imageTag"

echo "provide the following parameter to the plugin API:"
echo "imageTag=$imageTag"