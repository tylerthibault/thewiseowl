from flask_app import app
from flask_app.controllers import controller_routes
from flask_app.controllers.people import controller_family, controller_kiddo, controller_parent
 

# keep this at the bottom of this file!!
if __name__=="__main__":	 
    app.run(debug=True)	