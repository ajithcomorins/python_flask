from flask import Flask
import mysql.connector

con = mysql.connector(host='localhost', user='root',password='',database='python')

def insert

# from flask import Flask,render_template,request,redirect,url_for,flash,jsonify,session
# import mysql.connector
# app = Flask(__name__)
# app.secret_key = "mysecretkey"


# # @app.route('/<name>/<int:age>')
# # def home(name,age):
# #     return "welcome Mrs. {0} and your age is {1}".format(name,age)


# # @app.route('/sports/<int:id>')
# # def sports(id):
# #     return "Raina {0}".format(id)

# # @app.route('/')
# # def home():
# #     return render_template('index.html')

# # @app.route('/department')
# # def department():
# #     return render_template('dept.html')


# # @app.route('/about')
# # def about():
# #     return render_template('about.html')

# con = mysql.connector.connect(host='localhost', user='root',password='',database='python')

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/add_user',methods=['POST'])
# def add_user():
#     if request.method == 'POST':
#         try:
#             data = request.get_json()
#             user_name = data['name']
#             user_email = data['email']
#             res = con.cursor()
#             data_value =('insert into add_user (name,email) values (%s,%s)')
#             val = (user_name,user_email)  
#             res.execute(data_value,val)
#             con.commit()
#             return jsonify("success")
#         except Exception as e:
#             return str(e)

# @app.route('/update',methods=['PUT'])
# def update():
#     try:
#         data = request.get_json()
#         user_id = data['id']
#         user_name = data['name']
#         user_email = data['email']
#         res = con.cursor()
#         update_data = ('update add_user SET name=%s,email= %s WHERE id=%s')
#         val = (user_name,user_email,user_id)
#         res.execute(update_data,val)
#         con.commit()
#         return "update successfully"
#     except Exception as e:
#         return str(e)


# @app.route('/delete',methods=['DELETE'])
# def delete():
#     try:
#         data = request.get_json()
#         user_id = data['id']
#         res = con.cursor()
#         delete_data = ('delete from add_user WHERE id=%s')
#         val = [user_id]
#         res.execute(delete_data,val)
#         con.commit()
#         return "delete Successfully"
#     except Exception as e:
#         return str(e)


# @app.route('/select',methods=['GET'])
# def select():
#     try:
#         res = con.cursor()
#         select_data = ('select * from add_user')
#         res.execute(select_data)
#         all_value = res.fetchall()
#         return all_value
#     except Exception as e:
#         return str(e)



# @app.route('/login',methods=['POST'])
# def login():
#     try:
#         data = request.get_json()
#         user_name = data['name']
#         user_email = data['email']
#         res = con.cursor()
#         login_check = ('select * from add_user Where name=%s and email=%s')
#         val = (user_name,user_email)
#         row = res.execute(login_check,val)
#         row_value = res.fetchone()
#         print(row_value)
#         if row_value is None:
#             return "user_name and user_email error"
#         else:
#             return row_value[0].name
#     except Exception as e:
#         return str(e)


# @app.route('/logout')
# def logout():
#     try:
#         session.clear()
#         return "logout successfully"
#     except Exception as e:
#         return srt(e)

# if(__name__) == "__main__":
#     app.run(debug=True)