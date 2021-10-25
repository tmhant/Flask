# main.py

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# MySql datebase
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:mycard_1688@192.168.11.128:3306/app"

db = SQLAlchemy(app)

# 模型( model )定義


class Product(db.Model):
    __tablename__ = 'product'
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(30), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    img = db.Column(
        db.String(100), unique=True, nullable=False)
    description = db.Column(
        db.String(255), nullable=False)
    state = db.Column(
        db.String(10), nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(
        db.DateTime, onupdate=datetime.now, default=datetime.now)

    def __init__(self, name, price, img, description, state):
        self.name = name
        self.price = price
        self.img = img
        self.description = description
        self.state = state


class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
    update_time = db.Column(
        db.DateTime, onupdate=datetime.now, default=datetime.now, nullable=False)

    db_user_atc = db.relationship("AddToCar", backref="user")

    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.role = role


class AddToCar(db.Model):
    __tablename__ = 'addtocar'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(5), nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
    update_time = db.Column(
        db.DateTime, onupdate=datetime.now, default=datetime.now, nullable=False)

    db_product_addtocar = db.relationship("AddToCar", backref="product")
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)
    pid = db.Column(db.Integer, db.ForeignKey('product.pid'), nullable=False)

    def __init__(self, uid, pid, quantity, state):
        self.uid = uid
        self.pid = pid
        self.quantity = quantity
        self.state = state


@app.route('/')
def index():

    # Create data
    db.create_all()
    # 單筆
    # product_max = Product(
    #     'Max', 8888, 'https://picsum.photos/id/1047/1200/600', '', '')
    # db.session.add(product_max)
    # db.session.commit()

    # 多筆
    p1 = Product('Isacc', 3333, 'https://picsum.photos/id/1047/1200/601', '', 'Y')
    p2 = Product('Dennis', 9999, 'https://picsum.photos/id/1049/1200/602', '', 'Y')
    p3 = Product('Joey', 7777, 'https://picsum.photos/id/1033/1200/603', '', 'Y')
    p4 = Product('Fergus', 6666, 'https://picsum.photos/id/1041/1200/604', '', 'Y')
    p5 = Product('John', 5555, 'https://picsum.photos/id/1070/1200/605', '', 'Y')
    p6 = Product('Jerry', 4444, 'https://picsum.photos/id/1044/1200/606', '', 'Y')

    # 新增使用者
    u1 = User('Max', '123456', 'Admin')
    p = [p1, p2, p3, p4, p5, p6, u1]

    db.session.add_all(p)
    db.session.commit()
    # query = Product.query.filter_by(name='Max').first()
    # print(query.name)
    # print(query.price)

    # 可以用動態參數傳入
    # filters = {'name': 'John', 'price': 5555}
    # query = Product.query.filter_by(**filters).first()
    # print(query.name)
    # print(query.price)

    # Updata data
    # query = Product.query.filter_by(name='Max').first()

    # 將 price 修改成 10 塊
    # query.price = 10
    # db.session.commit()

    # Delete data
    # query = Product.query.filter_by(name='John').first()
    # db.session.delete(query)
    # db.session.commit()
    return 'ok'


if __name__ == "__main__":
    app.run(debug=True)
