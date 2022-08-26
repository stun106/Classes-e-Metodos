from syscombat import Syscombat
nick = input('informe o nome do seu Heroi: ')
rpg = Syscombat(nick)    
print(f'Nickname: {rpg.nickname}\nSua conta foi logada com sucesso...' )
print('\n')
print('Seleção de Personagem:')

print('[1] - Blade Knigth: Guerreiro\n[2] - Soul Master: Mago\n[3] - Muse Elf: Arqueira\n[4] - Magic Gladiator: Magico e Gladiador\n')
rpg.BkStatus()
rpg.SmStatus()
rpg.MeStatus()
rpg.MgStatus()
choice = int(input('escolha seu Heroi, seguindo as instruções a cima: '))
print(rpg.selectHero(choice))

  

   
