@echo off

set /p accessKeyId=Enter accessKeyId:
set /p secretAccessKey=Enter secretAccessKey:
set /p sessionToken=Enter sessionToken:
set /p region=Enter region:
set /p repositoryUri=Enter repositoryUri:

set AWS_ACCESS_KEY_ID=%accessKeyId%
set AWS_SECRET_ACCESS_KEY=%secretAccessKey%
set AWS_SESSION_TOKEN=%sessionToken%

FOR /F "tokens=1,2 delims=/" %%i in ("%repositoryUri%") do (
  set hostname=%%i
)

echo "Login..."
aws ecr get-login-password --region %region% | docker login --username AWS --password-stdin %hostname%