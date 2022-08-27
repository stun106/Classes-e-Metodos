from time import sleep
from syscombat import Syscombat
nick = input('informe o nome do seu Heroi: ')
rpg = Syscombat(nick)    
print(f'Nickname: {rpg.nickname}\nSua conta foi logada com sucesso...' )
print('\n')
print('Seleção de Personagem:')

print('[1] - Blade Knigth: Guerreiro\n[2] - Soul Master: Mago\n[3] - Muse Elf: Arqueira\n[4] - Magic Gladiator: Magico e Gladiador\n')

choice = int(input('escolha seu Heroi, seguindo as instruções a cima: '))
# rpg.HeroSM = choice
# rpg.HeroMe = choice
# rpg.HeroMG = choice
if choice == 1:
    rpg.BkStatus(choice)
    print(rpg.selectBK)
elif choice == 2:
    rpg.SmStatus(choice)
    print(rpg.selectSM)
elif choice == 3:
    rpg.MeStatus(choice)
    print(rpg.selectME)
else:
    rpg.MgStatus(choice)
    print(rpg.selectMG)
print('\n')
sleep(1.0)
print('-'*50)
print('Lore: MuOnline, um jogo 3D online produzido pela Webzen é um MMORPG, o primeiro de seu tipo, desenvolvido na Coréia. MU é um jogo altamente envolvido em fantasia, baseado no continente legendário do MU. Você pode escolher cinco classes diferentes: o guerreiro (Dark Knight), a elfa (Fairy Elf), o mago (Dark Wizard), o gladiador mágico (Magic Gladiator) e o senhor da escuridão (Dark Lord), e transforma-se em um aventureiro audaz na missão para conservar a terra do MU. Os gráficos feitos dentro do ambiente 3D são gloriosos, e envolvem o jogador assiduamente com a tecnologia do motor 3D GL, desenvolvido pela Webzen, fazem possível do impossível. O que existe atrás das lendas e mistérios do MU? Deixe a viagem começar...')
print('-'*50)
sleep(4.0)
print('\n')
print('seu personagem desperta numa cidade chamada Lorencia..')
print('\n')
print('ao acordar se depara com um enorme esqueleto vindo em sua direção, oque você faz?')
print('\n')
question = int(input('Press [1] para "Atacar" ou [2] para Fugir: '))
rpg.health = question
rpg.damage = question
rpg.defesa = question
while True:
    if rpg.health <= 0:
        print(rpg.Died())
    elif rpg.HPmonster <= 0:
        print(rpg.Killmonster())
    rolldice = str(input('press "Y" para jogar o dado: '))
    rpg.rolldice = rolldice
    print('Jogando o Dado ...')
    sleep(1.5)
    print(f'Dado: {rpg.rolldice}')
    sleep(0.5)
    if rpg.rolldice <= 4 and rpg.HPmonster > 0: 
        print(rpg.Ataque())
        pass    
    else:
        if rpg.rolldice > 4 and rpg.health > 0:
            print(rpg.ataqueMob())
        continue


        

    
    
        


  

   
