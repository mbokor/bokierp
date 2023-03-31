from flask import Flask
from flask_restful import Api
from config import Config
from extensions import db
from flask_migrate import Migrate
from resources.todo import TodoListResource, TodoResource, TodoStatus_inArbeit
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)
api.add_resource(TodoListResource, "/todos")
api.add_resource(TodoResource, "/todo/<int:todo_id>")
api.add_resource(TodoStatus_inArbeit, "/todo/<int:todo_id>/in_Arbeit")

if __name__ == "__main__":
    app.run(port=5000, debug=True)