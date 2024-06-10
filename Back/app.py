# -*- coding: utf-8 -*-
from flask import Flask,request, jsonify
# config import
from config import app_config, app_active
#
from flask_restful import Resource, Api
from sqlalchemy import create_engine, text
from json import dumps
from flask_cors import CORS,cross_origin
# from flask_restplus import Api

config = app_config[app_active]

db_connect = create_engine('mysql+mysqlconnector://root@localhost/fatec')
#db_connect = create_engine('mysql+mysqlconnector://admin:admin@192.168.13.236/fatec').

def create_app(config_name):

    app = Flask(__name__, template_folder='templates')

    # api = Api(app,
    #           version='1.0',
    #           title='Sensores Arduino',
    #           description='Api simples de monitoramento',
    #           doc='/docs')
    #http://localhost:5000/monitoramento 
    #http://10.0.0.215:5000/monitoramento
    #http://nitro-carlao:5000/monitoramento
    # net::ERR_CONNECTION_REFUSED
    cors = CORS(app, resources={r'/monitoramento/*':{'origins':'*'}})

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    # app.config['CORS_HEADERS'] = 'Content-Type'    
    # rota basica 
    @app.route('/', methods=["GET"])
    def test():
        result = "Ola mundo"
        return result
    
    @app.route('/monitoramento/grafico1', methods=['GET'])
    def TotalizacaoRegistro():
       conn = db_connect.connect()
       query = conn.execute(text('SELECT dispositivo, COUNT(dispositivo) as TotalRegistros FROM monitoramento GROUP BY dispositivo limit 10'))
       conn.commit()
       result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
       conn.close()
       return jsonify(result)

    @app.route('/monitoramento', methods=['POST', 'GET', 'DELETE', 'PUT'])
    def users():
        # origin = request.headers.get('Origin')
        if ( request.method == "POST" ):
            conn = db_connect.connect()
            temperatura = request.json['temperatura']
            umidade = request.json['umidade']
            dispositivo = request.json['dispositivo']        
            luminosidade = request.json['luminosidade']
            conn.execute(text("insert into monitoramento (temperatura, umidade, dispositivo, luminosidade ) values ( '{0}', '{1}', '{2}' , '{3}')".format(temperatura, umidade, dispositivo,luminosidade)))        
                    
            #
            query = conn.execute(text('select * from monitoramento ORDER BY id DESC LIMIT 1'))
            conn.commit()
            result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
            #
            return jsonify(result) 
        
        elif ( request.method == "GET" ):
            conn = db_connect.connect()
            query = conn.execute(text('select * from monitoramento order by id DESC limit 10'))
            conn.commit()
            result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]

            # response = jsonify(result)
            # response.headers.add('Access-Control-Allow-Credentials', 'false')
            # response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            # response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
            # response.headers.add('Access-Control-Allow-Origin', origin)
            #net::ERR_CONNECTION_REFUSED
            return jsonify(result)
            #return "ola"
            #return response
 
        elif ( request.method == "PUT" ):
            conn = db_connect.connect()
            id_ = request.json['id']
            temperatura = request.json['temperatura']
            umidade = request.json['umidade']
            dispositivo = request.json['dispositivo'] 
            luminosidade = request.json['luminosidade'] 
            query = conn.execute(text("update monitoramento set temperatura = '{0}' , umidade = '{1}' , dispositivo = '{2}' , luminosidade = '{3}' where Id = {4}".format(temperatura, umidade, dispositivo, luminosidade, id_)))
            conn.commit()        
            query = conn.execute(text('select * from monitoramento order by temperatura'))
            result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]        
            return jsonify(result) 
        
        elif ( request.method == "DELETE" ):
            conn = db_connect.connect()
            id_ = request.json['id']
            query = conn.execute(text("delete from monitoramento where Id = {0}".format(id_)))
            conn.commit()        
            query = conn.execute(text('select * from monitoramento order by temperatura'))
            result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]        
            return jsonify(result) 
        

    @app.route('/monitoramento/<id>', methods=['GET'])
    # @cross_origin()
    def usersID(self, id):
        if ( request.method == "GET" ):
            conn = db_connect.connect()
            query = conn.execute(text('select * from monitoramento order by temperatura'))
            result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
            return jsonify(result)
    
    return app
