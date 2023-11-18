from flask import Flask
import redis
import os

app = Flask(__name__)

# Get MongoDB endpoint
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", "6379")

# Connect to Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

@app.route('/')
def index():
    # Check if the key 'visited_count' exists in Redis
    if redis_client.exists('visited_count'):
        # If exists, increment the count
        redis_client.incr('visited_count')
    else:
        # If doesn't exist, set the count to 1
        redis_client.set('visited_count', 1)
    
    # Get the current count from Redis
    count = redis_client.get('visited_count').decode('utf-8')
    
    return f"Hello! You've visited this page {count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
