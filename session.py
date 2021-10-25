from flask import Flask, session
from datetime import timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)

 # 设置session


@app.route('/set')
def index():

    #設置session
     session['username'] = 'name'
    #如果設置了 session.permanent 為 True，那麽過期時間是31天
     session.permanent = True
     return 'set session ok'


@app.route('/get')
def get():
    #讀取session
    return session.get('username')

@app.route('/del')
def delete():
    #刪除session
    session['username'] = False
    return 'delete session ok'

if __name__ == "__main__":
    app.run(debug=True)
