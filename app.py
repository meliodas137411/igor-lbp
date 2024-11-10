from flask import Flask
from controllers.main import main as main_blueprint
from blueprints.auth import auth as auth_blueprint

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'


app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
