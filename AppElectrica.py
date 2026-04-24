from flask import Flask, render_template, request

app = Flask(__name__)

# Esta parte es la que hace los cálculos
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            # Recibimos los datos del formulario del celu
            cliente = request.form.get('cliente', 'Cliente')
            voltaje = float(request.form.get('voltaje'))
            potencia = float(request.form.get('potencia'))
            
            # Cálculo de Amperaje: I = P / V
            if voltaje > 0:
                amperios = potencia / voltaje
                resultado = f"Resultado para {cliente}: {amperios:.2f} Amperes"
            else:
                resultado = "El voltaje debe ser mayor a 0"
        except:
            resultado = "Error: Por favor, ingresa solo números"
            
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    # host='0.0.0.0' permite que el celular entre por la red Wi-Fi
    # port=5000 es el puerto de salida
    # debug=False ayuda a que algunos navegadores no bloqueen la conexión
    app.run(host='0.0.0.0', port=5000, debug=False)