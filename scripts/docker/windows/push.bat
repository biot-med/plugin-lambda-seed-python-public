@echo off

set /p repositoryUri=Enter repositoryUri:
set /p fullImageName=Enter fullImageName (an output from the build.bat script execution):

FOR /F "tokens=2 delims=:" %%i in ("%fullImageName%") do (
  set imageTag=%%i
)

docker tag %fullImageName% %repositoryUri%:%imageTag%
if %errorlevel% neq 0 exit /b %errorlevel%

docker push %repositoryUri%:%imageTag%
if %errorlevel% neq 0 exit /b %errorlevel%

echo provide the following parameter to the plugin API:
echo imageTag=%imageTag%