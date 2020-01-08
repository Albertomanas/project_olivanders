from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = 'Juan'
    return render_template('index.html', user=user)
# Aquí meteremos lo que queremos que le salga al usuario en cada ruta
# especifica
