import falcon, json
from .models import PathModel

import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)



class Paths(object):
    #Liste des paths d'un user
    def on_get(self,req,resp,user_id):
        '''
        :param req: A request object
        :param resp: A response object
        :param user_id: user_id received in http path to query parcours object
        :return:
        '''
        paths_obj= PathModel.objects(user_id=user_id)
        print(paths_obj)
        #Query book collection to get a record with user_id 
        list_paths = []
        for path in paths_obj:
            path_details ={
                "id": str( path["id"]),
                "user_id": path["user_id"],
                "name": path["name"]
            }
            list_paths.append(path_details)

        resp.body = json.dumps({'status': falcon.HTTP_200, 'message': 'paths succesfully get', 'paths': list_paths})
        #It will set response body as a json object of book fields.
        resp.status = falcon.HTTP_200
        #Finally return 200 response on success

    def on_post(self,req,resp):
        '''
         This method will recevie the book data in request body in order to store it in database
        :param req: It contains json of parcours's name .......
        :param resp:
        :return:
        '''
        paths_data = req.media
        #req.media will deserialize json object
        paths_obj=PathModel.objects.create(**paths_data)
        #passing book_data to create method. It will create a database document in book collection.
        resp.body = json.dumps({'status': falcon.HTTP_200, 'message': 'paths succesfully created', 'path':str(paths_obj.id)})
        resp.status=falcon.HTTP_200

#Detail d'un path donné
class Path(object):
    def on_get(self,req,resp,path_id):
        '''
        :param req: A request object
        :param resp: A response object
        :param book_id: path received in http path to query paths object
        :return:
        '''
        path_obj= PathModel.objects.get(id=path_id)
        path_details={
            "user_id": path_obj["user_id"],
            "name": path_obj["name"]
        }
        
        #Query paths collection to get a record with id = 
        resp.body = json.dumps({'status': falcon.HTTP_200, 'message': 'paths succesfully get', "path": path_details})
        #It will set response body as a json object of book fields.
        resp.status = falcon.HTTP_200
        #Finally return 200 response on success