# import aioredis
# from fastapi import Request, HTTPException
# from functools import wraps
# from datetime import datetime
#
# REDIS_HOST = "127.0.0.1"
# REDIS_PORT = 6379
#
#
# async def get_redis():
#     redis = await aioredis.create_redis_pool(f'redis://{REDIS_HOST}:{REDIS_PORT}')
#     return redis
#
#
# async def close_redis(redis):
#     redis.close()
#     await redis.wait_closed()
#
#
# def rate_limit(key_prefix: str, max_requests: int, expire_time: int):
#     def decorator(func):
#         @wraps(func)
#         async def wrapper(request: Request, *args, **kwargs):
#             user_id = request.headers.get('user_id')
#             if not user_id:
#                 raise HTTPException(status_code=400, detail="user_id header is missing")
#
#             redis = await get_redis()
#             try:
#                 key = f"{key_prefix}:{user_id}:{datetime.now().strftime('%Y-%m-%d')}"
#                 current_count = await redis.incr(key)
#
#                 if current_count == 1:
#                     await redis.expire(key, expire_time)  # set expiration time for the key
#
#                 if current_count > max_requests:
#                     raise HTTPException(
#                         status_code=429,
#                         detail=f"Rate limit exceeded. Max {max_requests} requests per day allowed."
#                     )
#
#                 return await func(request, *args, **kwargs)
#
#             finally:
#                 await close_redis(redis)
#
#         return wrapper
#
#     return decorator
