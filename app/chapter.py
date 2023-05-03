from flask import Flask,request,Blueprint
from datetime import datetime
from app import db,ma

chapter_bp =Blueprint('chapter',__name__)

class Chapter(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    lession = db.Column(db.String(100))
    topic = db.Column(db.String(100))
    datatime = db.Column(db.DateTime,default = datetime.utcnow)


# chapter
class Chapterschema(ma.Schema):
    class Meta:
        fields = ('id','lession','topic','datatime')
chapterschema=Chapterschema()

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@chapter_bp.route('/chapter_add',methods=['POST'])
def chapter_add():
    data = request.get_json()
    add_lession = data['lession']
    add_topic = data['topic']
    add_chapter = Chapter(lession=add_lession,topic = add_topic)
    db.session.add(add_chapter)
    db.session.commit()
    return "Create new chapter Successfully"

@chapter_bp.route('/chapter_read',methods=['GET'])
def chapter_read():
    read_chapter = Chapter.query.all()
    result = chapterschema.jsonify(read_chapter,many=True)
    return result

@chapter_bp.route('/chapter_update/<id>',methods=['PUT'])
def chapter_update(id):
    update = Chapter.query.get(id)
    update.lession = request.json['lession']
    update.topic = request.json['topic']
    db.session.commit()
    return "update successfully"

@chapter_bp.route('/chapter_delete/<id>',methods=['POST'])
def chapter_delete(id):
    delete = Chapter.query.get(id)
    db.session.delete(delete)
    db.session.commit()
    return "Data delete successfully"



