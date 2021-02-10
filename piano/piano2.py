import pygame
pygame.mixer.pre_init(44100,-16,2,2048)
pygame.mixer.init()
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((1024,318))
timer=pygame.time.Clock()


image=pygame.image.load("piano1.png")
mixer=pygame.mixer.Sound


BLACK=(0,0,0)
WHITE=(225,225,225)
RED=(225,0,0)
GRAY=(50,50,50)

x=0
y=97
width=700
height=350

def drow_game():
    screen.fill(WHITE)
    screen.blit(image,(x,-y))
    timer.tick(20)
    pygame.display.update()

while True:
    pygame.time.delay(20)
    keys = pygame.key.get_pressed()
    sound = {
        pygame.K_a: mixer("f.wav"),
        pygame.K_s: mixer("g.wav"),
        pygame.K_d: mixer("a.wav"),
        pygame.K_f: mixer("b.wav"),
        pygame.K_g: mixer("c1.wav"),
        pygame.K_h: mixer("d1.wav"),
        pygame.K_j: mixer("e1.wav"),
        pygame.K_k: mixer("f1.wav"),
        pygame.K_z: mixer("g1.wav"),
        pygame.K_x: mixer("a1.wav"),
        pygame.K_c: mixer("b1.wav"),
        pygame.K_v: mixer("c2.wav"),
        pygame.K_b: mixer("d2.wav"),
        pygame.K_n: mixer("e2.wav")
    }


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    for key in sound:
        if keys[key]:
            sound.get(key).play()


    drow_game()