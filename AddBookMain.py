import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QFileDialog
from PySide6.QtGui import QIcon, QPixmap
import PySide6
import shutil
from functools import partial
from AddBookPage import Ui_Form

import mysql.connector as mc

class AddBook(QWidget):
    def __init__(self,u_id,username):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        dlg = QFileDialog(self)  

        self.ui.add_book_picture.clicked.connect(partial(self.openImage,u_id))
            
    def openImage(self,u_id):
        imagePath, _ = QFileDialog.getOpenFileName(self, "Upload Image File")
        pixmap = QPixmap(imagePath)
        self.ui.book_picture_edit.setPixmap(pixmap.scaled(151,181))
        #self.ui.book_picture_edit.setPixmap(pixmap)
        self.resize(pixmap.size())
        self.adjustSize()
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="sep_project"
        )
        mycursor = mydb.cursor()
        querygetlatestid = "SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE (TABLE_NAME = 'book')"
        mycursor.execute(querygetlatestid)
        result = mycursor.fetchall()
        print(result)
        #print(result[1][0])
   
        mydb.close()

        num = str(result[0][0])
        destination = ("images/b" +num+".jpg")
        print(destination)
        shutil.copyfile(imagePath,destination)

        self.ui.add_button.clicked.connect(partial(self.addnewbook,num,u_id))

    def addnewbook(self,num,u_id):
        bookauthor = self.ui.name_edit.text()
        bookname =self.ui.book_name_edit.text()
        price = self.ui.lineEdit.text()
        if bookauthor == "":
            print("Please enter author name")
        if bookname == "":
            print("Please enter book name")
        if price == "":
            print("Please enter price")
        else:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="sep_project"
            )
            mycursor = mydb.cursor()
            query = "INSERT INTO book(bookName, bookAuthor,SellerID, Picture, Price) VALUES ('"+str(bookname)+"','"+str(bookauthor)+"','"+str(u_id)+"','b"+str(num)+"','"+str(price)+"')"
            mycursor.execute(query)
            mydb.commit()
            print("New book had been added")

    