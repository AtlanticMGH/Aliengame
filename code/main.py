def start():
    import pygame
    import sys
    from random import randrange
    from alien import alien
    from ammoc import ammoc
    from sword import sword
    from wall import wall


    pygame.init()
    screen = pygame.display.set_mode([800,800])
    clock = pygame.time.Clock()
    pygame.display.set_caption("Aliengame")

    playerup = pygame.image.load("playerup.png")
    playerleft = pygame.image.load("playerleft.png")
    playerdown = pygame.image.load("playerdown.png")
    playerright = pygame.image.load("playerright.png")

    bxu = []
    byu = []

    bxd = []
    byd= []

    bxl = []
    byl = []

    bxr = []
    byr = []

    class bullet:
        h = 5
        w = 5

    def newupbullet():
        bxu.append(playerx + 7)
        byu.append(playery - 5)

    def newdownbullet():
        bxd.append(playerx + 7)
        byd.append(playery + 25)

    def newleftbullet():
        bxl.append(playerx - 5)
        byl.append(playery + 7)

    def newrightbullet():
        bxr.append(playerx + 25)
        byr.append(playery + 7)

    ax = []
    ay = []

    ammox = []
    ammoy = []

    def newammo():
        ammox.append(randrange(1, 700))
        ammoy.append(randrange(1, 720))

    wallhealth = []
    wallx = []
    wally = []

    def newupwall():
        wallx.append(playerx)
        wally.append(playery-100)
        wallhealth.append(5)

    def newdownwall():
        wallx.append(playerx)
        wally.append(playery+100)
        wallhealth.append(5)
    
    def newleftwall():
        wallx.append(playerx-100)
        wally.append(playery)
        wallhealth.append(5)
    
    def newrightwall():
        wallx.append(playerx+100)
        wally.append(playery)
        wallhealth.append(5)

    def newalien():
        alrx = randrange(1, 700)
        alry = randrange(1, 700)

        more_less = randrange(0,10)
        if more_less < 5:
            alrx = randrange(1, 700)
            alry = randrange(1, 300)
        if more_less >= 5:
            alrx = randrange(100, 700)
            alry = randrange(500, 700)
            
        ax.append(alrx)
        ay.append(alry)

    def draw():
        pygame.draw.rect(screen, (0,0,0), (0,0,800,800))
        pygame.draw.rect(screen, (255,0,0), (300,300,200,200))
        if pcam == "u":
            screen.blit(playerup, (x,y,h,w))
        if pcam == "l":
            screen.blit(playerleft, (x,y,h,w))
        if pcam == "d":
            screen.blit(playerdown, (x,y,h,w))
        if pcam == "r":
            screen.blit(playerright, (x,y,h,w))
        
        if swordswing == True:
            screen.blit(pygame.transform.rotate(sword.swordImg, rotation), (playerx-5, playery+5))

        for i in range(len(ammox)):
            screen.blit(ammoc.ammoImg, (ammox[i], ammoy[i], ammoc.ammoh, ammoc.ammow))

        for i in range(len(ay)):
            screen.blit(alien.alienImg, (ax[i], ay[i], alien.ah, alien.aw))

        for i in range(len(wallx)):
            screen.blit(wall.wallImg, (wallx[i], wally[i], wall.wallw, wall.wallw))

        for i in range(len(byu)):
            pygame.draw.rect(screen, (255,255,255), (bxu[i], byu[i], bullet.h, bullet.w))

        for i in range(len(byd)):
            pygame.draw.rect(screen, (255,255,255), (bxd[i], byd[i], bullet.h, bullet.w))

        for i in range(len(byr)):
            pygame.draw.rect(screen, (255,255,255), (bxr[i], byr[i], bullet.h, bullet.w))

        for i in range(len(byl)):
            pygame.draw.rect(screen, (255,255,255), (bxl[i], byl[i], bullet.h, bullet.w))

        screen.blit(ammotext, ammotextrect)
        screen.blit(killtext, killtextrect)
        screen.blit(secstext, secstextrect)
        screen.blit(weaponstext, weaponstextrect)
        screen.blit(ultstext, ultstextrect)

        pygame.display.update()

    x = 700
    y = 700
    h = 20
    w = 20 
    playerx = x
    playery = y
    rotation = 0
    swordswing = False

    waitt = 0
    waittt = 0
    waitttt = 0
    pcam = "u"
    newalien()
    newammo()

    dwall = pygame.draw.rect(screen, (155,155,155), (0, 798, 800, 2), 0)
    uwall = pygame.draw.rect(screen, (155,155,155), (0, 0, 800, 2), 0)
    rwall = pygame.draw.rect(screen, (155,155,155), (798, 0, 2, 800), 0)
    lwall = pygame.draw.rect(screen, (155,155,155), (0, 000, 2, 800), 0)

    ammo = 5
    kill = 0
    secsalive = 0
    secs = 0
    mins = 0
    ult_power = 0
    maxaliensspawn = 5
    minaliensspawn = 1

    weapon = 1
    weapontext = "Melee"

    screen.blit(playerup, (x,y,h,w))

    go = True
    while go:

        font1 = pygame.font.SysFont('freesanbold.ttf', 30)

        ammotext = font1.render(f'Ammo : {ammo}', True, (0, 255, 0))
        ammotextrect = ammotext.get_rect()
        ammotextrect.topright = (750, 25)

        killtext = font1.render(f'Kills : {kill}', True, (0, 255, 0))
        killtextrect = killtext.get_rect()
        killtextrect.topleft = (50, 25)

        secstext = font1.render(f'Alive : {mins}:{secsalive}', True, (0, 255, 0))
        secstextrect = secstext.get_rect()
        secstextrect.topleft = (450, 25)

        weaponstext = font1.render(f'Weapon : {weapon}', True, (0, 255, 0))
        weaponstextrect = weaponstext.get_rect()
        weaponstextrect.topleft = (250, 25)

        ultstext = font1.render(f'Ultimate : {ult_power}    100 = Ready', True, (0, 255, 0))
        ultstextrect = ultstext.get_rect()
        ultstextrect.topleft = (50, 50)

        if waitt >= 0 and waitt != 500:
            waitt += 1
        if waittt != 50:
            waittt += 1
        if waitttt != 50:
            waitttt += 1
        secs += 1

        playerx = x
        playery = y
        playerrect = pygame.Rect(playerx,playery,20,20)

        for i in range(len(ammox)):
            if i >= len(ammox):
                break
            ammorect = pygame.Rect(ammox[i], ammoy[i], ammoc.ammoh, ammoc.ammow)

            if playerrect.colliderect(ammorect):
                ammo += 5
                ammox.pop(i)
                ammoy.pop(i)

        for i in range(len(ax)):
            if ax[i] < playerx - 10:
                ax[i] += 0.5
            if ax[i] > playerx - 10:
                ax[i] -= 0.5

        for i in range(len(ay)):
            if ay[i] < playery - 20:
                ay[i] += 0.5
            if ay[i] > playery - 20:
                ay[i] -= 0.5

        for ai in range(len(ay)):
            if ai >= len(ay):
                break
            alienrect = pygame.Rect(ax[ai], ay[ai], alien.aw, alien.ah)
            if alienrect.colliderect(playerrect):
                sys.exit()
            for i in range(len(byu)):
                byurect = pygame.Rect(bxu[i], byu[i], bullet.h, bullet.w)
                if byurect.colliderect(alienrect):
                    ax.pop(ai)
                    ay.pop(ai)
                    kill += 1



            for i in range(len(byd)):
                bydrect = pygame.Rect(bxd[i], byd[i], bullet.h, bullet.w)
                if bydrect.colliderect(alienrect):
                    ax.pop(ai)
                    ay.pop(ai)
                    kill += 1

            for i in range(len(byr)):
                byrrect = pygame.Rect(bxr[i], byr[i], bullet.h, bullet.w)
                if byrrect.colliderect(alienrect):
                    ax.pop(ai)
                    ay.pop(ai)
                    kill += 1

            for i in range(len(byl)):
                bylrect = pygame.Rect(bxl[i], byl[i], bullet.h, bullet.w)
                if bylrect.colliderect(alienrect):
                    ax.pop(ai)
                    ay.pop(ai)
                    kill += 1

        for i in range(len(wallx)):
            if i >= len(wallx):
                break
            for ai in range(len(ay)):
                if ai >= len(ay):
                    break
                wallrect = pygame.Rect(wallx[i], wally[i], wall.wallh, wall.wallw)
                alienrect = pygame.Rect(ax[ai], ay[ai], alien.ah, alien.aw)
                if alienrect.colliderect(playerrect):
                    sys.exit()
                if wallrect.colliderect(alienrect):
                    temphealth = wallhealth[i] - 1
                    if temphealth <= 0:
                        wallhealth.pop(i)
                    else:
                        wallhealth.insert(i, temphealth)





        for i in range(len(byu)):
            byu[i] -= 7
        for i in range(len(byd)):
            byd[i] += 7
        for i in range(len(bxr)):
            bxr[i] += 7
        for i in range(len(bxl)):
            bxl[i] -= 7





        for event in pygame.event.get():
            if event.type == pygame.QUIT : sys.exit()

        pr = pygame.key.get_pressed()

        if pr[pygame.K_1]: # range
            weapon = 1
        if pr[pygame.K_2]: # melee
            weapon = 2

        mouse_presses = pygame.mouse.get_pressed()

        #building a wall
        if mouse_presses[0] and waittt == 50:
            if pcam == "u":
                newupwall()
            if pcam == "d":
                newdownwall()
            if pcam == "r":
                newrightwall()
            if pcam == "l":
                newleftwall()

            waittt = 0



        #movement
        if pr[pygame.K_d] and not playerrect.colliderect(rwall):
            x += 5
            pcam = "r"
        if pr[pygame.K_a] and not playerrect.colliderect(lwall):
            x -= 5
            pcam = "l"
        if pr[pygame.K_w] and not playerrect.colliderect(uwall):
            y -= 5
            pcam = "u"
        if pr[pygame.K_s] and not playerrect.colliderect(dwall):
            y += 5
            pcam = "d"
        #lookdirection
        if pr[pygame.K_LEFT]:
            pcam = "l"
        if pr[pygame.K_RIGHT]:
            pcam = "r"
        if pr[pygame.K_DOWN]:
            pcam = "d"
        if pr[pygame.K_UP]:
            pcam = "u"


        if weapon == 2:
            if pr[pygame.K_SPACE] and rotation == 0:
                swordswing = True

        if swordswing == True:
            swordrect = pygame.Rect(playerx-10, playery+5, sword.swordh, sword.swordw)
            for ai in range(len(ay)):
                if ai >= len(ay):
                    break
                alienrect = pygame.Rect(ax[ai], ay[ai], alien.ah, alien.aw)
                if alienrect.colliderect(swordrect):
                    ax.pop(ai)
                    ay.pop(ai)
                    kill += 1
            rotation += 5

        if rotation == 180:
            swordswing = False
            rotation = 0

        if waitt == 500 and len(ax) < 10:
            if ult_power != 100:
                ult_power += 10

            for i in range(randrange(minaliensspawn,maxaliensspawn)):
                newalien()


            if ammo > 0:
                if randrange(1,4) == 2:
                    newammo()
            elif ammo == 0:
                newammo()
            waitt = 0



        if weapon == 1:
            if pr[pygame.K_SPACE] and waittt == 50 and ammo > 0:
                if pcam == "u":
                    newupbullet()
                if pcam == "d":
                    newdownbullet()
                if pcam == "r":
                    newrightbullet()
                if pcam == "l":
                    newleftbullet()
                ammo -= 1
                waittt = 0

        if secs == 50:
            secsalive += 1
            secs = 0

            if secsalive == 60:
                mins += 1
                secsalive = 0
                maxaliensspawn += 2
                minaliensspawn += 2

        if pr[pygame.K_u] and ult_power == 100:
            ult_power = 0
            ay.clear()
            ax.clear()


        draw()
        clock.tick(50)