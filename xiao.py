import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout,QHBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QKeyEvent, QPixmap


class TophMercados(QWidget):

    def __init__(self):

        super().__init__()
        
        self.setGeometry(0,25,1590,840)
        self.setWindowTitle("Toph Mais")

        layoutVPri = QVBoxLayout()
        layoutVDet = QVBoxLayout()
        layoutH = QVBoxLayout()
        layoutHB = QVBoxLayout()

#  Label de cima do layout Principal
        labelACima= QLabel("Toph Mais Supermercados")
        labelACima.setStyleSheet("QLabel{background-color:#665c49; color:#e8fdff; font-size:25pt}")
        labelACima.setFixedHeight(110)


#  Label debaixo do layout Principal
        labelABaixo = QLabel()
        labelABaixo.setStyleSheet("QLabel{background-color:#807462}")
        labelABaixo.setFixedHeight(690)
    
        labelBCima= QLabel()
        labelBCima.setStyleSheet("QLabel{background-color:#807462}")
        labelBCima.setFixedWidth(100)
        labelBCima.setLayout(layoutVDet)
# 
        labelBBaixo= QLabel()
        labelBBaixo.setStyleSheet("QLabel{background-color:#807462}")
        labelBBaixo.setFixedWidth(200)
        labelBBaixo.setLayout(layoutVDet)
# 
        # labelInterna= QLabel()
        # labelInterna.setStyleSheet("QLabel{background-color:#a69785}")
        # labelInterna.setFixedWidth(400)
        # labelInterna.setLayout(layoutHDet)
# 
        # labelInternaB= QLabel()
        # labelInternaB.setStyleSheet("QLabel{background-color:#a69785}")
        # labelInternaB.setFixedWidth(100)
        # labelInternaB.setLayout(layoutHDet)

        
        labelACima.setLayout(layoutVPri)
        
        labelBCima.setLayout(layoutVDet)

        layoutH.addWidget(labelACima)
        layoutH.addWidget(labelABaixo)

        layoutHB.addWidget(labelBCima)
        layoutHB.addWidget(labelBBaixo)

        self.setLayout(layoutH)

        self.setLayout(layoutHB)
# 
        # layoutVDet.addWidget(labelBCima)
# 
        # layoutVDet.addWidget(labelBBaixo)
# 
        # layoutHDet.addWidget(labelInterna)
# 
        # layoutHDet.addWidget(labelInternaB)



        # self.setLayout(layoutVPri)
        
        # self.setLayout(layoutVDet)

        # self.setLayout(layoutHDet)

app = QApplication(sys.argv)

janela = TophMercados()
janela.show()

app.exec_()