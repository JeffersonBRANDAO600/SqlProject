from PyQt5 import uic, QtWidgets
import mysql.connector
banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "usuario_cad"  
)

def funcao_principal():
    nome = cadastro.lineEdit.text()
    sobrenome = cadastro.lineEdit_2.text()
    email = cadastro.lineEdit_3.text()
    genero = ""

    print("Nome:",nome)
    print("Sobrenome:",sobrenome)
    print("Email:",email)

    if cadastro.radioButton.isChecked() :
        print("Genero masculino")
        genero = "Maculino"
    elif cadastro.radioButton_2.isChecked() :
        print("Genero feminino")
        genero = "Feminino"
    elif cadastro.radioButton_3.isChecked() :
        print("Outro")
        genero = "Outro"


    cursor = banco.cursor()
    comando_SQL = "INSERT INTO pessoa (pnome,snome,email,gene) VALUES (%s,%s,%s,%s)"
    dados = (str(nome),str(sobrenome),str(email),genero)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    cadastro.lineEdit.setText("")
    cadastro.lineEdit_2.setText("")
    cadastro.lineEdit_3.setText("")

def chama_segunda_tela():
    listar_dados.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM pessoa"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    listar_dados.tableWidget.setRowCount(len(dados_lidos))
    listar_dados.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            listar_dados.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def excluir_dados():

    linha = listar_dados.tableWidget.currentRow()
    listar_dados.tableWidget.removeRow(linha)
    
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM pessoa")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM pessoa WHERE id="+str(valor_id))
    print(valor_id)





app=QtWidgets.QApplication([])
cadastro=uic.loadUi("cadastro.ui")
listar_dados=uic.loadUi("lista_de_cadastrados.ui")
tela_editar = uic.loadUi("menu_editar.ui")
cadastro.enviar.clicked.connect(funcao_principal)
cadastro.cadastrados.clicked.connect(chama_segunda_tela)
listar_dados.pushButton.clicked.connect(excluir_dados)
cadastro.show()
app.exec()


# criando a tabela

'''create table pessoa (
   id INT NOT NULL AUTO_INCREMENT,
   pnome VARCHAR(50),
   snome VARCHAR(50),  
   email VARCHAR(50),
   gene VARCHAR(20),
   PRIMARY KEY (id)

);''' 

# inserindo registros na tabela

"""INSERT INTO pessoa (pnome,snome,email,gene) VALUES ("Joao","Lacerda","joaolacerda@hotmail","Masculino");""" 
