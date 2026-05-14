import logging
import time
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class LoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()
        
        logger.info(f"Pristigao je request: {request.method} {request.path}")
        
        return None
    
    def process_response(self, request, response):
        if hasattr(request, 'start_time'):
            duration = time.time() - request.start_time
            logger.info(f"Završeno: {request.method} {request.path} | Status: {response.status_code} | Trajanje: {duration:.2f} sekundi")
        
        return response
    
    def process_exception(self, request, exception):
        logger.error(f"Greška prilikom obrade requesta: {request.method} {request.path} | Greška: {str(exception)}")
        return None