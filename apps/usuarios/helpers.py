import pyodbc
import cx_Oracle

class CompararMatricula():
    def comparacao(usuario_com_lib, usuario_sem_lib, usuario_efetua_liberacao):

        # Listas do DBMTRIZ
        usuario_com_liberacao_triz = []
        usuario_sem_liberacao_triz = []
        liberacao_dbmaker = []

        # Listas do DBSJOSE
        usuario_com_liberacao_oracle = []
        usuario_sem_liberacao_oracle = []
        liberacao_oracle = []

        # Configurações do oracle
        db_config = {
            'user': 'aplicacao',
            'password': '@@aplicacao#$',
            'dsn': 'oracle-scan:1521/DBERP'
        }


        # Conexão e equiparação no DBMTRIZ
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
            liberacao_dbmaker.append(acesso)
        try:
            for liberar_triz in liberacao_dbmaker:
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
            for liberar_sjose in liberacao_dbmaker:
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
            liberacao_oracle.append(acesso)
        try:
            for liberar_oracle in liberacao_oracle:
                cursor.execute(f"INSERT INTO USUARIO_PERFIL (ID_USUARIO, CD_PERFIL, CD_USUARIO, DT_ATUALIZACAO) VALUES ({usuario_sem_lib}, '{liberar_oracle}', {usuario_efetua_liberacao}, '')")

        except Exception as error:
            with open('log.txt', 'a') as file:
                file.write(f"Erro oracle: {error}\n")

        try:
            loja = cursor.execute(f"SELECT US_LOJA FROM APLICACAO.USUARIO WHERE US_IDUSUARIO = {usuario_sem_lib}")
            loja = str(loja.fetchall())

            chars = "\''()[],"
            loja = loja.translate(str.maketrans('', '', chars))

            print(f"\nATENÇÃO!! Rode o enviausuario para a loja {loja}\n")
        except Exception as error:
            with open('log.txt', 'a') as file:
                file.write(f"Erro enviausuario: {error}\n")

        connection.commit()
        connection.close()

        acessos_liberados = f"Acessos liberados no oracle:\n{liberacao_oracle}\nAcessos liberados no dbmaker:\n{liberacao_dbmaker}"

        return acessos_liberados