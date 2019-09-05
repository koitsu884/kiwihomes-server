import logging


logger = logging.getLogger(__name__)


class LoggingRequestMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # print('(1) init')

    def __call__(self, request):
        response = self.get_response(request)
        logger.info(request)

        # print('(3): after get_response')

        return response
