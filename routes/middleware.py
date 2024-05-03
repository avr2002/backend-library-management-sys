from fastapi import Request, Response
from time import time
from collections import defaultdict
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp


# class InjectUserIdMiddleware(BaseHTTPMiddleware):
#     def __init__(self, app: ASGIApp):
#         super().__init__(app)
#
#     async def dispatch(self, request: Request, call_next: ASGIApp) -> Response:
#         # Inject user_id into request headers for demo purposes
#         request.headers['user_id'] = 'user_1'  # Set a default user_id (change as needed)
#
#         # Call the inner application
#         response = await call_next(request)
#
#         return response


class InjectUserIdMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)
        self.rate_limit_records: dict[str, float] = defaultdict(float)

    async def log_message(self, message: str):
        print(message)

    async def dispatch(self, request: Request, call_next) -> Response:
        client_ip = request.client.host
        current_time = time()

        if current_time - self.rate_limit_records[client_ip] < 10000:  # 1 request per second
            # self.rate_limit_records[client_ip] = 0
            return Response(content="Rate Limit Exceeded", status_code=429)

        self.rate_limit_records[client_ip] = current_time
        path = request.url.path
        await self.log_message(f"Rquest to path: {path}")

        # Process the request
        current_time = time()
        response = await call_next(request)
        process_time = time() - current_time

        # Add custom headers without modifying the original headers object
        custom_headers = {"X-Process-Time": str(process_time)}
        for header, value in custom_headers.items():
            response.headers.append(header, value)

        # Asynchronus logging of processing time
        await self.log_message(f"Response for {path} took {process_time} seconds.")

        return response
