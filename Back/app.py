from flask import Flask, request, jsonify

from config import app_config, app_active

from flask_restful import Resource, Api
from sqlalchemy import create_engine, text
from json import dumps
from flask_cors import CORS, cross_origin


config = app_config[app_active]

db_connect = create_engine("mysql+mysqlconnector://root@localhost/fatec")


def create_app(config_name):

    app = Flask(__name__, template_folder="templates")


    cors = CORS(app, resources={r"/monitoramento/*": {"origins": "*"}})

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")

    @app.route("/", methods=["GET"])
    def test():
        result = "Ola mundo"
        return result

    @app.route("/monitoramento/grafico1", methods=["GET"])
    def TotalizacaoRegistro():
        conn = db_connect.connect()
        query = conn.execute(
            text(
                "SELECT dispositivo, COUNT(dispositivo) as TotalRegistros FROM monitoramento GROUP BY dispositivo limit 20"
            )
        )
        conn.commit()
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        conn.close()
        return jsonify(result)

    @app.route("/monitoramento/graficopizza", methods=["GET"])
    def GraficoPizza():
        conn = db_connect.connect()
        query = conn.execute(
            text(
                "SELECT dispositivo, COUNT(dispositivo) as TotalRegistros FROM monitoramento GROUP BY dispositivo limit 20"
            )
        )
        conn.commit()
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        conn.close()
        return jsonify(result)

    @app.route("/monitoramento/graficomedidor", methods=["GET"])
    def GraficoMedidor():
        conn = db_connect.connect()
        query = conn.execute(
            text(
                "SELECT ROUND(AVG(temperatura),0) as MED_TEMPERATURA, ROUND(AVG(umidade),0) as MED_UMIDADE, ROUND(AVG(luminosidade),0) as MED_LUMINOSIDADE FROM MONITORAMENTO "
            )
        )
        conn.commit()
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        conn.close()
        return jsonify(result)

    @app.route("/monitoramento/graficobarra", methods=["GET"])
    def GraficoBarra():
        conn = db_connect.connect()
        query = conn.execute(
            text(
                "SELECT dispositivo, COUNT(dispositivo) as TotalRegistros FROM monitoramento GROUP BY dispositivo limit 20"
            )
        )
        conn.commit()
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        conn.close()
        return jsonify(result)

    @app.route("/monitoramento/graficolinhas", methods=["GET"])
    def GraficoLinhas():
        conn = db_connect.connect()
        query = conn.execute(
            text(
                "SELECT dispositivo, COUNT(dispositivo) as TotalRegistros FROM monitoramento GROUP BY dispositivo limit 20"
            )
        )
        conn.commit()
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        conn.close()
        return jsonify(result)

    @app.route("/monitoramento", methods=["POST", "GET", "DELETE", "PUT"])
    def users():
        if request.method == "POST":
            conn = db_connect.connect()
            temperatura = request.json["temperatura"]
            umidade = request.json["umidade"]
            dispositivo = request.json["dispositivo"]
            luminosidade = request.json["luminosidade"]
            conn.execute(
                text(
                    "insert into monitoramento (temperatura, umidade, dispositivo, luminosidade ) values ( '{0}', '{1}', '{2}' , '{3}')".format(
                        temperatura, umidade, dispositivo, luminosidade
                    )
                )
            )

            query = conn.execute(
                text("select * from monitoramento ORDER BY id DESC LIMIT 1")
            )
            conn.commit()
            result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
            return jsonify(result)

        elif request.method == "GET":
            conn = db_connect.connect()
            query = conn.execute(
                text("select * from monitoramento order by id DESC limit 20")
            )
            conn.commit()
            result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]

            return jsonify(result)


        elif request.method == "PUT":
            conn = db_connect.connect()
            id_ = request.json["id"]
            temperatura = request.json["temperatura"]
            umidade = request.json["umidade"]
            dispositivo = request.json["dispositivo"]
            luminosidade = request.json["luminosidade"]
            query = conn.execute(
                text(
                    "update monitoramento set temperatura = '{0}' , umidade = '{1}' , dispositivo = '{2}' , luminosidade = '{3}' where Id = {4}".format(
                        temperatura, umidade, dispositivo, luminosidade, id_
                    )
                )
            )
            conn.commit()
            query = conn.execute(
                text("select * from monitoramento order by temperatura")
            )
            result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
            return jsonify(result)

        elif request.method == "DELETE":
            conn = db_connect.connect()
            id_ = request.json["id"]
            query = conn.execute(
                text("delete from monitoramento where Id = {0}".format(id_))
            )
            conn.commit()
            query = conn.execute(
                text("select * from monitoramento order by temperatura")
            )
            result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
            return jsonify(result)

    @app.route("/monitoramento/<id>", methods=["GET"])
    def usersID(self, id):
        if request.method == "GET":
            conn = db_connect.connect()
            query = conn.execute(
                text("select * from monitoramento order by temperatura")
            )
            result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
            return jsonify(result)

    return app