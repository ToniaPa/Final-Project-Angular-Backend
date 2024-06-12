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
def update_worker(afm):
    try:
        # data = request.get_json() # = problem!
        data = request.get_json
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
        workers = Worker.objects.exclude('id')       
        # workers = Worker.objects.all()        
        workers_list = [worker.to_mongo().to_dict() for worker in workers]
        if (workers_list):     
            return Response(json.dumps(workers_list), status=200)
            #  return Response(json.dumps(workers_list, default=str), status=200)   
        return Response(json.dumps({"msg": "Collection Workers is empty"}), status=404)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)    


@worker.route("/afm/<string:afm>", methods=["DELETE"])
# @jwt_required()
def delete_worker(afm):
    try:
        # data = request.get_json() # = problem!
        data = request.get_json        
        Worker.objects(afm=afm).delete()        
        return Response(json.dumps({"msg": "Worker deleted successfully!"}), status=200)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)
    

    # data = request.get_json()
    # print("def delete_worker, data: ", data)    
    # print("def delete_worker, AFM:", afm) 
    # try:       
    #     result = Worker.delete_one({"afm": afm})
    #     print(result.deleted_count)
    #     return Response(json.dumps({"msg": "Worker was deleted successfully"}), status=200)    
    # except Exception as e:
    #     print("from exception:", e)
    #     return Response(json.dumps({"msg": str(e)}), status=400)

# # @worker.route("/delete/<string:worker_id>", methods=["DELETE"])
# @worker.route("/delete/afm/<string:afm>", methods=['GET','DELETE', 'POST'])
# # @jwt_required()
# def delete_worker(afm):
#     data = request.get_json()
#     print("def delete_worker, data: ", data)    
#     print("def delete_worker, AFM:", afm) 
#     try:
#         # data = request.get_json()
#         # print(data)        
#         # Worker(**data).delete()
#         # Worker.objects(_id=worker_id).delete_one(**data)
#         # Worker.objects(afm=afm).delete_one(**data)
#         # Worker.delete_one(afm=afm)
#         result = Worker.delete_one({"afm": afm})
#         print(result.deleted_count)
#         return Response(json.dumps({"msg": "Worker deleted successfully"}), status=200)    
#     except Exception as e:
#         print("from exception:", e)
#         return Response(json.dumps({"msg": str(e)}), status=400)
    

    
# @worker.route("/check_duplicate_email/<string:email>", methods=["GET"])
# def check_duplicate_email(email):
#     try:
#         if Worker.objects(email=email):
#             return Response(json.dumps({"msg": "Email already in use (backend)"}), status=400)
#         return Response(json.dumps({"msg": "Email available (backend)"}), status=200)
#     except Exception as e:
#         print(e)
#         return Response(json.dumps({"msg": str(e)}), status=400)
    

# @worker.route("/check_duplicate_afm/<string:afm>", methods=["GET"])
# def check_duplicate_afm(afm):
#     try:
#         if Worker.objects(afm=afm):
#             return Response(json.dumps({"msg": "AFM already in use (backend)"}), status=400)
#         return Response(json.dumps({"msg": "AFM available (backend)"}), status=200)
#     except Exception as e:
#         print(e)
#         return Response(json.dumps({"msg": str(e)}), status=400)