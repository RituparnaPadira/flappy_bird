import pygame
import sys
from pygame.locals import *
import random
import time

swidth=1600
sheight=840
screen = pygame.display.set_mode((swidth,sheight))

def welcome():
    screen.blit(pygame.image.load('gallery/images/wlcm.png'),(0,0))
    screen.blit(pygame.image.load('gallery/images/wlcmb.png'), (swidth/3+20,sheight/4))
    pygame.mixer.Sound('gallery/audio/Betya - Lauren Duski.mp3').play()
    while True:
        
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and event.key==K_SPACE:
                pygame.mixer.stop()
                return
        screen.blit(pygame.image.load('gallery/images/wlcm_g.png'),(swidth/3,10))
        pygame.display.update()
        time.sleep(0.01)
        screen.blit(pygame.image.load('gallery/images/wlcm_b.png'), (swidth/3,10))
        pygame.display.update()
        time.sleep(0.01)


def game():
    pygame.mixer.Sound('gallery/audio/Gentle Breeze - Geographer.mp3').play()
    birdx=swidth/2 -10
    birdy=sheight/2
    birdht=pygame.image.load('gallery/images/bird.png').get_height()
    curr=0
    points=0

    pipe1 = makePipe()
    pipe2 = makePipe()
    pipe3 = makePipe()
    pipe4 = makePipe()
    
    pipes = [pipe1,pipe2,pipe3,pipe4]
    pset=(2*swidth)/3
    for pipe in pipes:
        pipe[0]['x']=pset
        pipe[1]['x']=pset
        pset+=400

    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                birdy-=55
                pygame.mixer.Sound('gallery/audio/Swoosh.mp3').play()
                
        birdy+=15
        
        for pipe in pipes:
            pipe[0]['x']-=10
            pipe[1]['x']-=10
        if -1<pipes[0][0]['x']<10:
            pipes.append(makePipe())
        if pipes[0][0]['x']< -70:
            pipes.pop(0)

        cpipe=pipes[curr]
        if cpipe[0]['x']<swidth/2+20 and cpipe[0]['x']>swidth/2-20:
            if cpipe[0]['y']<birdy+birdht or cpipe[1]['y']+pipeheight>birdy:
                pygame.mixer.stop()
                pygame.mixer.Sound('gallery/audio/Cartoon Boing.mp3').play()
                time.sleep(1)
                return points
        elif curr<2:
            if cpipe[0]['x']<swidth/2-20:
               curr+=1

        if cpipe[0]['x']<swidth/2-9 and cpipe[0]['x']>swidth/2-20:
            points+=1
        p=str(points)
            
        screen.blit(pygame.image.load('gallery/images/bgr.png'), (0,0))
        for pipe in pipes:
            screen.blit(pygame.image.load('gallery/images/pipe.png'), (pipe[0]['x'],pipe[0]['y']))
            screen.blit(pygame.transform.rotate(pygame.image.load('gallery/images/pipe.png'),180), (pipe[1]['x'],pipe[1]['y']))
        screen.blit(pygame.image.load('gallery/images/grnd.png'), (0,basey))
        screen.blit(pygame.image.load('gallery/images/bird.png'), (birdx, birdy))
        pw=0
        for digit in p:
            pw+=pygame.image.load('gallery/images/'+digit+'.png').get_width()
        px = swidth-pw-20
        for digit in p:
            i=pygame.image.load('gallery/images/'+digit+'.png')
            screen.blit(i, (px,10))
            px+=i.get_width()
        pygame.display.update()
        FPSCLOCK.tick(40)

def makePipe():
    pipex=swidth+50
    offset = pygame.image.load('gallery/images/bird.png').get_height()+100
    yl = offset + random.randint(0,basey-offset-20)
    yu = yl-offset-pipeheight
    pipe = [{'x':pipex, 'y':yl}, {'x':pipex, 'y':yu}]
    return pipe


def over(points):
    pygame.mixer.Sound('gallery/audio/Cartoon (Sting) - Twin Musicom.mp3').play()
    screen.blit(pygame.image.load('gallery/images/over.png'), (0,0))
    screen.blit(pygame.image.load('gallery/images/wlcmb.png'), (swidth/4-10,sheight/4))
    pw=0
    p=str(points)
    for digit in p:
        pw+=pygame.image.load('gallery/images/'+digit+'.png').get_width()
    px = (4*swidth)/5
    for digit in p:
        i=pygame.image.load('gallery/images/'+digit+'.png')
        screen.blit(i, (px,sheight/2))
        px+=i.get_width()
    pygame.display.update()
    while True:
        screen.blit(pygame.image.load('gallery/images/over_y.png'), (swidth/3,10))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and event.key==K_RETURN:
                pygame.mixer.stop()
                return
        
        screen.blit(pygame.image.load('gallery/images/over_b.png'), (swidth/3,10))
        pygame.display.update()


pygame.init()
FPSCLOCK = pygame.time.Clock()
basey=sheight-pygame.image.load('gallery/images/grnd.png').get_height()
pipeheight = pygame.image.load('gallery/images/pipe.png').get_height()
pygame.display.set_caption("Flappy Bird by Rituparna")
while True:
    welcome()
    over(game())
