"""
main module of the server file
"""
from app import app, db
from config import Config


if __name__ == '__main__':
    print("Creating database tables...")
    db.create_all()
    print("Done!")

    # app.run(debug=Config.DEBUG)
    app.secret_key=Config.SECRET_KEY
    app.run(host='0.0.0.0', port=8087, debug=True)