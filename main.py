import os
import json
import time
import random
from datetime import datetime
os.system("cls")

#Variáveis globais
arquivo_cadastros = "pacientes.json"
arquivo_prontuarios = "prontuarios.json"
menuPrincipal = True
menuCadastros = True
menuProntuarios = True

#Funções
def inicializar_arquivo_cadastros() -> None: 
    if not os.path.exists(arquivo_cadastros):
        with open(arquivo_cadastros, 'w') as arq:
            json.dump([], arq)
            
def inicializar_arquivo_prontuarios() -> None: 
    if not os.path.exists(arquivo_prontuarios):
        with open(arquivo_prontuarios, 'w') as arq:
            json.dump([], arq)

def carregar_cadastros():
    with open(arquivo_cadastros, 'r') as arq:
        try:
            return json.load(arq)
        except Exception as e:
            print(f"Erro ao carregar cadastros: {e}")
            time.sleep(0.5)
            return []
        
def carregar_prontuarios():
    with open(arquivo_prontuarios, 'r') as arq:
        try:
            return json.load(arq)
        except Exception as e:
            print(f"Erro ao carregar prontuarios: {e}")
            time.sleep(0.5)
            return []

def salvar_cadastro(cadastro):
    with open(arquivo_cadastros, 'w') as arq:
        json.dump(cadastro, arq, indent=4)
        
def salvar_prontuario(prontuario):
    with open(arquivo_prontuarios, 'w') as arq:
        json.dump(prontuario, arq, indent=4)
        
def cadastrar_usuario():
    cadastros = carregar_cadastros()
    cadastrarOn = True
    while cadastrarOn:
        
        #Validar RG
        while True:
            os.system("cls")
            print("--- Cadastrar usuário ---\n")
            rgPaciente = input("RG do paciente (apenas números): ").strip()
            
            if rgPaciente == "":
                print("\nDigite algo!\n")
                time.sleep(0.5)
                os.system("cls")
                continue
            
            if rgPaciente.isdigit() == False or len(rgPaciente) != 9:
                print("\nRG inválido!\n")
                time.sleep(0.5)
                os.system("cls")
                continue
            
            rgRepetido = False
            for i in cadastros:
                if i['rg'] == rgPaciente:
                    print("\nEste RG já foi cadastrado.\n")
                    
                    while True:
                        opcao = input("Deseja tentar novamente? (s/n): ").strip().lower()
                        if opcao not in ['s', 'n']:
                            print("\nOpção inválida!\n")
                            time.sleep(0.5)
                            continue
                        break
                    
                    if opcao == 'n':
                        cadastrarOn = False
                        break
                    elif opcao == 's':
                        rgRepetido = True
                        continue
                    os.system("cls")
            
            if rgRepetido:
                continue
                   
            break
        
        if cadastrarOn == False:
            os.system("cls")
            print("\nCadastro cancelado.\n")
            time.sleep(0.5)
            os.system("cls")
            break

        #Validar nome do paciente
        while True:
            os.system("cls")
            print("--- Cadastrar usuário ---\n")
            nomePaciente = input("Nome do paciente: ").strip()
            
            if nomePaciente == "":
                print("\nDigite algo!\n")
                time.sleep(0.5)
                continue
            
            break

        #Validar data de nascimento
        while True:
            os.system("cls")
            print("--- Cadastrar usuário ---\n")
            dataNascimento = input("Data de nascimento (ddmmaa): ").strip()
            
            if dataNascimento == "":
                print("\nDigite algo!\n")
                time.sleep(0.5)
                continue
            
            if not dataNascimento.isdigit() or not (len(dataNascimento) == 6):
                print("\nData inválida! Use o formato DDMMAA.\n")
                time.sleep(0.5)
                continue
            
            dia = int(dataNascimento[:2])
            mes = int(dataNascimento[2:4])
            ano = int(dataNascimento[4:])
            
            if (dia < 1 or dia > 31) or (mes < 1 or mes > 12) or (ano < 0 or ano > datetime.now().year):
                print("\nData inválida!\n")
                time.sleep(0.5)
                continue
            
            break

        #Validar CPF do responsável
        while True:
            os.system("cls")
            print("--- Cadastrar usuário ---\n")
            cpfResponsavel = input("CPF do responsável (apenas números): ").strip()
            
            if cpfResponsavel == "":
                print("\nDigite algo!\n")
                time.sleep(0.5)
                continue
            
            if not cpfResponsavel.isdigit() or len(cpfResponsavel) != 11:
                print("\nCPF inválido! Deve conter 11 dígitos.\n")
                time.sleep(0.5)
                continue
            
            break
        
        #Validar nome do responsável
        while True:
            os.system("cls")
            print("--- Cadastrar usuário ---\n")
            nomeResponsavel = input("Nome do responsável: ").strip()
            
            if nomeResponsavel == "":
                print("\nDigite algo!\n")
                time.sleep(0.5)
                continue
            
            break
        
        #Validar telefone do responsável
        while True:
            os.system("cls")
            print("--- Cadastrar usuário ---\n")
            telefoneResponsavel = input("DDD e telefone do responsável (apenas números): ").strip()
            
            if telefoneResponsavel == "":
                print("\nDigite algo!\n")
                time.sleep(0.5)
                continue
            
            if not telefoneResponsavel.isdigit():
                print("\nTelefone inválido!\n")
                time.sleep(0.5)
                continue
            
            break
        
        #Gerando novo cadastro
        dataCadastro = datetime.now().strftime("%d%m%y")
        novo_usuario = {
            'rg': rgPaciente,
            'nome': nomePaciente,
            'dataNascimento': dataNascimento,
            'cpfResponsavel': cpfResponsavel,
            'nomeResponsavel': nomeResponsavel,
            'telefoneResponsavel': telefoneResponsavel,
            'dataCadastro': dataCadastro
        }

        #Salvando no arquivo JSON
        cadastros.append(novo_usuario)
        salvar_cadastro(cadastros)
        
        os.system("cls")
        print("--- Cadastrar usuário ---\n\nPaciente cadastrado com sucesso!\n")
        input("Pressione Enter para continuar...")
        os.system("cls")
        cadastrarOn = False

def editar_usuario():
    cadastros = carregar_cadastros()
    editarOn = True
    while editarOn:
        
        #Validar RG
        while True:
            os.system("cls")
            print("--- Editar usuário ---\n")
            rgPaciente = input("RG do paciente (apenas números): ").strip()
            
            cadastroLocalizado = False
            for i in cadastros:
                if i['rg'] == rgPaciente:
                    cadastroLocalizado = i
                    break
                
            if not cadastroLocalizado:
                print("\nCadastro não encontrado!\n")
                while True:
                    opcao = input("Deseja tentar novamente? (s/n): ").strip().lower()
                    if opcao not in ['s', 'n']:
                        print("\nOpção inválida!\n")
                        time.sleep(0.5)
                        continue
                    break
                if opcao == 'n':
                    editarOn = False
                    break
                elif opcao == 's':
                    continue
                
            break

        if editarOn == False:
            os.system("cls")
            print("\nEdição cancelada.\n")
            time.sleep(0.5)
            os.system("cls")
            break

        # Editar nome do paciente
        while True:
            os.system("cls")
            print("--- Editar usuário ---\n")
            nome = input(f"Nome do paciente: {cadastroLocalizado['nome']}\n(Deixe vazio para manter os dados antigos)\n\nAlterar para: ").strip()
            if nome == "":
                nome = cadastroLocalizado['nome']
            break

        # Editar data de nascimento
        while True:
            os.system("cls")
            print("--- Editar usuário ---\n")
            dataNascimento = input(f"Data de nascimento: {cadastroLocalizado['dataNascimento']}\n(Deixe vazio para manter os dados antigos)\n\nAlterar para: ").strip()
            if dataNascimento == "":
                dataNascimento = cadastroLocalizado['dataNascimento']
                break

            if not dataNascimento.isdigit() or len(dataNascimento) != 6:
                print("\nData inválida! Use o formato DDMMAA.\n")
                time.sleep(0.5)
                continue

            dia = int(dataNascimento[:2])
            mes = int(dataNascimento[2:4])
            ano = int(dataNascimento[4:])

            if (dia < 1 or dia > 31) or (mes < 1 or mes > 12) or (ano < 0 or ano > datetime.now().year):
                print("\nData inválida!\n")
                time.sleep(0.5)
                continue
            break

        # Editar CPF do responsável
        while True:
            os.system("cls")
            print("--- Editar usuário ---\n")
            cpf = input(f"CPF do responsável: {cadastroLocalizado['cpfResponsavel']}\n(Deixe vazio para manter os dados antigos)\n\nAlterar para: ").strip()
            if cpf == "":
                cpf = cadastroLocalizado['cpfResponsavel']
                break
            if not cpf.isdigit() or len(cpf) != 11:
                print("\nCPF inválido! Deve conter 11 dígitos.\n")
                time.sleep(0.5)
                continue
            break

        # Editar nome do responsável
        while True:
            os.system("cls")
            print("--- Editar usuário ---\n")
            nomeResp = input(f"Nome do responsável: {cadastroLocalizado['nomeResponsavel']}\n(Deixe vazio para manter os dados antigos)\n\nAlterar para: ").strip()
            if nomeResp == "":
                nomeResp = cadastroLocalizado['nomeResponsavel']
            break

        # Editar telefone do responsável
        while True:
            os.system("cls")
            print("--- Editar usuário ---\n")
            telefone = input(f"Telefone do responsável: {cadastroLocalizado['telefoneResponsavel']}\n(Deixe vazio para manter os dados antigos)\n\nAlterar para: ").strip()
            if telefone == "":
                telefone = cadastroLocalizado['telefoneResponsavel']
                break
            if not telefone.isdigit():
                print("\nTelefone inválido!\n")
                time.sleep(0.5)
                continue
            break

        # Atualizando dados
        cadastroLocalizado['nome'] = nome
        cadastroLocalizado['dataNascimento'] = dataNascimento
        cadastroLocalizado['cpfResponsavel'] = cpf
        cadastroLocalizado['nomeResponsavel'] = nomeResp
        cadastroLocalizado['telefoneResponsavel'] = telefone

        salvar_cadastro(cadastros)

        os.system("cls")
        print("--- Editar usuário ---\n\nCadastro atualizado com sucesso!\n")
        input("Pressione Enter para continuar...")
        os.system("cls")
        editarOn = False

def deletar_usuario():
    cadastros = carregar_cadastros()
    deletarOn = True
    while deletarOn:

        # Validar RG
        while True:
            os.system("cls")
            print("--- Deletar usuário ---\n")
            rgPaciente = input("RG do paciente (apenas números): ").strip()

            cadastroLocalizado = None
            for i in cadastros:
                if i['rg'] == rgPaciente:
                    cadastroLocalizado = i
                    break

            if not cadastroLocalizado:
                print("\nCadastro não encontrado!\n")
                while True:
                    opcao = input("Deseja tentar novamente? (s/n): ").strip().lower()
                    if opcao not in ['s', 'n']:
                        print("\nOpção inválida!\n")
                        time.sleep(0.5)
                        continue
                    break

                if opcao == 'n':
                    deletarOn = False
                    break
                elif opcao == 's':
                    continue

            break

        if deletarOn == False:
            os.system("cls")
            print("\nOperação cancelada.\n")
            time.sleep(0.5)
            os.system("cls")
            break

        # Confirmar exclusão
        while True:
            os.system("cls")
            print("--- Deletar usuário ---\n")
            print(f"Nome do paciente: {cadastroLocalizado['nome']}")
            print(f"RG: {cadastroLocalizado['rg']}")
            print(f"Data de nascimento: {cadastroLocalizado['dataNascimento']}")
            print(f"Responsável: {cadastroLocalizado['nomeResponsavel']}")
            print(f"CPF do responsável: {cadastroLocalizado['cpfResponsavel']}")
            print(f"Telefone do responsável: {cadastroLocalizado['telefoneResponsavel']}\n")
            opcao = input("Tem certeza que deseja deletar este cadastro? (s/n): ").strip().lower()
            if opcao not in ['s', 'n']:
                print("\nOpção inválida!\n")
                time.sleep(0.5)
                continue
            break

        if opcao == 'n':
            os.system("cls")
            print("\nOperação cancelada.\n")
            time.sleep(0.5)
            os.system("cls")
            break
        elif opcao == 's':
            # Apagar prontuarios relacionados
            prontuarios = carregar_prontuarios()
            prontuarios_para_remover = []
            for prontuario in prontuarios:
                if prontuario['rg'] == rgPaciente:
                    # Apaga os arquivos .txt dos prontuarios desse paciente
                    for idProntuario in prontuario['idProntuarios']:
                        try:
                            os.remove(f"{idProntuario}.txt")
                        except FileNotFoundError:
                            pass  # Se o arquivo não existir, ignora
                    prontuarios_para_remover.append(prontuario)

            # Remove os prontuarios do JSON
            for p in prontuarios_para_remover:
                prontuarios.remove(p)

            salvar_prontuario(prontuarios)

            # Remove o cadastro do paciente
            cadastros.remove(cadastroLocalizado)
            salvar_cadastro(cadastros)

            os.system("cls")
            print("--- Deletar usuário ---\n\nCadastro e prontuários removidos com sucesso!\n")
            input("Pressione Enter para continuar...")
            os.system("cls")
            deletarOn = False

def buscar_usuario():
    cadastros = carregar_cadastros()
    buscarOn = True
    while buscarOn:

        # Validar RG
        while True:
            os.system("cls")
            print("--- Buscar usuário ---\n")
            rgPaciente = input("RG do paciente (apenas números): ").strip()

            cadastroLocalizado = None
            for i in cadastros:
                if i['rg'] == rgPaciente:
                    cadastroLocalizado = i
                    break

            if not cadastroLocalizado:
                print("\nCadastro não encontrado!\n")
                while True:
                    opcao = input("Deseja tentar novamente? (s/n): ").strip().lower()
                    if opcao not in ['s', 'n']:
                        print("\nOpção inválida!\n")
                        time.sleep(0.5)
                        continue
                    break

                if opcao == 'n':
                    buscarOn = False
                    break
                elif opcao == 's':
                    continue

            break

        if buscarOn == False:
            os.system("cls")
            print("\nBusca cancelada.\n")
            time.sleep(0.5)
            os.system("cls")
            break

        # Exibir informações do cadastro localizado
        os.system("cls")
        print("--- Buscar usuário ---\n")
        print(f"Nome do paciente: {cadastroLocalizado['nome']}")
        print(f"RG: {cadastroLocalizado['rg']}")
        print(f"Data de nascimento: {cadastroLocalizado['dataNascimento']}")
        print(f"Nome do responsável: {cadastroLocalizado['nomeResponsavel']}")
        print(f"CPF do responsável: {cadastroLocalizado['cpfResponsavel']}")
        print(f"Telefone do responsável: {cadastroLocalizado['telefoneResponsavel']}")
        print(f"Data de cadastro: {cadastroLocalizado['dataCadastro']}\n")
        
        input("Pressione Enter para continuar...")
        os.system("cls")
        buscarOn = False

def listar_usuarios():
    cadastros = carregar_cadastros()

    os.system("cls")
    print("--- Lista de usuários cadastrados ---\n")

    if not cadastros:
        print("Nenhum cadastro encontrado.\n")
        input("Pressione Enter para continuar...")
        os.system("cls")
        return

    # Cabeçalho da tabela
    print(f"{'RG':<12} {'Nome':<25} {'Nascimento':<13} {'Responsável':<25} {'CPF':<13} {'Telefone':<15} {'Data de cadastro':<10}")
    print("-" * 126)

    # Linhas da tabela
    for usuario in cadastros:
        print(f"{usuario['rg']:<12} "
              f"{usuario['nome'][:24]:<25} "
              f"{usuario['dataNascimento']:<13} "
              f"{usuario['nomeResponsavel'][:24]:<25} "
              f"{usuario['cpfResponsavel']:<13} "
              f"{usuario['telefoneResponsavel']:<15} "
              f"{usuario['dataCadastro']:<10}")
    
    print()
    input("Pressione Enter para continuar...")
    os.system("cls")

def criar_prontuario():
    prontuarios = carregar_prontuarios()
    cadastros = carregar_cadastros()
    criarOn = True

    while criarOn:
        os.system("cls")
        print("--- Criar prontuário ---\n")
        rgPaciente = input("RG do paciente (apenas números): ").strip()

        paciente_encontrado = False
        for i in cadastros:
            if i['rg'] == rgPaciente:
                paciente_encontrado = True
                break

        if not paciente_encontrado:
            print("\nPaciente não encontrado!\n")
            while True:
                opcao = input("Deseja tentar novamente? (s/n): ").strip().lower()
                if opcao not in ['s', 'n']:
                    print("\nOpção inválida!\n")
                    time.sleep(0.5)
                    continue
                break
            if opcao == 'n':
                criarOn = False
                break
            elif opcao == 's':
                continue

        break

    if criarOn == False:
        os.system("cls")
        print("\nCriação de prontuário cancelada.\n")
        time.sleep(0.5)
        os.system("cls")
        return

    idProntuario = datetime.now().strftime("%Y%m%d%H%M%S")

    encontrado = False
    for prontuario in prontuarios:
        if prontuario['rg'] == rgPaciente:
            prontuario['idProntuarios'].append(idProntuario)
            encontrado = True
            break

    if not encontrado:
        prontuarios.append({
            'rg': rgPaciente,
            'idProntuarios': [idProntuario]
        })

    salvar_prontuario(prontuarios)

    os.system("cls")
    print("--- Criar prontuário ---\n")
    print("Digite o conteúdo do prontuário linha por linha.")
    print("Para finalizar, pressione Enter em branco.\n")

    with open(f"{idProntuario}.txt", "w", encoding="utf-8") as f:
        while True:
            linha = input()
            if linha.strip() == "":
                break
            f.write(linha + "\n")

    os.system("cls")
    print("--- Criar prontuário ---\n\nProntuário criado com sucesso!\n")
    input("Pressione Enter para continuar...")
    os.system("cls")

def buscar_prontuarios():
    prontuarios = carregar_prontuarios()
    cadastros = carregar_cadastros()
    buscarOn = True

    while buscarOn:
        os.system("cls")
        print("--- Buscar prontuários ---\n")
        rgPaciente = input("RG do paciente (apenas números): ").strip()

        pacienteLocalizado = False
        for i in cadastros:
            if i['rg'] == rgPaciente:
                pacienteLocalizado = True
                break

        if not pacienteLocalizado:
            print("\nPaciente não encontrado!\n")
            while True:
                opcao = input("Deseja tentar novamente? (s/n): ").strip().lower()
                if opcao not in ['s', 'n']:
                    print("\nOpção inválida!\n")
                    time.sleep(0.5)
                    continue
                break
            if opcao == 'n':
                buscarOn = False
                os.system("cls")
                break
            elif opcao == 's':
                os.system("cls")
                continue

        prontuariosPaciente = None
        for p in prontuarios:
            if p['rg'] == rgPaciente:
                prontuariosPaciente = p['idProntuarios']
                break

        if not prontuariosPaciente or len(prontuariosPaciente) == 0:
            print("\nNenhum prontuário encontrado para este paciente.\n")
            input("Pressione Enter para continuar...")
            os.system("cls")
            break

        while True:
            os.system("cls")
            print("--- Prontuários encontrados ---\n")
            for idx, idp in enumerate(prontuariosPaciente):
                try:
                    dataFormatada = datetime.strptime(idp, "%Y%m%d%H%M%S").strftime("%d/%m/%Y às %H:%M:%S")
                except:
                    dataFormatada = idp
                print(f"{idx + 1}. {dataFormatada}")

            print("\nDigite o número do prontuário que deseja visualizar.")
            print("Ou pressione Enter em branco para cancelar.\n")
            escolha = input("Número: ").strip()

            if escolha == "":
                os.system("cls")
                print("\nBusca cancelada.\n")
                time.sleep(0.5)
                os.system("cls")
                return

            if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(prontuariosPaciente):
                print("\nEscolha inválida!\n")
                time.sleep(0.5)
                continue

            idSelecionado = prontuariosPaciente[int(escolha) - 1]
            break

        while True:
            os.system("cls")
            print(f"--- Prontuários encontrados ---\n")
            confirmar = input(f"\nDeseja visualizar o prontuário {escolha}? (s/n): ").strip().lower()
            if confirmar not in ['s', 'n']:
                print("\nOpção inválida!\n")
                time.sleep(0.5)
                continue
            break

        if confirmar == 'n':
            os.system("cls")
            print("\nVisualização cancelada.\n")
            time.sleep(0.5)
            os.system("cls")
            return

        os.system("cls")
        print(f"--- Prontuário {escolha} ---\n")

        try:
            with open(f"{idSelecionado}.txt", "r", encoding="utf-8") as f:
                conteudo = f.read()
                print(conteudo)
        except:
            print("Erro ao abrir o arquivo do prontuário.")

        print("\n")
        input("Pressione Enter para retornar ao menu...")
        os.system("cls")
        buscarOn = False

def excluir_prontuario():
    prontuarios = carregar_prontuarios()
    cadastros = carregar_cadastros()
    excluirOn = True

    while excluirOn:
        os.system("cls")
        print("--- Excluir prontuário ---\n")
        rgPaciente = input("RG do paciente (apenas números): ").strip()

        pacienteLocalizado = False
        for i in cadastros:
            if i['rg'] == rgPaciente:
                pacienteLocalizado = True
                break

        if not pacienteLocalizado:
            print("\nPaciente não encontrado!\n")
            while True:
                opcao = input("Deseja tentar novamente? (s/n): ").strip().lower()
                if opcao not in ['s', 'n']:
                    print("\nOpção inválida!\n")
                    time.sleep(0.5)
                    continue
                break
            if opcao == 'n':
                excluirOn = False
                os.system("cls")
                break
            elif opcao == 's':
                os.system("cls")
                continue

        prontuariosPaciente = None
        for p in prontuarios:
            if p['rg'] == rgPaciente:
                prontuariosPaciente = p['idProntuarios']
                prontuarioId = p
                break

        if not prontuariosPaciente or len(prontuariosPaciente) == 0:
            print("\nNenhum prontuário encontrado para este paciente.\n")
            input("Pressione Enter para continuar...")
            os.system("cls")
            break

        while True:
            os.system("cls")
            print("--- Prontuários encontrados ---\n")
            for idx, idp in enumerate(prontuariosPaciente):
                try:
                    dataFormatada = datetime.strptime(idp, "%Y%m%d%H%M%S").strftime("%d/%m/%Y às %H:%M:%S")
                except:
                    dataFormatada = idp
                print(f"{idx + 1}. {dataFormatada}")

            print("\nDigite o número do prontuário que deseja excluir.")
            print("Ou pressione Enter em branco para cancelar.\n")
            escolha = input("Número: ").strip()

            if escolha == "":
                os.system("cls")
                print("\nExclusão cancelada.\n")
                time.sleep(0.5)
                os.system("cls")
                return

            if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(prontuariosPaciente):
                print("\nEscolha inválida!\n")
                time.sleep(0.5)
                continue

            idSelecionado = prontuariosPaciente[int(escolha) - 1]
            break

        os.system("cls")
        print(f"--- Conteúdo do prontuário {escolha} ---\n")
        try:
            with open(f"{idSelecionado}.txt", "r", encoding="utf-8") as f:
                conteudo = f.read()
                print(conteudo)
        except:
            print("Erro ao abrir o arquivo do prontuário.")

        while True:
            print("\n")
            confirmar = input(f"Tem certeza que deseja excluir o prontuário {escolha}? (s/n): ").strip().lower()
            if confirmar not in ['s', 'n']:
                print("\nOpção inválida!\n")
                time.sleep(0.5)
                continue
            break

        if confirmar == 'n':
            os.system("cls")
            print("\nExclusão cancelada.\n")
            time.sleep(0.5)
            os.system("cls")
            return

        os.system("cls")
        try:
            os.remove(f"{idSelecionado}.txt")
            prontuarioId['idProntuarios'].remove(idSelecionado)
            salvar_prontuario(prontuarios)
            print("\nProntuário excluído com sucesso!\n")
        except:
            print("\nErro ao excluir prontuário.\n")

        input("Pressione Enter para continuar...")
        os.system("cls")
        excluirOn = False

#Menu
inicializar_arquivo_cadastros()
inicializar_arquivo_prontuarios()
while menuPrincipal:
    os.system("cls")
    print("--- Prontuário Digital - Hospital Sabará ---\n\n1 - Gerenciar cadastros\n2 - Gerenciar prontuários\n0 - Sair\n")
    opcao = input("Escolha uma opção: ")
    os.system("cls")
    match opcao:
        case "1":
            menuCadastros = True
            while menuCadastros:
                print("--- Gerenciador de cadastros ---\n\n1 - Novo cadastro\n2 - Buscar cadastro\n3 - Listar cadastros\n4 - Editar cadastro\n5 - Excluir cadastro\n0 - Voltar ao menu principal\n")
                opcao = input("Escolha uma opção: ")
                os.system("cls")
                match opcao:
                    case "1":
                        cadastrar_usuario()
                    case "2":
                        buscar_usuario()
                    case "3":
                        listar_usuarios()
                    case "4":
                        editar_usuario()
                    case "5":
                        deletar_usuario()
                    case "0":
                        print("Voltando ao menu principal...")
                        time.sleep(0.5)
                        os.system("cls")
                        menuCadastros = False
                    case _:
                        print("Opção inválida. Tente novamente.")
                        time.sleep(1)
                        os.system("cls")
        case "2":
            menuProntuarios = True
            while menuProntuarios:
                print("--- Gerenciador de prontuários ---\n\n1 - Novo prontuário\n2 - Buscar prontuário\n3 - Excluir prontuário\n0 - Voltar ao menu principal\n")
                opcao = input("Escolha uma opção: ")
                os.system("cls")
                match opcao:
                    case "1":
                        criar_prontuario()
                    case "2":
                        buscar_prontuarios()
                    case "3":
                        excluir_prontuario()
                    case "0":
                        print("Voltando ao menu principal...")
                        time.sleep(0.5)
                        os.system("cls")
                        menuProntuarios = False
                    case _:
                        print("Opção inválida. Tente novamente.")
                        time.sleep(1)
                        os.system("cls")
        case "0":
            print("Saindo...")
            time.sleep(1.5)
            os.system("cls")
            menuPrincipal = False
        case _:
            print("Opção inválida. Tente novamente.")
            time.sleep(1.5)
            os.system("cls")
