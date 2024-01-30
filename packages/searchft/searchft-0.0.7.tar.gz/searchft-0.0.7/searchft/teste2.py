from googlesearch import search

def buscar(item, size = 10):
    lista = []
    for url in search(item, size):
        print(url)
        lista.append(url)
    
    return lista

resposta = buscar('my eyes')

print('------------------------------')
print(resposta)
