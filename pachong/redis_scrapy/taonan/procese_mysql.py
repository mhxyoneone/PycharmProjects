# _*_ coding:utf-8 _*_
import redis
import pymysql
import json
# import sys
# # reload(sys)
# sys.setdefaultencoding('utf-8')

def get_data():
    rediscli = redis.Redis(host="127.0.0.1", port=6379, db=0)

    mysqlcli = pymysql.connect(host="127.0.0.1", port=3306, user="kevin", passwd="qweasdzxc", db="mysql",charset="utf8")
    num = 0
    while True:
        cur = mysqlcli.cursor()

        #cur.execute("SELECT * FROM taonan ")

        source,data = rediscli.blpop("taonan_spider:items")
        item = json.loads(data.decode('utf-8'))
        # value_1 = item['username'],item['age'],item['header_pic'],item['image_pic'],item['content'],item['place_from'],item['education'],item['user_url']
        # sql_wd = "insert into taonan (user_name,age,header_pic,image_pic,content,place_from,education,user_url)VALUES(%s)",[value_1]
        try:
            cur.execute("""insert into taonan (user_name,age,header_pic,image_pic,content,place_from,education,user_url) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",[item['username'],item['age'],item['header_pic'],item['image_pic'],item['content'],item['place_from'],item['education'],item['user_url']])
            mysqlcli.commit()
            cur.close()
            num += 1
            print(num)
        except:
            print('pass')
        #print(item['username'])
    # cur = mysqlcli.cursor()
    # sql_my = """insert into taonan(user_name,age,header_pic,image_pic,content,place_from,education,user_url)VALUES('Mini','31岁','http://thumb1.taonanw.com/cut_image_2701982_0.jpg@210w_280h_80q_0l_1c_1e','http://thumb1.taonanw.com/1_2701982_market_131622713544_0.jpg@60w_70h_80q_0l_1c_1e','我想要个什么样的人呢?我不知道。可是这样一个人,应该在见了之后才知道他是真命天子,会让我有想和他过一生的冲动,会让我宁愿收拾所有任性懒散,把最好的一面呈现在他面前。 ','上海长宁','大专','http://www.taonanw.com/u_2701982')"""
    # cur.execute(sql_my)
    # mysqlcli.commit()
    # print('done')
if __name__ == '__main__':

    get_data()