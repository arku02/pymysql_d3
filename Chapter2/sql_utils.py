import pymysql
import configparser 

config = configparser.ConfigParser()
config.read('../Chapter1/config.ini')

class SqlManager():
    def __init__(self,database=None):
        self.connection = pymysql.connect(
            host=config.get('DB', 'host'),
            user=config.get('DB', 'user'),
            password=config.get('DB', 'password'),
            port=config.getint('DB', 'port'),
            cursorclass=pymysql.cursors.DictCursor,
            database=database
        )
    
    def create_database(self, database):
        sql = f"""
        CREATE DATABASE IF NOT EXISTS {database}
        """ 
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            # 一樣先用, f-str, 因為 2-4.ipynb 好像不用 f-str 會當成字串, 然後報錯
            
    @property
    def dbs(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES;")
            dbs = cursor.fetchall()
        print(dbs)

    

# 查詢使用者的 function


# 建立寫入使用者的 function
    def create_user(self, name, age, username, password):
        with self.connection.cursor() as cursor:
            sql = """
                INSERT INTO user (name, age, username, password)
                VALUES(%s,%s, %s, %s)
            """
            cursor.execute(sql, (name, age, username, password))

        self.connection.commit()
    
        print(f"\033[31m成功寫入使用者: {username}")