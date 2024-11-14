from flask import Flask
from blueprints.reading_emails_bp import bp_email
app = Flask(__name__)

app.register_blueprint(bp_email)


if __name__ == '__main__':
    app.run()
