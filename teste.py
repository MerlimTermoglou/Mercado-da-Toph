import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QBoxLayout, QVBoxLayout,QHBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QKeyEvent, QPixmap

class TophMercados(QWidget):
    def __init__(self):
        super().__init__()

        # Inicializando variáveis de controle
        self.total = 0.0  # Armazena o total da compra
        self.linha = 0    # Controla a linha atual da tabela

        # Configurando a janela principal
        self.setGeometry(10, 25, 1600, 900)
        self.setWindowTitle("Caixa da Padaria")
        self.showMaximized()

        # Criando layouts para organizar os widgets
        layoutVerEs = QHBoxLayout()
        layoutVerDi = QHBoxLayout()
        layoutHor = QHBoxLayout()

        # Criando label e edit para a coluna esquerda
        labelColEsq = QLabel()
        labelColEsq.setStyleSheet("QLabel{background-color:#401d05;}")
        labelColEsq.setFixedWidth(800)

        # Configurando o logotipo da padaria
        labelLogo = QLabel()
        labelLogo.setPixmap(QPixmap("to.png"))
        labelLogo.setScaledContents(True)

        # Configurando labels e edits para entrada de dados
        labelCodigo = QLabel("Codigo do Produto")
        labelCodigo.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.codigoEdit = QLineEdit()
        self.codigoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt}")

        # Repetir para outros campos como nome do produto, descrição, quantidade, preço unitário, subtotal, etc.

        # Adicionando widgets ao layout vertical da coluna esquerda
        layoutVerEs.addWidget(labelLogo)

        layoutVerEs.addWidget(labelCodigo)
        layoutVerEs.addWidget(self.codigoEdit)

        # Repetir para outros campos

        labelColEsq.setLayout(layoutVerEs)

        # Criando a tabela de dados do lado direito
        self.tbResumo = QTableWidget(self)
        self.tbResumo.setColumnCount(5)
        self.tbResumo.setRowCount(10)

        # Configurando cabeçalho da tabela
        titulos = ["Código", "Nome Produto", "Quantidade", "Preço Unitario", "Preço Total"]
        self.tbResumo.setHorizontalHeaderLabels(titulos)

        # Configurando label e edit para a coluna direita
        labelTotalPagar = QLabel("Total a pagar")
        labelTotalPagar.setStyleSheet("QLabel{color:black;font-size:25pt}")
        self.totalPagarEdit = QLineEdit("0,00")
        self.totalPagarEdit.setEnabled(False)
        self.totalPagarEdit.setStyleSheet("QLineEdit{padding:10px;font-size:50pt}")

        # Adicionando widgets ao layout vertical da coluna direita
        layoutVerDi.addWidget(self.tbResumo)
        layoutVerDi.addWidget(labelTotalPagar)
        layoutVerDi.addWidget(self.totalPagarEdit)

        labelColDir = QLabel()
        labelColDir.setStyleSheet("QLabel{background-color:#e8d9ba}")
        labelColEsq.setFixedWidth(800)
        labelColDir.setLayout(layoutVerDi)

        # Adicionando colunas esquerda e direita ao layout horizontal principal
        layoutHor.addWidget(labelColEsq)
        layoutHor.addWidget(labelColDir)

        self.setLayout(layoutHor)

        # Capturando a tecla que o usuário está digitando e 
        # Chamando a função (keyPressEvent) para executar um comando quando
        # for acionada.
        self.keyPressEvent = self.keyPressEvent

    def keyPressEvent(self, e):
        # Verifica se a tecla F2 foi pressionada
        if e.key() == Qt.Key_F2:
            print('Você teclou F2')

            # Adiciona os itens à tabela
            self.tbResumo.setItem(self.linha, 0, QTableWidgetItem(str(self.codigoEdit.text())))
            self.tbResumo.setItem(self.linha, 1, QTableWidgetItem(str(self.nomeProdutoEdit.text())))
            self.tbResumo.setItem(self.linha, 2, QTableWidgetItem(str(self.quantiProdutoEdit.text())))
            self.tbResumo.setItem(self.linha, 3, QTableWidgetItem(str(self.valProdutoEdit.text())))
            self.tbResumo.setItem(self.linha, 4, QTableWidgetItem(str(self.subTotalEdit.text())))
            self.linha += 1

            # Atualiza o total da compra
            self.total += float(self.subTotalEdit.text())
            self.totalPagarEdit.setText(str(self.total))

            # Limpa os LineEdit
            self.codigoEdit.setText("")
            self.nomeProdutoEdit.setText("")
            self.quantiProdutoEdit.setText("")
            self.valProdutoEdit.setText("")
            self.subTotalEdit.setText("Aperte F3 para calcular o SubTotal")
            self.descProdutoEdit.setText("")

        # Verifica se a tecla F3 foi pressionada
        elif e.key() == Qt.Key_F3:
            # Calcula o subtotal e exibe
            qtd = self.quantiProdutoEdit.text()
            prc = self.valProdutoEdit.text()
            res = float(qtd) * float(prc)
            self.subTotalEdit.setText(str(res))


app = QApplication(sys.argv)

janela = TophMercados()
janela.show()

app.exec_()