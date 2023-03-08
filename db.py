import sqlite3
import os
import Crol
from flask import jsonify

class DB():
    def __init__(self):
        self.file = './database.db'
        self.conn = []

        # 한번 읽으면 기존 Table Data는 저장해놓도록 하자. 
        # 전체 테이블 데이터
        self.tabledata = []
        # 보여지는 테이블 데이터(기간 별 필터링을 통해)
        self.renderdata = []

        # Insert해서 넣었다 빼는 거랑, 넣을때 data랑 모양 다를수 있음 . 넣을때의 data를 가지고 있다가 전처리 해서 넘기도록하자

        # DB 파일이 존재하는 경우
        if os.path.isfile(self.file):
            print("DB is exists. I Can Connect it")
            self.conn = sqlite3.connect(self.file, isolation_level=None,check_same_thread=False)
            
            # Table 내 컨텐츠 존재하는지 새로 업데이트 해야하는지 확인
            cur = self.conn.cursor()
            cur.execute('select count(*) from users')
            
            # DB 파일만 있고 내용이 없을 시 내용을 채워 넣음
            if list(cur)[0][0] == 0:
                print("DB is exists. But, Data is None. I Will Crol it")
                data = Crol.Crolling()
                self.Table_setter(data)
                self.insert(data)


        # DB 파일이 존재하지 않는 경우
        else:
            print("DB is None. I Will make it")
            self.conn = sqlite3.connect(self.file, isolation_level=None,check_same_thread=False)
            # Execute Crol and get Crol Data
            # Make DB from Croling Data
            data = Crol.Crolling()
            self.Table_setter(data)
            self.create()
            self.insert(data)
        
        print('create & connect database')

    def create(self):
        print("Create Start")
        cur = self.conn.cursor()
        cur.execute(
        '''
        create table users (name text, employeenum text, count text, lastlogin text)
        '''
        )
        # conn.close()
    
    def insert(self,data):
        print("Insert Start")
        cur = self.conn.cursor()
        for val in data:
            cur.execute("insert into users values(?,?,?,?);",(val[0],val[1],val[2],val[3]))
        

# 뺄때 넘기기 좋게 만들어서 넣자

    def select(self):
        # Read Current DB File
        print("Read Start")
        cur = self.conn.cursor()
        cur.execute("select * from users")
        json_file = []

        
        for row in cur: 
            json_file.append({"application":row[0],"instance":row[1],"status":row[2],"status2":row[3]})
        
        print("Read End")
        self.tabledata = json_file

        return jsonify(json_file)

    def update(self):
        # Update
        print("Update Start")
        cur = self.conn.cursor()
        cur.execute("delete from users")

        data = Crol.Crolling()
        self.insert(data)

    def Table_setter(self,data):
        self.tabledata = data
    
    def render_setter(self,data):
        self.renderdata = data

    def Table_getter(self,data):
        return self.tabledata
    
    def render_getter(self,data):
        return self.renderdata
    
        
