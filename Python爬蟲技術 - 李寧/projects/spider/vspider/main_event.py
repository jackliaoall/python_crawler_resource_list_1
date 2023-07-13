from PyQt5.QtCore import *
from spider import  *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QtWebEngineWidgets import *

class MainEvent(QObject):
    def __init__(self,ui):
        self.ui = ui
    def onclick_search(self):
        # 从文本输入框获取搜索关键字
        self.search_thread = SearchSpider('search',self.ui.textedit_keyword.toPlainText())
        # 绑定事件
        self.search_thread.sendmsg.connect(lambda  page_number,every_page_goods_number:
                                           self.search_callback(page_number,every_page_goods_number))
        # 开启线程开始抓取数据
        self.search_thread.start()
    def search_callback(self,page_number,every_page_goods_number):
        self.ui.lcdnumber_pages.setProperty('value',page_number)
        self.ui.lcdnumber_every_page_goods_number.setProperty('value',every_page_goods_number)

    # 开始抓取图书列表
    def onclick_fetch_goods_list(self):
        # keyword, max_page_index,max_thread_number
        keyword = self.ui.textedit_keyword.toPlainText()
        fetch_page_number = int(self.ui.textedit_fetch_page_number.toPlainText())
        thread_number = int(self.ui.spinbox_thread_number.text())
        
        self.goods_list_spider = GoodsListSpider(self.ui.textedit_keyword.toPlainText(), fetch_page_number,
                                                 thread_number)
    
        self.goods_list_spider.finished.connect(
            lambda time, book_number: self.fetch_goods_list_finished(time, book_number))
        
        self.goods_list_spider.start()

    def fetch_goods_list_finished(self, time, book_number):
        self.ui.lcdnumber_time.setProperty('value', time)
    def onclick_load_goods_list(self):
        grid = self.ui.tablewidget_goods_list

        grid.setColumnCount(7)
        grid.setHorizontalHeaderLabels(['控制', '封面','书名','当前价格','评论数','出版日期','出版社'])
        control_cell_widget_width = 300
        grid.setColumnWidth(0, control_cell_widget_width)
        grid.setColumnWidth(2, 200)
        grid.setColumnWidth(1, 200)
        db = Database()
        db.open(False)
        self.goods_list = db.select_goods_list()
        grid.setRowCount(len(self.goods_list))
        index = 0
        self.lcd_list = []
        buttons = []
        labels = []
        for goods in self.goods_list:
            title = QTableWidgetItem(goods['title'])
            grid.setItem(index, 2, title)
            price = QTableWidgetItem(str(goods['price']))
            grid.setItem(index, 3, price)
            comment_num = QTableWidgetItem(str(goods['comment_num']))
            grid.setItem(index, 4, comment_num)
            publication_date = QTableWidgetItem(goods['publication_date'])
            grid.setItem(index, 5, publication_date)
            publisher = QTableWidgetItem(goods['publisher'])
            grid.setItem(index, 6, publisher)
            grid.setRowHeight(index, 200)

            ############### 显示封面图像 ##############
            label = MyLabel(self.ui.centralwidget)
            labels.append(label)
            filename = str(index + 1).zfill(8)
            pixmap = QPixmap('images/' + filename)
            pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
            cover_image_cell_widget = QWidget()

            label.setPixmap(pixmap)
            label.setFixedHeight(200)
            label.setFixedWidth(200)
            lay_out = QHBoxLayout(cover_image_cell_widget)
            lay_out.addWidget(label)
            lay_out.setAlignment(Qt.AlignCenter)
            lay_out.setContentsMargins(0, 0, 0, 0)
            cover_image_cell_widget.setLayout(lay_out)

            grid.setCellWidget(index, 1, cover_image_cell_widget)
            ###########################################
            font = QFont()
            font.setPointSize(18)

            control_cell_widget = QWidget()
            button = MyButton(control_cell_widget)

            button.setGeometry(QRect(10, 10, 280, 60))
            button.setText("开始抓取和分析（3个线程）")
            button.setFont(font)
            button.setObjectName(goods['goods_url'])

            buttons.append(button)

            label_thread1 = QLabel(control_cell_widget)
            label_thread1.setFont(font)
            label_thread1.setText("线程1：")
            label_thread1.setGeometry(QRect(10, 80, 60, 31))

            lcdnumber_thread1 = QLCDNumber(control_cell_widget)
            lcdnumber_thread1.setGeometry(QRect(80, 80, 81, 31))
            lcdnumber_thread1.setFont(font)

            label_thread2 = QLabel(control_cell_widget)
            label_thread2.setFont(font)
            label_thread2.setText("线程2：")
            label_thread2.setGeometry(QRect(10, 120, 60, 31))

            lcdnumber_thread2 = QLCDNumber(control_cell_widget)
            lcdnumber_thread2.setGeometry(QRect(80, 120, 81, 31))
            lcdnumber_thread2.setFont(font)

            label_thread3 = QLabel(control_cell_widget)
            label_thread3.setFont(font)
            label_thread3.setText("线程3：")
            label_thread3.setGeometry(QRect(10, 160, 60, 31))

            lcdnumber_thread3 = QLCDNumber(control_cell_widget)
            lcdnumber_thread3.setGeometry(QRect(80, 160, 81, 31))
            lcdnumber_thread3.setFont(font)


            label_sentiments = QLabel(control_cell_widget)
            label_sentiments.setFont(font)
            label_sentiments.setText("情感指数")
            label_sentiments.setGeometry(QRect(200, 80, 80, 31))
            lcdnumber_sentiments = QLCDNumber(control_cell_widget)
            lcdnumber_sentiments.setGeometry(QRect(200, 120, 80, 31))
            lcdnumber_sentiments.setFont(font)
            lcdnumber_sentiments.setProperty('value',0.000)

            grid.setCellWidget(index,0,control_cell_widget)

            lcdnumbers = []
            lcdnumbers.append(lcdnumber_thread1)
            lcdnumbers.append(lcdnumber_thread2)
            lcdnumbers.append(lcdnumber_thread3)
            lcdnumbers.append(lcdnumber_sentiments)
            self.lcd_list.append(lcdnumbers)
            ##################显示控制组件######################


            index += 1

        for i in range(0,len(buttons)):
            buttons[i].index = i
            buttons[i].goods_url = self.goods_list[i]['goods_url']
            buttons[i].main_event = self
            buttons[i].clicked.connect( buttons[i].fetch_and_analyse_goods)

        for i in range(0, len(labels)):
            labels[i].index = i
            labels[i].main_event = self
            labels[i].book_title = self.goods_list[i]['title']
            labels[i].mousePressEvent = labels[i].show_analysis_chart
        db.close()
class MyLabel(QLabel):
    def show_analysis_chart(self, value):
        pass
class MyButton(QPushButton):
    def fetch_and_analyse_goods(self):
        pass
