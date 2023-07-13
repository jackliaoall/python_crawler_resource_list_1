import sqlite3
import os

class Database:
    def __init__(self):
        self.db_path = 'goods.sqlite'
    def open(self,clear_data = True):
        if not os.path.exists(self.db_path):
            self.conn = sqlite3.connect(self.db_path)
            c = self.conn.cursor()
            c.execute('''CREATE TABLE t_goods_list
             (id INT PRIMARY KEY     NOT NULL,
              title           TEXT    NOT NULL,
              now_price       REAL     NOT NULL,
              pre_price       REAL    NOT NULL,
              comment_num     INT     NOT NULL,
              publication_date DATE NOT NULL,
              publisher TEXT NOT NULL,
              image_url TEXT,
              goods_url TEXT NOT NULL

              );

              ''')
            c.execute('''
                          CREATE TABLE t_goods_comment_list
                                     (goods_id INT    NOT NULL,
                                      detail          TEXT,
                                      score           INT,
                                      time            DATETIME,
                                      sentiment       REAL
                                      );
                          ''', {})
            self.conn.commit()
            print('成功创建数据库')
        else:  # 打开数据库
            self.conn = sqlite3.connect(self.db_path)
            if clear_data:
                c = self.conn.cursor()
                c.execute('''
                    delete from t_goods_list;
                ''')
                self.conn.commit()
    # 插入商品列表
    def insert_goods_list(self,goods_list):
        c = self.conn.cursor()
        c.executemany('insert into t_goods_list values(?,?,?,?,?,?,?,?,?)',goods_list)
        self.conn.commit()
    # 关闭数据库
    def close(self):
        print('数据库已经关闭')
        self.conn.close()

    def select_goods_list(self):
        c = self.conn.cursor()
        goods_list = c.execute('SELECT * FROM t_goods_list ORDER BY id')
        result = []
        for goods in goods_list:
            goods_info = {}
            goods_info['title'] = goods[1]
            goods_info['price'] = goods[2]
            goods_info['comment_num'] = goods[4]
            goods_info['publication_date'] = goods[5]
            goods_info['publisher'] = goods[6]
            goods_info['image_url'] = goods[7]
            goods_info['goods_url'] = goods[8]
            result.append(goods_info)
        return result