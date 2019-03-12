from random import seed, randrange

n1 = ["Felicia", "Catulo", "Osmund", "Artmio", "Senizio"]
n2 = ["Cartuxo", "Olambro", "Romulo", "Ambulo", "Atomon"]
n3 = ["Sereno", "Soterno", "Moncoes", "Oscaran", "Topovi"]
n4 = ["Lasmia", "Mantega", "Casas", "Lorentao", "Melkioz"]
nn = 5

def GeraRegistro(pp):
    global n1, n2, n3, n4, nn
    nome = n1[randrange(nn)] + ' ' + n2[randrange(nn)] + ' ' + n3[randrange(nn)] + ' ' + n4[randrange(nn)]
    datan = '{dia:02}'.format(dia = randrange(28) + 1) + '{mes:02}'.format(mes = randrange(12) + 1) + '{ano:04}'.format(ano = randrange(17) + 2000)
    ident = '{a:08}'.format(a = randrange(100000000))
    if pp == '':
        registro = [' '] * 56
        registro[:len(nome)] = nome
        registro[40:48] = datan
        registro[48:56] = ident
        return ''.join(registro) 
    elif randrange(2) == 0:
        registro = list(pp)
        registro[40:48] = datan
        registro[48:56] = ident
        return ''.join(registro)
    else:
        registro = list(pp)
        registro[48:56] = ident
        return ''.join(registro)
 
def GeraArquivo(nomearq, nreg):
    seed()
    metade = nreg // 2
    tab = ['' for k in range(nreg // 10)] 
    arq = open(nomearq, "w")
    for k in range(metade):
        reg = GeraRegistro('')
        arq.write(reg + '\n')
        if k % 5 == 0:
            tab[k // 5] = reg
    for k in range(len(tab)):
        for j in range(5):
            reg = GeraRegistro(tab[k])
            arq.write(reg + '\n')
    arq.close()

GeraArquivo('teste1.txt', 50)
GeraArquivo('teste2.txt', 100)
GeraArquivo('teste3.txt', 500)
GeraArquivo('teste4.txt', 1000)
GeraArquivo('teste5.txt', 10000)
GeraArquivo('teste6.txt', 50000)
GeraArquivo('teste7.txt', 100000)
GeraArquivo('teste8.txt', 500000)
GeraArquivo('teste9.txt', 1000000)
GeraArquivo('teste10.txt', 10000000)
 
