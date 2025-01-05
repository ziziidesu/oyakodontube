from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# InvidiousインスタンスURL（https://inv.nadeko.net/を使用）
INVIDIOUS_URL = "https://inv.nadeko.net/api/v1/search"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    # Invidious APIで検索
    params = {"q": query, "page": 1, "sort_by": "relevance"}
    response = requests.get(INVIDIOUS_URL, params=params)

    if response.status_code == 200:
        videos = response.json()
        return jsonify(videos)
    else:
        return jsonify({"error": "Failed to fetch data from Invidious"}), 500

if __name__ == '__main__':
    app.run(debug=True)
