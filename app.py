from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('Honne.html')

@app.route('/como_leer_manga')
def como_leer_manga():
    return render_template('Comoleermanga.html')

@app.route('/mangas')
def mangas():
    return render_template('Mangas.html')

if __name__ == '__main__':
    app.run(debug=True)
