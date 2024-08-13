from flask import Blueprint

app = Blueprint('app', __name__)

# Define the routes and their corresponding controller methods
@app.route('/users', methods=['GET'])
def index():
    from app.Http.Controllers.user_controller import UserController
    return UserController().index()

@app.route('/users/<int:user_id>', methods=['GET'])
def show(user_id):
    from app.Http.Controllers.user_controller import UserController
    return UserController().show(user_id)

@app.route('/users/create', methods=['GET', 'POST'])
def create():
    from app.Http.Controllers.user_controller import UserController
    return UserController().create()

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit(user_id):
    from app.Http.Controllers.user_controller import UserController
    return UserController().edit(user_id)

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete(user_id):
    from app.Http.Controllers.user_controller import UserController
    return UserController().delete(user_id)
