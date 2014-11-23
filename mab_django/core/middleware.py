class CorsMiddleware(object):

    def process_response(self, request, response):
        """
            Do NOT use this middleware in production! For development only.
        """
        response['Access-Control-Request-Headers'] = 'X-Requested-With, accept, content-type'
        response['Access-Control-Allow-Methods'] = 'GET, POST'
        with (open('responses.txt'), 'wb+') as f:
            f.write(str(response.__dict__))
        return response
