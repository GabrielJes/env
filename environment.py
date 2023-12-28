#!/usr/bin/env python3
import subprocess
import json
from time import sleep
import argparse

def verf():
    """Verificar se o ambiente virtual está instalado da maneira mais básica possível"""
    CheckingEnvInstallation = lambda: subprocess.run(['virtualenv', '--version'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    jsonPATH = 'args.json'  # Caminho fixo para o arquivo JSON
    ReadArchivejson = lambda jsonPATH: json.load(open(jsonPATH, encoding='utf-8'))
    Datajson = ReadArchivejson(jsonPATH)
    
    try:
        ExecVerify = CheckingEnvInstallation()
        if int(ExecVerify.returncode) == 0:
            print(Datajson['0'])
        elif int(ExecVerify.returncode) == 1:
            print(Datajson['1'])
        elif int(ExecVerify.returncode) == 2:
            print(Datajson['2'])
        elif int(ExecVerify.returncode) == 126:
            print(Datajson['126'])
        elif int(ExecVerify.returncode) == 127:
            print(Datajson['127'])
        elif int(ExecVerify.returncode) == 128:
            print(Datajson['128'])
        
        print(f"Localizado arquivo virtualenv.")
            
    except Exception as e:
        print(f"Erro: {e}")
        
    return True

def init(EnvironmentName: str): 
    try:
        exec_t = subprocess.run(['virtualenv', EnvironmentName], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        confirm = exec_t.returncode
        if confirm == 0:
            try:
                command = f'{EnvironmentName}\\Scripts\\activate'
                result = subprocess.run([command], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                if result.returncode == 0:
                    print(f"Ativado com sucesso")
            except Exception as error:
                print(error)
    except Exception as e:
        print(f'Error: {e}')

def main():
    parser = argparse.ArgumentParser(description='Verificar e inicializar ambiente virtual.')
    # Removida a opção de passar o caminho do JSON como argumento
    # parser.add_argument('--json', required=True, help='Caminho para o arquivo JSON de configuração')
    parser.add_argument('--init', action='store_true', help='Inicializar ambiente virtual (requer o nome do ambiente)')

    args = parser.parse_args()

    if args.init:
        nome_ambiente = input('Nome do ambiente virtual: ')
        init(nome_ambiente)
    else:
        print("Verificando instalação...")
        sleep(0.5)
        verf()

if __name__ == "__main__":
    main()
