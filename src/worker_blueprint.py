from bson import ObjectId
from flask import Blueprint, request, Response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.worker_model import Worker
import json
from mongoengine.errors import NotUniqueError

worker = Blueprint("worker", __name__)

@worker.route("/create", methods=["POST"])
# @jwt_required()
def add_worker():
    try:
        data = request.get_json()
        print(data)        
        Worker(**data).save()
        return Response(json.dumps({"msg": "Worker added"}), status=201)
    except NotUniqueError:
        return Response(json.dumps({"msg": "Email or AFM already in use"}), status=400)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)


@worker.route("/email/<string:email>", methods=["GET"])
# @jwt_required()
def get_worker_by_email(email):
    try:
        worker = Worker.objects(email=email).first()
        if worker:
            return Response(json.dumps(worker.to_mongo()), status=200)
        return Response(json.dumps({"msg": "Worker not found"}), status=404)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)


@worker.route("/afm/<string:afm>", methods=["GET"])
def get_worker_by_afm(afm):
    try:
        worker = Worker.objects(afm=afm).exclude("id").first()
        if worker:
            return Response(json.dumps(worker.to_mongo()), status=200)
        return Response(json.dumps({"msg": "Worker not found"}), status=404)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)


@worker.route("/afm/<string:afm>", methods=["PATCH"])
def update_worker_by_afm(afm):
    try:
        data = request.get_json() 
        # data = request.get_json # = problem for update
        print(data)
        Worker.objects(afm=afm).update_one(**data)
        return Response(json.dumps({"msg": "Worker updated"}), status=200)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)


###

@worker.route("/", methods=["GET"])
# @jwt_required()
def get_all_workers():    
    try:        
        # workers = Worker.objects.exclude('id')       
        workers = Worker.objects.all()        
        workers_list = [worker.to_mongo().to_dict() for worker in workers]
        if (workers_list):     
            # return Response(json.dumps(workers_list), status=200)
             return Response(json.dumps(workers_list, default=str), status=200)   
        return Response(json.dumps({"msg": "Collection Workers is empty"}), status=404)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)    


@worker.route("/afm/<string:afm>", methods=["DELETE"])
# @jwt_required()
def delete_worker(afm):
    try:
        # data = request.get_json() # = problem for delete!
        data = request.get_json        
        Worker.objects(afm=afm).delete()        
        return Response(json.dumps({"msg": "Worker deleted successfully!"}), status=200)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)


#  // id is undefined.... => δεν έχω την τιμή του...!
# @worker.route("/afm/<string:_id>", methods=["PATCH"])
# def update_worker_by_id(id):
#     try:
#         data = request.get_json() 
#         # data = request.get_json # = problem for update
#         print("data =", data)
#         print("id =", id)
#         # data1 = Worker.objects.all()  
#         # worker1 = json.dumps(data1, default=str)
#         # print(data1)

#         Worker.objects(_id=ObjectId(id)).update_one(**data)
#         return Response(json.dumps({"msg": "Worker updated"}), status=200)
#     except Exception as e:
#         print(e)
#         return Response(json.dumps({"msg": str(e)}), status=400)


    
