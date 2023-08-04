import funcoes
def jogar():
    funcoes.titulo("Bem vindo ao jogo da Forca!")
    print('Digite um tema: frutas, objetos, comidas ')
    tema = funcoes.is_theme('tema: ')
    erros = dicas = 0
    enforcou = False
    acertou = False
    palavra_secreta = funcoes.carrega_palavra_secreta(tema)
    letra_certa = funcoes.inicializa_letras_acertadas(palavra_secreta)

    print(f'Tente advinhar a palavra:  {letra_certa}')

    while True:
        chute = str(input('Chute uma letra ou palavra: ')).lower().strip()

        if chute in palavra_secreta:
            funcoes.chute_certo(chute, palavra_secreta, letra_certa)

        elif chute not in palavra_secreta:
            erros += 1
            dicas += 1
            funcoes.chute_errado(chute, dicas, palavra_secreta, tema)
            funcoes.desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letra_certa
        print(letra_certa)

        if chute == palavra_secreta or acertou:
            print(f'ACERTOU ! a palavra era {palavra_secreta}')
            funcoes.imprime_mensagem_vencedor()
            break
        elif enforcou:
            funcoes.imprime_mensagem_perdedor(palavra_secreta)
            break
        else:
            continue
    print("---- Fim do jogo ----")


if __name__ == "__main__":
    jogar()