import time, random, json

savename = 'saves/save_jogoGloria.json'

def jogoGloria(resume = None):
    class Jogador:
        def __init__(self, nome):
            self.id = nome
            self.casa = 1
            self.espera = 0
            self.ganhador = False

        def avanca(self, casas = 1):
            '''
            O jogador avança e verifica-se se acaba numa casa especial.
            '''
            self.casa += casas
            if self.casa > 50:
                self.casa = 100 - self.casa
            if self.casa in casas_especiais:
                tabuleiro()
                print('Casa especial!')
                accao = casas_especiais[self.casa]
                print(accao)

                match accao[0]:
                    case 'A':
                        quanto_avanca = int(accao[7])
                        self.avanca(quanto_avanca)
                    case 'R':
                        if self.casa == 5:
                            self.casa = 1
                        else:
                            quanto_recua = int(accao[6])
                            self.avanca(-quanto_recua)
                    case 'F':
                        self.espera = int(accao[5])
                    case 'J':
                        nova_casa = 50
                        casa_se_recua = 1
                        for j in jogadores:
                            if j == self:
                                continue
                            if (j.casa - self.casa)**2 < (self.casa - nova_casa)**2:
                                if (j.casa - self.casa) > 0:
                                    nova_casa = j.casa
                                else:
                                    if j.casa > casa_se_recua:
                                        casa_se_recua = j.casa
                        if nova_casa == 50:
                            self.casa = casa_se_recua
                        else:
                            self.casa = nova_casa
                    case 'C':
                        self.ganhador = True

    def tabuleiro():
        def mostrarCasa(casa, sentido):
            jogadores_na_casa = []
            for j in jogadores:
                if j.casa == percurso[casa]:
                    jogadores_na_casa.append(j.id)
            if len(jogadores_na_casa) == 0:
                print(f'{sentido} {[percurso[casa]]}', end=' ')
            else:
                print(f'{sentido} {jogadores_na_casa}', end=' ')

        print()
        time.sleep(2)
        for casas in range(5):
            if casas % 2 == 0:
                for casa in range(casas * 10, (casas * 10) + 10):
                    mostrarCasa(casa, '>')
            else:
                for casa in range((casas * 10) + 9, (casas * 10) - 1, -1):
                    mostrarCasa(casa, '<')
            print()


    try:
        novojogo = False
        jogadores = []
        if resume is not None: # Saved game will be resumed
            data = resume

            percurso = data['percurso']
            for jogador in data['jogadores']:
                jogadores.append(Jogador(jogador['id']))
                jogadores[-1].casa = jogador['casa']
                jogadores[-1].espera = jogador['espera']
            vezde = data['vez de']
        
        else:
            novojogo = True

            percurso = [i + 1 for i in range(50)]
            pessoas = 0
            while pessoas <= 1:
                pessoas = int(input('Número de jogadores (2-6): '))
            nomes = set()
            for jogador in range(pessoas):
                if jogador == 6:
                    break
                while True:
                    nome = input(f'Nome do jogador {jogador + 1}: ')
                    nomes.add(nome)
                    if len(nomes) < (jogador + 1):
                        print('Já há um jogador com esse nome, escolha outro.')
                    else:
                        jogadores.append(Jogador(nome))
                        break

        casas_especiais = {
            1:'Partida',
            3:'Avança 3 casas',
            5:'Recua até a partida',
            8:'Avança 3 casas',
            16:'Fica 1 vez sem jogar',
            22:'Avança 2 casas',
            27:'Junta-te ao seguinte jogador',
            31:'Avança 1 casa',
            35:'Fica 2 vezes sem jogar',
            38:'Avança 4 casas',
            44:'Recua 1 casa',
            49:'Recua 3 casas',
            50:'CHEGADA'
        }
                        
        acabou = False
        while not acabou:
            for jog in jogadores:
                if not novojogo:
                    if jog.id == vezde:
                        novojogo = True
                    else:
                        continue

                elif jog.espera > 0:
                    jog.espera -= 1
                    continue
                
                else:
                    vezde = jog.id

                tabuleiro()

                if jog.casa > 42:
                    fimstr = f', se estes somam exatamente {50 - jog.casa} ganha!'
                else:
                    fimstr = '.'
                input(f'Joga {jog.id}. "Enter" para lançar os dados{fimstr}')
                dados = [random.randint(1,6), random.randint(1,6)]
                
                print('Dados:', dados)
                print(f'{jog.id} avança {sum(dados)} casas!')
                jog.avanca(sum(dados))

                if jog.ganhador:
                    acabou = jog.id
                    break

        print(f'\nGanhou {acabou}!')

        with open(savename, "w") as json_save:
            json.dump({}, json_save)

    except KeyboardInterrupt:
        try:
            save_dict = {
                "jogadores": [],
                "percurso": percurso,
                "vez de": vezde       
            }
            for jogador in jogadores:
                save_dict["jogadores"].append({
                    "id": jogador.id,
                    "casa": jogador.casa,
                    "espera": jogador.espera
                })
            with open(savename, "w") as json_save:
                json.dump(save_dict, json_save)
        except UnboundLocalError:
            pass


if __name__ == "__main__":
    jogoGloria()
