from flask import Flask, jsonify

# con el jsonify vamos a convertir el diccionario en un Json adeacuado

app = Flask(__name__)

# Datos para el ejercicio del trazador cubico sujeto
data_e1 = {
    "x" : [0,1,2,3,4,5],
    "y" : [0.5,0.8,1.0,0.9,1.2,0.7]
} 

# Datos para el ejercicio del polinomio de minimos cuadrados
data_e2 = {
    "x" : [0,1,2,3,4],
    "y" : [1.1,3.5,2.8,4.2,5.0]
}

# Datos para el ejercicio de resolucion de ecuaciones lineales
data_e4 = {
    "a" : [[1,2,1],[2,-1,1],[3,1,-1]],
    "b" : [4,1,-2]
}


# vamos a realizar los metodos get para obtener los datos cuando se realizar la solicitud

# obtener los datos del primer ejercicio
@app.route("/api/data_e1", methods=['GET'])
def get_data_e1():
    return jsonify(data_e1)

# obtener los datos del segundo ejercicio
@app.route("/api/data_e2", methods=['GET'])
def get_data_e2():
    return jsonify(data_e2)

# obtener los datos del cuarto ejercicio
@app.route("/api/data_e4", methods=['GET'])
def get_data_e4():
    return jsonify(data_e4)


# para iniciar el servidor
if __name__ == "__main__":
    app.run(debug=True)