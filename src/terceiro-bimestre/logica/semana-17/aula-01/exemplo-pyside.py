import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle("Interface Moderna")
janela.resize(300, 200)

botao = QPushButton("Entrar")

botao.setStyleSheet("""
QPushButton {
    background-color: #0078D7;
    color: white;
    font-size: 16px;
    border-radius: 10px;
    padding: 10px;
}
QPushButton:hover {
    background-color: #005EA6;
}
""")

layout = QVBoxLayout()
layout.addWidget(botao)

janela.setLayout(layout)
janela.show()

sys.exit(app.exec())


