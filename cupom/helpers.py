import os
from bin.banco import HOSTBD, USUSARIO, SENHA, BANCO
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

host=HOSTBD
user=USUSARIO
password=SENHA
database=BANCO

class Cupom():
    def situacaoAtual():
        dados = []
        quantidade = 0
        msg = ''
        con = mysql.connector.connect(host=host, user=user, password=password, database=database)
        try:
            cursor = con.cursor()

            cursor.execute(f"SELECT numero_cupom, numero_pdv, numero_loja, dat_hor_proc, situacao_movimento FROM exp_imp_movimento where situacao_movimento='1';")

            colunas = [col[0] for col in cursor.description]
            for linha in cursor.fetchall():
                dados.append(dict(zip(colunas, linha)))

            cursor.close()
            con.close()

            quantidade = len(dados)
            if quantidade == 0:
                msg = 'Nenhum cupom encontrado'
                dados = []
            return msg, dados, quantidade

        except Exception as error:
            msg = str(error)
            return msg, dados, quantidade
    
    def consultaCupom(data, numero_cupom):
        dados = []
        quantidade = 0
        msg = ''
        con = mysql.connector.connect(host=host, user=user, password=password, database=database)
        try:
            cursor = con.cursor()

            if data == '' and numero_cupom == '':
                msg = 'Preencha os filtros para realizar a pesquisa'
                print(msg)
                return msg, dados, quantidade

            cursor.execute(f"SELECT numero_cupom, numero_pdv, numero_loja, dat_hor_proc, situacao_movimento FROM exp_imp_movimento WHERE data_movimento='{data}' and numero_cupom={numero_cupom};")

            colunas = [col[0] for col in cursor.description]
            for linha in cursor.fetchall():
                dados.append(dict(zip(colunas, linha)))

            cursor.close()
            con.close()

            quantidade = len(dados)
            if quantidade == 0:
                msg = 'Nenhum cupom encontrado'
                dados = []
            return msg, dados, quantidade

        except Exception as error:
            msg = str(error)
            return msg, dados, quantidade