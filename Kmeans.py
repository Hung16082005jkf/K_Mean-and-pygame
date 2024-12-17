# import package
import os
os.environ["SDL_AUDIODRIVER"] = "dummy"
import pygame
pygame.init()

from random import randint
import math
from sklearn.cluster import KMeans

#draw background
pygame.init()
screen=pygame.display.set_mode((1000,600))
run=True

# create color
GREY=(154,149,149)
BLACK=(0,0,0)
BLINK=(195,165,165)
WHITE=(255,255,255)
BLUE=(40,29,193)

YELLOW=(189,208,67)
GREEN=(84,202,55)
RED=(255,0,0)
TIM=(204,253,255)
GREY_1=(102,0,204)
ORIGIN=(255,153,52)
RED_STRONG=(153,0,76)
GREEN_STRONG=(0,102,102)
TIM_SMILE=(204,204,255)

# create list_color
COLOR=[YELLOW,GREEN,RED,TIM,GREY_1,ORIGIN,RED_STRONG,GREEN_STRONG,TIM_SMILE]

#create font text
font=pygame.font.SysFont("sans",50)
font_small=pygame.font.SysFont("sans",20)

#create text
text_1=font.render("K",True,BLACK)
text_2=font.render("=",True,BLACK)
text_4=font.render("run",True,WHITE)
text_5=font.render("random",True,WHITE)
text_6=font.render("eroll",True,WHITE)
text_7=font.render("algorithm",True,WHITE)
text_8=font.render("+",True,WHITE)
text_9=font.render("-",True,WHITE)
text_10=font.render("algorithm",True,WHITE)
text_11=font.render("reset",True,WHITE)

#create list rỗng
points=[]
erolll=0
k=0
clutters=[]
colors=[]
longs=[]
labels=[]
clutters_new=[]

# create funtion_name is long
def long(a,b,c,d):
    long_1=math.sqrt((a-b)**2+(c-d)**2)
    return long_1

while run:

    screen.fill(GREY)

    #draw parner
    pygame.draw.rect(screen,BLACK,(50,50,610,360)) 
    pygame.draw.rect(screen,BLINK,(55,55,600,350))

    #draw Control button
    pygame.draw.rect(screen,BLACK,(700,50,50,50)) # +
    pygame.draw.rect(screen,BLACK,(800,50,50,50)) # -
    pygame.draw.rect(screen,BLACK,(700,140,150,50)) # run
    pygame.draw.rect(screen,BLACK,(700,220,150,50)) # random
    pygame.draw.rect(screen,BLACK,(700,400,170,50)) # algorithm
    pygame.draw.rect(screen,BLACK,(700,480,150,50)) # reset
    pygame.draw.rect(screen,BLACK,(695,295,220,70))#eroll
    pygame.draw.rect(screen,GREY,(700,300,210,60))#eroll

    mouse_x,mouse_y=pygame.mouse.get_pos()
    # create logic control
    for event in pygame.event.get():
        #button quit
        if event.type == pygame.QUIT:
            run=False
        #button mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #button +
                if 700<mouse_x<750 and 50<mouse_y<100:
                    k=k+1 
                #button -  
                if 800<mouse_x<850 and 50<mouse_y<100:
                    k=k-1
                #button run
                if 700<mouse_x<850 and 140<mouse_y<190:
                    clutters_new=[]
                    labels=[]
                    if clutters == []:
                        continue
                    for i in range(len(points)):
                        longs=[]
                        for x in range(len(clutters)):
                            n=long(points[i][0],clutters[x][0],points[i][1],clutters[x][1])
                            longs.append(n)
                        label=min(longs)
                        vi_tri=longs.index(label)
                        labels.append(vi_tri)
                    for i in range(k):
                        sum_x=0
                        sum_y=0
                        count=0
                        for m in range(len(points)):
                            if labels[m] == i:
                                sum_x+=points[m][0]
                                sum_y+=points[m][1]
                                count+=1
                        if count!=0:
                            clutters_new.append([sum_x/count,sum_y/count])

                #button random
                if 700<mouse_x<850 and 220<mouse_y<270:
                    labels=[]
                    clutters_new=[]
                    clutters=[]
                    for i in range(k):
                        clutter=[randint(50,660),randint(50,410)]
                        clutters.append(clutter)

                #button algorithm nút này đang bị lỗi em chưa fix được ai giúp em với ạ
                if 700<mouse_x<870 and 400<mouse_y<450:
                    kmeans=KMeans(n_clusters=k).fit(points)
                    # print(kmeans.cluster_centers_)
                    clutters=kmeans.cluster_centers_
                    print("algorithm")
                    print(clutters)

                #button reset
                if 700<mouse_x<850 and 480<mouse_y<530:
                    points=[]
                    k=0
                    erolll=0
                    clutters=[]
                    
                #button points in parner
                if 55<mouse_x<655 and 55<mouse_y<405:
                    labels=[]
                    point=[mouse_x,mouse_y]
                    points.append(point)
                try:
                    #button eroll
                    if 695<mouse_x<915 and 295<mouse_y<365:
                        erolll=0
                        if clutters != [] and labels != []:
                            for i in range(len(points)):
                                erolll+=long(points[i][0],clutters[labels[i]][0],points[i][1],clutters[labels[i]][1])
                except:
                    continue
    #draw points in parner   
    for i in range(len(points)):
        pygame.draw.circle(screen,BLUE,(points[i][0],points[i][1]),5)
        if labels == []: 
            pygame.draw.circle(screen,BLINK,(points[i][0],points[i][1]),4)
        else:
            pygame.draw.circle(screen,COLOR[labels[i]],(points[i][0],points[i][1]),4)

    if 55<mouse_x<655 and 55<mouse_y<405:
        text_12=font_small.render("(" + str(mouse_x) + ":" + str(mouse_y) + ")",True,BLACK)
        screen.blit(text_12,(mouse_x+10,mouse_y))     
    # draw clutters
    for i in range(len(clutters)):
        if clutters_new == []:
            pygame.draw.circle(screen,COLOR[i],(clutters[i][0],clutters[i][1]),10)
        else:
            for l in range(len(clutters_new)):
                pygame.draw.circle(screen,COLOR[l],(int(clutters_new[l][0]),int(clutters_new[l][1])),10)

    text_3=font.render(str(k),True,BLACK)

    #draw text
    screen.blit(text_1,(880,47))
    screen.blit(text_2,(910,50))
    screen.blit(text_3,(940,47))
    screen.blit(text_4,(720,140))
    screen.blit(text_5,(710,220))
    screen.blit(text_8,(720,50))
    screen.blit(text_9,(800,50))
    screen.blit(text_6,(700,300))
    screen.blit(text_2,(780,300))
    screen.blit(text_10,(700,400))
    screen.blit(text_11,(700,480))
    text_13=font.render(str(int(erolll)),True,BLACK)
    screen.blit(text_13,(810,300))
    pygame.display.flip()
pygame.quit()

