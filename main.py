import pygame
from pygame.locals import *
import random

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 0
        self.gravity = 0.5
        self.jump_height = -10
        self.image = pygame.image.load("image/bird0.png")
        self.rect = self.image.get_rect()  # 把图片作为一个矩形放到rect对象中，为什么用这个 它可以很轻松的调用出他的四个边的位置
        self.rect.center = [self.x, self.y]

    # def draw(self, screen):
    #     screen.blit(self.image, (self.x, self.y))
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        self.rect.center = [self.x, self.y]

        if self.velocity > 0:  # different movements of bird:
            self.image = pygame.image.load("image/bird1.png")
        elif self.velocity < 0:
            self.image = pygame.image.load("image/bird2.png")
        else:
            self.image = pygame.image.load("image/bird0.png")

        # if self.y >= screen_height - self.height:  # Ensures valid ground collision
        #     self.y = screen_height - self.height
        #     self.velocity = 0

        # judge the border
        if self.y < 0 or self.y > 708:
            return "game_over"
        # judge the score
        # global score
        # for pipe in pipeGroup:
        #     if self.rect.left <= pipe.rect.right and not pipe.scored:
        #         score += 1
        #         pipe.scored = True
        #         print(score)
        #         break

    def jump(self):
        self.velocity = self.jump_height

class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()  # type: pygame.Rect
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, pipe_gap, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.gap = pipe_gap
        self.scored = False
        location = random.randint(400, 700)
        if position == 1:
            self.rect.bottomleft = (x,  location - self.gap)
        if position == -1:
            self.rect.topleft = (x, location)

    def update(self):
        global scrollSpeed
        self.rect.x -= scrollSpeed

        num_pipes = 5  # Number of active pipe pairs

        # Picture loop:
        if self.rect.right <= 0:
            # print(f"Killing pipe at {self.rect.x}")

            global pipe_gap
            pipe_gap = random.randint(300, 350)

            # Check if number of active pipes is below the limit
            if len(pipeGroup) < num_pipes * 2:
                new_x = random.randint(screen_width + 200, screen_width + 400)
                pipeGroup.add(Pipe(new_x, pipe_gap, bottomPipe, -1))
                pipeGroup.add(Pipe(new_x, pipe_gap, topPipe, 1))
            # check whether pipe is overlap , and remove the overlapped
            for pipe in pipeGroup:
                for other_pipe in pipeGroup:
                    if pipe != other_pipe and pipe.rect.colliderect(other_pipe.rect):
                        pipe.kill()  # Remove the overlapping pipe
            self.kill()
            global score
            score += 1
            if score % 10 == 0:
                scrollSpeed += 2

    def draw(self, screen):
        screen.blit(self.rect, screen)

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 850
screen_height = 820

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# game variables
groundScroll = 0
scrollSpeed = 4
pipe_gap = random.randint(300, 350)
game_over = False
score = 0

# font init:
pygame.font.init()
font = pygame.font.SysFont(None, 40)

# image init:
bg = pygame.image.load("image/bg.png")
groundImage = pygame.image.load("image/ground.png")
gameOver = pygame.image.load("image/restart.png")
birdDead = pygame.image.load("image/birddead.png")
topPipe = pygame.image.load("image/top.png")
bottomPipe = pygame.image.load("image/bottom.png")

# class init:
bird = Bird(200, screen_height // 2, 50, 50)
restart_button = Button(350, 400, gameOver)
# top_pipe = Pipe(800, pipe_gap, topPipe, 1)
# bottom_pipe = Pipe(800, pipe_gap, bottomPipe, -1)

# game group
birdGroup = pygame.sprite.Group()
pipeGroup = pygame.sprite.Group()
# buttonGroup = pygame.sprite.Group()
collideGroup = pygame.sprite.Group()

# group add:
birdGroup.add(bird)

# pipeGroup.add(top_pipe)
# pipeGroup.add(bottom_pipe)   替代：pipeGroup.add(Pipe(800, pipe_gap, bottomPipe, -1))

def restart():
    global bird, birdGroup, groundScroll, score, scrollSpeed
    bird = Bird(100, screen_height // 2, 50, 50)
    birdGroup.empty()
    birdGroup.add(bird)
    scrollSpeed = 5
    groundScroll = 0
    score = 0
    pipeGroup.empty()
    game_init()

def check_collision():
    global game_over
    for pipe in pipeGroup:
        if bird.rect.colliderect(pipe.rect):
            game_over = True
            break

def game_init():
    for i in 800, 1200, 1600:
        pipeGroup.add(Pipe(i, pipe_gap, bottomPipe, -1))
        pipeGroup.add(Pipe(i, pipe_gap, topPipe, 1))

game_init()
# game loop:
run = True
while run:
    clock.tick(fps)

    screen.blit(bg, (0, 0))
    check_collision()

    # 渲染并显示分数
    text = font.render(f'Score: {score / 2 }', True, (255, 255, 255))
    screen.blit(text, (20, 20))  # 在屏幕左上角显示分数

    if game_over:
        restart_button.draw(screen)
        screen.blit(birdDead, bird.rect)
    else:
        if bird.update() == "game_over":
            game_over = True

        pipeGroup.draw(screen)
        pipeGroup.update()

        birdGroup.draw(screen)

        groundScroll -= scrollSpeed
        if abs(groundScroll) > 100:
            groundScroll = 0
    # game_over judge:
    # if bird.update() == "game_over":
    #     bird.image = birdDead
    #     restart_button.draw(screen)
    #     birdGroup.draw(screen)
    #     pygame.display.update()
    #     pygame.time.delay(4000)
    #     restart()
    screen.blit(groundImage, (groundScroll, 708))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over:
                bird.jump()
            else:
                if restart_button.is_clicked(event):
                    restart()
                    game_over = False
    pygame.display.update()
pygame.quit()
