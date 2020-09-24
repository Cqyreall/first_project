from flask import Flask, render_template
app = Flask(__name__)

from controllers.teams_controller import teams_blueprint
from controllers.games_controller import games_blueprint

app.register_blueprint(teams_blueprint)
app.register_blueprint(games_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)