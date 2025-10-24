from flask import Flask, send_from_directory
import os

# Serve the static `build/web` output produced by your pygbag/pygame-web build.
BUILD_DIR = os.path.join(os.path.dirname(__file__), 'build', 'web')

app = Flask(__name__, static_folder=BUILD_DIR, static_url_path='')


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/<path:path>')
def static_proxy(path):
    # Serve files from the build folder, fall back to index.html for SPA behavior
    full_path = os.path.join(app.static_folder, path)
    if os.path.exists(full_path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    # Local dev server (not for production on Heroku)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
