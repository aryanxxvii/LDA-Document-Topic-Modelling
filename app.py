from flask import Flask, request, jsonify
import redis
import json
from model import find_similar_articles  # Importing from model.py
from cache_config import redis_client

# Initialize Flask app
app = Flask(__name__)


@app.route('/search', methods=['POST'])
def search():
    """Search for similar articles based on input text"""
    user_input = request.json.get('text')

    if not user_input:
        return jsonify({"error": "No input text provided"}), 400

    # First check if the result is cached in Redis
    cache_result = redis_client.get(user_input)

    if cache_result:
        return jsonify(json.loads(cache_result))  # Return cached result

    # If not cached, fetch the result using LDA model
    similar_articles = find_similar_articles(user_input)

    # Cache the result in Redis for future requests
    redis_client.setex(user_input, 3600, json.dumps(similar_articles))  # Cache for 1 hour

    return jsonify(similar_articles)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
