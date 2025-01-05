from flask import Flask, render_template, request, jsonify
import requests
import os

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
    # Renderが指定する環境変数でポートを取得
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
