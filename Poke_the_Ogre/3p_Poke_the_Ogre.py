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
YELLOW = (255,255,0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Poke the Ogre")
clock = pygame.time.Clock()

total_damage = 0
times_last_hit = []
damage_incress = 1
incress_duration = 8 # segundos

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

def draw_text3(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLUE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text4(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, RED)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text5(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, YELLOW)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def draw_hp_bar2(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, RED, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def draw_hp_bar3(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, YELLOW, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

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
	if radio != 0:
		x, y = (dx/radio, dy/radio)
	else:
		x, y = (0, 0)
	return x, y

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
		self.start_time = pygame.time.get_ticks()

class Player1(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 500
		self.rect.y = 133

	def update(self):
		current_time = pygame.time.get_ticks()
		elapsed_time = current_time - self.start_time
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
		if self.counter2:
			self.start_time = pygame.time.get_ticks()
		if not self.counter2:
			if elapsed_time >= 3000:
				self.counter2 = True

class Player2(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 900
		self.rect.y = 133
				
	def update(self):
		current_time = pygame.time.get_ticks()
		elapsed_time = current_time - self.start_time
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
		if self.counter2:
			self.start_time = pygame.time.get_ticks()
		if not self.counter2:
			if elapsed_time >= 3000:
				self.counter2 = True

class Player3(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 500
		self.rect.y =  366
			
	def update(self):
		current_time = pygame.time.get_ticks()
		elapsed_time = current_time - self.start_time
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
		if self.counter2:
			self.start_time = pygame.time.get_ticks()
		if not self.counter2:
			if elapsed_time >= 3000:
				self.counter2 = True

class Area(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/area.png").convert(),(210,160))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 700
		self.rect.centery = 266
		self.speed = 20

	def update(self):
		target = ogre
		x,y = direction(self, target)
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
		self.n = 6000
		self.start_time1 = pygame.time.get_ticks()

	def update(self):
		current_time = pygame.time.get_ticks()
		elapsed_time = current_time - self.start_time1
		target_list = [player1, player2, player3]
		target_list = [t for t in target_list if t.hp >0]
		distance_list = [(distance(self,t),t) for t in target_list]
		if len(distance_list)==0:
			distance_list = [(0,self.target)]
		self.target = sorted(distance_list, key=lambda x: x[0])[0][1]

		if self.counter:
			x,y = direction(self, self.target)
			self.rect.centerx += self.speed*x
			self.rect.centery += self.speed*y
		if self.counter:
			
			if ((abs(self.target.rect.centerx - self.rect.centerx) < 4 and 
			abs(self.target.rect.centery - self.rect.centery) < 4)):
				self.counter = False
				attack1 = Ogre_anim(ogre.rect.center)
				all_sprites.add(attack1)
				self.start_time1 = pygame.time.get_ticks()

		if elapsed_time >= self.n:
			self.counter = True

class Ogre_anim(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = ogre_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 35 # VELOCIDAD DE LA animación(mientras menor el numero, mas rapido la animacion)
		self.counter = True

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
			if self.counter:
				self.counter = False
				ogre_crush_sound.play()
			
			ogre.attack = True
		if self.frame == 46:
			self.counter = True
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

def show_game_over_screenp3():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 3 WINS", 40, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	draw_text1(screen, "P1 " + str(int(player1.damage)) , 20, WIDTH // 2, 420)
	draw_text1(screen, "P2 " + str(int(player2.damage)) , 20, WIDTH // 2, 440)
	draw_text1(screen, "P3 " + str(int(player3.damage)) , 20, WIDTH // 2, 460)
	
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

ogre_crush_sound = pygame.mixer.Sound("sound/ogre_crush.wav")

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
		total_damage = 0
		times_last_hit = []
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
		ogre = Ogre()
		all_sprites.add(player1, player2, player3, ogre)
		p_list.add(player1, player2, player3)
		ogre_list.add(ogre)
		start_time = pygame.time.get_ticks()

	if game_over2:
		total_damage = 0
		times_last_hit = []
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
		ogre = Ogre()
		all_sprites.add(player1, player2, player3, ogre)
		p_list.add(player1, player2, player3)
		ogre_list.add(ogre)
		start_time = pygame.time.get_ticks()

	if game_over3:
		total_damage = 0
		times_last_hit = []
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
		ogre = Ogre()
		all_sprites.add(player1, player2, player3, ogre)
		p_list.add(player1, player2, player3)
		ogre_list.add(ogre)
		start_time = pygame.time.get_ticks()
	
	if game_over5:
		total_damage = 0
		times_last_hit = []
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
		ogre = Ogre()
		all_sprites.add(player1, player2, player3, ogre)
		p_list.add(player1, player2, player3)
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
		ogre = Ogre()
		all_sprites.add(player1, player2, player3, ogre)
		p_list.add(player1, player2, player3)	
		ogre_list.add(ogre)
		start_time = pygame.time.get_ticks()
		
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()
	
	
	now = (pygame.time.get_ticks() - start_time)//1000
	e = player1.hp == 0 and player2.hp == 0 and player3.hp == 0
	if now >= 120 or len(p_list) == 0:
		a = player1.damage
		b = player2.damage
		c = player3.damage
		if a > b and a > c:
			game_over1 = True
		if b > a and b > c:
			game_over2 = True
		if c > a and c > b:
			game_over3 = True
		if a == b and a > c:
			game_over5 = True
		if b == c and b > a:
			game_over5 = True
		if a == c and a > b:
			game_over5 = True
		if a == b == c:
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
		
	# Checar colisiones - player1 - ogre
	hits = pygame.sprite.spritecollide(player1, ogre_list, False)
	for hit in hits:
		keystate = pygame.key.get_pressed()
		if player1.counter1:
			if keystate[pygame.K_e]:
				total_damage += damage_incress
				times_last_hit.append(pygame.time.get_ticks())
				player1.damage += total_damage
				player1.counter1 = False
		if not keystate[pygame.K_e]:
			player1.counter1 = True
	# Checar colisiones - player2 - ogre
	hits = pygame.sprite.spritecollide(player2, ogre_list, False)
	for hit in hits:
		keystate = pygame.key.get_pressed()
		if player2.counter1:
			if keystate[pygame.K_p]:
				total_damage += damage_incress
				times_last_hit.append(pygame.time.get_ticks())
				player2.damage += total_damage
				player2.counter1 = False
		if not keystate[pygame.K_p]:
			player2.counter1 = True

	# Checar colisiones - player3 - ogre
	hits = pygame.sprite.spritecollide(player3, ogre_list, False)
	for hit in hits:
		keystate = pygame.key.get_pressed()
		if player3.counter1:
			if keystate[pygame.K_y]:
				total_damage += damage_incress
				times_last_hit.append(pygame.time.get_ticks())
				player3.damage += total_damage
				player3.counter1 = False
		if not keystate[pygame.K_y]:
			player3.counter1 = True

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)
	
	# Escudo.
	draw_text1(screen, "P1", 20, 110, 6)
	draw_text1(screen, "P2", 20, 400, 6)
	draw_text1(screen, "P3", 20, 700, 6)

	draw_hp_bar(screen, 120, 5, player1.hp//10)
	draw_text2(screen, str(int(player1.hp)) + "/1000", 10, 145, 6)

	draw_hp_bar(screen, 415, 5, player2.hp//10)
	draw_text2(screen, str(int(player2.hp))+ "/1000", 10, 440, 6)

	draw_hp_bar(screen, 715, 5, player3.hp//10)
	draw_text2(screen, str(int(player3.hp))+ "/1000", 10, 740, 6)
	for p in p_list:
		if p.hp > 0:
			if p == player1:
				draw_hp_bar(screen, p.rect.x, p.rect.y - 10, p.hp//10)
			if p == player2:
				draw_hp_bar2(screen, p.rect.x, p.rect.y - 10, p.hp//10)
			if p == player3:
				draw_hp_bar3(screen, p.rect.x, p.rect.y - 10, p.hp//10)

	#tabla de puntuación

	draw_text3(screen,"P1 " + str(int(player1.damage)) , 10, 1050, 300)
	draw_text4(screen,"P2 " + str(int(player2.damage)) , 10, 1050, 310)
	draw_text5(screen, "P3 " + str(int(player3.damage)) , 10, 1050, 320)
	
	#reloj
	draw_text1(screen, str((((pygame.time.get_ticks() - start_time)//60000)+(60))%(60))+":" + str((((pygame.time.get_ticks() - start_time)//1000)+(60))%(60)), 30, 570, 50)
		
	pygame.display.flip()
pygame.quit()