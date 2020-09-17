# FlaskApp
Flask api to store and get  data using mongodb

http:localhost:5000/add :- Add data into database.If there are any duplicate key('name') entry then it will return the duplicate names with error code 400 .

http:localhost:5000/show :- Retrive all stored data values from database .If database is empty then it will return [] with response code 200 otherwise it will return all data with response code 200

If server failure occure then it will return Error code 500
