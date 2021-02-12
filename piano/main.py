import pygame

## initalizing the mixer and pygame
pygame.mixer.pre_init(44100,-16,20,2048)
pygame.mixer.init()
pygame.init()

pygame.mixer.set_num_channels(10) # to play multible sounds at the same time

# setting the size of the screen
screen=pygame.display.set_mode((1024,318))
# setting the time
timer=pygame.time.Clock()


sounds_folder = "res\\sounds\\"
images_folder = "res\\imgs\\" 

# loading paino image to the screen
image=pygame.image.load(images_folder + "piano1.png")


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
        pygame.K_a: mixer(sounds_folder + "f.wav"),
        pygame.K_s: mixer(sounds_folder + "g.wav"),
        pygame.K_d: mixer(sounds_folder + "a.wav"),
        pygame.K_f: mixer(sounds_folder + "b.wav"),
        pygame.K_g: mixer(sounds_folder + "c1.wav"),
        pygame.K_h: mixer(sounds_folder + "d1.wav"),
        pygame.K_j: mixer(sounds_folder + "e1.wav"),
        pygame.K_k: mixer(sounds_folder + "f1.wav"),
        pygame.K_z: mixer(sounds_folder + "g1.wav"),
        pygame.K_x: mixer(sounds_folder + "a1.wav"),
        pygame.K_c: mixer(sounds_folder + "b1.wav"),
        pygame.K_v: mixer(sounds_folder + "c2.wav"),
        pygame.K_b: mixer(sounds_folder + "d2.wav"),
        pygame.K_n: mixer(sounds_folder + "e2.wav")
}



def drow_game():
    screen.fill(WHITE)
    screen.blit(image,(x,-y))
    timer.tick(20)
    pygame.display.update()
#the number of channel working
n_channel = 0
last_key = 0
time_of_last_click = 500000

while True:
    pygame.time.delay(60)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    for key in sound:
        
        interval_between_clicks = pygame.time.get_ticks() - time_of_last_click
        if (last_key == key) & (interval_between_clicks<= 1000):
            continue
        elif keys[key]:
           pygame.mixer.Channel(n_channel).play(sound.get(key))
           
           last_key = key
           time_of_last_click = pygame.time.get_ticks()
           print(time_of_last_click)
           
           n_channel += 1
           if n_channel >= 2: n_channel = 0
    drow_game()
