import pygame
from random import randint
pygame.init()
screen=pygame.display.set_mode((400,650))
pygame.display.set_caption('flappy bird')
FPS=60
clock=pygame.time.Clock()
x_bird=50
y_bird=250
tube1_x=400
tube2_x=600
tube3_x=800
road_x=0

tube_width=50
tube1_height=randint(100,400)
tube2_height=randint(100,400)
tube3_height=randint(100,400)
d_2tube=150
bird_dord_velocity=0
gravity=0.5
tube_volocity=2
score=0
high_score =0
font=pygame.font.Font('04B_19.ttf',40)
font1=pygame.font.SysFont('sys',35)
tube1_pass=False
tube2_pass=False
tube3_pass=False
backgroud_img=pygame.image.load('background.png')
backgroud_img=pygame.transform.scale(backgroud_img,(400,600))
road_img=pygame.image.load('road.jpg')
road_img=pygame.transform.scale(road_img,(400,90))
button_img=pygame.image.load('playbtn.png')
button_img=pygame.transform.scale(button_img,(100,82))
menu_img =pygame.image.load('menu_icon.jpg')
menu_img=pygame.transform.scale(menu_img,(30,30))
flappybird_img=pygame.image.load('flappybird.png')
flappybird_img=pygame.transform.scale(flappybird_img,(350,200))

bird_img=pygame.image.load('bird.png')
bird_img=pygame.transform.scale(bird_img,(35,35))

tube_img=pygame.image.load('tube.png')
tube_op_img=pygame.image.load('tube_op.png')


dong_img=pygame.image.load('dong.png')
bac_img=pygame.image.load('bac.png')
vang_img=pygame.image.load('vang.png')
gameover_img=pygame.image.load('gameover.png')
gameover_img=pygame.transform.scale(gameover_img,(350,200))
def draw_road():
    road = screen.blit(road_img, ((road_x), 570))
    road=screen.blit(road_img,((road_x + 400),570))
def update_score(score, high_score):
    if score> high_score:
        high_score =score
    return high_score

menu =True
pausing= False
running=True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    clock.tick(60)
    screen.fill((255,255,255))
    screen.blit(backgroud_img,(0,0))

    # ép ảnh ống và vẽ ống
    tube1_img=pygame.transform.scale(tube_img,(tube_width,tube1_height))
    tube1=screen.blit(tube1_img,(tube1_x,0))
    tube2_img = pygame.transform.scale(tube_img, (tube_width, tube2_height))
    tube2 = screen.blit(tube2_img, (tube2_x, 0))
    tube3_img = pygame.transform.scale(tube_img, (tube_width, tube3_height))
    tube3 = screen.blit(tube3_img, (tube3_x, 0))

    #éo ảnh và vẽ ống đối diện
    tube1_op_img=pygame.transform.scale(tube_op_img,(tube_width,600-(tube1_height + d_2tube)))
    tube1_op=screen.blit(tube1_op_img,(tube1_x,tube1_height+d_2tube))
    tube2_op_img = pygame.transform.scale(tube_op_img, (tube_width, 600 - (tube2_height + d_2tube)))
    tube2_op = screen.blit(tube2_op_img, (tube2_x, tube2_height + d_2tube))
    tube3_op_img = pygame.transform.scale(tube_op_img, (tube_width, 600 - (tube3_height + d_2tube)))
    tube3_op = screen.blit(tube3_op_img, (tube3_x, tube3_height + d_2tube))

    #di chuyển ống
    tube1_x -=tube_volocity
    tube2_x -= tube_volocity
    tube3_x -= tube_volocity

    #tạo ống mới
    if tube1_x <-tube_width:
        tube1_x =550
        tube1_height=randint(100,400)
        tube1_pass=False
    if tube2_x <-tube_width:
        tube2_x =550
        tube2_height=randint(100,400)
        tube2_pass =False
    if tube3_x <-tube_width:
        tube3_x =550
        tube3_height=randint(100,400)
        tube3_pass =False

    #bầu trời
    troi=pygame.draw.rect(screen, (255,255,255),(1,0,400,1))
    #vẽ đường
    draw_road()
    road_x -=1
    if road_x < -400:
        road_x =0

    #vẽ nút pause
    pause =screen.blit(menu_img,(10,10))
    #vẽ chim
    bird=screen.blit(bird_img,(x_bird, y_bird))
    #tạo chim rơi
    y_bird +=bird_dord_velocity
    bird_dord_velocity +=gravity
    #ghi điẻm
    if not pausing:
        score_txt=font.render( str(score),True,(255,255,255))
        screen.blit(score_txt,(200,50))
    #cộng điểm
    if tube1_x+tube_width<=x_bird and tube1_pass==False:
        score +=1
        tube1_pass=True
    if tube2_x+tube_width<=x_bird and tube2_pass==False:
        score +=1
        tube2_pass=True
    if tube3_x+tube_width<=x_bird and tube3_pass==False:
        score +=1
        tube3_pass=True
    # khi dừng
    if pausing:
        tube_volocity = 0
        bird_dord_velocity = 0
        road_x =0
    #menu
    if menu:
        screen.blit(backgroud_img, (0, 0))
        road = screen.blit(road_img, (0, 570))
        screen.blit(button_img, (150, 400))
        screen.blit(flappybird_img, (25, 70))
        pausing=True
    #kiểm tra chạm và endgame
    tubes=[tube1,tube2,tube3,tube3_op,tube2_op,tube1_op,road,troi]
    for tube in tubes:
        if bird.colliderect(tube):
            pygame.draw.rect(screen, (211, 206, 143), (50, 230, 300, 170), 0, 20)
            pygame.draw.rect(screen, (126,126,126), (50, 230, 300, 170), 2, 20)
            gameover_txt = font1.render("   MEDAL",True,(220,122,1))
            screen.blit(gameover_txt,(60,250))
            gameover_1 =font1.render("Score:", True,(220,122,1))
            screen.blit(gameover_1,(210,250))
            gameover_1 = font1.render("High Score:", True, (220, 122, 1))
            screen.blit(gameover_1, (210, 320))
            high_score =update_score(score, high_score)
            high_score_txt = font.render((f'{str(high_score)}'), True, (220,122,1))
            screen.blit(high_score_txt, (210, 350))
            gameover_1 =font.render( str(score), True,(220,122,1))
            screen.blit(gameover_1,(210,280))
            button = screen.blit(button_img, (150,400))
            gameover = screen.blit(gameover_img, (35, 30))
            if score >=0:
                dong=screen.blit(dong_img,(70,250))
            if score >=10:
                dong=screen.blit(dong_img,(70,250))
            if score >=20:
                dong=screen.blit(dong_img,(70,250))
            menu =False
            pausing=True
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running==False
            pygame.quit()
        #thiết lập nút bấm
        if event.type == pygame.KEYDOWN :
            if event.key ==pygame.K_SPACE:
                bird_dord_velocity =0
                bird_dord_velocity -=7
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button ==1:
                if (150 < mouse_x < 250) and (400 < mouse_y < 482):
                    if pausing:
                        x_bird = 50
                        y_bird = 250
                        tube1_x = 400
                        tube2_x = 600
                        tube3_x = 800
                        tube_volocity=2
                        score =0
                        pausing=False
                        menu= False
                if( 10 < mouse_x < 50) and ( 10 < mouse_y < 50):
                    menu =True

    pygame.display.flip()

