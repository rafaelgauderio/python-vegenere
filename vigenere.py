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

# informar um texto para criptografar e a chave
textopuro = input('Informe um texto para criptografar com a cifra de vegenere: ')
chave = input('Informe a chave de criptografia: ')

textocifrado = criptografar(textopuro,chave)
texto_descriptogradado = descriptografar(textocifrado,chave) 

# imprimir a cifra criptografada e depois descriptografada
print(f'Texto crifrado: {textocifrado}')
print(f'Texto Descriptogradado: {texto_descriptogradado}')

    