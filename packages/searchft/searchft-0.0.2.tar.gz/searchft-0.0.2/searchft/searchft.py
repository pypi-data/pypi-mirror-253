from googlesearch import search
import webbrowser

class Searchft:
    '''
    Classe onde ficam os métodos da biblioteca

    Methods
    -------
        buscar(pesquisar, size):
            efetua pelo item.
        visitarLink(link):
            abre o link no navegador da máquina.
        
    '''
    def buscar(pesquisar: str, size = 10):
        '''
        Recebe o conteúdo da pesquisa e a quantidade de links que devem ser retornados.

        Parameters
        ----------
            pesquisar: str
                conteúdo da pesquisa.
            size: int
                quantidade de links a serem retornados.
        
        Returns
        -------
            resultado: list
                retorna uma lista com os links encontrados, caso a quantidade de links enontrados seja menor que informada pelo usuário, retorna somente a quantidade encontrada. 
        '''
        resultado = []
        for url in search(pesquisar, size):
            # print(url)
            resultado.append(url)
        
        if len(resultado) == 0:
            resultado.append(None)
        
        return resultado
    
    def visitarLink(link: str):
        '''
        Abre o link recebido, no navegador.

        Parameters
        ----------
            link: str
                link que o usuário deseja abrir.

        Returns
        -------
            None 
        '''
        webbrowser.open(link)
    
