import falcon
import mongoengine as mongo

# Resources
from resources.tvseries.controller import torrent

# Middleware
import middlewares

# Init falcon app
app = falcon.API(middleware=[
    middlewares.JSONTranslator()
])

# DB
mongo.connect('torrent')

# Routes
app.add_route('/search/{show}', torrent)
