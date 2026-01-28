from waitress import serve
from app import app, init_db

if __name__ == "__main__":
    init_db()
    serve(app, host="0.0.0.0", port=5000)
