try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                'src'
            )
        )
    )
except:
    raise
from random import randint

from backup import Backup
from pessoa import InimigoFactory, Jogador
from pokemon import PokemonFactory

"""
Módulo do game, será aqui onde você vai jogar o PokeTerminal.
"""


def game(jogador: Jogador) -> None:
    """
    Função responsável pelo funcionamento do jogo.
    """
    print(f'É um prazer vê-lo aqui {jogador.nome} :)')
    while True:
        print('-'*40)
        print('1 - Realizar save (sobreescreve o anterior)')
        print('2 - Batalhar contra um inimigo')
        print('3 - Capturar um pokemon')
        print('4 - Fechar o jogo')
        escolha = input()

        if escolha == '1':
            Backup.realizar_save(jogador)  # Realiza o save do jogo
            print('Save realizado com sucesso, agora na próxima vez que você quiser jogar já estará funcionando :)')
        elif escolha == '2':
            # Apresenta os pokemons disponíveis para a luta do jogador
            jogador.apresentar_pokemons()
            pokemon_escolhido = int(
                input('Escolha o número do pokemon que você quer usar na batalha: '))
            inimigo = InimigoFactory.get_inimigo()  # Gera um inimigo

            # Escolhe aleatoriamente um pokemon inimigo
            pokemon_inimigo = randint(0, len(inimigo.lista_pokemons) - 1)

            # Caso o id do pokemon passado pelo jogador não exista
            if not jogador.batalhar(pokemon_escolhido, inimigo, pokemon_inimigo):
                print('Não foi possivel começar a luta, escolha um pokemon válido.')
                continue

        elif escolha == '3':
            pokemon_achado = PokemonFactory.get_pokemon()  # Gera um pokemon aleatório

            print('Você encontrou:')

            pokemon_achado.apresentar_pokemon()
            escolher = input('Deseja captura-lo? S/N ')

            if escolher == 'S':
                jogador.capturar_pokemon(pokemon_achado)
                print('Você capturou ele com sucesso!!!')
        elif escolha == '4':
            # Encerra o game
            print('Obrigado por jogar!!')
            break


def inicio_game(jogador: Jogador) -> None:
    """
    Função responsável pela escolha do primeiro pokemon do jogador.
    """
    print(
        f'Bem vindo ao nosso mundo {jogador.nome}, que tal escolher o seu pokemon inicial? '
    )
    while True:

        print('1 - Magicarpa, 2 - Pikachu, 3 - Onix, 4 - Charmander')
        escolha = input('Escolha o seu pokemon inicial: ')

        if escolha == '1':
            # Gera uma magicarpa com nível aleatório
            jogador.capturar_pokemon(PokemonFactory.get_pokemon('magicarpa'))
            print(
                'Magicarpa escolhida com sucesso! Ela pode parecer fraca, mas só pra quem é cego rsrs')
            break
        elif escolha == '2':
            # Gera um pikachu com nível aleatório
            jogador.capturar_pokemon(PokemonFactory.get_pokemon('pikachu'))
            print(
                'Pikachu escolhido com sucesso! hmmm você quer seguir a mesma jornada do anime?')
            break
        elif escolha == '3':
            # Gera um onix com nível aleatório
            jogador.capturar_pokemon(PokemonFactory.get_pokemon('onix'))
            print(
                'Onix escolhido com sucesso! Tenho que admitir, foi dificil trazer ele pra cá.')
            break
        elif escolha == '4':
            # Gera um charmander com nível aleatório
            jogador.capturar_pokemon(PokemonFactory.get_pokemon('charmander'))
            print('Charmander escolhido com sucesso! Uma escolha padrão.')
            break


tem_backup = input(
    'Antes de começarmos, você quer importar algum backup? S/N ')
if tem_backup == 'S':
    try:
        # Tenta carregar o save, caso o save não exista ou o jogador não tenha um
        # pokemon, ele terá que criar um novo jogo.
        player = Backup.carregar_save()
        if not player.lista_pokemons:
            print(
                'Você não tem nenhum pokemon, você precisa escolhar o seu inicial. Para começarmos essa aventura divertida')

            nome = input('Qual é o nome do seu personagem? ')
            player = Jogador(nome)  # Cria um jogador
            # Chama a função de escolha do primeiro pokemon
            inicio_game(player)
            game(player)  # Inicia o jogo
            exit()

        game(player)  # Caso ele tenha save, iniciará o game com o jogador do save
        exit()
    except Exception as e:
        # Caso tente usar um save que não existe, obrigará a criar um novo jogo.
        print('Pelo que parece você não tem nenhum backup, quando você realizar o primeiro save, será criado.')

nome = input('Qual vai ser o nome do seu personagem? ')
player = Jogador(nome)  # Cria um jogador
inicio_game(player)  # Chama a função de escolha do primeiro pokemon
game(player)  # Inicia o jogo
