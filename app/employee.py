from flask import Flask,request,Blueprint,jsonify
from datetime import datetime
from flask_jwt_extended import create_access_token
from app import db,ma,Todo
from flask_jwt_extended import jwt_required
from flask_jwt_extended import current_user

employee_bp =Blueprint('employee',__name__)

class Employee(db.Model):
    emp_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    job_desc = db.Column(db.String(100))
    salary = db.Column(db.String(100))
    employee_id = db.Column(db.String(100))
    branch_id = db.Column(db.String(100))
    datetime = db.Column(db.DateTime,default = datetime.utcnow)

class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('emp_id','name','email','job_desc','salary','employee_id','branch_id','dateTime')
employeeSchema=EmployeeSchema()

class Todoschema(ma.Schema):
    class Meta:
        fields = ('id','task','datatime')
todoschema=Todoschema(exclude=['id','datatime'])


@employee_bp.route('/empolyee_add',methods=['POST'])
def employee_add():
    data = request.get_json()
    name = data['name']
    email = data['email']
    job_desc = data['job_desc']
    salary = data['salary']
    employee_id = data['employee_id']
    branch_id = data['branch_id']
    new_employee = Employee(name=name,email=email,job_desc=job_desc,salary=salary,employee_id=employee_id,branch_id=branch_id)
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({"status":"success"})

@employee_bp.route('/employee_read',methods=['GET'])
def employee_read():
    read_employee = Employee.query.all()
    result = employeeSchema.jsonify(read_employee,many=True)
    return result

# filter query
@employee_bp.route('/filter',methods=['GET'])
def filter():
    try:
        employee_id = request.json['employee_id'] 
        filter_employee = Employee.query.filter(Employee.employee_id != employee_id).all()
        result = employeeSchema.jsonify(filter_employee,many=True)
        return result
    except Exception as e:
            return str(e)


# join query
@employee_bp.route('/join',methods=['GET'])
def join():
    # join_table = Employee.query.join(Todo,Employee.branch_id == Todo.id).filter(Employee.emp_id == 1).all()
    # result =employeeSchema.jsonify(join_table,many=True)
    join_table = Todo.query.join(Employee,Todo.id == Employee.branch_id).filter(Todo.id == 1).all()
    result =todoschema.jsonify(join_table,many=True)
    return result

# login query 
@employee_bp.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    name = data['name']
    email = data['email']
    employee_table = Employee.query.filter_by(name=name,email=email).first()
    
    if employee_table:
        access_token = create_access_token(identity=employee_table.emp_id)
        return jsonify(access_token=access_token)
    
    return "please check in login details and try again."

@employee_bp.route("/user_id", methods=["GET"])
@jwt_required()
def protected():
    # We can now access our sqlalchemy User object via `current_user`.
    return jsonify(current_user.emp_id)


# date filter query
@employee_bp.route('/date_filter',methods=['POST'])
def datafilter():
    data = request.get_json()
    start_date = data['start_date']
    end_date = data['end_date']
    records = Employee.query.filter(Employee.datetime.between(start_date,end_date)).all()
    result = employeeSchema.jsonify(records,many=True)
    return result


 # check if someone already register with the email
@employee_bp.route('/already_register',methods=['POST'])
def already_exists():
    data = request.get_json()
    name = data['name']
    email = data['email']
    job_desc = data['job_desc']
    salary = data['salary']
    employee_id = data['employee_id']
    branch_id = data['branch_id']

    email_exists = Employee.query.filter_by(email=email).first()
    if not email_exists:
        new_employee = Employee(name=name,email=email,job_desc=job_desc,salary=salary,employee_id=employee_id,branch_id=branch_id)
        db.session.add(new_employee)
        db.session.commit()
        return "Create new employee"
    else:
        return "This email_id alreay_register"