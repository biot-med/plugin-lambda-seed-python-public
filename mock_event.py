notification_mock_event = {
    'version': '2.0',
    'routeKey': '$default',
    'rawPath': '/',
    'rawQueryString': '',
    'headers': {
        'content-length': '2099',
        'x-amzn-tls-version': 'TLSv1.2',
        'x-forwarded-proto': 'https',
        'x-forwarded-port': '443',
        'x-forwarded-for': '44.194.185.170',
        'accept': 'application/json, application/octet-stream, application/cbor, application/*+json',
        'hooktype': 'NOTIFICATION',
        'x-amzn-tls-cipher-suite': 'ECDHE-RSA-AES128-GCM-SHA256',
        'x-amzn-trace-id': 'Root=1-644a7355-3613e58f152aed8563981070',
        'traceparent': '00-644a735422c8116c6f662f52adc4d153-5617eac22fd158f0-00',
        'host': 'rnis3tgocg35xey4msdsbngbta0qfigj.lambda-url.us-east-1.on.aws',
        'content-type': 'application/json',
        'accept-encoding': 'gzip, x-gzip, deflate',
        'user-agent': 'Apache-HttpClient/5.1.4 (Java/17.0.6)'
    },
    'requestContext': {
        'accountId': 'anonymous',
        'apiId': 'rnis3tgocg35xey4msdsbngbta0qfigj',
        'domainName': 'rnis3tgocg35xey4msdsbngbta0qfigj.lambda-url.us-east-1.on.aws',
        'domainPrefix': 'rnis3tgocg35xey4msdsbngbta0qfigj',
        'http': {
        'method': 'POST',
        'path': '/',
        'protocol': 'HTTP/1.1',
        'sourceIp': '44.194.185.170',
        'userAgent': 'Apache-HttpClient/5.1.4 (Java/17.0.6)'
        },
        'requestId': 'd3679ee8-e44d-4de4-9f3f-807a6afa936b',
        'routeKey': '$default',
        'stage': '$default',
        'time': '27/Apr/2023:13:06:29 +0000',
        'timeEpoch': 1682600789501
    },
    'body': '{"metadata":{"entityTypeName":"patient","actionName":"_create","status":"SUCCESS","startTime":"2023-04-27T13:06:28.234829169Z","endTime":"2023-04-27T13:06:28.802236037Z","traceId":"644a735430897dbe0e3752bef49bc310","initiator":{"subject":{"id":"505f563b-5d85-4f45-b003-6acdac43209a"},"sourceIpAddress":"192.114.169.190"}},"data":{"entity":{"_name":{"firstName":"ben","lastName":"rose test trace id"},"_description":null,"_email":"ben+11@biot-med.com","_phone":null,"_locale":"en_US","_gender":"MALE","_dateOfBirth":"2012-09-07","_address":null,"_mfa":{"enabled":false,"expirationInMinutes":null},"_additionalPhone":null,"_nationalId":"1231152352","_id":"72b65591-2bc4-4b8a-877b-827a5a1057b3","_ownerOrganization":{"id":"00000000-0000-0000-0000-000000000000","name":"BioT","templateId":"2aaa71cf-8a10-4253-9576-6fd160a85b2d","parentEntityId":null},"_caregiver":{"id":"1b76a006-00c1-47ee-abd4-486c80be9f60","name":"created by name (E123334)","templateId":"336ad952-5261-48b5-918f-0d5aef03dced","parentEntityId":null},"_creationTime":"2023-04-27T13:06:28.444Z","_lastModifiedTime":"2023-04-27T13:06:28.444Z","_invitationAccepted":false,"_template":{"id":"a38f32d7-de6c-4252-9061-9bcdc253f6c9","name":"Patient","displayName":"Patient"},"_referencers":null,"generic":null,"_enabled":"ENABLED","_caption":"rose test trace id ben (1231152352)","_username":null,"_registrationSource":null,"_canLogin":true},"additionalData":{}},"jwt":"eyJhbGciOiJSUzUxMiJ9.eyJzZXJ2aWNlVXNlcklkIjoiYmM4NDM5YmItNTY4NC00MzJhLWFjMzgtY2QyMTgwZGMxM2MwIiwic2NvcGVzIjpbIlBST1RFQ1RFRF9BUEkiLCJBQ1RJT05fTk9USUZJQ0FUSU9OIiwiUEVSTUlTU0lPTlNfU1lOQ19QRVJNSVNTSU9OUyJdLCJ0b2tlblR5cGUiOiJTRVJWSUNFX0lOVEVSTkFMIiwianRpIjoiMDcyMzU5NDUtNGJjZS00OGQ4LWFjMjQtZWUwNWIwOGE1OGIzIiwiZXhwIjoxNjgyNjAyNTU5fQ.CBe-k_kAeUL0BD6i9RDNNLDCTDyJwkZxrIcvgsfnMq8hS619AioYIil45R2L_vCFITvt7K-B7SIK8263r81fC77JjVART36-35FcDnpP4owJ69UUKQ_rkodJcwhLttOSqV0AKa75gPN4JG5PMGXucQeDR9ASV1GJTSa3QJeK46S3F1KLPoNbpDgislrPcZOfTCIpKB9HI3twhTYy4-QaNXXcb7WPKNYTzY24BiCJ-MHktG1j-4p2yOSr5Jx2eNJcKUyAuDE9CZNGyXVFaPxD0qsPbqTqLioCy-MbeX6DJTpqCbCdGLe6AArE2qUZ0LdG-9f1q4xlTvHYj2KzMpKT8Q"}',
    'isBase64Encoded': False
}


pre_intercept_mock_event = {
  "version": "2.0",
  "routeKey": "$default",
  "rawPath": "/",
  "rawQueryString": "",
  "headers": {
    "content-length": "7875",
    "x-amzn-tls-version": "TLSv1.3",
    "x-forwarded-proto": "https",
    "accept-language": "en-us",
    "x-forwarded-port": "443",
    "x-forwarded-for": "18.214.61.164",
    "accept": "application/json, application/octet-stream, application/cbor, application/*+json",
    "hooktype": "INTERCEPTOR_PRE",
    "authorization": "Bearer eyJhbGciOiJSUzUxMiJ9.eyJzZXJ2aWNlVXNlcklkIjoiNjc4NmQ2MGQtZTIzYi00ZDFiLTk2OWMtNzFhMTkzYWMxODVjIiwic2NvcGVzIjpbIlNFVFRJTkdTX01JTklNSVpFRF9TRUFSQ0hfVEVNUExBVEUiLCJVTVNfVVNFUlNfVVBEQVRFX1VTRVIiLCJNRUFTVVJFTUVOVF9HRVRfTEFTVF9NRUFTVVJFTUVOVFMiLCJGSUxFX1NFQVJDSF9GSUxFUyIsIlNFVFRJTkdTX1NFQVJDSF9BVFRSSUJVVEUiLCJGSUxFX0dFVF9GSUxFX01FVEFEQVRBIiwiU0VUVElOR1NfU0VBUkNIX0VOVElUWV9UWVBFUyIsIlBST1RFQ1RFRF9BUEkiLCJVTVNfVVNFUlNfU0VBUkNIX1VTRVIiLCJFTlRJVFlfUkVMQVRJT05TSElQX1NFQVJDSCIsIlNFVFRJTkdTX0dFVF9SRUZFUkVOQ0VfQVRUUklCVVRFUyIsIlNFVFRJTkdTX0dFVF9URU1QTEFURSIsIkVOVElUWV9SRUxBVElPTlNISVBfQVRUUklCVVRFX1JFRkVSRU5DRVNfQ09VTlQiLCJFTlRJVFlfRU5USVRZX1NFQVJDSCIsIlVNU19VU0VSU19DUkVBVEVfVVNFUiIsIlVNU19VU0VSU19ERUxFVEVfVVNFUiIsIlBMVUdJTl9JTlRFUkNFUFRPUiIsIlNFVFRJTkdTX0dFVF9DVVNUT01fQVRUUklCVVRFUyIsIlNFVFRJTkdTX1NFQVJDSF9URU1QTEFURSIsIlBFUk1JU1NJT05TX1NZTkNfUEVSTUlTU0lPTlMiXSwidG9rZW5UeXBlIjoiU0VSVklDRV9JTlRFUk5BTCIsImp0aSI6IjQzY2QyNDg4LTgyZTItNDUwMi04MTQzLTU5YTg5ODAyZDNiZSIsImV4cCI6MTcxMTAyODEwOX0.TWMpYFC99U15OkcsTP59Wb_c902sU30DXY-HNI0t-iqbiCc2zKJoS-iN_yyYYXbdRKN1uCwHzF2JsOCeXRLEcARp0WEHR4C8Ct7qk80YdalW_9wTTzvbNTvvcx9n4qJK31ne61m7KKGOBRFv3apWNhmBNtDWJGeJSgYnS1wJRYUUEpblopRVw11arsm5TGci21K08PsgwENEoDxxCV-MKsLQjRPu5RXAqPXQTOOafcwLBMpNwvzf2eIqN8udrHuqgqbEUs_WZ9Frnkrh2Y5hqvP6Ewj4nFSf03PYDQpt0STIiq7T5zsWdOUEltmhFhXL5DmlAfwZB_YYU3zcFkEJrA",
    "x-amzn-tls-cipher-suite": "TLS_AES_128_GCM_SHA256",
    "x-amzn-trace-id": "Self=1-65fc35a0-0002ccbd3f9ccdb570eeddd4;Root=1-65fc35a0-192b8c084f3381e84745ef37",
    "traceparent": "00-65fc35a05ce4c540b5e1cd1616f6fa21-89b65f9147e74718-00",
    "host": "v3xsg6ytmzrwxjt57erjegvaoa0ifhwz.cell-1-lambda-url.us-east-1.on.aws",
    "content-type": "application/json",
    "accept-encoding": "gzip, x-gzip, deflate",
    "user-agent": "Apache-HttpClient/5.1.4 (Java/17.0.6)"
  },
  "requestContext": {
    "accountId": "anonymous",
    "apiId": "v3xsg6ytmzrwxjt57erjegvaoa0ifhwz",
    "domainName": "v3xsg6ytmzrwxjt57erjegvaoa0ifhwz.cell-1-lambda-url.us-east-1.on.aws",
    "domainPrefix": "v3xsg6ytmzrwxjt57erjegvaoa0ifhwz",
    "http": {
      "method": "POST",
      "path": "/",
      "protocol": "HTTP/1.1",
      "sourceIp": "18.214.61.164",
      "userAgent": "Apache-HttpClient/5.1.4 (Java/17.0.6)"
    },
    "requestId": "27faf494-5201-49b0-a933-46d51c90146f",
    "routeKey": "$default",
    "stage": "$default",
    "time": "21/Mar/2024:13:26:56 +0000",
    "timeEpoch": 1711027616696
  },
  "body": "{\"initiatorData\":{\"subjectId\":\"3e256d8d-e5e2-42bf-a091-1e6b4afef2fb\",\"ownerOrganizationId\":\"00000000-0000-0000-0000-000000000000\",\"tokenType\":\"USER\"},\"method\":\"GET\",\"entityName\":\"caregiver\",\"apiId\":\"GET/organization/v1/users/caregivers\",\"request\":{\"body\":null,\"path\":\"/organization/v1/users/caregivers\",\"queryParameters\":{\"searchRequest\":[\"{\\\"limit\\\":30,\\\"filter\\\":{\\\"_ownerOrganization.id\\\":{\\\"in\\\":[\\\"00000000-0000-0000-0000-000000000000\\\"],\\\"notIn\\\":[],\\\"filter\\\":{}}},\\\"freeTextSearch\\\":\\\"\\\"}\"]},\"headers\":{\"sec-fetch-mode\":\"cors\",\"content-length\":\"0\",\"referer\":\"https://organization.app.dev.biot-gen2.biot-med.com/\",\"sec-fetch-site\":\"same-site\",\"x-forwarded-proto\":\"https\",\"accept-language\":\"en-us\",\"origin\":\"https://organization.app.dev.biot-gen2.biot-med.com\",\"x-forwarded-port\":\"443\",\"x-forwarded-for\":\"147.235.209.7:3824\",\"accept\":\"application/json, text/plain, */*\",\"authorization\":\"Bearer eyJhbGciOiJSUzUxMiJ9.eyJyZWZyZXNoVG9rZW5JZCI6ImIxNmNjMzc0LTQyZTAtNDllNi1hOTE3LTE0OGQxYTFhOWIwOCIsInRlbmFudElkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIiwic2NvcGVzIjpbIlNFVFRJTkdTX01JTklNSVpFRF9TRUFSQ0hfVEVNUExBVEUiLCJQUk9URUNURURfQVBJIiwiU0VUVElOR1NfUE9SVEFMX0JVSUxERVJfR0VUX1ZJRVdfRlVMTF9BVFRSSUJVVEVTIiwiU0VUVElOR1NfR0VUX1RFTVBMQVRFIiwiVU1TX1VTRVJTX1NFTEZfVVBEQVRFX1VTRVIiLCJVTVNfVVNFUlNfU0VMRl9ERUxFVEVfVVNFUiIsIk9SR0FOSVpBVElPTl9HRVRfQlVJTFRfSU5fVEVNUExBVEVTIiwiVU1TX1VTRVJTX1NFTEZfR0VUX1VTRVIiLCJTRVRUSU5HU19TRUFSQ0hfVEVNUExBVEUiXSwidG9rZW5UeXBlIjoiVVNFUiIsImp0aSI6IjkzNDdkMmY3LWU1MTEtNDllOC04ZmE0LWY1ZDI1NjQzMTUwNiIsInN1YiI6IjNlMjU2ZDhkLWU1ZTItNDJiZi1hMDkxLTFlNmI0YWZlZjJmYiIsImV4cCI6MTcxMjA2MzE4OH0.YhgQosQTUgriyP2uUwcsc8gVP_vTK-6Sg8kVm4GP9evsp1VDJUce55aiP-71XeX3vDN3XUmgCxz8ZCuDmUk1-NxrD2zjXrP1MbnY1q0OoZoVQHGOYQmcy1NMNy_3OHYBZwaO0dN0n34gZ5XyvQ6L1xL-m1SNXi-EEL8TpjKPIqaC54FfSgLjbA8Cfrndh_HBQbRtXcVTAyBZee29d6rNq1z0hfcaoDmStshftYWM9yYK3byPUYeVTyM9RhvB2QLRdlGnmMGOtqG697YxkQUbcART4IR_9jNfKod09sqFvf0ND-qD0DYGFE3AW4kBT5nfwGQvxrcvhI29l76IzUqgfg\",\"sec-ch-ua\":\"\\\"Google Chrome\\\";v=\\\"123\\\", \\\"Not:A-Brand\\\";v=\\\"8\\\", \\\"Chromium\\\";v=\\\"123\\\"\",\"x-amzn-trace-id\":\"Self=1-660bff90-586f219a305944c6255a2835;Root=1-660bff90-004902df7ea2cec35a13be46\",\"sec-ch-ua-mobile\":\"?0\",\"traceparent\":\"00-660bff9042e0ac8a1c378fd7f00d2b8d-2a9647ced4f9fb47-00\",\"sec-ch-ua-platform\":\"\\\"macOS\\\"\",\"host\":\"api.dev.biot-gen2.biot-med.com\",\"accept-encoding\":\"gzip, x-gzip, deflate\",\"user-agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36\",\"sec-fetch-dest\":\"empty\"},\"pathVariables\":[]}}",
  "isBase64Encoded": False
}

nonspecific_mock_event = {
    'version': '2.0',
    'routeKey': '$default',
    'rawPath': '/', 'rawQueryString': '',
    'headers': {
        'x-amzn-tls-cipher-suite': 'TLS_AES_128_GCM_SHA256',
        'content-length': '86',
        'x-amzn-tls-version': 'TLSv1.3',
        'x-amzn-trace-id': 'Self=1-65f15be4-0eaebadb538c961655cc14ba;Root=1-65f15be4-333a14ca59889bef6a9686fd',
        'x-forwarded-proto': 'https',
        'host': 'd747wy4wvxbdfvh24tw44pwm640ofqxk.cell-1-lambda-url.us-east-1.on.aws',
        'x-forwarded-port': '443',
        'content-type': 'application/json',
        'x-forwarded-for': '192.114.169.190',
        'accept-encoding': 'gzip, deflate, br',
        'accept': '*/*',
        'user-agent': 'PostmanRuntime/7.34.0'
    },
    'requestContext': {
        'accountId': 'anonymous',
        'apiId': 'd747wy4wvxbdfvh24tw44pwm640ofqxk',
        'domainName': 'd747wy4wvxbdfvh24tw44pwm640ofqxk.cell-1-lambda-url.us-east-1.on.aws',
        'domainPrefix': 'd747wy4wvxbdfvh24tw44pwm640ofqxk',
        'http': {
            'method': 'POST',
            'path': '/',
            'protocol': 'HTTP/1.1',
            'sourceIp': '192.114.169.190',
            'userAgent': 'PostmanRuntime/7.34.0'
        },
        'requestId': '268ffc6d-c9c7-4181-a86e-2057f1bf8847',
        'routeKey': '$default',
        'stage': '$default',
        'time': '13/Mar/2024:07:55:16 +0000',
        'timeEpoch': 1710316516895},
    'body': '{\\n    \"name\": \"john\",\\n    \"surname\": \"smith\",\\n    \"email\": \"john@biotmail.com\"\\n}\\n',
    'isBase64Encoded': False
}
