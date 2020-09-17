from flask import json
import pymongo
from pymongo import MongoClient




class MongoApi:
    #INITIALIZE AND CONNECT DATABASE
    def __init__(self,data):
        self.__client=MongoClient('localhost',27017)
        database = data['database']
        collection = data['collection']
        cursor = self.__client[database]
        self.collection = cursor[collection]
        self.data = data
        self.err=[]
    
    #SERVICE TO ADD DATA INTO DATABASE

    def add_data(self,data):
        self.err=[]
        flag=False
        addflag=False
        new_doc=data
        length=len(new_doc)
        if length > 0 :
                for i in range(length):
                    try :
                        doc1=new_doc[i]
                        r1=list(self.collection.find({"name" : doc1["name"]}))
                        if len(r1)>0 :
                            flag=True
                            raise NameError()
                    except NameError:
                        self.err.append({"name" : doc1['name']});
                    except :
                         return {
                                'status' : 'Server Error',
                                'status ID' : 500
                            }
                try:
                    if not flag:
                        responses=self.collection.insert_many(new_doc)
                except :
                    return {
                                'status' : 'Server Error',
                                'status ID' : 500
                            }   

        if len(self.err)>0:
            return {
                        'status' : "Few data are already present.",
                        'status ID' : 400,
                        'duplicate_values' : self.err
                   }
        else:
            return {
                        'status' : 'Data inserted Successfully',
                        'status ID' : 200
                   }    




    #SERVICE TO GET DATA FROM DATABASE

    def get_all_data(self):
        try :
            self.data=list(self.collection.find({},projection={'_id': False}))
            if self.data:
                return {
                        "status" : "Successfull",
                        "status ID" : 200,
                        "alldata" : self.data
                    } 
            else:
                 return {
                        "status" : "Successfull",
                        "status ID" : 200,
                        "alldata" : []
                    }        
        except :
            return {
                        'status' : 'Server Error',
                        'status ID' : 500
                }
                    
