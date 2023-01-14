from bisect import bisect_left as busca_binaria


def mediana(A, B):
    if len(A) == 0 and len(B) == 0:
        raise Exception('Ô fio, manda lista com alguma coisa né mêo')

    #print(f'\nA: {A}; B: {B}')
    contagem_final = len(A) + len(B)
    usar_dois_valores = contagem_final % 2 == 0
    posicao_mediana = (
        contagem_final // 2 - 1
        if usar_dois_valores
        else contagem_final // 2
    )
    resultado = None
    ponta_maxima, outro = (A, B) if len(B) == 0 or len(A) > 0 and A[-1] > B[-1] else (B, A)
    fim_maxima = len(ponta_maxima)
    fim_outro = len(outro)
    posicao_encaixe = ultimo_indice = -1

    while resultado is None:
        if fim_outro == 0:
            usar_posicao = posicao_encaixe + posicao_mediana - ultimo_indice
            resultado = ponta_maxima[usar_posicao]
            if usar_dois_valores:
                resultado = (resultado + ponta_maxima[usar_posicao + 1]) / 2.0
        else:
            posicao_outro = fim_outro - 1
            valor_outro = outro[posicao_outro]
            posicao_encaixe = busca_binaria(ponta_maxima, valor_outro, lo=0, hi=fim_maxima)
            quantidade_anterior = posicao_encaixe + posicao_outro
            #print('   Encaixe na ponta máxima:', posicao_encaixe, '/ Qtd. anterior:', quantidade_anterior)
            ultimo_indice = quantidade_anterior + 1
            penultimo_valor = valor_outro
            ultimo_valor = ponta_maxima[posicao_encaixe]

            if posicao_mediana == quantidade_anterior:
                resultado = penultimo_valor
                if usar_dois_valores:
                    resultado = (resultado + ultimo_valor) / 2.0
            elif posicao_mediana == quantidade_anterior + 1:
                resultado = ultimo_valor
                if usar_dois_valores:
                    resultado = (resultado + ponta_maxima[posicao_encaixe + 1]) / 2.0
            else:
                if posicao_outro == 0 or \
                        posicao_encaixe > 0 and ponta_maxima[posicao_encaixe - 1] > outro[posicao_outro - 1]:
                    #print('   mantendo')
                    fim_maxima = posicao_encaixe
                    fim_outro = posicao_outro
                else:
                    #print('   trocando')
                    fim_maxima = posicao_outro
                    fim_outro = posicao_encaixe
                    ponta_maxima, outro = outro, ponta_maxima

    return resultado


if __name__ == "__main__":
    assert mediana([], [1]) == 1
    assert mediana([2], []) == 2
    assert mediana([], [1, 2]) == 1.5
    assert mediana([2, 4], []) == 3
    assert mediana([], [2, 3, 4]) == 3
    assert mediana([2, 4, 6], []) == 4
    assert mediana([1, 3, 7, 9], [1, 5, 9, 20]) == 6
    assert mediana([1, 3, 7, 9], [1, 9, 20]) == 7
    assert mediana([1, 1, 1, 2], [3, 4, 8, 9, 10, 10]) == 3.5
    assert mediana([1, 2, 3, 3, 5], [8, 11, 13]) == 4
    assert mediana([0, 0], [0, 0]) == 0

