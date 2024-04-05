import pysftp as sf
import threading

class helpersProgramas():
    def verificaprog():
        dados = []
        with open('bin/listalojas', 'r') as file:
            for line in file:
                address = line.strip()
                try:
                    try:
                        username = 'root'
                        password = 'Rt9jkb43'
                        hostkey_file = 'bin/known_hosts'
                        cnopts = sf.CnOpts()
                        cnopts.hostkeys.load(hostkey_file)

                        with sf.Connection(address, username=username, password=password, cnopts=cnopts) as sftp:
                            with open('log', 'a') as file:
                                file.write(f"Verificando: {address}\n\n")
                            result = str((sftp.execute("sh /etc/shell/verificaprog1")))
                            chars = "''()[],"
                            result = result.translate(str.maketrans('', '', chars))
                            result = result.replace("b", "").replace("n", "")
                            dados.append(line + ': ' + result)

                    except Exception:
                        username = 'root'
                        password = 'rt9jkb43'
                        hostkey_file = 'bin/known_hosts'
                        cnopts = sf.CnOpts()
                        cnopts.hostkeys.load(hostkey_file)

                        with sf.Connection(address, username=username, password=password, cnopts=cnopts) as sftp:
                            with open('log', 'a') as file:
                                file.write(f"Verificando: {address}\n\n")
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
        def desativatudo(address):
            try:
                username = 'root'
                password = 'Rt9jkb43'
                hostkey_file = 'bin/known_hosts'
                cnopts = sf.CnOpts()
                cnopts.hostkeys.load(hostkey_file)

                with sf.Connection(address, username=username, password=password, cnopts=cnopts) as sftp:
                    with open('log', 'a') as file:
                        file.write(f"Desativando: {address}\n")
                    result = sftp.execute("sh /etc/shell/desativatudo && sh /etc/shell/ativtudo")
                    
            except Exception:
                username = 'root'
                password = 'rt9jkb43'
                hostkey_file = 'bin/known_hosts'
                cnopts = sf.CnOpts()
                cnopts.hostkeys.load(hostkey_file)

                with sf.Connection(address, username=username, password=password, cnopts=cnopts) as sftp:
                    with open('log', 'a') as file:
                        file.write(f"Desativando: {address}\n")
                    result = sftp.execute("sh /etc/shell/desativatudo && sh /etc/shell/ativtudo")
                    dados.append(result)
        

        def verifica_tempo_limite(address):
            tempo_limite = 15
            thread = threading.Thread(target=desativatudo, args=(address,))
            thread.start()
            thread.join(tempo_limite)
            if thread.is_alive():
                with open('log', 'a') as file:
                    file.write(f"Loja {address} finalizada\n\n")
                raise TimeoutError(f"Loja {address} finalizada\n")
            
        with open('bin/listalojas', 'r') as file: 
            for line in file:
                address = line.strip()
                try:
                    verifica_tempo_limite(address)
                except TimeoutError as e:
                    print(e)
        dados = helpersProgramas.verificaprog()

        return dados