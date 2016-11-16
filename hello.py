#
def app(environ, start_response):
    status = '200 OK'
    headers = [
            ('Content-Type', 'text/plain')
            ]
    body = headers
    start_response(status, headers )
    return  body 
