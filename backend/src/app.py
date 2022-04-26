import falcon
from mongoengine import connect
from .endpoints import Paths, Path

connect('pathsdb', host='127.0.0.1', port=27017)

app = application = falcon.API()

paths = Paths()
path = Path()

app.add_route('/paths', paths)
app.add_route('/paths/{user_id}', paths)
app.add_route('/path/{path_id}', path)
