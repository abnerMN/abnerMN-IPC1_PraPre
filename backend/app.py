from flask import Flask,jsonify,request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def es_vocal(letra):
    return letra in "aeiouáéíóú"

@app.route('/calcular', methods=['POST'])
def calcular():
    a=float(request.json['numero1'])
    b=float(request.json['numero2'])
    operacion=request.json['signo']
    if operacion=='+':
        c=a+b
        return jsonify({
            'message':'200',
            'respuesta' : c
        })

    elif operacion=='-':
        c=a-b
        return jsonify({
            'message':'200',
            'respuesta' : c
        })

    elif operacion=='*':
        c=a*b
        return jsonify({
            'message':'200',
            'respuesta' : c
        })

    elif operacion=='/':
        c=a/b
        return jsonify({
            'message':'200',
            'respuesta' : c
        })

@app.route('/primo', methods=['POST'])
def Primo():
    a=int(request.json['inferior'])
    b=int(request.json['superior'])
    b=b+1
    contador=0
    for i in range(a,b):
        if i%2!=0:
            contador+=1
    return jsonify({
        'message':'200',
        'primos' : contador
        })


@app.route('/vocales', methods=['POST'])
def vocales ():
    frase=request.json['frase']
    frase=frase.lower()
    palabras =len(frase.split())
    consonantes=0
    vocales=0
    for letra in frase:
        if letra.isalpha() and not es_vocal(letra):
            consonantes+=1
        if letra.isalpha() and es_vocal(letra):
            vocales+=1

    return jsonify({
        'message':'200',
        'palabras' : palabras,
        'consonantes': consonantes,
        'vocales': vocales
        })



if __name__ == "__main__":
    app.run(threaded=True, debug=True, port=3000)
