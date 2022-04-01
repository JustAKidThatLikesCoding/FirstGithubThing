from unicodedata import category
import pygame, time, random, sys

InMenu = True

def startgame():
    global InMenu

    width = 750
    height = 500

    screen = pygame.display.set_mode((width, height))
    pygame.init()

    player = pygame.image.load('assets/player.png')
    startbtn = pygame.image.load('assets/startbtn.png')
    quitbtn = pygame.image.load('assets/quitbtn.png')
    menubtn = pygame.image.load('assets/menubtn.png')
    goonbtn = pygame.image.load('assets/go-on.png')
    cat1 = pygame.image.load('assets/rain.png')
    cat2 = pygame.image.load('assets/rain.png')
    cat3 = pygame.image.load('assets/rain.png')
    cat4 = pygame.image.load('assets/rain.png')
    potat1 = pygame.image.load('assets/potat.png')
    potat2 = pygame.image.load('assets/potat.png')
    potat3 = pygame.image.load('assets/potat.png')
    potat4 = pygame.image.load('assets/potat.png')
    menuimg = pygame.image.load('assets/menu.png').convert()
    bg = pygame.image.load('assets/bg.png').convert()
    dedscreen = pygame.image.load('assets/dead.png')
    font = pygame.font.SysFont('calibri ',50)

    outsidecolor = (255,255,255)
    standing = False

    px = 345
    py = 468

    px2 = 30
    py2 = 30

    bx = 600
    by = 400

    bx2 = 100
    by2 = 100

    bgx = 0
    bgy = 0

    catx = random.randint(0,730)
    catx2 = random.randint(0,730)
    catx3 = random.randint(0,730)
    catx4 = random.randint(0,730)
    
    patx = random.randint(0,730)
    patx2 = random.randint(0,730)
    patx3 = random.randint(0,730)
    patx4 = random.randint(0,730)

    caty = 0
    caty2 = 0
    caty3 = 0
    caty4 = 0

    paty = 0
    paty2 = 0
    paty3 = 0
    paty4 = 0

    lspeed = 0.1
    rspeed = 0.1

    enemywalkspeed = 0.035
    enemydirection = 0
    jumpingpower = 0.075
    gravity = 0.0001
    velocity = 0
    enemyvelocity = 0

    indawall = False
    Dead = False
    abletowalk = True
    walking = False
    Paused = False
    InGame = True
    lwall = False
    rwall = False

    while InMenu:
        screen.fill((255,255,255))
        screen.blit(menuimg, (0,0))
        screen.blit(startbtn, (100,250))
        screen.blit(quitbtn, (550,250))
        quitrect = pygame.draw.rect(screen, (outsidecolor), (550,250,100,25), 1)
        startrect = pygame.draw.rect(screen, (outsidecolor), (100,250,100,25), 1)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mx,my = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clickdastart = pygame.Rect.collidepoint(startrect, mx,my)
                clickdaquit = pygame.Rect.collidepoint(quitrect, mx,my)
                if clickdastart:
                    outsidecolor = (0,0,0)
                    startrect = pygame.draw.rect(screen, (outsidecolor), (100,250,100,25), 1)
                    pygame.display.flip()
                    time.sleep(0.4)
                    outsidecolor = (255,255,255)
                    startrect = pygame.draw.rect(screen, (outsidecolor), (100,250,100,25), 1)
                    pygame.display.flip()
                    time.sleep(0.4)
                    InMenu = False

                if clickdaquit:
                    outsidecolor = (0,0,0)
                    quitrect = pygame.draw.rect(screen, (outsidecolor), (550,250,100,25), 1)
                    pygame.display.flip()
                    time.sleep(0.4)
                    outsidecolor = (255,255,255)
                    quitrect = pygame.draw.rect(screen, (outsidecolor), (550,250,100,25), 1)
                    pygame.display.flip()
                    time.sleep(0.4)
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

    while InGame:

        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            px -= lspeed

        if key[pygame.K_d]:
            px += rspeed

        if key[pygame.K_ESCAPE]:
            Paused = True
            while Paused:
                screen.fill((0,0,0))
                title = font.render("Paused", False, (255,255,255))
                screen.blit(title, (305,100))
                screen.blit(menubtn, (325,200))
                screen.blit(goonbtn, (325,250))
                menurect = pygame.draw.rect(screen, (outsidecolor), (325,200,100,25), 1)
                goonrect = pygame.draw.rect(screen, (outsidecolor), (325,250,100,25), 1)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        mx,my = pygame.mouse.get_pos()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        clickdamenu = pygame.Rect.collidepoint(menurect, mx,my)
                        clickdagoon = pygame.Rect.collidepoint(goonrect, mx,my)
                        if clickdamenu:
                            outsidecolor = (0,0,0)
                            menurect = pygame.draw.rect(screen, (outsidecolor), (325,200,100,25), 1)
                            pygame.display.flip()
                            time.sleep(0.4)
                            outsidecolor = (255,255,255)
                            menurect = pygame.draw.rect(screen, (outsidecolor), (325,200,100,25), 1)
                            pygame.display.flip()
                            time.sleep(0.4)
                            InGame = False
                            InMenu = True
                            Paused = False

                        if clickdagoon:
                            outsidecolor = (0,0,0)
                            goonrect = pygame.draw.rect(screen, (outsidecolor), (325,250,100,25), 1)
                            pygame.display.flip()
                            time.sleep(0.4)
                            outsidecolor = (255,255,255)
                            goonrect = pygame.draw.rect(screen, (outsidecolor), (325,250,100,25), 1)
                            pygame.display.flip()
                            time.sleep(0.4)
                            Paused = False

                
                pygame.display.update()
        
        screen.fill((255,255,255))
        screen.blit(menuimg, (0,0))
        playerrectthing = pygame.Rect(px,py,px2,py2)
        cr = pygame.Rect(catx,caty,15,15)
        cr2 = pygame.Rect(catx2,caty2,15,15)
        cr3 = pygame.Rect(catx3,caty3,15,15)
        cr4 = pygame.Rect(catx4,caty4,15,15)
        pr = pygame.Rect(patx,paty,15,15)
        pr2 = pygame.Rect(patx2,paty2,15,15)
        pr3 = pygame.Rect(patx3,paty3,15,15)
        pr4 = pygame.Rect(patx4,paty4,15,15)
        screen.blit(cat1, (catx, caty))
        screen.blit(cat2, (catx2,caty2))
        screen.blit(cat3, (catx3,caty3))
        screen.blit(cat4, (catx4,caty4))
        screen.blit(potat1, (patx,paty))
        screen.blit(potat2, (patx2,paty2))
        screen.blit(potat3, (patx3,paty3))
        screen.blit(potat4, (patx4,paty4))
        collision = pygame.Rect.colliderect(playerrectthing, cr)
        collision2 = pygame.Rect.colliderect(playerrectthing, cr2)
        collision3 = pygame.Rect.colliderect(playerrectthing, cr3)
        collision4 = pygame.Rect.colliderect(playerrectthing, cr4)
        collision5 = pygame.Rect.colliderect(playerrectthing, pr)
        collision6 = pygame.Rect.colliderect(playerrectthing, pr2)
        collision7 = pygame.Rect.colliderect(playerrectthing, pr3)
        collision8 = pygame.Rect.colliderect(playerrectthing, pr4)
        screen.blit(player, (px,py))
        pygame.display.flip()

        if collision or collision2 or collision3 or collision4 or collision5 or collision6 or collision7 or collision8:
            Dead = True
            InGame = False

        if paty == 0:
            patsped1 = random.randint(10,20)

        if paty2 == 0:
            patsped2 = random.randint(10,20)

        if paty3 == 0:
            patsped3 = random.randint(10,20)
            
        if paty4 == 0:
            patsped4 = random.randint(10,20)

        if caty == 0:
            catsped1 = random.randint(10,20)
            
        if caty2 == 0:
            catsped2 = random.randint(10,20)
            
        if caty3 == 0:
            catsped3 = random.randint(10,20)
        
        if caty4 == 0:
            catsped4 = random.randint(10,20)

        if paty >= 500:
            patx = random.randint(0,750)
            paty = 0

        if paty2 >= 500:
            patx = random.randint(0,750)
            paty2 = 0

        if paty3 >= 500:
            patx3 = random.randint(0,750)
            paty3 = 0

        if paty4 >= 500:
            patx4 = random.randint(0,750)
            paty4 = 0

        if caty >= 500:
            catx = random.randint(0,750)
            caty = 0

        if caty2 >= 500:
            catx2 = random.randint(0,750)
            caty2 = 0

        if caty3 >= 500:
            catx3 = random.randint(0,750)
            caty3 = 0

        if caty4 >= 500:
            catx4 = random.randint(0,750)
            caty4 = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if py >= 469:
            standing = True
            velocity = 0
            py = 468

        if px <= 0:
            px = 1

        if px >= 720:
            px = 719

        if bgx >= 749:
            bgx = 0

        if bgx <= -749:
            bgx = 750

        velocity += gravity
        py += velocity
        caty += catsped1 / 100
        caty2 += catsped2 / 100
        caty3 += catsped3 / 100
        caty4 += catsped4 / 100
        paty += patsped1 / 100
        paty2 += patsped2 / 100
        paty3 += patsped3 / 100
        paty4 += patsped4 / 100

    while Dead:
        screen.fill((245, 66, 66))
        screen.blit(dedscreen, (0,0))
        screen.blit(startbtn, (525,300))
        screen.blit(quitbtn, (525,250))
        screen.blit(menubtn, (525,350))
        quitrect = pygame.draw.rect(screen, (outsidecolor), (525,250,100,25), 1)
        startrect = pygame.draw.rect(screen, (outsidecolor), (525,300,100,25), 1)
        menurect = pygame.draw.rect(screen, (outsidecolor), (525,350,100, 25), 1)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mx,my = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clickdastart = pygame.Rect.collidepoint(startrect, mx,my)
                clickdaquit = pygame.Rect.collidepoint(quitrect, mx,my)
                clickdamenu = pygame.Rect.collidepoint(menurect, mx,my)

                if clickdamenu:
                    outsidecolor = (0,0,0)
                    menurect = pygame.draw.rect(screen, (outsidecolor), (525,350,100, 25), 1)
                    pygame.display.flip()
                    time.sleep(0.4)
                    outsidecolor = (255,255,255)
                    menurect = pygame.draw.rect(screen, (outsidecolor), (525,350,100, 25), 1)
                    pygame.display.flip()
                    time.sleep(0.4)
                    InMenu = True
                    Dead = False

                if clickdastart:
                    outsidecolor = (0,0,0)
                    startrect = pygame.draw.rect(screen, (outsidecolor), (525,300,100,25), 1)
                    pygame.display.flip()
                    time.sleep(0.4)
                    outsidecolor = (255,255,255)
                    startrect = pygame.draw.rect(screen, (outsidecolor), (525,300,100,25), 1)
                    pygame.display.flip()
                    time.sleep(0.4)
                    InMenu = False
                    Dead = False

                if clickdaquit:
                    outsidecolor = (0,0,0)
                    quitrect = pygame.draw.rect(screen, (outsidecolor), (525,250,100,25), 1)
                    pygame.display.flip()
                    time.sleep(0.4)
                    outsidecolor = (255,255,255)
                    quitrect = pygame.draw.rect(screen, (outsidecolor), (525,250,100,25), 1)
                    pygame.display.flip()
                    time.sleep(0.4)
                    pygame.quit()
                    sys.exit()


while True:
    startgame()