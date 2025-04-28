import logging

logger = logging.getLogger('django')

class GlobalExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except Exception as e:
            logger.error("Unhandled Exception", exc_info=True)
            # Optional: you can return a custom error response too
            from django.http import JsonResponse
            return JsonResponse({'error': 'Something went wrong'}, status=500)