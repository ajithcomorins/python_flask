from flask import Flask,request,Blueprint,jsonify
from flask_sqlalchemy import SQLAlchemy
from app import db,ma
from datetime import datetime


todo_bp =Blueprint('todo',__name__)


class Todolist(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    task = db.Column(db.String(100))
    datatime= db.Column(db.DateTime,default = datetime.utcnow)
    

# todo
class Todolistschema(ma.Schema):
    class Meta:
        fields = ('id','task','datatime')
todolistschema=Todolistschema()



@todo_bp.route('/todo_add',methods=['POST'])
def add():
    data = request.get_json()
    add_task = data['task']
    todo = Todolist(task=add_task)
    db.session.add(todo)
    db.session.commit()
    return "success"

@todo_bp.route('/todo_read',methods=['GET'])
def read():
    todo = Todolist.query.all()
    result = todolistschema.jsonify(todo,many=True)
    return result

@todo_bp.route('/todo_update',methods=['PUT'])
def update():
    update = Todolist.query.get(request.json['id'])
    update.task = request.json['task']
    db.session.commit()
    return jsonify({"status":"success"})

@todo_bp.route('/todo_delete/<id>',methods=['POST'])
def delete(id):
    delete = Todolist.query.get(id)
    db.session.delete(delete)
    db.session.commit()

    return "status:success"


