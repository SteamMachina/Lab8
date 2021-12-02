def exercice_one(): #Soizic
    chain = open("chain.txt", "r")
    chain_list = []
    for line in chain.readlines():
        line = line.split('\n')
        chain_list.append(line[:-1][0].split(', '))
    chain_list = chain_list[1][0].split(' ')
    D1 = {}
    D2 = {}
    for i in range(len(chain_list)) :
        D1[chain_list[i]] = i
        D2[i] = chain_list[i]
    return D1, D2

  
