import global_variables as gv
import button
from global_variables import *

videos_b = button.Button_game("../WRO/src/img/btn-video.png"," ",40,100,color1= (0,0,0),color2=(0,0,0))
tutoriales_b = button.Button_game("../WRO/src/img/Tutoriales.png"," ",40,300,color1= (0,0,0),color2=(0,0,0))
demo_b = button.Button_game("../WRO/src/img/Boton_demo.png"," ",40,500,color1= (0,0,0),color2=(0,0,0))

logo_img = pygame.image.load("../WRO/src/img/Bit-12.png")
logo_rec = pygame.Surface.get_rect(logo_img, topleft = (1250, 100),)

Fundes_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/Fundesteam.png"), (200,200))
Fundes_rec = pygame.Surface.get_rect(Fundes_img, topleft = (20, 850),)

Mincyt_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/Mincyt.png"), (268,181))
Mincyt_rec = pygame.Surface.get_rect(Mincyt_img, topleft = (220, 875),)


Earth_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/Earth.png"), (191,133))
Earth_rec = pygame.Surface.get_rect(Mincyt_img, topleft = (520, 900),)

Semilleros_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/Semilleros.png"), (195,178))
Semilleros_rec = pygame.Surface.get_rect(Mincyt_img, topleft = (770, 860),)

wro2_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/wro2.png"), (277,81))
wro2_rec = pygame.Surface.get_rect(Mincyt_img, topleft = (1000, 950),)


status_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/status.png"), (225,924))
status_rec = pygame.Surface.get_rect(Fundes_img, topleft = (1450, 50),)


rect_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/rect.png"), (118,76))
rect_rec = pygame.Surface.get_rect(rect_img, topleft = (1700, 40),)

rect2_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/rect.png"), (118,76))
rect2_rec = pygame.Surface.get_rect(rect2_img, topleft = (1700, 40 + 86),)


rect3_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/rect.png"), (118,76))
rect3_rec = pygame.Surface.get_rect(rect3_img, topleft = (1700, 40 + 86 * 2),)

rect4_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/rect.png"), (118,76))
rect4_rec = pygame.Surface.get_rect(rect4_img, topleft = (1700, 40 + 86 * 3),)


rect5_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/rect.png"), (118,76))
rect5_rec = pygame.Surface.get_rect(rect5_img, topleft = (1700, 40 + 86 * 4),)

rect6_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/rect.png"), (118,76))
rect6_rec = pygame.Surface.get_rect(rect6_img, topleft = (1700, 40 + 86 * 5),)


rect7_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/rect.png"), (118,76))
rect7_rec = pygame.Surface.get_rect(rect7_img, topleft = (1700, 40 + 86 * 6),)

rect8_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/rect.png"), (118,76))
rect8_rec = pygame.Surface.get_rect(rect8_img, topleft = (1700, 40 + 86 * 7),)


rect9_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/rect.png"), (118,76))
rect9_rec = pygame.Surface.get_rect(rect9_img, topleft = (1700, 40 + 86 * 8),)

rect10_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/rect.png"), (118,76))
rect10_rec = pygame.Surface.get_rect(rect10_img, topleft = (1700, 40 + 86 * 9),)


rect11_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/rect.png"), (118,76))
rect11_rec = pygame.Surface.get_rect(rect11_img, topleft = (1700, 40 + 86 * 10),)

volver_b = button.Button_game("../WRO/src/img/volver.png", "", 40, 300)
volver2_b = button.Button_game("../WRO/src/img/volver.png", "", 40, 300)

reiniciar_b = button.Button_game("../WRO/src/img/reiniciar.png", "", 40, 150)


Tuto_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/Tuto.png"), (444,140))
Tuto_rec = pygame.Surface.get_rect(Fundes_img, topleft = (725, 50),)

demobut_img = pygame.transform.scale(pygame.image.load("../WRO/src/img/demobut.png"), (462,135))
demobut_rec = pygame.Surface.get_rect(Fundes_img, topleft = (750, 50),)

Tutobut = button.Button_game("../WRO/src/img/Tutobut.png", "",50, 400)

Tutobut1 =  button.Button_game("../WRO/src/img/Tutobut1.png", "", 50, 250)

Tutobut2 = button.Button_game("../WRO/src/img/Tutobut2.png", "", 50, 550)

Tutobut3 = button.Button_game("../WRO/src/img/Tutobut3.png", "", 50, 700)

Pause_b = button.Button_game("../WRO/src/img/Pause.png", "", 1060, 900)

video_img = pygame.image.load("../WRO/src/img/video.png")
video_rec = pygame.Surface.get_rect(Fundes_img, topleft = (650, 250),)

tutorial = False
demo = False
menu = True
cosechar = False
operacion = False
consumibles = False

def mostrar_indicadores():
    screen.blit(rect_img,rect_rec)
    screen.blit(rect2_img,rect2_rec)
    screen.blit(rect3_img,rect3_rec)
    screen.blit(rect4_img,rect4_rec)
    screen.blit(rect5_img,rect5_rec)
    screen.blit(rect6_img,rect6_rec)
    screen.blit(rect7_img,rect7_rec)
    screen.blit(rect8_img,rect8_rec)
    screen.blit(rect9_img,rect9_rec)
    screen.blit(rect10_img,rect10_rec)
    screen.blit(rect11_img,rect11_rec)
def menu_principal():
    global tutorial,menu, demo
    screen.blit(logo_img,logo_rec)
    screen.blit(Fundes_img,Fundes_rec)
    screen.blit(Mincyt_img,Mincyt_rec)
    screen.blit(Earth_img,Earth_rec)
    screen.blit(Semilleros_img,Semilleros_rec)
    screen.blit(wro2_img,wro2_rec)


    demo_b.draw()
    demo_b.btn_is_press()
    tutoriales_b.draw()
    tutoriales_b.btn_is_press()
    videos_b.draw()
    videos_b.btn_is_press()
    if demo_b.click:
        menu = False
        tutorial = False
        demo = True
    # dibujando y comprobando el evento click en el boton video 

    elif tutoriales_b.click:
        menu = False
        tutorial = True
        demo = False
    # dibujan do y comprobando el evento click en el boton video 

    elif videos_b.click:
        screen.fill((187,225,90))

def demoi():
    global menu,demo,tutorial
    screen.blit(status_img,status_rec)
    mostrar_indicadores()
    screen.blit(demobut_img,demobut_rec)
    volver_b.draw()
    volver_b.btn_is_press()
    reiniciar_b.draw()
    reiniciar_b.btn_is_press()
    if volver_b.click:
        menu = True
        demo = False
        tutorial = False
    if reiniciar_b.click:
        pass
def tutoriales():
    global menu,demo,tutorial
    screen.blit(video_img,video_rec)
    Tutobut1.draw()
    Tutobut1.btn_is_press()
    Tutobut.draw()
    Tutobut.btn_is_press()
    Tutobut2.draw()
    Tutobut2.btn_is_press()
    Tutobut3.draw()
    Tutobut3.btn_is_press()
    Pause_b.draw()
    Pause_b.btn_is_press()
    if Tutobut1.click:
        menu = True
        demo = False
        tutorial = False
    if Tutobut.click:
        pass
    if Tutobut2.click:
        pass
    if Tutobut3.click:
        pass
    if Pause_b.click:
        pass

while gv.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gv.running = False

    screen.fill((176,186,185))
    if menu:
        menu_principal()
        
    elif tutorial:
        tutoriales()
    elif demo:
        demoi()    
    
    pygame.display.flip()
pygame.quit()