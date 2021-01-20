# Importando bibliotecas 
from PyQt5 import uic, QtWidgets
import wikipedia
# Conectando a aplicação
app=QtWidgets.QApplication([])
# Buscando as informações
def wiki():
    wikipedia.set_lang('pt')
    pergunta = str(primeira_tela.lineEdit.text())
    n = wikipedia.summary(pergunta)
    primeira_tela.close()
    segunda_tela.show()
    segunda_tela.label_2.setText(n)

# Carregando os arquivos
primeira_tela = uic.loadUi('primeira_tela.ui')
segunda_tela = uic.loadUi('segunda_tela.ui')
# Botões
primeira_tela.pushButton.clicked.connect(wiki)
# Mostrando a primeira tela
primeira_tela.show()
# Executando a aplicação 
app.exec()
