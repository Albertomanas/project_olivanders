from app import app
from flask import render_template
from Lógica.Gilded_rose import Gilded_rose


@app.route('/')
@app.route('/index/<numero_de_dias>')
def index(numero_de_dias=0):
    items = Gilded_rose((lista_de_items, int(numero_de_dies)))
    items.main()
    dias = numero_de_dias
    return render_template('index.html', items=items, dias=dias)
# Aquí meteremos lo que queremos que le salga al usuario en cada ruta
# especifica
