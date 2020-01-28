"""
main module of the server file
"""
from config import Config
from app import app, db



if __name__ == '__main__':
    print("Creating database tables...")
    db.create_all()
    print("Done!")

    # app.run(debug=Config.DEBUG)
    app.secret_key=Config.SECRET_KEY
    app.run(host='0.0.0.0', port=8087, debug=True)