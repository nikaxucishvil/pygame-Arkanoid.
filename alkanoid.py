# import pygame
import pygame
pygame.init()
# screen
screen = pygame.display.set_mode((500, 500))
RED = (255,0,0)
# CLASSES
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x,y, width, height)
        self.fill_color = (200,255,255)
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(screen, self.fill_color, self.rect)
    
    def colidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def coliderect(self, rect):
        return self.rect.colliderect(rect)



class Picture(Area):
    def __init__(self, filename, x=0, y=0,width=10,height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

# ობიექტები
ball = Picture("ball_1615463127.png", 160, 200, 50, 50)
platform = Picture("platform.png", 200, 330, 100, 30)
# მოონსტრების ჩატვირთვა
start_x = 5
start_y = 5
count = 9
monsters = []
for j in range(3):
    y = start_y + (55 * j)
    x = start_x + (27.5 * j)
    for i in range(count):
        enemy = Picture("enemy_1615463121.png", x, y, 50, 50)
        monsters.append(enemy)
        x += 55
    count = count -1

#  დროშები
move_right = False
move_left = False

# ბურთის სიჩგარეები
dx = 3
dy = 3
# game loop
run = True
monster = 24
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_LEFT:
                move_left = False
    
    # პლათფორმის მოძრაობა
    if move_right:
        platform.rect.x += 10
    elif move_left:
        platform.rect.x -= 10

    # ball move
    ball.rect.x += dx
    ball.rect.y += dy

    if ball.rect.colliderect(platform.rect):
        dy*= (-1)
    
    if ball.rect.x >450 or ball.rect.x <0:
        dx *= (-1)

    if ball.rect.y <0:
        dy *= (-1)

    # ეკრანის ფერი
    screen.fill((200,255,255))

    # წაგების ლოგიკა
    if ball.rect.y > 450:
        font = pygame.font.Font(None, 45)
        text = "YOU LOSE"
        text_surface = font.render(text, True, RED)
        screen.blit(text_surface, (180, 200))
        run = False

    # ციკლის მთავარი ნაწილი
    for monst in  monsters:
        monst.draw()
        if monst.rect.colliderect(ball.rect):
            monsters.remove(monst)
            dy*= (-1)
            monster -= 1
            if monster == 0:
                font = pygame.font.Font(None, 45)
                win_text = "YOU WIN"
                win_text_surface = font.render(win_text, True, RED)
                screen.fill((0,255,0))
                screen.blit(win_text_surface, (180, 200))
                run = False
        


    ball.draw()
    platform.draw()
    # კადრის განახლება
    pygame.display.update()
    pygame.time.Clock().tick(40)
