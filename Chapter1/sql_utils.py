# 引入所需套件
import pymysql
from configparser import ConfigParser

# 讀取 config.ini 檔案取得資料庫連線資訊
config = ConfigParser()
config.read('config.ini')


class SqlManager:
    dbs = "SHOW DATABASES;"
    full_passengers = "SELECT * FROM my_titanic.full_passengers;"
    def __init__(self):
        self.connection = pymysql.connect(
            host=config.get('DB', 'host'),
            user=config.get('DB', 'user'),
            password=config.get('DB', 'password'),
            port=config.getint('DB', 'port'),
    # port 拿倒是字串, 所以要強制轉成 int
            cursorclass=pymysql.cursors.DictCursor,
)
# 建立 function 執行 SQL 查詢
    def sql_query(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
        return result

    def get_leonard_males(self):
        leonard_males = []
        result = self.sql_query(SqlManager.full_passengers)
        for i in result:
            if 'Leonard' in i["pname"] and i["sex"] == "male" and i['pname'].startswith ('Leonard') is False: 
                leonard_males.append({
                    "id" : i['id'],
                    'pclass' : i['pclass'],
                    'pname' : i['pname']
                })  
        return leonard_males