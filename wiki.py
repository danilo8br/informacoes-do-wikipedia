from PyQt5 import uic, QtWidgets
import wikipedia

app=QtWidgets.QApplication([])

def wiki():
    wikipedia.set_lang('pt')
    pergunta = str(primeira_tela.lineEdit.text())
    n = wikipedia.summary(pergunta)
    primeira_tela.close()
    segunda_tela.show()
    segunda_tela.label_2.setText(n)


primeira_tela = uic.loadUi('primeira_tela.ui')
segunda_tela = uic.loadUi('segunda_tela.ui')

primeira_tela.pushButton.clicked.connect(wiki)

primeira_tela.show()

app.exec()
