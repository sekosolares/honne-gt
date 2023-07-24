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

@app.route('/webtoons')
def webtoons():
    return render_template('WebToons.html')

@app.route('/explorar')
def explorar():
    return render_template('Explorar.html')

@app.route('/contenido/<template_name>')
def go_to(template_name):
    if template_name == 'KimetsuNoYaiba':
        return render_template('KimetsuNoYaiba.html')
    elif template_name == 'Aventura':
        return render_template('Aventura.html')
    elif template_name == 'Shonen':
        return render_template('Shonen.html')
    elif template_name == 'Jidaimono':
        return render_template('Jidaimono.html')
    elif template_name == 'Accion':
        return render_template('Accion.html')
    elif template_name == 'Cap1':
        return render_template('Cap1.html')

    return render_template('Explorar.html')


if __name__ == '__main__':
    app.run(debug=True)
