from global_variables import *
class Button_game:
    def __init__(self,img, title="", x=0, y=0, xt=0, yt=0, color1 =(255,255,255), color2=(255,255,255), size=16):
        # Button label
        self.color1 = color1
        self.color2 = color2
        self.title = title
        self.xt = xt
        self.yt = yt
        self.click = False
        self.size = size

        self.X_POS = x
        self.Y_POS = y
        self.img = img
        self.btn_surf = pygame.image.load(self.img)
        self.BTN_RECT = pygame.Surface.get_rect(self.btn_surf, topleft =(self.X_POS,self.Y_POS))
    # Function to create dynamic text

    
    def btn_is_press(self):
        self.mouse = pygame.mouse.get_pressed(num_buttons=3)
        self.click = False
        if self.BTN_RECT.collidepoint(pygame.mouse.get_pos()) and self.mouse[0]:
            self.click = True
        else:
            self.click = False

    def draw(self):
        global screen
        screen.blit(self.btn_surf, self.BTN_RECT)
