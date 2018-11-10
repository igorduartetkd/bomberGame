import pygame
import Pyro4


salas = {}
n = 1
with Pyro4.locateNS() as ns:
    for sala, sala_uri in ns.list(prefix="server.").items():
        print(n, "- ", sala)
        salas[n] = (Pyro4.Proxy(sala_uri))
        n += 1

idSala = int(input("Qual sala deseja se conectar? (posicao): "))
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

pygame.init()
clock = pygame.time.Clock()

tela = pygame.display.set_mode((800, 480))

arquivo = "img/bomb1.png"
imgTeste = pygame.image.load(arquivo)
imgTeste = pygame.transform.scale(imgTeste, (53, 53))
rectb = imgTeste.get_rect()
x = 7
y = 4
rectb = rectb.move((x*54, y*54))
arquivo2 = "img/fundo1.jpg"
imgTeste2 = pygame.image.load(arquivo2)
imgTeste2 = pygame.transform.scale(imgTeste2, (800, 480))
rectf = imgTeste2.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    tela.blit(imgTeste2, rectf)
    #rect = server.list_bombs()
    tela.blit(imgTeste, rectb)
    pygame.display.update()
    clock.tick(30)