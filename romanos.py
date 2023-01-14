VALORES = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def para_arabico(romano):
    pos = 0
    total = 0
    
    while pos < len(romano):
        simbolo = romano[pos]
        valor = VALORES[simbolo]
        
        if pos + 1 < len(romano):
            proximo = romano[pos + 1]
            valor_proximo = VALORES[proximo]
            
            if valor < valor_proximo:
                valor = valor_proximo - valor
                pos += 1
        
        total += valor
        pos += 1

    return total
    

if __name__ == '__main__':
    print(para_arabico('MCMXIX'))
    print(para_arabico('XVIII'))
    print(para_arabico('XIX'))
    print(para_arabico('XLIV'))
    print(para_arabico('LXXXIX'))
    print(para_arabico('MCMXLV'))

