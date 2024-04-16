from flask import Flask,jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__) 

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
from datos import datos

if __name__ == '__main__':
    app.run(debug=True,port=4000)


@app.route('/inicio',methods=['GET'])
@cross_origin()
def inicio():
    inciovacunacion = []
    finvacunacion = []
    
    for dato in datos:
        inciovacunacion.append(dato['field25']) 
        finvacunacion.append(dato['field64'])

    return jsonify(
        
        {
            'fechadelaprimera_vacunacion':inciovacunacion[0],
            'primera_vacunacion_porcentaje':inciovacunacion[1],
            'fechadelaultima_vacunacion':finvacunacion[1],
            'ultima_vacunacion_porcentaje':finvacunacion[0]
        })


@app.route('/ultimosvacunados',methods=['GET'])
@cross_origin()
def ultimos10():
    ultimosVacunados = []
    fechaUltimosvacunados=[]
    
    i=0
    
    for dato in datos:
        if i==0:
            
            for x in range(54, 64):
                fechaUltimosvacunados.append(dato['field'+str(x)])
            
        if i==1:
            
             for x in range(54, 64):
                ultimosVacunados.append(dato['field'+str(x)])
                
        i=i+1      
    
    return jsonify(
        
        {
            
            'ultimas_10_vacunaciones_porcentaje':fechaUltimosvacunados,
            'fechas_de_las_10_ultimas_vacunaciones':ultimosVacunados,

        })

@app.route('/primerosvacunados',methods=['GET'])
@cross_origin()
def primeros10():
    
    primerosVacunados = []
    fechaprimerosvacunados=[]
    
    i=0
    
    for dato in datos:
        if i==0:
            
            for x in range(25, 35):
                fechaprimerosvacunados.append(dato['field'+str(x)])
            
        if i==1:
            
             for x in range(25, 35):
                primerosVacunados.append(dato['field'+str(x)])
                
        i=i+1      
    
    return jsonify(
        
        {
            
            'primeros_10_vacunaciones_porcentaje':primerosVacunados,
            'fechas_de_los_10_primeras_vacunaciones':fechaprimerosvacunados,

        })

@app.route('/ping',methods=['GET'])
def ping():
    return 'Pong!'


@app.route('/data',methods=['GET'])
@cross_origin()
def data():
    return jsonify({'data':datos}) 
