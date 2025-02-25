import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set secret key for session management
app.secret_key = os.environ.get("SESSION_SECRET", "dev_key_123")  # Always use environment variable in production

# Admin password
app.config['ADMIN_PASSWORD'] = "d8g7HsmXes0zgH4efHvWB2MkV0cdiWh854kqeCHuf5gyHxFuDCzAbJyTNrBi4s4EuRf6iWXu95sqAgV1sj5f1PtV8k7Ja3VA5Cni"

# File upload configurations
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')

# Create upload directory for PDFs if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

db.init_app(app)

with app.app_context():
    import models
    db.create_all()
