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


@timesheet.route("/", methods=["GET"])
# @jwt_required()
def get_all_timesheets():    
    try:        
        # timesheets = Timesheet.objects.exclude('id')       
        timesheets = Timesheet.objects.all()        
        timesheets_list = [timesheet.to_mongo().to_dict() for timesheet in timesheets]
        if (timesheets_list):     
            # return Response(json.dumps(timesheets_list), status=200)
             return Response(json.dumps(timesheets_list, default=str), status=200)   
        return Response(json.dumps({"msg": "Collection Timesheets is empty"}), status=404)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)   
    

@timesheet.route("/id/<string:id>", methods=["DELETE"])
# @jwt_required()
def delete_timesheet_by_id(id):
    try:
        print(id)
        # data = request.get_json() # = problem for delete!
        data = request.get_json        
        Timesheet.objects(pk=id).delete()        
        return Response(json.dumps({"msg": "Timesheet deleted successfully!"}), status=200)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)


