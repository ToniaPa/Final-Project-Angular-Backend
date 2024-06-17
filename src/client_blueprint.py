from bson import ObjectId
from flask import Blueprint, request, Response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.client_model import Client
import json
from mongoengine.errors import NotUniqueError

client = Blueprint("client", __name__)

@client.route("/create", methods=["POST"])
# @jwt_required()
def add_client():
    try:
        data = request.get_json()
        print(data)        
        Client(**data).save()
        return Response(json.dumps({"msg": "Client added"}), status=201)
    except NotUniqueError:
        return Response(json.dumps({"msg": "Email or AFM already in use"}), status=400)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)


@client.route("/email/<string:email>", methods=["GET"])
# @jwt_required()
def get_client_by_email(email):
    try:
        client = Client.objects(email=email).first()
        if client:
            return Response(json.dumps(client.to_mongo()), status=200)
        return Response(json.dumps({"msg": "Client not found"}), status=404)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)


@client.route("/afm/<string:afm>", methods=["GET"])
def get_client_by_afm(afm):
    try:
        client = Client.objects(afm=afm).exclude("id").first()
        if client:
            return Response(json.dumps(client.to_mongo()), status=200)
        return Response(json.dumps({"msg": "Client not found"}), status=404)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)


@client.route("/afm/<string:afm>", methods=["PATCH"])
def update_client_by_afm(afm):
    try:
        data = request.get_json() 
        # data = request.get_json # = problem for update
        print(data)
        Client.objects(afm=afm).update_one(**data)
        return Response(json.dumps({"msg": "Client updated"}), status=200)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)


###

@client.route("/", methods=["GET"])
# @jwt_required()
def get_all_clients():    
    try:        
        # client = Client.objects.exclude('id')       
        clients = Client.objects.all()        
        clients_list = [client.to_mongo().to_dict() for client in clients]
        if (clients_list):     
            # return Response(json.dumps(clients_list), status=200)
             return Response(json.dumps(clients_list, default=str), status=200)   
        return Response(json.dumps({"msg": "Collection Clients is empty"}), status=404)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)    


@client.route("/afm/<string:afm>", methods=["DELETE"])
# @jwt_required()
def delete_client(afm):
    try:
        # data = request.get_json() # = problem for delete!
        data = request.get_json        
        Client.objects(afm=afm).delete()        
        return Response(json.dumps({"msg": "Client deleted successfully!"}), status=200)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)


#  // id is undefined.... => δεν έχω την τιμή του...!
# @client.route("/afm/<string:_id>", methods=["PATCH"])
# def update_client_by_id(id):
#     try:
#         data = request.get_json() 
#         # data = request.get_json # = problem for update
#         print("data =", data)
#         print("id =", id)
#         # data1 = Client.objects.all()  
#         # client1 = json.dumps(data1, default=str)
#         # print(data1)

#         Client.objects(_id=ObjectId(id)).update_one(**data)
#         return Response(json.dumps({"msg": "Client updated"}), status=200)
#     except Exception as e:
#         print(e)
#         return Response(json.dumps({"msg": str(e)}), status=400)


    
