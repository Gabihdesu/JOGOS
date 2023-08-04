import random

def titulo(text):
    print("*" * 50)
    print(f'{text:^50}')
    print("*" * 50)


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') ##r = ler t= arquivo de texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') ## w= write t= text + = cria um arquivo de texto
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo. Contate o adm.\033[31m')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def dicas_todas(thema, palavra, dicas):
    dicas_dict = {
        'frutas': {
            'banana': ['Os macacos adoram!', 'É amarela.'],
            'maca': ['Existe uma marca com esse nome', 'Envenenou uma princesa'],
            'uva': ['Fazem uma ótima bebida com essa fruta.', 'Pode ser roxa ou verde'],
            'lixia': ['Só tem no Natal', 'Por fora é vermelha e por dentro é branca'],
            'laranja': ['O Brasil exporta em grandes quantidades', 'É cítrica'],
            'limao': ['Tem gente que ama torta de...', 'É azeda'],
            'melancia': ['Tem uma personagem de desenho que ama.', 'É rica em água.'],
            'caqui': ['É vermelha.', 'Pode ser adstringente.'],
            'abacate': ['Faz bem para o colesterol.', 'É verde'],
            'mamao': ['Solta o intestino.', 'Tem várias sementes redondas'],
        },

        'objetos': {
            'caneca': ['Usa para tomar coisas quentes', 'Pode ser temática'],
            'livro': ['Contém histórias', 'Não julgue pela capa'],
            'relogio': ['Íntimo das horas', 'Pode ser digital'],
            'bola': ['É redondo', 'Essencial no futebol'],
            'oculos': ['Tem duas pernas', 'Quem tem miopia precisa'],
            'mochila': ['Tem costura', 'Todo estudante tem'],
            'caderno': ['Geralmente tem pauta', 'É retangular'],
            'lapis': ['Aparece no Titanic', 'Geralmente feito com madeira'],
            'teclado': ['Melhor amigo do progrmador', 'Tem letras'],
            'garrafa': ['Tem formato cilídrico', 'Usado para beber']
        },

        'comidas': {
            'pizza': ['É famosa nos EUA', 'Tem muito queijo'],
            'macarrao': ['Italiano', 'É uma massa'],
            'arroz': ['Os japoneses e os brasileiros comem muito', 'É branco'],
            'feijao': ['É rico é proteinas', 'É o elemento principal de um prato típico do Brasil'],
            'hamburguer': ['É o queridinhos dos fest-food', 'É uma combinação de elementos'],
            'sushi': ['Prato típico do Japão', 'Sempre tem alga'],
            'salada': ['Prato light', 'Tem gente que enche de tempero'],
            'chocolate': ['Difícil alguém não gostar', 'Aliado da TPM'],
            'sorvete': ['É servido gelado', 'Originalmente era feito com fruta'],
            'batata': ['Alimento muito versátil', 'Geralmente servido como acompanhamento']
        }
    }

    if thema in dicas_dict and palavra in dicas_dict[thema]:
        dicas_para_palavra = dicas_dict[thema][palavra]
        if dicas == 1:
            print(dicas_para_palavra[0])
        elif dicas == 2:
            print(dicas_para_palavra[1])


def carrega_palavra_secreta(theme, primeira_linha_valida = 0):
    arquivo = open(f'{theme}.txt', 'r')
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()

    numero = random.randint(primeira_linha_valida, len(palavras))
    palavra_secreta = palavras[numero]
    palavras.clear()
    return palavra_secreta



def inicializa_letras_acertadas(text):
    return ["_" for letra in text]


def chute_certo(chute, palavra, letra_certa):
    for i, letra in enumerate(palavra):
        if chute == letra:
            letra_certa[i] = letra #o _ vai ser substituido pela letra



def is_theme(tema):
    valido = False
    list = ['frutas', 'objetos', 'comidas' ]
    while not valido:
        theme = str(input(tema)).strip().lower()
        if theme not in list:
            print('\033[0;31mERRO ! Escolha um dos temas acima.\033[m')
        else:
            valido = True
            return theme


def chute_errado(chute, dicas, palavra, tema):
    print(f'Não tem letra {chute} na palavra.')

    if dicas <= 2:
        print('Receber dica ?')
        resp = str(input('S ou N ? ')).strip().upper()[0]
        if resp not in 'SsNn':
            print('Valor digitado inválido !')
            resp = str(input('S ou N ? ')).strip().upper()[0]
        if resp in 'Ss':
            dicas_todas(tema, palavra, dicas)
    else:
        print('fim das dicas.')



def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()