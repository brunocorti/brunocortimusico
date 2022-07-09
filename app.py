from flask import Flask ,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)
CORS(app)
# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://sql10505112:k6mZvI1jN9@sql10.freesqldatabase.com/sql10505112'
#                                               user:clave@localhost/nombreBaseDatos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
ma=Marshmallow(app)
# defino la tabla
class Fecha(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    dia=db.Column(db.Integer)
    mes=db.Column(db.Integer)
    locacion=db.Column(db.String(100))
    lugar=db.Column(db.String(100))
    direccion=db.Column(db.String(100))
    horario=db.Column(db.String(100))
    def __init__(self,dia,mes,locacion,lugar,direccion,horario):   #crea el  constructor de la clase
        self.dia=dia   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.mes=mes
        self.locacion=locacion
        self.lugar=lugar
        self.direccion=direccion
        self.horario=horario

db.create_all()  # crea las tablas
#  ************************************************************
class FechaSchema(ma.Schema):
    class Meta:
        fields=('id','dia','mes','locacion','lugar','direccion','horario')
fecha_schema=FechaSchema()            # para crear un producto
fechas_schema=FechaSchema(many=True)  # multiples registros
@app.route('/',methods=['GET'])
def get_Fechas():
    all_fechas=Fecha.query.all()     # query.all() lo hereda de db.Model
    result=fechas_schema.dump(all_fechas)  # .dump() lo hereda de ma.schema
    return jsonify(result)
@app.route('/fechas/<id>',methods=['GET'])
def get_fecha(id):
    fecha=Fecha.query.get(id)
    return fecha_schema.jsonify(fecha)

@app.route('/', methods=['POST']) # crea ruta o endpoint
def create_fecha():
    print(request.json)  # request.json contiene el json que envio el cliente
    dia=request.json['dia']
    mes=request.json['mes']
    locacion=request.json['locacion']
    lugar=request.json['lugar']
    direccion=request.json['direccion']
    horario=request.json['horario']
    new_fecha=Fecha(dia,mes,locacion,lugar,direccion,horario)
    db.session.add(new_fecha)
    db.session.commit()
    return fecha_schema.jsonify(new_fecha)

@app.route('/' ,methods=['PUT'])
def update_fecha(id):
    fecha=Fecha.query.get(id)
   
    dia=request.json['dia']
    mes=request.json['mes']
    locacion=request.json['locacion']
    lugar=request.json['lugar']
    direccion=request.json['direccion']
    horario=request.json['horario']

    fecha.dia=dia
    fecha.mes=mes
    fecha.locacion=locacion
    fecha.lugar=lugar
    fecha.direccion=direccion
    fecha.horario=horario
    db.session.commit()
    return fecha_schema.jsonify(fecha)

@app.route('/',methods=['DELETE'])
def delete_fecha(id):
    fecha=Fecha.query.get(id)
    db.session.delete(fecha)
    db.session.commit()
    return fecha_schema.jsonify(fecha)
# programa principal
if __name__=='__main__':  
    app.run(debug=True, port=5000)  