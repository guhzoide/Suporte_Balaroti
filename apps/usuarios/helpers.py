import pyodbc
import requests
import cx_Oracle
import smtplib
import pysftp as sf
from lib.banco import PASSWORD_SERVER_LOWER, SERVER_USER, SERVIDOR_EMAIL_VENDAS
from lib.banco import DB_CONFIG, EMAIL, SENHA_EMAIL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class LiberarMatricula():
    def comparacao(usuario_com_lib, usuario_sem_lib, usuario_efetua_liberacao):

        # Listas do DBMTRIZ
        usuario_com_liberacao_triz = []
        usuario_sem_liberacao_triz = []
        dbmaker = []

        # Listas do DBSJOSE
        usuario_com_liberacao_oracle = []
        usuario_sem_liberacao_oracle = []
        oracle = []

        # Configurações do oracle
        db_config = DB_CONFIG

        # Conexão e equiparação no BDMTRIZ
        conn = pyodbc.connect('DSN=BDMTRIZ')
        cur = conn.cursor()
        result = cur.execute(f"SELECT USP_ACESSO FROM SYSADM.USPERMIS WHERE USPERMIS.USP_IDUSUARIO  = {usuario_com_lib};")
        result = cur.fetchall()

        for row in result:
            for col in row:
                col = col.strip()
                chars = "\''()[],"
                col = col.translate(str.maketrans('', '', chars))
                usuario_com_liberacao_triz.append(col)


        result = cur.execute(f"SELECT USP_ACESSO FROM SYSADM.USPERMIS WHERE USPERMIS.USP_IDUSUARIO  = {usuario_sem_lib};")

        for row in result:
            for col in row:
                col = col.strip()
                chars = "\''()[],"
                col = col.translate(str.maketrans('', '', chars))
                usuario_sem_liberacao_triz.append(col)

        # Comparação dos acessos e impressão das diferenças
        acessos_diferentes_dbmaker = set(usuario_com_liberacao_triz) - set(usuario_sem_liberacao_triz)

        for acesso in acessos_diferentes_dbmaker:
            dbmaker.append(acesso)
        try:
            for liberar_triz in dbmaker:
                cur.execute(f"insert into SYSADM.USPERMIS (USP_IDUSUARIO, USP_ACESSO, USP_TIPO) values ({usuario_sem_lib}, '{liberar_triz}', '');")

        except Exception as error:
            with open('log.txt', 'a') as file:
                file.write(f"Erro triz: {error}\n")

        cur.commit()
        cur.close()

        # Conexão e equiparação no DBSJOSE
        conn = pyodbc.connect('DSN=DBSJOSE;UID=sysadm')
        cur = conn.cursor()

        try:
            for liberar_sjose in dbmaker:
                cur.execute(f"insert into SYSADM.USPERMIS (USP_IDUSUARIO, USP_ACESSO, USP_TIPO) values ({usuario_sem_lib}, '{liberar_sjose}', '');")

        except Exception as error:
            with open('log.txt', 'a') as file:
                file.write(f"Erro sjose: {error}\n")

        cur.commit()
        cur.close()

        # Conexão e equiparação no ORACLE
        connection = cx_Oracle.connect(**db_config)
        cursor = connection.cursor()
        sql_select = f"SELECT CD_PERFIL FROM APLICACAO.USUARIO_PERFIL WHERE ID_USUARIO = {usuario_com_lib}"
        result = cursor.execute(sql_select)

        for row in result:
            for col in row:
                col = col.strip()
                chars = "\''()[],"
                col = col.translate(str.maketrans('', '', chars))
                usuario_com_liberacao_oracle.append(col)

        sql_select = f"""
            SELECT CD_PERFIL FROM APLICACAO.USUARIO_PERFIL WHERE ID_USUARIO = {usuario_sem_lib} 
        """
        result = cursor.execute(sql_select)

        for row in result:
            for col in row:
                col = col.strip()
                chars = "\''()[],"
                col = col.translate(str.maketrans('', '', chars))
                usuario_sem_liberacao_oracle.append(col)

        acessos_diferentes_oracle = set(usuario_com_liberacao_oracle) - set(usuario_sem_liberacao_oracle)

        for acesso in acessos_diferentes_oracle:
            oracle.append(acesso)
        try:
            for liberar_oracle in oracle:
                cursor.execute(f"INSERT INTO USUARIO_PERFIL (ID_USUARIO, CD_PERFIL, CD_USUARIO, DT_ATUALIZACAO) VALUES ({usuario_sem_lib}, '{liberar_oracle}', {usuario_efetua_liberacao}, '')")

        except Exception as error:
            with open('log.txt', 'a') as file:
                file.write(f"Erro oracle: {error}\n")

        try:
            loja = cursor.execute(f"SELECT US_LOJA FROM APLICACAO.USUARIO WHERE US_IDUSUARIO = {usuario_sem_lib}")
            loja = str(loja.fetchall())

            chars = "\''()[],"
            loja = loja.translate(str.maketrans('', '', chars))

            texto = f"\nATENÇÃO!! Rode o enviausuario para a loja {loja}\n"
        except Exception as error:
            with open('log.txt', 'a') as file:
                file.write(f"Erro enviausuario: {error}\n")

        perfis = []
        for perfil in oracle:
            result = cursor.execute(f"SELECT DE_PERFIL FROM APLICACAO.PERFIL WHERE PERFIL.CD_PERFIL = {perfil}")
            result = str(result.fetchall())
            chars = "\''()[],"
            result = result.translate(str.maketrans('', '', chars))
            perfis.append(result)

        connection.commit()
        connection.close()
        return perfis, dbmaker, texto
    
    def liberar(usuario_lib, usuario_efetua_liberacao):
        try:          
            try:
                conn = pyodbc.connect('DSN=BDMTRIZ')
                cur = conn.cursor()
                cur.execute(f"insert into SYSADM.USPERMIS (USP_IDUSUARIO, USP_ACESSO, USP_TIPO) values ({usuario_lib}, 'Vendas Master', '');")
                cur.commit()
                cur.close()
            except:
                pass

            try:
                conn = pyodbc.connect('DSN=DBSJOSE; UID=sysadm')
                cur = conn.cursor()
                cur.execute(f"insert into SYSADM.USPERMIS (USP_IDUSUARIO, USP_ACESSO, USP_TIPO) values ({usuario_lib}, 'Vendas Master', '');")
                cur.commit()
                cur.close()
            except:
                pass
            
            db_config = DB_CONFIG
            connection = cx_Oracle.connect(**db_config)
            cursor = connection.cursor()
            liberacoes = ['032', '023']

            for liberacao in liberacoes:
                try:
                    cursor.execute(f"INSERT INTO USUARIO_PERFIL (ID_USUARIO, CD_PERFIL, CD_USUARIO, DT_ATUALIZACAO) VALUES ({usuario_lib}, '{liberacao}', {usuario_efetua_liberacao}, '')")
                except:
                    pass

            loja_vendedor = cursor.execute(f"SELECT US_LOJA FROM APLICACAO.USUARIO WHERE US_IDUSUARIO = {usuario_lib}")
            loja_vendedor = str(loja_vendedor.fetchall())

            chars = "\''()[],"
            loja_vendedor = loja_vendedor.translate(str.maketrans('', '', chars))

            connection.commit()
            connection.close()
            texto = f"Acessos liberados, rode o enviausuario para a loja {loja_vendedor}\n"
            return texto
        except Exception as error:
            texto = f"Ocorreu um erro ao liberar:\n {error}"
            return texto

    def criarEmailZimbra(email, senha, acesso, nome):
        if acesso == 'Gestao':
            pass

        else:
            #try:
            address = SERVIDOR_EMAIL_VENDAS
            username = SERVER_USER
            password = 'rt9jkb43'
            hostkey_file = 'bin/known_hosts'
            cnopts = sf.CnOpts()
            cnopts.hostkeys.load(hostkey_file)

            with sf.Connection(address, username=username, password=password, cnopts=cnopts) as sftp:
                result = sftp.execute(f"/opt/zimbra/bin/zmprov ca {email} {senha} displayName '{nome}'")
                print(result)
            # except Exception as error:
            #     print(f"Erro e-mail: {str(error)}")
                    

    def gerenteContaOmni(nome, email, matricula, senha, descricao_vendedor, codigo_vendedor, descricao_gestao, codigo_gestao):
        url = "https://user-api.omni.chat/v1/users"

        payload = {
        "configuration": {
            "stickerSendingDisabled": True,
            "cannotStartConversation": False,
            "multipleRecipientsDisabled": True
        },

        "supervisedTeams":[
            {
                "id": f"{codigo_vendedor}",
                "name": f"{descricao_vendedor}"
            }
        ],
        "supervisedTeams":[
            {
                "id": f"{codigo_gestao}",
                "name": f"{descricao_gestao}"
            }
        ],

        "teams":[
            {
                "id": f"{codigo_gestao}",
                "name": f"{descricao_gestao}"
            }
        ],

        "name": f"{nome}",
        "username": f"{email}",
        "password": f"{senha}",
        "salesPersonCode": f"{matricula}",
        "roles": ["service", "supervisor"]
        }
        headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": "PQRBLpZj2U7P97QrIQrTu7uukbVhkVZu2S0mppWd",
        "x-api-secret": "r:7a2fb21821337f4c8d3f15a471030b2e"
        }

        # email_servidor = "mx.balaroti.com.br"
        # porta = 465
        # usuario = EMAIL
        # senha_email_envio = SENHA_EMAIL

        # de =usuario
        # para = email

        # mensagem = MIMEMultipart()
        # mensagem["From"] = de
        # mensagem["To"] = para
        # mensagem["Subject"] = "OmniChat"

        # corpo = f"Olá, segue e-mail e senha para acesso ao OmniChat:\n{email}\n{senha}"
        # mensagem.attach(MIMEText(corpo, "plain"))

        # try:
        #     servidor_smtp = smtplib.SMTP_SSL(email_servidor, porta)
        #     servidor_smtp.login(usuario, senha_email_envio)
        #     servidor_smtp.sendmail(de, para, mensagem.as_string())

        #     texto = "E-mail enviado com sucesso!"
        #     servidor_smtp.quit()
        # except Exception as error:
        #     print(f"Erro e-mail: {error}")

        # try:
        #     conn = pyodbc.connect('DSN=BDMTRIZ')
        #     cur = conn.cursor()
        #     cur.execute(f"UPDATE SYSADM.USUARIO SET US_EMAIL='{email}' WHERE US_IDUSUARIO={matricula};")
        #     cur.commit()
        #     cur.close()
        # except Exception as error:
        #     print(f"Erro atualiza banco: {error}")

        try:
            result = requests.post(url, json=payload, headers=headers)
            print(result)
            texto = "Conta criada com sucesso"
        except Exception as error:
            print(f"Erro cria omni: {error}")

        return texto

    def vendedorContaOmni(nome, email, matricula, senha, descricao_vendedor, codigo_vendedor):
        url = "https://user-api.omni.chat/v1/users"

        payload = {
            "configuration": {
                "stickerSendingDisabled": True,
                "cannotStartConversation": False,
                "multipleRecipientsDisabled": True
            },
            "teams":[
                {
                    "id": f"{codigo_vendedor}",
                    "name": f"{descricao_vendedor}"
                }
            ],
            "name": f"{nome}",
            "username": f"{email}",
            "password": f"{senha}",
            "salesPersonCode": f"{matricula}",
            "roles": ["service"]
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "x-api-key": "PQRBLpZj2U7P97QrIQrTu7uukbVhkVZu2S0mppWd",
            "x-api-secret": "r:7a2fb21821337f4c8d3f15a471030b2e"
        }

        # email_servidor = "mx.balaroti.com.br"
        # porta = 465
        # usuario = EMAIL
        # senha_email_envio = SENHA_EMAIL

        # de =usuario
        # para = email

        # mensagem = MIMEMultipart()
        # mensagem["From"] = de
        # mensagem["To"] = para
        # mensagem["Subject"] = "OmniChat"

        # corpo = f"Olá, segue e-mail e senha para acesso ao OmniChat:\n{email}\n{senha}"
        # mensagem.attach(MIMEText(corpo, "plain"))

        # try:
        #     servidor_smtp = smtplib.SMTP_SSL(email_servidor, porta)
        #     servidor_smtp.login(usuario, senha_email_envio)
        #     servidor_smtp.sendmail(de, para, mensagem.as_string())

        #     texto = "E-mail enviado com sucesso!"
        #     servidor_smtp.quit()
        # except Exception as error:
        #     print(f"Erro e-mail: {error}")

        # try:
        #     conn = pyodbc.connect('DSN=BDMTRIZ')
        #     cur = conn.cursor()
        #     cur.execute(f"UPDATE SYSADM.USUARIO SET US_EMAIL='{email}' WHERE US_IDUSUARIO={matricula};")
        #     cur.commit()
        #     cur.close()
        # except Exception as error:
        #     print(f"Erro atualiza banco: {error}")

        try:
            result = requests.post(url, json=payload, headers=headers)
            print(result)
            texto = "Conta criada com sucesso"
        except Exception as error:
            print(f"Erro cria omni: {error}")

        return texto