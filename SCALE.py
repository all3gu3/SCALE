import pygame, sys, random, math, time
C1x=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
C1y=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
c1w=20
C2x=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
C2y=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
c2w=9

#Llena de 'miles' los espacios para rellenar después
def inicializaMatrices():
    for i in range (0,21):
        for j in range (0,25):
            C1x[i].append(1000)
            C1y[i].append(1000)
            C2x[i].append(1000)
            C2y[i].append(1000)
            
#PINTA CUADRITO AMARILLO EN LA POSICIÓN INDICADA#
def pintaCuadritoA(xi,yi):#Recibo la coordenada del cuadrito que quiero pintar
    pygame.draw.rect(screen,  (249,231,159) , (C1x[xi][yi],C1y[xi][yi],c1w,c1w))

#PINTA CUADRITO ROSA EN LA POSICIÓN INDICADA#
def pintaCuadritoR(xi,yi):#Recibo la coordenada del cuadrito que quiero pintar
    pygame.draw.rect(screen, (245,183,177) , (C1x[xi][yi],C1y[xi][yi],c1w,c1w))
    
#PINTA CUADRITO MINI AZUL EN LA POSICIÓN INDICADA#
def pintaCuadritoB(xi,yi):#Recibo la coordenada del cuadrito que quiero pintar
    pygame.draw.rect(screen,  (174,214,241) , (C2x[xi][yi],C2y[xi][yi],c2w,c2w))

#PINTA CUADRITO MINI VERDE EN LA POSICIÓN INDICADA#
def pintaCuadritoV(xi,yi):#Recibo la coordenada del cuadrito que quiero pintar
    pygame.draw.rect(screen, (204,241,174) , (C2x[xi][yi],C2y[xi][yi],c2w,c2w))

########################################################################
                    #DIBUJA FIGURAS EN EL TABLERO#
########################################################################
#PINTA RECTAGULO DE LAS MEDIDAS INDICADAS#
def pintaRectangulo1(xi,yi):#Recibo medidas del cuadrito que quiero pintar
    nav=20-yi
    for n in range (1,xi+1):
        for m in range (nav,21):
            pintaCuadritoA(n,m)

#PINTA RECTANGULO MINI DE LAS MEDIDAS INDICADAS#
def pintaRectangulo2(xi,yi):#Recibo medidas del cuadrito que quiero pintar
    nav=20-yi
    for n in range (1,xi+1):
        for m in range (nav,21):
            pintaCuadritoV(n,m)

#PINTA RAYA HORIZONTAL DE LA MEDIDA INDICADA#
def pintaRayaH(xi,yi):#Recibo el largo de la raya que quiero pintar
    nav=20-yi
    m=1
    for n in range (1,xi+1):
        pintaCuadritoR(n,18)

#PINTA RAYA VERTICAL DE LA MEDIDA INDICADA#
def pintaRayaV(xi,yi):#Recibo el largo de la raya que quiero pintar
    nav=20-yi
    for m in range (nav,21):
            pintaCuadritoR(1,m)
        
########################################################################
                        #DIBUJA LOS TABLEROS#
########################################################################
def dibujaCuadro1():
    pygame.draw.rect(screen, (97,106,107), (275,100,512,457))
    pygame.draw.rect(screen, (23,165,137), (272,97,512,462),7)
    x=1
    y=1
    for i in range (105,550,25):#Recorre en y
        for j in range (280,775,25):#Dibuja una línea de cuadritos en x
            pygame.draw.rect(screen, (169,223,191), (j,i,20,20))
            C1x[x][y]=j
            C1y[x][y]=i
            x+=1
        y+=1
        x=1
            

def dibujaCuadro2():
    pygame.draw.rect(screen, (97,106,107), (15,100,225,225))
    pygame.draw.rect(screen, (155,89,182), (13,97,230,230),7)
    x=1
    y=1
    for i in range (103,315,11):#Recorre en y
        for j in range (19,235,11):#Dibuja una línea de cuadritos en x
            pygame.draw.rect(screen, (215,189,216), (j,i,9,9))
            C2x[x][y]=j
            C2y[x][y]=i
            x+=1
        y+=1
        x=1
        
#############################################################
#############################################################
        
pygame.init()
screen = pygame.display.set_mode((800,600))
calibriFont = pygame.font.SysFont("Calibri", 20)
#############################
## DECLARACION DE IMAGENES ##
#############################
L1 = pygame.image.load("L1.png")
L1 = pygame.transform.scale(L1, (200,50))

L2 = pygame.image.load("L2.png")
L2 = pygame.transform.scale(L2, (200,50))

T1 = pygame.image.load("T1.png")
T1 = pygame.transform.scale(T1, (180,60))

sc = pygame.image.load("sc.png")
sc = pygame.transform.scale(sc, (200,60))

B1 = pygame.image.load("B1.png")
B1 = pygame.transform.scale(B1, (60,30))

N1 = pygame.image.load("N1.png")
N1 = pygame.transform.scale(N1, (130,65))

N2 = pygame.image.load("N2.png")
N2 = pygame.transform.scale(N2, (130,65))

N3 = pygame.image.load("N3.png")
N3 = pygame.transform.scale(N3, (130,65))

B3 = pygame.image.load("B3.png")
B3 = pygame.transform.scale(B3, (60,30))

plus = pygame.image.load("plus.png")
plus = pygame.transform.scale(plus, (20,20))

minus = pygame.image.load("minus.png")
minus = pygame.transform.scale(minus, (20,20))

plus2 = pygame.image.load("plus.png")
plus2 = pygame.transform.scale(plus2, (20,20))

minus2 = pygame.image.load("minus.png")
minus2 = pygame.transform.scale(minus2, (20,20))

ask = pygame.image.load("ask.png")
ask = pygame.transform.scale(ask, (20,20))
##############################################################
##############################################################

inicializaMatrices()
A=random.randint(1,3)
B=random.randint(1,3)
C=1
D=1
E=random.randint(1,3)
F=random.randint(1,3)
nivel=1
fin=0
puntos=0
fallidos=0
mal=0
tiempo=0
tiempo1=0
tiempo2=0
tiempo3=0
mal1=0
mal2=time.time()
preg=0
preg2=0
preg3=0
pregunta=0

###############################################################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            x, y = pygame.mouse.get_pos()
            if((x>=15 and x<=75) and (y>=520 and y<=550)):
                fin=1
        #CONTROLADORES DEL LARGO
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            x, y = pygame.mouse.get_pos()
            if((x>=205 and x<=225) and (y>=420 and y<=440)):
                C+=1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            x, y = pygame.mouse.get_pos()
            if((x>=230 and x<=250) and (y>=420 and y<=440)):
                C-=1
        ############################################################
        #CONTROLADORES DEL LARGO
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            x, y = pygame.mouse.get_pos()
            if((x>=205 and x<=225) and (y>=450 and y<=470)):
                D+=1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            x, y = pygame.mouse.get_pos()
            if((x>=230 and x<=250) and (y>=450 and y<=470)):
                D-=1
        ############################################################
        #REVISA LOS ACIERTOS DEL USUARIO AL PRESIONAR 'LISTO'
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            x, y = pygame.mouse.get_pos()
            if((x>=15 and x<=75) and (y>=485 and y<=515)):
                if(C==A*E and D==B*F):
                    puntos+=1
                    A=random.randint(1,5)
                    B=random.randint(1,5)
            else:
                mal=1
                mal2=mal1+2
        ############################################################
        #VERIFICA EL NIVEL
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            x, y = pygame.mouse.get_pos()
            if((x>=100 and x<=143) and (y>=520 and y<=550)):
                A=random.randint(1,3)
                B=random.randint(1,3)
                C=1
                D=1
                E=random.randint(1,3)
                F=random.randint(1,3)
                nivel=1
            if((x>=144 and x<=187) and (y>=520 and y<=550)):
                A=random.randint(2,4)
                B=random.randint(2,4)
                C=1
                D=1
                E=random.randint(2,3)
                F=random.randint(2,3)
                nivel=2
            if((x>=188 and x<=230) and (y>=520 and y<=550)):
                A=random.randint(3,4)
                B=random.randint(3,4)
                C=1
                D=1
                E=random.randint(2,4)
                F=random.randint(2,4)
                nivel=3
    ###################################################################3
    if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            x, y = pygame.mouse.get_pos()
            if((x>=0 and x<=20) and (y>=0 and y<=20)):
                pregunta=1
                preg=time.time()
                preg+=4
                preg2=preg+5
                preg3=preg2+5
                

    
    screen.fill((46,64,83))
    ################################
    #https://docs.google.com/presentation/d/1eQullB03oYCixB9fXDZoVDx5WclRRz0zR_Do7QFZcTA/edit#slide=id.g62760ffc8d_0_82
    screen.blit(L1, (10,350))#Imagen
    screen.blit(L2, (10,420))#Imagen
    screen.blit(sc, (30,20))#Imagen
    screen.blit(T1, (430,10))#Imagen
    screen.blit(B1, (15,485))#Imagen
    screen.blit(B3, (15,520))#Imagen
    screen.blit(plus, (205,420))#Imagen
    screen.blit(plus2, (205,450))#Imagen
    screen.blit(minus, (230,420))#Imagen
    screen.blit(minus2, (230,450))#Imagen
    if(nivel==1):
        screen.blit(N1,(100,485))
    elif(nivel==2):
        screen.blit(N2,(100,485))
    elif(nivel==3):
        screen.blit(N3,(100,485))
    #####################################################################
    # DECLARACIÓN DE ETIQUETAS
    #####################################################################
    n1 = calibriFont.render(str(A), 1, (174, 178, 241),(20,20,20))
    n2 = calibriFont.render(str(B), 1, (174, 178, 241),(20,20,20))
    n3 = calibriFont.render(str(C), 1, (174, 178, 241),(20,20,20))
    n4 = calibriFont.render(str(D), 1, (174, 178, 241),(20,20,20))
    escala=(str(E)+"L,"+ str(F)+"A")
    n5 = calibriFont.render(escala, 1, (174, 178, 241),(20,20,20))
    n6 = calibriFont.render("Te has equivocado calculando las medidas de tu figura!", 1, (174, 178, 241),(20,20,20))
    elPuntaje=("Puntos: "+str(puntos))
    n7 = calibriFont.render(elPuntaje, 1, (174, 178, 241),(20,20,20))
    n8 = calibriFont.render("Este es SCALE, un juego de escalas. Debes dibujar figuras agregando bloques...", 1, (174, 178, 241),(20,20,20))
    n9 = calibriFont.render("Arriba, en 'ESCALA', dice por cuanto multiplicar el Largo y Ancho de la figura original.", 1, (174, 178, 241),(20,20,20))
    n10 = calibriFont.render("Cuando lo logres, presiona 'LISTO'. En el nivel 1, guíate con los cuadritos rojos  ", 1, (174, 178, 241),(20,20,20))
    #####################################################################
    screen.blit(n1, (150, 350))
    screen.blit(n2, (150, 380))
    screen.blit(n3, (175, 420))
    screen.blit(n4, (175, 450))
    screen.blit(n5, (170, 35))
    mal1=time.time()
    screen.blit(n7, (300, 35))
    if(pregunta==1 and mal1<preg) :
        screen.blit(n8,(15,570))
    elif(pregunta==1 and mal1<preg2):
        screen.blit(n9,(15,570))
    elif(pregunta==1 and mal1<preg3):
        screen.blit(n10,(15,570))
    #####################################################################
    #PINTA TABLEROS POR DEFECTO
    dibujaCuadro1()
    dibujaCuadro2()
    #PINTA LÍNEAS DE AYUDA
    if(nivel==1):
        pintaRayaV(1,(B*F)+1)
        pintaRayaH(A*E,1)
    #####################################################################
    #PINTA LAS FIGURAS CON MEDIDAS VARIABLES
    pintaRectangulo2(A,B-1)
    pintaRectangulo1(C,D+1)
    #####################################################################
    #PINTA EL ÍCONO DE INFORMACIÓN
    screen.blit(ask, (0, 0))
    
    
    pygame.display.flip()


