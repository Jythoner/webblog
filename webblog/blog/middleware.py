# -*- coding:utf-8 -*-
import logging
logger = logging.getLogger(__name__)


class TestMiddleware(object):

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        pass
