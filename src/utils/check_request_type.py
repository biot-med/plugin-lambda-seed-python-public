request_types = {
  "NOTIFICATION": "NOTIFICATION",
  "INTERCEPTOR_PRE": "INTERCEPTOR_PRE",
  "INTERCEPTOR_POST": "INTERCEPTOR_POST",
  "INTERCEPTOR_POST_ENTITY": "INTERCEPTOR_POST_ENTITY",
  "NONSPECIFIC": "NONSPECIFIC"
}

def check_request_type (event):
    hooktype_key = filter(lambda k: k.lower() == "hooktype", list(event["headeres"].keys()))
  
    if hooktype_key is not None and request_types[event["headers"][hooktype_key]] :
        return request_types[event["headeres"][hooktype_key]]
    else :
        print("No hooktype provided")
        return request_types["NONSPECIFIC"]
  