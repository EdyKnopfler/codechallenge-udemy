def pares(texto):
    estado = 1
    atual = texto[0] if len(texto) > 0 else ''
    cont1 = cont2 = 0
    resultado = 0
    
    for caractere in texto:
        if estado == 1:
            if caractere != atual:
                atual = caractere
                cont2 += 1
                estado = 2
            else:
                cont1 += 1
        else:
            if caractere != atual or cont2 == cont1:
                if cont1 == cont2:
                    resultado += 1
                atual = caractere
                cont1 = 1
                cont2 = 0
                estado = 1
            else:
                cont2 += 1
        #print(caractere, estado, cont1, cont2)
            
    if cont1 > 0 and cont1 == cont2:
        resultado += 1
        
    #print(cont1, cont2, resultado)
    return resultado

if __name__ == '__main__':
    assert pares('') == 0
    assert pares('D') == 0
    assert pares('EEDDEDEEEDDDEEDD') == 4
    assert pares('EDDDDEEEDE') == 3
    assert pares('EDDDDEEEDED') == 3

