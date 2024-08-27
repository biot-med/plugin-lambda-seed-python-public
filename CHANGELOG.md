# Version 1.5.5
**Released by**: Dan Tamam **Release Date**: 2024-08-27
## Changes
- Added biot_search method to http_utils, to simplify sending the standard biot search request
- All http requests sent with http_utils, will now convert their query dict values to strings
- Traceparent is now optional in all http_util methods
- Added log response method to http_utils, this can be used if directly using requests methods for non-json requests
- Add generic bad request response method
- Change no hooktype provided warning to use logger instead of print

# Version 1.5.4
**Released by**: Chen Zecharya **Release Date**: 2024-07-03
## Changes
- Removed case specific code from 'perform' method in all interceptors
- Updated comments on how to create new custom errors

# Version 1.5.3
**Released by**: Chen Zecharya **Release Date**: 2024-06-30
## Changes
- Plugin is now safe to be used through scheduler

# Version 1.5.2
**Released by**: Dan Tamam **Release Date**: 2024-06-05
## Changes
- Fixed imports

# Version 1.5.1
**Released by**: Dan Tamam **Release Date**: 2024-05-22
## Changes
- Fixed response body returned to the service in post and post entity interception modules

# Version 1.5.0
**Released by**: Shimi Karaso **Release Date**: 2024-05-02
## Changes
- Added dokcer image support. More details in the readme file
- Changed the way we are recognizing what constants to use (cloud_constants/local_dev_constants)
by depending on the AWS_REGION env var instead of the previous one in order support
local run for plugins of type image as a container

# Version 1.4.0
**Released by**: Arye Varman **Release Date**: 2024-04-11
## Changes
- Fixed issues with the seed
- Added Access Denied error to pre intercept
- Added examples for several api calls
- Added mock events

# Version 1.3.0
**Released by**: Adi Siman Tov **Release Date**: 2023-10-16
## Changes
- Changed seed structure - now using venv and requirements.txt file.
- Changed pack script to use dependencies from the venv directory
- **NOTE** .gitignore and pack script expects the venv name to be "seedenv"
- 
# Version 1.2.1
**Released by**: Dan Tamam **Release Date**: 2023-09-10
## Changes
- Removed BIOT_PUBLIC_KEY environment variable
- Lambda now gets public key from UMS API

# Version 1.2.0
**Released by**: David Kleinerman + Dan Tamam **Release Date**: 2023-08-16
## Breaking Changes
- Trace id is now in w3c format
## Changes
- Temporarily added dependency files

# Version 1.1.0
**Released by**: David Kleinerman **Release Date**: 2023-03-05
## Changes
 - Initial Release

## Bug Fixes
## Configuration Changes
## Known Issues
## Breaking Changes
