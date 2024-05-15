@echo off

@REM using the unix time in milliseconds as the image tag (could be any other random string)
for /f "delims=" %%a in (' powershell "[long]([DateTime]::UtcNow - (new-object DateTime 1970,1,1,0,0,0,([DateTimeKind]::Utc))).TotalMilliseconds" ') do (
    set "unixTimeMs=%%a"
)

set fullImageName=docker-image:%unixTimeMs%

docker build --platform linux/amd64 -t %fullImageName% .
docker tag %fullImageName% docker-image:latest
if %errorlevel% neq 0 exit /b %errorlevel%

echo fullImageName=%fullImageName%