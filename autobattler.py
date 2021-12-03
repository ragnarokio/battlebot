class dude:
	def __init__(self):
		self.name = 'unloaded'
		self.life = 1
		self.damage = 1
		self.tags = []
	def load(self, id):
		if id == 0:
			self.name = 'Knight'
			self.life = 3
			self.damage = 3
			self.tags = ['human']
		if id == 1:
			self.name = 'Giantslayer'
			self.life = 3
			self.damage = 2
			self.tags = ['human','giantslayer']
		if id == 2:
			self.name = 'Giant Warrior'
			self.life = 6
			self.damage = 2
			self.tags = ['giant']
		if id == 3:
			self.name = 'Battlefield Commander'
			self.life = 1
			self.damage = 1
			self.tags = ['human','bcommand']
		if id == 4:
			self.name = 'Giant Siegemaster'
			self.life = 4
			self.damage = 3
			self.tags = ['giant','trample','siegem']
		if id == 5:
			self.name = 'Aven Medic'
			self.life = 4
			self.damage = 1
			self.tags = ['bird','medic2']
		if id == 6:
			self.name = 'Aven Bandolier'
			self.life = 2
			self.damage = 2
			self.tags = ['bird','shock1']

class player:
	def __init__(self):
		self.team = [dude(),dude(),dude()]
	
player1 = player()
player1.team[0].load(0)
player1.team[1].load(1)
player1.team[2].load(2)

player2 = player()
player2.team[0].load(2)
player2.team[1].load(1)
player2.team[2].load(0)

class game:
	def __init__(self):
		self.player1 = player1
		self.player2 = player2
		self.alog = []
	def battle(self):
		team1 = self.player1.team
		team2 = self.player2.team
		while(len(team1)>0 and len(team2)>0):
			self.attack(team1[0],team2[0])
			self.alog.append('round ends')
		print('game end')
	def attack(self,dude1,dude2):
		self.alog.append(dude2.name+' attacks '+dude1.name+' for '+str(dude2.damage))
		dude1.life -= dude2.damage
		self.alog.append(dude1.name+' attacks '+dude2.name+' for '+str(dude1.damage))
		dude2.life -= dude1.damage
		if dude1.life < 1:
			self.alog.append(dude1.name+' dies')
			del self.player1.team[0]
		if dude2.life < 1:
			self.alog.append(dude2.name+' dies')
			del self.player2.team[0]

newgame = game()
newgame.battle()
print(newgame.alog)
		

