import sys
import os

# função para amortecer a chave de criptografia
def _amortecer_chave(textopuro, chave):
    chave_amortecida = ''
    i = 0
    for char in textopuro:
        if char.isalpha():
            chave_amortecida += chave[i % len(chave)]
            i = i + 1
        else:
            chave_amortecida = chave_amortecida + ''  
    return chave_amortecida

def _descriptografar_criptografar_caracter(caracter_textopuro, caracter_chave, mode='criptografar'):
    if caracter_textopuro.isalpha():
        primeira_letra_alfabeto = 'a'
        if caracter_textopuro.isupper():
            primeira_letra_alfabeto = 'A'
        posicao_anterior_caracter = ord(caracter_textopuro) - ord(primeira_letra_alfabeto)
        posicao_caracter_chave = ord(caracter_chave.lower()) - ord('a')

        if mode == 'criptografar':
            nova_posicao_caracter = (posicao_anterior_caracter + posicao_caracter_chave) % 26
    
        elif mode =='descriptografar':
            nova_posicao_caracter = (posicao_anterior_caracter - posicao_caracter_chave + 26 ) %26
        # pegar o caracter da tabela ASCII    
        return chr(nova_posicao_caracter + ord(primeira_letra_alfabeto))
    return caracter_textopuro

def criptografar(textopuro,chave):
    textocifrado = ''
    chave_amortecida = _amortecer_chave(textopuro, chave)
    for caracter_textopuro, caracter_chave in zip (textopuro, chave_amortecida):
       textocifrado = textocifrado + _descriptografar_criptografar_caracter(caracter_textopuro, caracter_chave)
    return textocifrado 
    
def descriptografar(textocifrado,chave):
    textopuro = ''
    chave_amortecida = _amortecer_chave(textocifrado, chave)
    for caracter_textocifrado, caracter_chave in zip(textocifrado, chave_amortecida):
        textopuro += _descriptografar_criptografar_caracter(caracter_textocifrado, caracter_chave, mode='descriptografar')
    return textopuro


# verificar se foi informado 4 parâmetros no console do terminal
if len(sys.argv) == 4:

    nome_arquivo_criptografia = sys.argv[0]
    arquivo_texto = sys.argv[1]
    chave = sys.argv[2]
    tipo = sys.argv[3]

    # verifica se arquivo de texto tem extensão .txt
    if arquivo_texto[len(arquivo_texto)-4:] != '.txt':
        print('O segundo parâmetro tem que ser um arquivo do tipo texto')

    # verificar se foi passada a chave de criptografia (se ela não é nula)
    elif chave == "":
        print('O terceiro parâmetro deve ser a chave de criptografia não nula')
    
    elif tipo !='criptografar' and tipo !='descriptografar':
        print('O terceiro parametro tem que ser a palavra criptografar ou descriptografar.\nDependendo da ação que desejas.')

    # se tudo foi validado ok. vai executar o script

    else:
        arquivo = open(arquivo_texto)
        textopuro= arquivo.read()
        arquivo.close()

        # informar um texto para criptografar e a chave
        #textopuro = input('Informe um texto para criptografar com a cifra de vegenere: ')
        #chave = input('Informe a chave de criptografia: ')

        if tipo == 'criptografar':        

            textocifrado = criptografar(textopuro,chave)
            texto_descriptogradado = descriptografar(textocifrado,chave)

            arquivo_texto = arquivo_texto[:len(arquivo_texto) - 4] + '.txt' 

            # criar um novo arquivo e salvar nele o texto criptografado
            arquivo_novo = open(arquivo_texto,'w+')
            arquivo_novo.write(textocifrado)
            arquivo_novo.close()

            # imprimindo na tela o texto cifrado que foi salvo no arquivo
            print(f'Texto crifrado: {textocifrado}')
            print(f'Texto Descriptogradado: {texto_descriptogradado}')
        elif tipo == 'descriptografar':
            
            texto_descriptogradado = descriptografar(textopuro,chave)

            arquivo_texto = arquivo_texto[:len(arquivo_texto) - 4] + '.txt' 

            # criar um novo arquivo e salvar nele o texto descriptografado
            arquivo_novo = open(arquivo_texto,'w+')
            arquivo_novo.write(texto_descriptogradado)
            arquivo_novo.close()
          
            print(f'Texto Descriptogradado: {texto_descriptogradado}')       

                

else:   
    print('Você deve informar o nome do arquivo e 4 parâmetros, conforme o comando abaixo')
    print('python <vinegere.py> <arquivo.txt> <chave de criptografia> <criptografar ou descriptografar>')