import pygame
import Pyro4


salas = {}
n = 1
with Pyro4.locateNS() as ns:
    for sala, sala_uri in ns.list(prefix="server.").items():
        print(n, "- ", sala)
        salas[n] = (Pyro4.Proxy(sala_uri))
        n += 1

#idSala = int(input("Qual sala deseja se conectar? (posicao): "))
idSala = 1
server = salas[idSala]

list_model_char = server.get_model_chars()
list_model_bomb = server.get_model_bombs()
list_model_gift = server.get_model_gifts()
list_model_wall = server.get_model_walls()
dic_img_model_char = dict()
dic_img_model_bomb = dict()
dic_img_model_gift = dict()
dic_img_model_wall = dict()
for id, path in list_model_char:
    img = pygame.image.load(path)
    dic_img_model_char[id] = img
for id, path in list_model_bomb:
    img = pygame.image.load(path)
    dic_img_model_bomb[id] = img
for id, path in list_model_gift:
    img = pygame.image.load(path)
    dic_img_model_gift[id] = img
for id, path in list_model_wall:
    img = pygame.image.load(path)
    dic_img_model_wall[id] = img

#my_nick = input("Nick name: ")
my_nick = "teste"
char = 1

id_my_char = server.start_char(char, my_nick)
print(id_my_char)
pygame.init()
clock = pygame.time.Clock()

screem = pygame.display.set_mode((800, 480))

background = pygame.image.load("img/fundo1.jpg")
background = pygame.transform.scale(background, (800, 480))
rect_background = background.get_rect()




list_chars = list()
list_bombs = list()
list_gifts = list()
list_walls = list()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    key = pygame.key.get_pressed()

    if key[pygame.K_UP]:
        server.move(id_my_char, 270)
    elif key[pygame.K_DOWN]:
        server.move(id_my_char, 90)
    elif key[pygame.K_LEFT]:
        server.move(id_my_char, 180)
    elif key[pygame.K_RIGHT]:
        server.move(id_my_char, 0)

    # drawing
    screem.blit(background, rect_background)

    list_chars = server.list_chars()
    list_bombs = server.list_bombs()
    list_gifts = server.list_gifts()
    list_walls = server.list_walls()

    alive = False
    for [model_char, orientation, position, scale, alpha, nick] in list_chars:
        if my_nick == nick:
            alive = True

        img = dic_img_model_char[model_char]
        img = pygame.transform.scale(img, scale)
        rect = img.get_rect()
        rect = rect.move(position)
        img = pygame.transform.rotate(img, orientation)
        screem.blit(img, rect)

    for [model_wall, position, scale, alpha] in list_walls:
        img = dic_img_model_wall[model_wall]
        img = pygame.transform.scale(img, scale)
        rect = img.get_rect()
        rect = rect.move(position)
        screem.blit(img, rect)


    pygame.display.update()
    clock.tick(30)