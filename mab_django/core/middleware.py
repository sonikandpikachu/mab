import logging
import pprint


logger = logging.getLogger(__name__)


class CorsMiddleware(object):

    def process_response(self, request, response):
        """
            Do NOT use this middleware in production! For development only.
        """
        response['Access-Control-Request-Headers'] = 'X-Requested-With, accept, content-type'
        response['Access-Control-Allow-Methods'] = 'GET, POST'
        pp = pprint.PrettyPrinter(indent=4)
        logger.warning(pp.pformat(request.__dict__))
        logger.warning(pp.pformat(response.__dict__))
        return response
