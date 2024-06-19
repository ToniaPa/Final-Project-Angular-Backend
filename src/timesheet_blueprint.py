from bson import ObjectId
from flask import Blueprint, request, Response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.timesheet_model import Timesheet
import json
from mongoengine.errors import NotUniqueError

timesheet = Blueprint("timesheet", __name__)

@timesheet.route("/create", methods=["POST"])
# @jwt_required()
def add_timesheet():
    try:
        data = request.get_json()
        print(data)        
        Timesheet(**data).save()
        return Response(json.dumps({"msg": "Timesheet added"}), status=201)
    except NotUniqueError:
        return Response(json.dumps({"msg": "Timesheet already in use"}), status=400)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)


@timesheet.route("/date/<date:dateOfWork>", methods=["GET"])
# @jwt_required()
def get_timesheets_by_date(dateOfWork):
    try:
        timesheets = Timesheet.objects(dateOfWork=dateOfWork).all()        
        timesheets_list = [timesheet.to_mongo().to_dict() for timesheet in timesheets]
        if (timesheets_list):     
            # return Response(json.dumps(timesheets_list), status=200)
             return Response(json.dumps(timesheets_list, default=str), status=200)   
        return Response(json.dumps({"msg": "Collection Timesheets is empty"}), status=404)
        # timesheet = Timesheet.objects(dateOfWork=dateOfWork).all()
        # if timesheet:
        #     return Response(json.dumps(timesheet.to_mongo()), status=200)
        # return Response(json.dumps({"msg": "Timesheets for given date not found"}), status=404)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)


@timesheet.route("/workerafm/<string:afm>", methods=["GET"])
def get_timesheets_by_worker_afm(workerAfm):
    try:
        timesheet = Timesheet.objects(workerAfm=workerAfm).exclude("id").first()
        if timesheet:
            return Response(json.dumps(timesheet.to_mongo()), status=200)
        return Response(json.dumps({"msg": "Timesheet for worker not found"}), status=404)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)
    
@timesheet.route("/clientafm/<string:afm>", methods=["GET"])
def get_timesheets_by_client_afm(clientAfm):
    try:
        timesheet = Timesheet.objects(clientAfm=clientAfm).exclude("id").first()
        if timesheet:
            return Response(json.dumps(timesheet.to_mongo()), status=200)
        return Response(json.dumps({"msg": "Timesheet for client not found"}), status=404)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)


@timesheet.route("/", methods=["GET"])
# @jwt_required()
def get_all_timesheets():    
    try:        
        # workers = Worker.objects.exclude('id')       
        timesheets = Timesheet.objects.all()        
        timesheets_list = [timesheet.to_mongo().to_dict() for timesheet in timesheets]
        if (timesheets_list):     
            # return Response(json.dumps(timesheets_list), status=200)
             return Response(json.dumps(timesheets_list, default=str), status=200)   
        return Response(json.dumps({"msg": "Collection Timesheets is empty"}), status=404)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)   
    

@timesheet.route("/id/<string:id>", methods=["PATCH"])
def update_timesheet_by_id(id):
    try:
        data = request.get_json() 
        # data = request.get_json # = problem for update
        print(data)
        Timesheet.objects(_id=ObjectId(id)).update_one(**data)
        return Response(json.dumps({"msg": "Timesheet updated"}), status=200)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400) 


@timesheet.route("/id/<string:id>", methods=["DELETE"])
# @jwt_required()
def delete_timesheet_by_id(id):
    try:
        # data = request.get_json() # = problem for delete!
        data = request.get_json        
        Timesheet.objects(_id=ObjectId(id)).delete()        
        return Response(json.dumps({"msg": "Timesheet deleted successfully!"}), status=200)
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


    
