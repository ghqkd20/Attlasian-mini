from flask import Flask
from flask import request
import db

app = Flask(__name__)
Database = db.DB()

# 초기 Table 데이터 전송
@app.route('/users')
def users():
    return Database.select()

@app.route('/period/')
def period():
    val = request.args.get('value')
    # Database.filterPeriod(value) - 필터 진행 후 Render data에 저장- json형태로 
    # Database.getRender 
    # Return 
    pass

@app.route('/download')
def download():
    # 현재 render된 데이터를 csv 형태로 다운로드
    pass

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

