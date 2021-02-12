import pygame

## initalizing the mixer and pygame
pygame.mixer.pre_init(44100,-16,20,2048)
pygame.mixer.init()
pygame.init()

# setting the size of the screen
screen=pygame.display.set_mode((1024,318))
# setting the time
timer=pygame.time.Clock()


sounds_file = "res\\sounds\\"
images_file = "res\\imgs\\" 

# loading paino image to the screen
image=pygame.image.load(images_file + "piano1.png")


## colors for the screen
BLACK=(0,0,0)
WHITE=(225,225,225)
RED=(225,0,0)
GRAY=(50,50,50)

x=0
y=97
width=700
height=350

## mapping keys to sounds
mixer=pygame.mixer.Sound
sound = {
        pygame.K_a: mixer(sounds_file + "f.wav"),
        pygame.K_s: mixer(sounds_file + "g.wav"),
        pygame.K_d: mixer(sounds_file + "a.wav"),
        pygame.K_f: mixer(sounds_file + "b.wav"),
        pygame.K_g: mixer(sounds_file + "c1.wav"),
        pygame.K_h: mixer(sounds_file + "d1.wav"),
        pygame.K_j: mixer(sounds_file + "e1.wav"),
        pygame.K_k: mixer(sounds_file + "f1.wav"),
        pygame.K_z: mixer(sounds_file + "g1.wav"),
        pygame.K_x: mixer(sounds_file + "a1.wav"),
        pygame.K_c: mixer(sounds_file + "b1.wav"),
        pygame.K_v: mixer(sounds_file + "c2.wav"),
        pygame.K_b: mixer(sounds_file + "d2.wav"),
        pygame.K_n: mixer(sounds_file + "e2.wav")
}



def drow_game():
    screen.fill(WHITE)
    screen.blit(image,(x,-y))
    timer.tick(20)
    pygame.display.update()


while True:
    #pygame.time.delay(20)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    for key in sound:
        if keys[key]:
            sound.get(key).play()

    drow_game()