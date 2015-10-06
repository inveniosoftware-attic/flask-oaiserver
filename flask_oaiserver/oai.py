from flask import Flask
from views.server import blueprint as server
from views.settings import blueprint as settings

app = Flask(__name__)
app.register_blueprint(server)
app.register_blueprint(settings)
app.debug = True

if __name__ == '__main__':
    app.run()
