#Tutorial BroCode sobre PyQt

import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtGui import (QIcon, QFont, QPixmap)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Nome da janela + tamanho + foto icone e cor de fundo
        self.setWindowTitle("First GUI")

        # X, Y, Width, Height
        self.setGeometry(750, 300, 500, 500)
        self.setWindowIcon(QIcon("./assets/guiImage.png"))
        self.setStyleSheet("background-color: black;")

        #Label, Escrita, com QLabel e QFont
        label = QLabel("Olá", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: white;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        
       # label.setAlignment(Qt.AlignTop) # Verticalmente topo
       # label.setAlignment(Qt.AlignBottom) #Verticalmente abaixo
       # label.setAlignment(Qt.AlignVcenter) # Verticalmente central
       # label.setAlignment(Qt.AlignRight) # Horizontalmente direita
       # label.setAlignment(Qt.AlignHCenter) # Horizontalmente central
       # label.setAlignment(Qt.AlignLeft) # Horizontalmente esquerda
       # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # Horizontalmente central e verticalmente para baixo
                                                              # o barra (or) " | " funciona aqui por combinar os bits das flags. Aqui é bitwise    
       # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) Alinha no centro
        label.setAlignment(Qt.AlignCenter) # Centro Centro


        #Label Imagem com PixMap
        labelImagem = QLabel(self)
        labelImagem.setGeometry(0, 0, 280, 230)

        #Centralizando a imagem
        labelImagem.setGeometry((self.width() - labelImagem.width()) // 2, 
                                (self.height() - labelImagem.height()) // 2, 
                                labelImagem.width(), 
                                labelImagem.height())

        pixmap = QPixmap("./assets/guiImage.png")
        labelImagem.setPixmap(pixmap)

        labelImagem.setScaledContents(True) # Imagem ficar do tamanho da label


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()