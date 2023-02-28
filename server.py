from flask import Flask
import flask
import db

app = Flask(__name__)
Database = db.DB()

# 초기 Table 데이터 전송
@app.route('/users')
def users():
    return Database.select()

# Update Table 데이터
@app.route('/update')
def update():
    # Update하면 기존내역이 필요함? 없으면 table내용 싹 날리고 새로 넣어주면 되지
    Database.update()
    res = flask.make_response(Database.select())

    # CORS 설정
    res.headers.add("Access-Control-Allow-Origin", "*")
    res.headers.add('Access-Control-Allow-Headers', "*")
    res.headers.add('Access-Control-Allow-Methods', "*")
    
    return res

if __name__ == "__main__":
    # Data verification
    app.run(debug=False)

