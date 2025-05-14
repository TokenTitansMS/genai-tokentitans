class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  # In-memory SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_jwt_secret_key'  # Replace with a secure key in production