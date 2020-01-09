# cambiar
from app import app
from flask import render_template
from Lógica.Gilded_rose import Gilded_rose
from app.database import Inventory


@app.route('/')
@app.route('/index/<numero_de_dias>')
def index(numero_de_dias=0):
    numero_de_dias = numero_de_dias.strip('<')
    numero_de_dias = numero_de_dias.strip('>')
    items = Gilded_rose((Inventory.all_query_to_filtred_list()), int(numero_de_dias))
    items.main()
    dias = numero_de_dias
    return render_template('index.html', items=items, dias=dias)
# Aquí meteremos lo que queremos que le salga al usuario en cada ruta
# especifica
