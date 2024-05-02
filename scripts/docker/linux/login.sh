read -p "Enter accessKeyId: " accessKeyId
read -p "Enter secretAccessKey: " secretAccessKey
read -p "Enter sessionToken: " sessionToken
read -p "Enter region: " region
read -p "Enter repositoryUri: " repositoryUri

export AWS_ACCESS_KEY_ID="$accessKeyId"
export AWS_SECRET_ACCESS_KEY="$secretAccessKey"
export AWS_SESSION_TOKEN="$sessionToken"

hostname=$(echo "$repositoryUri" | awk -F[/] '{print $1}')

echo "Login..."
aws ecr get-login-password --region "$region" | docker login --username AWS --password-stdin "$hostname"