MODE_ENCRYPT = 1
MODE_DECRYPT = 0

chave = int(input('Digite o valor da chave')) #recebe a chave
palavra = str(input('Informe a palavra')) #recebe a palavra
#escolha = str(input('Digite E para encriptar ou D para descriptar')) recebe a opção desejada 

def cesar(data, chave, mode):
    alfabeto = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ' #alfabeto definido com letras maiúsculas e minusculas acentuadas
    new_data = ''
    for c in data:
        index = alfabeto.find(c) #c variavel definida para percorrer o alfabeto e selecionar a letra
        if index == -1:
            new_data += c
        else:
            new_index = index + chave if mode == MODE_ENCRYPT else index - chave #nova letra recebe a letra atual + a chave se o modo for o de encriptografar se não ira descriptografar utilizando a subtração da nova letra com a chave selecionada.
            new_index = new_index % len(alfabeto)
            new_data +=  alfabeto[new_index:new_index + 1]
    return new_data

print('  Original:', palavra)
cifrada = cesar(palavra, chave, MODE_ENCRYPT) #chamado metodo passando a palavra informada a chave e o modo a ser utilizado de encriptografar

print('Encriptada:', cifrada)
plain = cesar(cifrada, chave, MODE_DECRYPT) #chamado metodo passando a palavra informada a chave e o modo a ser utilizado de encriptografar

print('Descriptada:', plain) #chamado metodo passando a palavra informada a chave e o modo a ser utilizado de descriptografar