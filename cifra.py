ENCRYPT = 1
DECRYPT = 0


key = int(input('Digite o valor da chave até 76: '))

frase = input('Digite a frase: ')

alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'

def caesar(data, key, mode):
    new_data = ''
    for caractere  in data:
        index = alphabet.find(caractere)
        if index == -1:
            new_data += caractere 
        else:
            new_index = index + key if mode == ENCRYPT else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data

ciphered = caesar(frase, key, ENCRYPT)
print('Encriptada:', ciphered)
plain = caesar(ciphered, key, DECRYPT)
print('Decriptada:', plain) 