from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hel lowo rld'

if __name__ == "__main__":
	app.run()
