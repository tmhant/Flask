from flask_sqlalchemy import  SQLAlchemy
from flask import Flask

db = SQLAlchemy()

app = Flask(__name__)

#app.config['SQLALCHEMY_ECHO'] = True
#app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:mycard_1688@192.168.11.128:3306/app"

db.init_app(app)

@app.route('/select')
def select():
    sql_cmd = """
        select *
        from collection
        """

    query_data = db.engine.execute(sql_cmd).fetchall()
    print(query_data)
    

@app.route('/create')
def create_table():
    sql = """
    CREATE TABLE collection (
    id INT NOT NULL AUTO_INCREMENT,
    website CHAR(100) NOT NULL,
    title CHAR(100),
    description CHAR(100),
    artical_time CHAR(100),
    insert_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ID)
    )
    """
    try:
        db.engine.execute(sql)
        return 'Create table ok'
    except:
        return 'Create table Error'


@app.route('/insert')
def insert():
    sql = """
    INSERT INTO collection(
    website, title, description, artical_time)
    VALUES ('Mohan', '20', 'M', 2000)
    """
    try:
        db.engine.execute(sql)
        return 'Insert ok'
    except :
        return 'Insert Error'


@app.route('/update')
def update():
    sql ="""
    update collection set website = 'Max' where website= 'John'
    """
    try:
        db.engine.execute(sql)
        return 'Update ok'
    except:
        return 'Update Error'


@app.route('/delete')
def delete():
    sql = """
    delete from collection where id = 1
    """
    try:
        db.engine.execute(sql)
        return 'Delete ok'
    except:
        return 'Delete Error'

if __name__ == "__main__":
    app.run(debug=True)

