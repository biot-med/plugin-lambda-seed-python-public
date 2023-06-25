mock_event = {
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