#Samuel Shofowora
#This class was made to allow the user to momentarily stop the game at their own command.
class Pause():
    paused = True
    def __init__(self):
        self.K_c = K_c
        self.K_p = K_p

    def screentext(self, msg, color):
        screen_text = font.render(msg, True, color)
        window.blit(screen_text, [400,400])
        
    def pause(self):
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.self.K_c:
                        paused = False
                    elif event.key == pygame.self.K_p:
                        pygame.quit()
                        quit()
            window.fill(white)
            self.screentext("Paused",
                            black,
                            -100,
                            size="large")
            self.screentext("Press C to continue or P to quit",
                            black,
                            25)
            pygame.display.update()
            clock.tick(15)
