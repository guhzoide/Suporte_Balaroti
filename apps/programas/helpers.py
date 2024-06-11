import pysftp as sf
import threading
from lib.banco import PASSWORD_SERVER_UPPER, PASSWORD_SERVER_LOWER, SERVER_USER

class helpersProgramas():
    def verificaprog():
        dados = []
        with open('bin/listalojas', 'r') as file:
            for line in file:
                address = line.strip()
                try:
                    try:
                        username = SERVER_USER
                        password = PASSWORD_SERVER_UPPER
                        hostkey_file = 'bin/known_hosts'
                        cnopts = sf.CnOpts()
                        cnopts.hostkeys.load(hostkey_file)

                        with sf.Connection(address, username=username, password=password, cnopts=cnopts) as sftp:
                            with open('log', 'a') as file:
                                file.write(f"Verificando: {address}")
                            result = str((sftp.execute("sh /etc/shell/verificaprog1")))
                            chars = "''()[],"
                            result = result.translate(str.maketrans('', '', chars))
                            result = result.replace("b", "").replace("n", "")
                            dados.append(line + ': ' + result)

                    except Exception:
                        username = SERVER_USER
                        password = PASSWORD_SERVER_LOWER
                        hostkey_file = 'bin/known_hosts'
                        cnopts = sf.CnOpts()
                        cnopts.hostkeys.load(hostkey_file)

                        with sf.Connection(address, username=username, password=password, cnopts=cnopts) as sftp:
                            with open('log', 'a') as file:
                                file.write(f"Verificando: {address}")
                            result = str((sftp.execute("sh /etc/shell/verificaprog1")))
                            chars = "''()[],"
                            result = result.translate(str.maketrans('', '', chars))
                            result = result.replace("b", "").replace("n", "")
                            dados.append(line + ': ' + result)
                except Exception as error:
                    error = str(error)
                    dados.append(f"Erro ao verificar {address}: {error}")
                    with open('log', 'a') as file:
                        file.write(f"Erro: {address} - {error}\n\n")
        
        return list(dados)

    def desativatudo():
        def desativatudo_lojas(address):
            try:
                username = SERVER_USER
                password = PASSWORD_SERVER_UPPER
                hostkey_file = 'bin/known_hosts'
                cnopts = sf.CnOpts()
                cnopts.hostkeys.load(hostkey_file)

                with sf.Connection(address, username=username, password=password, cnopts=cnopts) as sftp:
                    with open('log', 'a') as file:
                        file.write(f"Desativando: {address}\n")
                    result = sftp.execute("sh /etc/shell/desativatudo && sh /etc/shell/ativtudo")
                    
            except Exception:
                username = SERVER_USER
                password = PASSWORD_SERVER_LOWER
                hostkey_file = 'bin/known_hosts'
                cnopts = sf.CnOpts()
                cnopts.hostkeys.load(hostkey_file)

                with sf.Connection(address, username=username, password=password, cnopts=cnopts) as sftp:
                    with open('log', 'a') as file:
                        file.write(f"Desativando: {address}\n")
                    result = sftp.execute("sh /etc/shell/desativatudo && sh /etc/shell/ativtudo")
                    dados.append(result)
        

        def verifica_tempo_limite_lojas(address):
            tempo_limite = 15
            thread = threading.Thread(target=desativatudo_lojas, args=(address,))
            thread.start()
            thread.join(tempo_limite)
            if thread.is_alive():
                with open('log', 'a') as file:
                    file.write(f"Loja {address} finalizada")
                raise TimeoutError(f"Loja {address} finalizada\n")
            
        def desativatudo_dep(address):
            try:
                username = SERVER_USER
                password = PASSWORD_SERVER_UPPER
                hostkey_file = 'bin/known_hosts'
                cnopts = sf.CnOpts()
                cnopts.hostkeys.load(hostkey_file)

                with sf.Connection(address, username=username, password=password, cnopts=cnopts) as sftp:
                    with open('log', 'a') as file:
                        file.write(f"Desativando: {address}\n")
                    result = sftp.execute("sh /etc/shell/desativatudo && sh /etc/shell/ativmqtudo && sh /etc/shell/ativsoctudo")
                    
            except Exception:
                username = SERVER_USER
                password = PASSWORD_SERVER_LOWER
                hostkey_file = 'bin/known_hosts'
                cnopts = sf.CnOpts()
                cnopts.hostkeys.load(hostkey_file)

                with sf.Connection(address, username=username, password=password, cnopts=cnopts) as sftp:
                    with open('log', 'a') as file:
                        file.write(f"Desativando: {address}\n")
                    result = sftp.execute("sh /etc/shell/desativatudo && sh /etc/shell/ativmqtudo && sh /etc/shell/ativsoctudo")
                    dados.append(result)
        

        def verifica_tempo_limite_dep(address):
            tempo_limite = 20
            thread = threading.Thread(target=desativatudo_dep, args=(address,))
            thread.start()
            thread.join(tempo_limite)
            if thread.is_alive():
                with open('log', 'a') as file:
                    file.write(f"Loja {address} finalizada")
                raise TimeoutError(f"Loja {address} finalizada\n")
            
        with open('bin/listalojas', 'r') as file: 
            for line in file:
                line = line.strip()
                if 'sjdep' or 'cascd' or 'loncd' in line:
                    address = line
                    verifica_tempo_limite_dep(address)
                address = line
                try:
                    verifica_tempo_limite_lojas(address)
                except TimeoutError as e:
                    print(e)
        dados = helpersProgramas.verificaprog()

        return dados