#Jonathan Salmon

#This class handles the initilization of pygame along with the drawing of all sprites
#and all nessecary calls to other calsses and functions in order to combine all classes
#and functions together to create a working game

import sys, pygame

import map, camera, player, timer, finish, dijkstras, LinearSearch

from image_loader import load_image

from pygame.locals import *

engine = []
wheel = []
gearbox = []
breakpedal = []
steeringwheel = []

enginelocationX = []
enginelocationY = []

carlocation = []

dijkstras = dijkstras.Graph()

#Main Game Loop
def main():
#Initialize objects
    clock = pygame.time.Clock()
    quit = False
    font = pygame.font.Font(None, 24)
    car = player.Player()
    cam = camera.Camera()
    timer.initialize()
    aim = timer.Finish()
    linear = LinearSearch.LinearSearch()

    #load different numbers of a class and save them as listvariables for
    # iteration over within the while loop
    engine = [timer.Engine() for i in range (0,2)]
    wheel = [timer.Wheels() for i in range (0,8)]
    steeringwheel = [timer.SteeringWheel() for i in range (0,3)]
    gearbox = [timer.Gearbox() for i in range (0,3)]
    breakpedal = [timer.BreakPedal() for i in range (0,5)]

    finish1 = finish.Alert()

    #Set sprite groups for different items
    map1 = pygame.sprite.Group()
    player1 = pygame.sprite.Group()
    engines = pygame.sprite.Group()
    wheels = pygame.sprite.Group()
    steeringwheels = pygame.sprite.Group()
    gearboxes = pygame.sprite.Group()
    breakpedals = pygame.sprite.Group()

    timeout = pygame.sprite.Group()

    #generate tiles
    for tile_num in range (0, len(map.map_tiles)):
        map.map_files.append(load_image(map.map_tiles[tile_num], False))
    for x in range (0, 24):
        for y in range (0, 24):
            map1.add(map.Map(map.map_1[x][y], x * 400, y * 400))


    #Add items to the map with the same number of items as classes created previously
    for i in range (0,2):
        engines.add(engine[i])
        enginelocationX.append(engine[i].returnEngineX())
        enginelocationY.append(engine[i].returnEngineY())

    for i in range (0,8):
        wheels.add(wheel[i])

    for i in range (0,3):
        steeringwheels.add(steeringwheel[i])

    for i in range (0,3):
        gearboxes.add(gearbox[i])

    for i in range (0,5):
        breakpedals.add(breakpedal[i])

    timeout.add(finish1)

    player1.add(car)

    cam.set_pos(car.x, car.y)

    aim.ReverseInsertionSort()

    while not quit:

        closestengine = dijkstras.addnodes(enginelocationX,enginelocationY,int(car.x + 700),int(car.y + 600))
        dijkstras.clearnodes()


    #Check for menu/reset, (keyup event - trigger ONCE)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if (keys[K_q]):
                    pygame.quit()
                    sys.exit(0)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit = True
                break

    #Check for key input. (KEYDOWN, trigger often)
        keys = pygame.key.get_pressed()
        #if (target.timeleft > 0):
        if keys[K_LEFT]:
            car.steerleft()
        if keys[K_RIGHT]:
            car.steerright()
        if keys[K_UP]:
            car.accelerate()
        else:
            car.soften()
        if keys[K_DOWN]:
            car.deaccelerate()

        cam.set_pos(car.x, car.y)



        #Show text data.
        text_fps = font.render('FPS: ' + str(int(clock.get_fps())), 1, (224, 16, 16))
        textpos_fps = text_fps.get_rect(centery=25, centerx=60)

        text_score = font.render('Score: ' + str(aim.score), 1, (224, 16, 16))
        textpos_score = text_fps.get_rect(centery=45, centerx=60)

        text_timer = font.render('Timer: ' + str(int((aim.timeleft / 60)/60)) + ":" + str(int((aim.timeleft / 60) % 60)), 1, (224, 16, 16))
        textpos_timer = text_fps.get_rect(centery=65, centerx=60)

        text_first = font.render(str(aim.first), 1, (255,255,255))
        textpos_first = text_fps.get_rect(centery=150, centerx=60)

        text_second = font.render(str(aim.second), 1, (255,255,255))
        textpos_second = text_fps.get_rect(centery=170, centerx=60)

        text_third = font.render(str(aim.third), 1, (255,255,255))
        textpos_third = text_fps.get_rect(centery=190, centerx=60)

        text_fourth = font.render(str(aim.fourth), 1, (255,255,255))
        textpos_fourth = text_fps.get_rect(centery=210, centerx=60)

        text_fith = font.render(str(aim.fith), 1, (255,255,255))
        textpos_fith = text_fps.get_rect(centery=230, centerx=60)

        text_closestengine = font.render("The Closest Engine is: " +linear.linearSearch(list(closestengine[1]), "point1") + " which is " + str(closestengine[0]) + " units from you", 1, (255,255,255))
        textpos_closestengine = text_fps.get_rect(centery = 350, centerx=60)

        linear.reset()

        #Render Scene.
        window.blit(background, (0,0))

        map1.update(cam.x, cam.y)
        map1.draw(window)

        car.grass(window.get_at(((CENTER_W + 25, CENTER_H + 50))).g)

        aim.ReverseInsertionSort()

        player1.update(cam.x, cam.y)
        player1.draw(window)


#Check for collision between the car and all the items placed on the map
#if collision has occured then replace the item in a new location and run reverse insetion sort
        for i in range (0,2):
            engine[i].update(cam.x, cam.y)
            if pygame.sprite.spritecollide(car, engines, True):
                engine[i].claim_item()
                engine[i].generate_finish()
                enginelocationX[i] = engine[i].returnEngineX()
                enginelocationY[i] = engine[i].returnEngineY()
                engine[i].add(engines)
                aim.ReverseInsertionSort()


        for i in range (0,8):
            wheel[i].update(cam.x, cam.y)
            if pygame.sprite.spritecollide(car, wheels, True):
                wheel[i].claim_item()
                wheel[i].generate_finish()
                wheel[i].add(wheels)
                aim.ReverseInsertionSort()

        for i in range (0,3):
            gearbox[i].update(cam.x, cam.y)
            if pygame.sprite.spritecollide(car, gearboxes, True):
                gearbox[i].claim_item()
                gearbox[i].generate_finish()
                gearbox[i].add(gearboxes)
                aim.ReverseInsertionSort()

        for i in range (0,3):
            steeringwheel[i].update(cam.x, cam.y)
            if pygame.sprite.spritecollide(car, steeringwheels, True):
                steeringwheel[i].claim_item()
                steeringwheel[i].generate_finish()
                steeringwheel[i].add(steeringwheels)
                aim.ReverseInsertionSort()

        for i in range (0,5):
            breakpedal[i].update(cam.x, cam.y)
            if pygame.sprite.spritecollide(car, breakpedals, True):
                breakpedal[i].claim_item()
                breakpedal[i].generate_finish()
                breakpedal[i].add(breakpedals)
                aim.ReverseInsertionSort()


#Draw all sprite groups onto window
        engines.draw(window)
        wheels.draw(window)
        gearboxes.draw(window)
        steeringwheels.draw(window)
        breakpedals.draw(window)


#If timer runs down to 0, reposition all text and run bubblesort on the information to reorder and reorganise
        if (aim.timeleft == 0):
            timeout.draw(window)
            car.speed = 0
            font = pygame.font.Font(None, 42)
            text_score = font.render('Final Score: ' + str(aim.score), 1, (224, 16, 16))
            textpos_score = text_fps.get_rect(centery=CENTER_H/2+200, centerx=CENTER_W-60)
            textpos_first = text_fps.get_rect(centery=CENTER_H/2+250, centerx=CENTER_W-40)
            textpos_second = text_fps.get_rect(centery=CENTER_H/2+280, centerx=CENTER_W-40)
            textpos_third = text_fps.get_rect(centery=CENTER_H/2+310, centerx=CENTER_W-40)
            textpos_fourth = text_fps.get_rect(centery=CENTER_H/2+340, centerx=CENTER_W-40)
            textpos_fith = text_fps.get_rect(centery=CENTER_H/2+370, centerx=CENTER_W-40)
            aim.bubblesort()


#Render the text onto the screen using predefined variables for content and position
        font = pygame.font.Font(None, 24)
        window.blit(text_fps, textpos_fps)
        window.blit(text_score, textpos_score)
        window.blit(text_timer, textpos_timer)
        window.blit(text_first, textpos_first)
        window.blit(text_second, textpos_second)
        window.blit(text_third, textpos_third)
        window.blit(text_fourth, textpos_fourth)
        window.blit(text_fith, textpos_fith)
        window.blit(text_closestengine, textpos_closestengine)
        pygame.display.flip()

        aim.update()

        clock.tick(64)













#Initialise pygame and window properties, along with entering the main game loop
pygame.init()

window = pygame.display.set_mode((pygame.display.Info().current_w,
                                  pygame.display.Info().current_h),
                                  pygame.FULLSCREEN)

pygame.mouse.set_visible(False)
font = pygame.font.Font(None, 24)

CENTER_W =  int(pygame.display.Info().current_w /2)
CENTER_H =  int(pygame.display.Info().current_h /2)

#new background surface
background = pygame.Surface(window.get_size())
background = background.convert_alpha()
background.fill((26, 26, 26))

#Enter the mainloop.
main()

pygame.quit()
sys.exit(0)