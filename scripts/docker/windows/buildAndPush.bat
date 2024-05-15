@echo off

set /p repositoryUri=Enter repositoryUri:

@REM using the unix time in milliseconds as the image tag (could be any other random string)
for /f "delims=" %%a in (' powershell "[long]([DateTime]::UtcNow - (new-object DateTime 1970,1,1,0,0,0,([DateTimeKind]::Utc))).TotalMilliseconds" ') do (
    set "imageTag=%%a"
)

echo Building an image...
docker build --platform linux/amd64 -t docker-image:%imageTag% .
if %errorlevel% neq 0 exit /b %errorlevel%

docker tag docker-image:%imageTag% docker-image:latest
if %errorlevel% neq 0 exit /b %errorlevel%

docker tag docker-image:%imageTag% %repositoryUri%:%imageTag%
if %errorlevel% neq 0 exit /b %errorlevel%

docker push %repositoryUri%:%imageTag%
if %errorlevel% neq 0 exit /b %errorlevel%

echo provide the following parameter to the plugin API:
echo imageTag=%imageTag%