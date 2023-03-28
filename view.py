import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from mainview import Ui_MainWindow



class Calculatrice(QMainWindow):
    def __init__(self):
        super(Calculatrice, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



    def calculate(self):
        P = 0
        E = 0
        G = 0
        if(self.ui.comboBox.currentIndex() == 0):
            P = 10
        elif(self.ui.comboBox.currentIndex() == 1):
            P = 6
        elif(self.ui.comboBox.currentIndex() == 2):
            P = 3
        elif(self.ui.comboBox.currentIndex() == 3):
            P = 1
        elif(self.ui.comboBox.currentIndex() == 4):
            P = 0.5
        elif(self.ui.comboBox.currentIndex() == 5):
            P = 0.2
        elif(self.ui.comboBox.currentIndex() == 6):
            P = 0.1
        
        if(self.ui.comboBox_2.currentIndex() == 0):
            E = 10
        elif(self.ui.comboBox_2.currentIndex() == 1):
            E = 6
        elif(self.ui.comboBox_2.currentIndex() == 2):
            E = 3
        elif(self.ui.comboBox_2.currentIndex() == 3):
            E = 2
        elif(self.ui.comboBox_2.currentIndex() == 4):
            E = 1
        elif(self.ui.comboBox_2.currentIndex() == 5):
            E = 0.5

        if(self.ui.comboBox_3.currentIndex() == 0):
            G = 100
        elif(self.ui.comboBox_3.currentIndex() == 1):
            G = 40
        elif(self.ui.comboBox_3.currentIndex() == 2):
            G = 15
        elif(self.ui.comboBox_3.currentIndex() == 3):
            G = 7
        elif(self.ui.comboBox_3.currentIndex() == 4):
            G = 3
        elif(self.ui.comboBox_3.currentIndex() == 5):
            G = 1
        
        result = P*E*G

        if(result > 400):
            self.ui.code_couleur.setStyleSheet("background-color : rgba(255, 0, 0, 150)")
        elif(result <= 400 and result > 200):
            self.ui.code_couleur.setStyleSheet("background-color : rgba(255, 170, 0, 150)")
        elif(result <= 200 and result > 70):
            self.ui.code_couleur.setStyleSheet("background-color : rgba(255, 255, 0, 150)")
        elif(result <= 70 and result > 20):
            self.ui.code_couleur.setStyleSheet("background-color : rgba(187, 255, 0, 150)")
        else:
            self.ui.code_couleur.setStyleSheet("background-color : rgba(0, 170, 0, 150)")
        self.ui.label_reponse.setText('R = '+str(result))
        
        

    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculatrice()
    window.show()

    sys.exit(app.exec())
