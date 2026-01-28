import os
from waitress import serve
from app import app, init_db

# DB do persistent disku na Renderu
os.environ["KJ_DB_PATH"] = "/data/database.db"

init_db()
serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", "10000")))
