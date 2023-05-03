from flask import Flask,request,Blueprint,jsonify,Response
from flask_sqlalchemy import SQLAlchemy
import json
import os   # image path select
from app import db,ma,app
import base64
import io
import PIL.Image as Image

image_bp=Blueprint('image',__name__)


class Photo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  data = db.Column(db.LargeBinary)

class Imagechema(ma.Schema):
    class Meta:
        fields = ('id','name','data')
imagechema=Imagechema()

@image_bp.route('/photo_add', methods=['POST'])
def index():
  try:
    file = request.files['image']
    name = file.filename
    data = file.read()
    image = Photo(name=name, data=data)
    db.session.add(image)
    db.session.commit()
    return 'Image uploaded successfully!'
  except Exception as e:
        return str(e)


@image_bp.route('/image/<int:id>')
def get_image(id):
  image = Photo.query.get(id)
  if image:
    return Response(image.data, mimetype='image/jpeg')
  else:
    return 'Image not found'


@image_bp.route('/images_read',methods=['GET'])
def get_images():
  images = Photo.query.all()
  image_list = []
  for image in images:
    image_dict = {'id': image.id, 'name': image.name, 'data': base64.b64encode(image.data).decode()}
    image_list.append(image_dict)
  return {'images': image_list}

@image_bp.route('/decode',methods=['GET'])
def decode():
    images = Photo.query.all()
    image_list = []
    for image in images:
        image_dict = {'id': image.id, 'name': image.name, 'data': base64.b64encode(image.data).decode()}
        image_decode = image.data
        encode = Image.open(io.BytesIO(image_decode))
        show = encode.show()
        return show