from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import sqlite3
from datetime import date
from PyQt5.QtPrintSupport import QPrinter

ui, _ = loadUiType('pos.ui')

class MainApp(QMainWindow,ui):

    items = ["ITEMS"]
    price = [0]
    images = ["IMAGES"]

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.LOGINBUTTON.clicked.connect(self.login)
        self.MAINFORMCLOSE.clicked.connect(self.logout)
        self.FOODBUTTON1.clicked.connect(lambda:self.addproduct(1))
        self.FOODBUTTON2.clicked.connect(lambda:self.addproduct(2))
        self.FOODBUTTON3.clicked.connect(lambda:self.addproduct(3))
        self.FOODBUTTON4.clicked.connect(lambda:self.addproduct(4))
        self.FOODBUTTON5.clicked.connect(lambda:self.addproduct(5))
        self.FOODBUTTON6.clicked.connect(lambda:self.addproduct(6))
        self.FOODBUTTON7.clicked.connect(lambda:self.addproduct(7))
        self.FOODBUTTON8.clicked.connect(lambda:self.addproduct(8))
        self.FOODBUTTON9.clicked.connect(lambda:self.addproduct(9))
        self.FOODBUTTON10.clicked.connect(lambda:self.addproduct(10))
        self.PRINT.clicked.connect(self.print_widget)
        self.NOPRINT.clicked.connect(self.noprint_widget)
        self.SETTINGS.clicked.connect(self.show_settings)
        self.ITEMSLIST.currentIndexChanged.connect(self.fill_details_on_combobox_selected)
        self.MODIFYBUTTON.clicked.connect(self.update_product)
        self.CONFIGUREBACK.clicked.connect(self.configurepage_to_productpage)

    #### ADMIN LOGIN CODE ####

    def login(self):
        un = self.USERNAME.text()
        pw = self.PASSWORD.text()
        if(un == "admin" and pw == "admin"):
            self.USERNAME.setText("")
            self.PASSWORD.setText("")
            self.getbill_number()
            self.tabWidget.setCurrentIndex(1)
        else:
            self.LOGININFO.setText("Invalid login details")

    #### LOG OUT CODE ####

    def logout(self):
        self.tabWidget.setCurrentIndex(0)

    #### GENERATE BILL NO AND DISPLAY DATE ####

    def getbill_number(self):
        con = sqlite3.connect("pos.db")
        cursor = con.execute("SELECT MAX(billno) FROM billitems")
        result = cursor.fetchall()  
        if result:
            try:
                for data in result:
                    billno = int(data[0]) + 1
            except:
                billno = 1
        else:
            billno = 1
        self.BILLNO.setText(str(billno)) 
        self.DATE.setText(str(date.today()))  
        self.configurepage()
 
    #### CONFIGURE ITEM DETAILS FROM DATABASE ####

    def configurepage(self):
        self.items = ["ITEMS"]
        self.price = [0]
        self.images = ["IMAGES"]
        con = sqlite3.connect("pos.db")
        cursor = con.execute("SELECT * FROM products")
        result = cursor.fetchall()
        if result:
            for prod in result:
                self.items.append(str(prod[0]))
                self.images.append(str(prod[1]))
                self.price.append(str(prod[2]))
        con.close()
        print(self.items)
        print(self.images)
        print(self.price)        

        ### SETTING FIRST ITEM ###
        self.FOODNAME1.setText(self.items[1]) 
        self.FOODPRICE1.setText("Rs : " + self.price[1])           
        filename = "./" + self.images[1]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE1.setPixmap(pm)
        

        ### SETTING 2ND ITEM ###
        self.FOODNAME2.setText(self.items[2]) 
        self.FOODPRICE2.setText("Rs : " + self.price[2])           
        filename = "./" + self.images[2]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE2.setPixmap(pm)


        ### SETTING 3RD ITEM ###
        self.FOODNAME3.setText(self.items[3]) 
        self.FOODPRICE3.setText("Rs : " + self.price[3])           
        filename = "./" + self.images[3]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE3.setPixmap(pm)


        ### SETTING 4TH ITEM ###
        self.FOODNAME4.setText(self.items[4]) 
        self.FOODPRICE4.setText("Rs : " + self.price[4])           
        filename = "./" + self.images[4]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE4.setPixmap(pm)

        ### SETTING 5TH ITEM ###
        self.FOODNAME5.setText(self.items[5]) 
        self.FOODPRICE5.setText("Rs : " + self.price[5])           
        filename = "./" + self.images[5]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE5.setPixmap(pm)

        ### SETTING 6TH ITEM ###
        self.FOODNAME6.setText(self.items[6]) 
        self.FOODPRICE6.setText("Rs : " + self.price[6])           
        filename = "./" + self.images[6]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE6.setPixmap(pm)

        ### SETTING 7TH ITEM ###
        self.FOODNAME7.setText(self.items[7]) 
        self.FOODPRICE7.setText("Rs : " + self.price[7])           
        filename = "./" + self.images[7]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE7.setPixmap(pm)

        ### SETTING 8TH ITEM ###
        self.FOODNAME8.setText(self.items[8]) 
        self.FOODPRICE8.setText("Rs : " + self.price[8])           
        filename = "./" + self.images[8]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE8.setPixmap(pm)


        ### SETTING 9TH ITEM ###
        self.FOODNAME9.setText(self.items[9]) 
        self.FOODPRICE9.setText("Rs : " + self.price[9])           
        filename = "./" + self.images[9]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE9.setPixmap(pm)

        ### SETTING 10TH ITEM ###
        self.FOODNAME10.setText(self.items[10]) 
        self.FOODPRICE10.setText("Rs : " + self.price[10])           
        filename = "./" + self.images[10]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE10.setPixmap(pm)



    #### ADD PRODUCT TO BILLS TABLE ####

    def addproduct(self,id):
        print("ADD PRODUCT FUNCTION CALLED",id)
        billno = int(self.BILLNO.text())
        itemname = str(self.items[id])
        unitprice = self.price[id]
        quantity = "1"
        con = sqlite3.connect("pos.db")
        cursor = con.execute("SELECT * FROM billitems WHERE itemname = '"+ itemname +"' and billno = "+ str(billno) +"")
        result = cursor.fetchall()
        if result:
            print("Already added")
            con.execute("UPDATE billitems SET quantity = quantity + 1, totalprice = totalprice + "+ str(unitprice) +" WHERE itemname = '"+ itemname +"' and billno = "+ str(billno) +"")
            con.commit()
        else:
            print("Adding New")
            con.execute("INSERT INTO billitems (billno, itemname, unitprice, quantity, totalprice) values("+ str(billno) +", '"+ itemname +"', "+ str(unitprice) +", "+ quantity +","+ str(unitprice) +")")
            con.commit()
        self.filltable()


    #### SHOW ADDED ITEMS TO THE TABLE #### 

    def filltable(self):
        total = 0
        self.billitems.setRowCount(0)
        self.billitems.clear()
        self.billitems.setColumnWidth(0,110)
        self.billitems.setColumnWidth(1,70)
        self.billitems.setColumnWidth(2,70)
        self.billitems.setColumnWidth(3,70)
        con = sqlite3.connect("pos.db")
        cursor = con.execute("SELECT itemname, unitprice, quantity, totalprice FROM billitems WHERE billno = "+ self.BILLNO.text() +"")
        result = cursor.fetchall()
        r = 0
        c = 0
        for row_number, row_data in enumerate(result):
            r += 1
            c = 0
            for column_number, data in enumerate(row_data):
                c += 1
        self.billitems.setColumnCount(c)        
        for row_number, row_data in enumerate(result):
            self.billitems.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.billitems.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        self.billitems.verticalHeader().setVisible(False)
        self.billitems.horizontalHeader().setVisible(False)
        cursor = con.execute("SELECT * FROM billitems WHERE billno = "+ str(self.BILLNO.text()) +"")
        result = cursor.fetchall()
        if result:
            for prod in result:
                total = total + int(prod[4])
        self.TOTAL.setText("%.2f" % (total))
        self.TAX.setText("%.2f" % (total * .05))
        self.GRANDTOTAL.setText("%.2f" % (total + (total * .05)))

    #### PRINT RECEIPT AND GO NEXT #### 
     
    def print_widget(self):
        if(self.GRANDTOTAL.text()!="0.00"):
            printer = QPrinter()
            painter = QPainter()
            painter.begin(printer)
            screen = self.PRINTAREA.grab()
            painter.drawPixmap(10,10,screen)
            painter.end()
            self.getbill_number()
            self.filltable()    


    #### NO PRINT RECEIPT AND GO NEXT #### 

    def noprint_widget(self):
        if(self.GRANDTOTAL.text()!="0.00"):
            self.getbill_number()
            self.filltable() 


    #### SHOW SETTINGS FORM #### 

    def show_settings(self):
        self.tabWidget.setCurrentIndex(2)
        con = sqlite3.connect("pos.db")
        cursor = con.execute("SELECT * FROM products")
        result = cursor.fetchall()
        if result:
            for prod in result:
                self.ITEMSLIST.addItem(str(prod[0]))


    #### SHOW VALUES WHEN PRODUCT IS SELECTED #### 

    def fill_details_on_combobox_selected(self):
        con = sqlite3.connect("pos.db")
        cursor = con.execute("SELECT * FROM products WHERE itemname = '"+ self.ITEMSLIST.currentText() +"'")
        result = cursor.fetchall()
        if result:
            for prod in result:
                self.ITEMNAME.setText(str(prod[0]))       
                self.ITEMPICTURE.setText(str(prod[1]))    
                self.ITEMPRICE.setText(str(prod[2]))
                self.SETTINGSNAME.setText(str(prod[0])) 
                self.SETTINGSPRICE.setText("Rs : " + str(prod[2]))           
                filename = "./" + str(prod[1])
                image = QImage(filename)
                pm = QPixmap.fromImage(image)
                self.SETTINGSIMAGE.setPixmap(pm)


    #### UPDATE MODIFIED VALUES #### 

    def update_product(self):
        con = sqlite3.connect("pos.db")
        cursor = con.execute("UPDATE products SET itemname = '"+ self.ITEMNAME.text() +"', imagename = '"+self.ITEMPICTURE.text() +"', unitprice = "+ self.ITEMPRICE.text() +" WHERE itemname = '"+ self.ITEMSLIST.currentText() +"'")
        con.commit()
        con.close()
        self.SETTINGSNAME.setText(self.ITEMNAME.text()) 
        self.SETTINGSPRICE.setText("Rs : " + self.ITEMPRICE.text())           
        filename = "./" + self.ITEMPICTURE.text()
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.SETTINGSIMAGE.setPixmap(pm)
        self.configurepage()
        self.CONFIGUREMSG.setText("Modified Successfully")

    #### CONFIGURE PAGE TO PRODUCTS PAGE #### 

    def configurepage_to_productpage(self):
        self.tabWidget.setCurrentIndex(1)        

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

