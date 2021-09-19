# -*- coding: utf-8 -*-
from playsound import playsound
import time,datetime

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
import sys
from os import path

from PyQt5.uic import loadUiType

FORM_CLASS ,_= loadUiType(path.join(path.dirname('__file__'),"mainWindow.ui"))

class Main(QMainWindow, FORM_CLASS):
    
    
    def __init__(self,parent = None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        
        
    def Handel_Buttons(self):
        self.fileButton.clicked.connect(self.openFile)
        self.okButton.clicked.connect(self.sleep_till_future)
    
    def openFile(self):
        options = QFileDialog.Options()
        self.fileName = QFileDialog.getOpenFileName(self,"Open Source","","Ses Dosyaları (*.mp3)", options=options)[0]
        print(self.fileName)
        
    
    def sleep_till_future(self): 
        """
             Bu fonksiyon şu anki zamanı alarak kullanıcının istediği bir dakikaya kadar uyur.
        """
        
        
        t = datetime.datetime.now()
        m=int(self.spinBox.text())
        future = datetime.datetime(t.year,t.month,t.day,t.hour,m)
    
        if future.minute <= t.minute:
            print("ERROR! Enter a valid minute in the future.")
        else:
            print( "Current time: " + str(t.hour)+":"+str(t.minute))
            print ("Sleep until : " + str(future.hour)+":"+str(future.minute))
    
            seconds_till_future = (future-t).seconds
            time.sleep( seconds_till_future )
            print ("I slept for "+str(seconds_till_future)+" seconds!")
            playsound(self.fileName)
    
    

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()


