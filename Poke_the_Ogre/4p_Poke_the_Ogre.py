import pygame, random
from random import randint

WIDTH = 1200
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)
BROWN = (50,20,30)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Poke the Ogre")
clock = pygame.time.Clock()

def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_hp_bar2(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BROWN, fill)
	pygame.draw.rect(surface, BROWN, border, 2)

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def distance(a,b):
	#pitagoras distancia entre a y b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	return (dx**2 + dy**2)**(1/2)

def direction(a,b):
	#vector unitario desde a a b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	radio = (dx**2 + dy**2)**(1/2)
	return dx/radio, dy/radio

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/ursa.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.hp = 1000
		self.counter1 = True
		self.counter2 = True
		self.damage = 0

class Player1(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 500
		self.rect.y = 133

	def update(self):
		time = pygame.time.get_ticks()
		self.hp += 0.04
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 1000:
			self.hp = 1000
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speed_x = -3
		if keystate[pygame.K_d]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_w]:
			self.speed_y = -3
		if keystate[pygame.K_s]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550
		if not self.counter2:
			if (time//100) % 50 == 0:
				self.counter2 = True

class Player2(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 900
		self.rect.y = 133
				
	def update(self):
		time = pygame.time.get_ticks()
		self.hp += 0.04
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 1000:
			self.hp = 1000
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -3
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_UP]:
			self.speed_y = -3
		if keystate[pygame.K_DOWN]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550
		if not self.counter2:
			if (time//100) % 50 == 0:
				self.counter2 = True

class Player3(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 500
		self.rect.y =  366
			
	def update(self):
		time = pygame.time.get_ticks()
		self.hp += 0.04
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 1000:
			self.hp = 1000
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_f]:
			self.speed_x = -3
		if keystate[pygame.K_h]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_t]:
			self.speed_y = -3
		if keystate[pygame.K_g]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550
		if not self.counter2:
			if (time//100) % 50 == 0:
				self.counter2 = True

class Player4(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 900
		self.rect.y =  366
				
	def update(self):
		time = pygame.time.get_ticks()
		self.hp += 0.04
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 1000:
			self.hp = 1000
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_j]:
			self.speed_x = -3
		if keystate[pygame.K_l]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_i]:
			self.speed_y = -3
		if keystate[pygame.K_k]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550
		if not self.counter2:
			if (time//100) % 50 == 0:
				self.counter2 = True

class Area(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/area.png").convert(),(210,160))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 700
		self.rect.centery = 266
		self.target = None
		self.speed = 20

	def update(self):
		self.target = ogre
		if (self.target.rect.centerx - self.rect.centerx) == 0:
			if self.target.rect.centery > self.rect.centery:
				self.rect.centery += self.speed 
			elif self.rect.centery > self.target.rect.centery:
				self.rect.centery -= self.speed
			else:
				self.rect.centery += 0
		elif (self.target.rect.centerx - self.rect.centerx) != 0:
			x,y = direction(self, self.target)
			self.rect.centerx += self.speed*x
			self.rect.centery += self.speed*y

class Ogre(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/ogre.png").convert(),(200,200))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 700
		self.rect.centery = 266
		self.speed = 4
		self.target = None
		self.hit = True
		self.counter = True
		self.attack = False
		self.counter2 = False

	def update(self):
		time1 = pygame.time.get_ticks()
		target_list = [player1, player2, player3, player4]
		target_list = [t for t in target_list if t.hp >0]
		distance_list = [(distance(self,t),t) for t in target_list]
		if len(distance_list)==0:
			distance_list = [(0,self.target)]
		self.target = sorted(distance_list, key=lambda x: x[0])[0][1]

		if self.counter:
			if (self.target.rect.centerx - self.rect.centerx) == 0:
				if self.target.rect.centery > self.rect.centery:
					self.rect.centery += self.speed 
				elif self.rect.centery > self.target.rect.centery:
					self.rect.centery -= self.speed
				else:
					self.rect.centery += 0
			elif (self.target.rect.centerx - self.rect.centerx) != 0:
				x,y = direction(self, self.target)
				self.rect.centerx += self.speed*x
				self.rect.centery += self.speed*y
		if self.counter:
			
			if ((abs(self.target.rect.centerx - self.rect.centerx) < 4 and 
			abs(self.target.rect.centery - self.rect.centery) < 4)):
				self.counter = False
				attack1 = Ogre_anim(ogre.rect.center)
				all_sprites.add(attack1)
		
		if (time1//100) % 60 == 0:
			self.counter = True

class Ogre_anim(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = ogre_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50 # VELOCIDAD DE LA animación

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(ogre_anim):
				self.kill()
			else:
				center = self.rect.center
				self.image = ogre_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center
		if self.frame == 45:
			ogre.attack = True
		if self.frame == 46:
			ogre.attack = False

def show_go_screen():
	
	screen.fill(BLACK)
	draw_text1(screen, "Poke The Ogre", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Hit the Ogre", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
		
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp1():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 1 WINS", 40, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	draw_text1(screen, "P1 " + str(int(player1.damage)) , 20, WIDTH // 2, 420)
	draw_text1(screen, "P2 " + str(int(player2.damage)) , 20, WIDTH // 2, 440)
	draw_text1(screen, "P3 " + str(int(player3.damage)) , 20, WIDTH // 2, 460)
	draw_text1(screen, "P4 " + str(int(player4.damage)) , 20, WIDTH // 2, 480)
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp2():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 2 WINS", 40, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	draw_text1(screen, "P1 " + str(int(player1.damage)) , 20, WIDTH // 2, 420)
	draw_text1(screen, "P2 " + str(int(player2.damage)) , 20, WIDTH // 2, 440)
	draw_text1(screen, "P3 " + str(int(player3.damage)) , 20, WIDTH // 2, 460)
	draw_text1(screen, "P4 " + str(int(player4.damage)) , 20, WIDTH // 2, 480)
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp3():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 3 WINS", 40, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	draw_text1(screen, "P1 " + str(int(player1.damage)) , 20, WIDTH // 2, 420)
	draw_text1(screen, "P2 " + str(int(player2.damage)) , 20, WIDTH // 2, 440)
	draw_text1(screen, "P3 " + str(int(player3.damage)) , 20, WIDTH // 2, 460)
	draw_text1(screen, "P4 " + str(int(player4.damage)) , 20, WIDTH // 2, 480)
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp4():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 4 WINS", 40, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	draw_text1(screen, "P1 " + str(int(player1.damage)) , 20, WIDTH // 2, 420)
	draw_text1(screen, "P2 " + str(int(player2.damage)) , 20, WIDTH // 2, 440)
	draw_text1(screen, "P3 " + str(int(player3.damage)) , 20, WIDTH // 2, 460)
	draw_text1(screen, "P4 " + str(int(player4.damage)) , 20, WIDTH // 2, 480)
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screend():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "DRAW", 40, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	draw_text1(screen, "P1 " + str(int(player1.damage)) , 20, WIDTH // 2, 420)
	draw_text1(screen, "P2 " + str(int(player2.damage)) , 20, WIDTH // 2, 440)
	draw_text1(screen, "P3 " + str(int(player3.damage)) , 20, WIDTH // 2, 460)
	draw_text1(screen, "P4 " + str(int(player4.damage)) , 20, WIDTH // 2, 480)
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

####----------------Ogre IMAGENES --------------
ogre_anim = []
for i in range(73):
	file = "img/ogre/{}.png".format(i)
	img = pygame.image.load(file).convert()
	img.set_colorkey(WHITE)
	img_scale = pygame.transform.scale(img, (400,400))
	ogre_anim.append(img_scale)

background = pygame.transform.scale(pygame.image.load("img/fond.png").convert(), (1300,700))

game_over1 = False
game_over2 = False
game_over3 = False
game_over4 = False
game_over5 = False
running = True
start = True
while running:
	if game_over1:
		show_game_over_screenp1()
		p_list = pygame.sprite.Group()
		screen.blit(background,(0,0))
		game_over1 = False
		area = Area()
		all_sprites = pygame.sprite.Group()
		all_sprites.add(area)
		ogre_list = pygame.sprite.Group()
		area_list = pygame.sprite.Group()
		area_list.add(area)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
		p_list.add(player1, player2, player3, player4)
		ogre = Ogre()
		all_sprites.add(ogre)
		ogre_list.add(ogre)
		start_time = pygame.time.get_ticks()

	if game_over2:
		show_game_over_screenp2()
		p_list = pygame.sprite.Group()
		screen.blit(background,(0,0))
		game_over2 = False
		area = Area()
		all_sprites = pygame.sprite.Group()
		all_sprites.add(area)	
		ogre_list = pygame.sprite.Group()
		area_list = pygame.sprite.Group()
		area_list.add(area)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
		p_list.add(player1, player2, player3, player4)
		ogre = Ogre()
		all_sprites.add(ogre)
		ogre_list.add(ogre)
		start_time = pygame.time.get_ticks()

	if game_over3:
		show_game_over_screenp3()
		p_list = pygame.sprite.Group()
		screen.blit(background,(0,0))
		area = Area()
		all_sprites = pygame.sprite.Group()
		all_sprites.add(area)
		game_over3 = False
		ogre_list = pygame.sprite.Group()
		area_list = pygame.sprite.Group()
		area_list.add(area)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
		p_list.add(player1, player2, player3, player4)
		ogre = Ogre()
		all_sprites.add(ogre)
		ogre_list.add(ogre)
		start_time = pygame.time.get_ticks()

	if game_over4:
		show_game_over_screenp4()
		p_list = pygame.sprite.Group()
		screen.blit(background,(0,0))
		game_over4 = False
		area = Area()
		all_sprites = pygame.sprite.Group()
		all_sprites.add(area)	
		ogre_list = pygame.sprite.Group()
		area_list = pygame.sprite.Group()
		area_list.add(area)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
		p_list.add(player1, player2, player3, player4)
		ogre = Ogre()
		all_sprites.add(ogre)
		ogre_list.add(ogre)
		start_time = pygame.time.get_ticks()
	
	if game_over5:
		show_game_over_screend()
		p_list = pygame.sprite.Group()
		screen.blit(background,(0,0))
		game_over5 = False
		area = Area()
		all_sprites = pygame.sprite.Group()
		all_sprites.add(area)
		ogre_list = pygame.sprite.Group()
		area_list = pygame.sprite.Group()
		area_list.add(area)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
		p_list.add(player1, player2, player3, player4)
		ogre = Ogre()
		all_sprites.add(ogre)
		ogre_list.add(ogre)
		start_time = pygame.time.get_ticks()

	if start:
		show_go_screen()

		start = False
		p_list = pygame.sprite.Group()
		screen.blit(background,(0,0))
		area = Area()
		all_sprites = pygame.sprite.Group()
		all_sprites.add(area)	
		ogre_list = pygame.sprite.Group()
		area_list = pygame.sprite.Group()
		area_list.add(area)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
		p_list.add(player1, player2, player3, player4)	
		ogre = Ogre()
		all_sprites.add(ogre)
		ogre_list.add(ogre)
		start_time = pygame.time.get_ticks()
		
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()
	
	
	now = (pygame.time.get_ticks() - start_time)//1000
	e = player1.hp == 0 and player2.hp == 0 and player3.hp == 0 and player4.hp == 0
	if now == 120 or len(p_list) == 0:
		a = player1.damage
		b = player2.damage
		c = player3.damage
		d = player4.damage
		if a > b and a > c and a > d:
			game_over1 = True
		if b > a and b > c and b > d:
			game_over2 = True
		if c > a and c > b and c > d:
			game_over3 = True
		if d > a and d > b and d > c:
			game_over4 = True
		if a == b and a > c and a > d:
			game_over5 = True
		if b == c and b > a and b > d:
			game_over5 = True
		if c == d and c > a and c > d:
			game_over5 = True
		if a == c and a > b and a > d:
			game_over5 = True
		if a == d and a > c and a > b:
			game_over5 = True
		if b == d and b > a and b > c:
			game_over5 = True
		if a == b and c == d and a != c:
			game_over5 = True
		if b == c and a == d and b != a:
			game_over5 = True
		if a == c and b == d and a != b:
			game_over5 = True
		if a == b == c and a > d:
			game_over5 = True
		if a == c == d and a > b:
			game_over5 = True
		if b == c == d and a < c:
			game_over5 = True
		if a == b == d and a > c:
			game_over5 = True

	
	all_sprites.update()
		
	# Checar colisiones - player1 - ogre
	hits = pygame.sprite.spritecollide(player1, area_list, False)
	for hit in hits:
		if ogre.attack:
			if player1.counter2:
				player1.counter2 = False
				player1.hp -= 217
	
	# Checar colisiones - player2 - ogre
	hits = pygame.sprite.spritecollide(player2, area_list, False)
	for hit in hits:
		if ogre.attack:
			if player2.counter2:
				player2.counter2 = False
				player2.hp -= 217
		
	# Checar colisiones - player3 - ogre
	hits = pygame.sprite.spritecollide(player3, area_list, False)
	for hit in hits:
		if ogre.attack:
			if player3.counter2:
				player3.counter2 = False
				player3.hp -= 217
		
	# Checar colisiones - player4 - ogre
	hits = pygame.sprite.spritecollide(player4, area_list, False)
	for hit in hits:
		if ogre.attack:
			if player4.counter2:
				player4.counter2 = False
				player4.hp -= 217
		
	# Checar colisiones - player1 - ogre
	hits = pygame.sprite.spritecollide(player1, ogre_list, False)
	for hit in hits:
		keystate = pygame.key.get_pressed()
		if player1.counter1:
			if keystate[pygame.K_e]:
				player1.counter1 = False
				player1.damage += 10
		if not keystate[pygame.K_e]:
			player1.counter1 = True
	# Checar colisiones - player2 - ogre
	hits = pygame.sprite.spritecollide(player2, ogre_list, False)
	for hit in hits:
		keystate = pygame.key.get_pressed()
		if player2.counter1:
			if keystate[pygame.K_p]:
				player2.counter1 = False
				player2.damage += 10
		if not keystate[pygame.K_p]:
			player2.counter1 = True

	# Checar colisiones - player3 - ogre
	hits = pygame.sprite.spritecollide(player3, ogre_list, False)
	for hit in hits:
		keystate = pygame.key.get_pressed()
		if player3.counter1:
			if keystate[pygame.K_y]:
				player3.counter1 = False
				player3.damage += 10
		if not keystate[pygame.K_y]:
			player3.counter1 = True

	# Checar colisiones - player4 - ogre
	hits = pygame.sprite.spritecollide(player4, ogre_list, False)
	for hit in hits:
		keystate = pygame.key.get_pressed()
		if player4.counter1:
			if keystate[pygame.K_o]:
				player4.counter1 = False
				player4.damage += 10
		if not keystate[pygame.K_o]:
			player4.counter1 = True
		
	screen.blit(background, [0, 0])

	all_sprites.draw(screen)
	
	# Escudo.
	draw_text1(screen, "P1", 20, 110, 6)
	draw_text1(screen, "P2", 20, 400, 6)
	draw_text1(screen, "P3", 20, 700, 6)
	draw_text1(screen, "P4", 20, 1000, 6)

	draw_hp_bar(screen, 120, 5, player1.hp//10)
	draw_text2(screen, str(int(player1.hp)) + "/1000", 10, 145, 6)
	draw_hp_bar(screen, player1.rect.x, player1.rect.y - 10, player1.hp//10)

	draw_hp_bar(screen, 415, 5, player2.hp//10)
	draw_text2(screen, str(int(player2.hp))+ "/1000", 10, 440, 6)
	draw_hp_bar(screen, player2.rect.x, player2.rect.y - 10, player2.hp//10)

	draw_hp_bar(screen, 715, 5, player3.hp//10)
	draw_text2(screen, str(int(player3.hp))+ "/1000", 10, 740, 6)
	draw_hp_bar(screen, player3.rect.x, player3.rect.y - 10, player3.hp//10)

	draw_hp_bar(screen, 1015, 5, player4.hp//10)
	draw_text2(screen, str(int(player4.hp))+ "/1000", 10, 1040, 6)
	draw_hp_bar(screen, player4.rect.x, player4.rect.y - 10, player4.hp//10)

	#tabla de puntuación

	draw_text2(screen,"P1 " + str(int(player1.damage)) , 10, 1050, 300)
	draw_text2(screen,"P2 " + str(int(player2.damage)) , 10, 1050, 310)
	draw_text2(screen, "P3 " + str(int(player3.damage)) , 10, 1050, 320)
	draw_text2(screen, "P4 " + str(int(player4.damage)) , 10, 1050, 330)
	
	#reloj
	draw_text1(screen, str((((pygame.time.get_ticks() - start_time)//60000)+(60))%(60))+":" + str((((pygame.time.get_ticks() - start_time)//1000)+(60))%(60)), 30, 570, 50)
		
	pygame.display.flip()
pygame.quit()