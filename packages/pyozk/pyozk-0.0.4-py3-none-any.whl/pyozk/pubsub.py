import redis

from .const import TIMEKEEPING_CHANNEL
from settings import REDIS_HOST, REDIS_PORT

# Connect to Redis
redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

def publish(channel, message):
    redis_client.publish(channel, message)

# # Create a Pub/Sub instance
# pubsub = redis_client.pubsub()
# # Subscribe to a channel
# pubsub.subscribe(TIMEKEEPING_CHANNEL)

# # Listen for messages
# for message in pubsub.listen():
#     if message['type'] == 'message':
#         print(f"Received message: {message['data'].decode('utf-8')}")
