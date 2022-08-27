MODE_ENCRYPT = 1
MODE_DECRYPT = 0

#modo =  ('Escolha E para encriptar ou D para decriptar o texto: ')

key = int(input('Digite o valor da chave até 76: '))
while key > 76 or key < 0:  
    print(" ")
    key = input("chave inválida, tente novamente")
    

frase = input('Digite a frase: ')

def caesar(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''
    for caractere  in data:
        index = alphabet.find(caractere)
        if index == -1:
            new_data += caractere 
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data

ciphered = caesar(frase, key, MODE_ENCRYPT)
print('Encriptada:', ciphered)
plain = caesar(ciphered, key, MODE_DECRYPT)
print('Decriptada:', plain) 