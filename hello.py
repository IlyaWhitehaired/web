def wsgi_application(environ, start_response): 
    status = '200 OK'
        ('Content-Type', 'text/plain')
    body = 'Hello, world!'