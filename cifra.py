




mode = int(input('Digite o 1 para ENCRYPT ou 0 para DECRYPT: ')) #recebe o modo

key = int(input('Digite o valor da chave até 76: '))  #recebe a chave

frase = input('Digite a frase: ')  #recebe a frase

alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'  #alfabeto definido com letras maiúsculas e minusculas acentuadas

def caesar(data, key, mode):
    new_data = ''
    for caractere  in data:
        index = alphabet.find(caractere)  #caractere variavel definida para percorrer o alfabeto e selecionar a letra
        if index == -1:
            new_data += caractere 
        else:
            new_index = index + key if mode == 1 else index - key #nova letra recebe a letra atual + a chave se o modo for o de encriptografar se não ira descriptografar utilizando a subtração da nova letra com a chave selecionada.
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data
    
if mode == 1:
    e = caesar(frase, key, 1)
    print('Encriptada:', e)
if mode == 0:
    d = caesar(frase, key, 0)
    print('Decriptada:', d)