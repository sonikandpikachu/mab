class CorsMiddleware(object):

    def process_response(self, request, response):
        """
            Do NOT use this middleware in production! For development only.
        """
        response['Access-Control-Request-Headers'] = 'X-Requested-With, accept, content-type'
        response['Access-Control-Allow-Methods'] = 'GET, POST'
        return response
