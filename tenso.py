def tenso(texto, lista_palavras):
    
    # poderia fazer o algoritmo de backtracking
    # tenso2.py
    def _permutacoes(lista):
        if len(lista) < 2:
            yield lista
            return
        
        for pos in range(len(lista)):
            sem_este = lista[:pos] + lista[pos+1:]
            for subpermutacao in _permutacoes(sem_este):
                yield [lista[pos]] + subpermutacao
            
    ocorrencias = []
    inicio = 0
    
    for permutacao in _permutacoes(lista_palavras):
        substring = ''.join(permutacao)
        tamanho = len(substring)
        
        while True:
            onde = texto.find(substring, inicio)
            if onde >= 0:
                ocorrencias.append(onde)
                inicio = onde + tamanho
            else:
                break
            
    return ocorrencias
    
if __name__ == '__main__':
    assert tenso(
        "carroratopenaratoratopanocarrocarrorato", ["carro", "pano", "rato", "carro"]) == [21]
    assert tenso(
        "tensotestetestevistatestetenso", ["tenso", "teste"]) == [0, 20]
    assert tenso(
        "psimpsimgatimcoisopsimpsimgatimgatimpsimpsim", ["psim", "psim", "gatim"]) == [0, 18, 31]

