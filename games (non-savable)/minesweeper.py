import random


def jogoCampoMinado(largura = 14, comprimento = 12):
    DIMENS = (largura, comprimento)
    campo, campo_ecra = [], []
    for linha in range( DIMENS[1]):
        campo.append([0] * DIMENS[0])
        campo_ecra.append([' '] * DIMENS[0])
    
    abcz = 'abcdefghijklmnopqrstuvwxyz'
    abc = ''
    for coluna in range( DIMENS[0]):
        abc += abcz[coluna]
    resultado = '?'

    # colocação de minas em 27% do campo
    for mina in range(int(DIMENS[0] * DIMENS[1] * 0.27)):
        colocada = False
        while not colocada:
            pos = {'Y': random.randrange(DIMENS[1]),
                   'X': random.randrange(DIMENS[0])}
            if campo[pos['Y']][pos['X']] == 0:
                campo[pos['Y']][pos['X']] = '*'
                colocada = True


    def mostrarCampo(testing = False):
        print('   ',end='  ')
        if testing:
            linhas = campo
            numlinha = 0
            for n in range(DIMENS[0]):
                if n < 10:
                    spaces = '  '
                else:
                    spaces = ' '
                print(f'{n}',end=spaces)
        else:
            linhas = campo_ecra
            numlinha = 1
            for l in abc:
                print(f'{l.upper()}',end='  ')


        for linha in linhas:
            print()
            if numlinha < 10:
                print(' ',end='')
            print(f'{numlinha}',end='  ')

            for quadrado in linha:
                print(f'[{quadrado}]',end='')

            numlinha += 1
        print()

    
    def adjacentes(y, x):
        return [{'Y': y - 1, 'X': x - 1},
                {'Y': y - 1, 'X': x},
                {'Y': y - 1, 'X': x + 1},
                {'Y': y,     'X': x - 1},
                {'Y': y,     'X': x + 1},
                {'Y': y + 1, 'X': x - 1},
                {'Y': y + 1, 'X': x},
                {'Y': y + 1, 'X': x + 1}]
    
    # verificação de quantidade de minas adjacentes em cada quadrado
    for linha in range(DIMENS[1]):
        for quadrado in range(DIMENS[0]):
            if campo[linha][quadrado] == '*':                
                for adj in adjacentes(linha, quadrado):
                    try:
                        if adj['X'] < 0 or adj['Y'] < 0:
                            raise IndexError
                        if campo[adj['Y']][adj['X']] != '*':
                            campo[adj['Y']][adj['X']] += 1
                    except IndexError:
                        pass
    
    # verificação de espaços vazios (guardados numa lista de dicionários)
    vazios = []
    for linha in range(DIMENS[1]):
        for quadrado in range(DIMENS[0]):
            if campo[linha][quadrado] == 0:
                for vazio in vazios:
                    if (linha, quadrado) in vazio['coords']:
                        jaNumVazio = True
                        break
                else:
                    jaNumVazio = False
                if jaNumVazio: continue

                vazios.append({
                    'coords':   [(linha, quadrado)],
                    'limites':  [],
                    'fechado':  False
                })
                ver_adj = [(linha, quadrado)]
                # itertest = 0
                while vazios[-1]['fechado'] == False and len(ver_adj) > 0:
                    seguinte = ver_adj.pop(0)
                    y = seguinte[0]
                    x = seguinte[1]

                    faltafechar = 8
                    for adj in adjacentes(y, x):
                        try:
                            if ((adj['Y'], adj['X']) in vazios[-1]['coords']
                            or (adj['Y'], adj['X']) in vazios[-1]['limites']
                            or (adj['X'] < 0 or adj['Y'] < 0)):
                                faltafechar -= 1
                                if faltafechar == 0 and len(ver_adj) == 0:
                                    vazios[-1]['fechado'] = True
                                    break
                                raise IndexError
                            
                            if campo[adj['Y']][adj['X']] == 0:
                                ver_adj.append( (adj['Y'], adj['X']))
                                vazios[-1]['coords'].append( ver_adj[-1])
                            else:
                                vazios[-1]['limites'].append( (adj['Y'], adj['X']))
                                faltafechar -= 1
                                if faltafechar == 0 and len(ver_adj) == 0:
                                    vazios[-1]['fechado'] = True
                                    break
                        except IndexError:
                            pass
                    
                    # if itertest%3 == 0:
                    #     mostrarCampo(True)
                    # itertest += 1
                    # print(f'{itertest} iter')
                    # print(f"coords: {vazios[-1]['coords']}", \
                    #       f"limites: {vazios[-1]['limites']}", \
                    #       f'falta ver: {ver_adj}', \
                    #       f"fechado: {vazios[-1]['fechado']}", sep='\n')


    def verInput(inpt):
        invalid = True
        while invalid:
            inps = inpt.split()
            for inp in inps:
                pos = {'bandeira': False}
                try:
                    if inp[-1] == 'm':
                        pos['bandeira'] = True
                        inp = inp[:-1]
                    if int(inp[1:]) >= 1 and int(inp[1:]) <= DIMENS[1]:
                        pos['Y'] = int(inp[1:]) - 1
                    else:
                        raise ValueError
                    
                    if inp[0] not in abc:
                        print('Escreva as coordenadas com uma das letras primeiro.',end=' ')
                    pos['X'] = abc.index(inp[0])
                    invalid = False            
        
                    yield pos

                except ValueError:
                    ex = [] # exemplos random para mostrar ao utilizador
                    for exemplos in range(3):
                        ex.append( random.choice(abc.upper()) + str(random.randint(1, DIMENS[1])))
                        if pos['bandeira']:
                            ex[-1] += 'm'

                    print(f'Tente novamente. (ex: {ex[0]}; {ex[1]}; {ex[2]})')
                    inpt = input('Coordenadas: ').lower()
                    invalid = True
                    break


    def revelar(pos):
        nonlocal campo_ecra
        if pos['bandeira']:
            campo_ecra[pos['Y']][pos['X']] = 'x'
            return
        
        y_rev = pos['Y']
        x_rev = pos['X']
        campo_ecra[y_rev][x_rev] = campo[y_rev][x_rev]

        match campo[y_rev][x_rev]:
            case 0:
                for vazio in vazios:
                    if (y_rev, x_rev) in vazio['coords']:
                        quadradosRevelados = vazio['coords'] + vazio['limites']
                        for qua in quadradosRevelados:
                            campo_ecra[qua[0]][qua[1]] = campo[qua[0]][qua[1]]
                        break
            case '*':
                nonlocal resultado
                campo_ecra = campo
                resultado = 'Perdeu.'


    def ganhou():
        nonlocal resultado
        ganhou = True
        for linha in range(DIMENS[1]):
            for qua in range(DIMENS[0]):
                if not isinstance(campo_ecra[linha][qua], int):
                    if campo[linha][qua] != '*':
                        ganhou = False
                        break
            if not ganhou:
                break
        else:
            resultado = 'Ganhou.'
        return ganhou

    ## Para testar (ganhar automaticamente):
    # poss = []
    # for l in range(DIMENS[1]):
    #     for c in range(DIMENS[0]):
    #         poss.append({'Y':l, 'X':c, 'bandeira': False})
    while campo_ecra != campo and not ganhou():
        mostrarCampo()
        # while len(poss) > 0:
        #     pos = poss.pop(random.randrange(len(poss)))
        #     if campo[pos['Y']][pos['X']] != '*':
        #         revelar(pos)
        #         # break # (opcional: CLI mais cheio)
        # 
        ## (Comentar as duas linhas seguintes para testar as comentadas em cima)
        for pos in verInput( input('\nRevelar coordenadas (adiciona "m" no final para marcar se acreditas que contêm uma mina): ').lower()):
            revelar(pos)
        
    mostrarCampo()
    print(resultado)


if __name__ == "__main__":
    jogoCampoMinado(8,6)
