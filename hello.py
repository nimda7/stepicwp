#
def app(environ, start_response):
    status = '200 OK'
    headers = [
            ('Content-Type', 'text/plain')
            ]
    body = headers
    start_response(status, headers )
    resp = environ['QUERY_STRING'].split('&')
    res = [item+"\r\n" for item in resp ]
    return  res
 
