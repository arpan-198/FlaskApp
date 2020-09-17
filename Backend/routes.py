from Backend import app
from flask import  request,  Response , json
from .Database.db import MongoApi
from .Database.model import DataModel
from .Database.database_info import database_Info

#API ROUTE TO ADD DATA 

@app.route('/add',methods=['POST'])
def store_data():
    if request.method == "POST":
        model=DataModel()
        data=request.json
        if data is None or data == [] or (not model.check(data)):
            return Response(response=json.dumps({"Error": "Please provide correct data"}),
                            status=400,
                            mimetype='application/json')
        mongo_obj = MongoApi(database_Info)
        response=mongo_obj.add_data(data)
        resID=response['status ID']
        convertresponse=json.dumps(response);
        return Response(response=convertresponse,
                    status=resID,
                    mimetype='application/json')
    
    
#API ROUTE TO GET DATA 


@app.route('/show',methods=['GET'])
def show_data():
    if request.method == "GET":
        mongo_obj = MongoApi(database_Info)
        response=mongo_obj.get_all_data()
        resID=response['status ID']
        return Response(response=json.dumps(response['alldata']),
                    status=resID,
                    mimetype='application/json')