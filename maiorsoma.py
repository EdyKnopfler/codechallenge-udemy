def calc(v,n):
    
    # 5 elementos
    #  0  1  2  3  4
    # -1  0  1  2  3
    # -2 -1  0  1  2
    # -3 -2 -1  0  1
    # -4 -3 -2 -1  0
    # -5 -4 -3 -2 -1
    
    soma_max = float('-inf')
    
    for i in range(n + 1):
        soma = 0
        pos = -i
        for j in range(n):
            soma += v[pos]
            pos += 1
        if soma > soma_max:
            soma_max = soma
    
    return soma_max


if __name__=="__main__":
    assert calc([8,7,8,9,1,2,1,4],4) == 32
    assert calc([5,0,-1,3,-2,5,7,9],4) == 26
    assert calc([7,1,3,-1,3,0,7,1],5) == 19
    assert calc([5,0,-1,3,8,5,7,9],4) == 29     
