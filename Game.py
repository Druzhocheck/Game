import pygame
import random

pygame.init()

display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Cats ordinary life')
Emerald = pygame.image.load('D:\VSCode\Project\Game\Sprites\Emerald.png')
pygame.display.set_icon(Emerald)

dog_img = [pygame.image.load('D:\VSCode\Project\Game\Sprites\Dogs\Dogers\Doger-1.png'),
              pygame.image.load('Sprites\Dogs\Dogers\Doger-2.png'), pygame.image.load('Sprites\Dogs\Dogers\Doger-3.png'),
              pygame.image.load('Sprites\Dogs\Dogers\Doger-4.png'), pygame.image.load('Sprites\Dogs\Dogers\Doger-5.png'),
              pygame.image.load('Sprites\Dogs\Dogers\Doger-6.png'), pygame.image.load('Sprites\Dogs\Dogers\Doger-7.png')]

cat_img = [pygame.image.load('Sprites\Cats\Catters\Cat-1.png'),
           pygame.image.load('Sprites\Cats\Catters\Cat-2.png'), pygame.image.load('Sprites\Cats\Catters\Cat-3.png'),
           pygame.image.load('Sprites\Cats\Catters\Cat-4.png'), pygame.image.load('Sprites\Cats\Catters\Cat-5.png'),
           pygame.image.load('Sprites\Cats\Catters\Cat-6.png'), pygame.image.load('Sprites\Cats\Catters\Cat-7.png'),
           pygame.image.load('Sprites\Cats\Catters\Cat-8.png'), pygame.image.load('Sprites\Cats\Catters\Cat-9.png'),
           pygame.image.load('Sprites\Cats\Catters\Cat-10.png'), pygame.image.load('Sprites\Cats\Catters\Cat-12.png')] 
bird_img = [pygame.image.load('Sprites\Birds\Birders\Bird-1.png'), pygame.image.load('Sprites\Birds\Birders\Bird-2.png'),
            pygame.image.load('Sprites\Birds\Birders\Bird-3.png'), pygame.image.load('Sprites\Birds\Birders\Bird-4.png'),
            pygame.image.load('Sprites\Birds\Birders\Bird-5.png'), pygame.image.load('Sprites\Birds\Birders\Bird-6.png'),
            pygame.image.load('Sprites\Birds\Birders\Bird-7.png'), pygame.image.load('Sprites\Birds\Birders\Bird-8.png'),]

cats = 0
dogs = 0
birds = 0
# dog = 100 * 80
cat_width = 80
cat_height = 40
cat_x = display_width // 3
cat_y = display_height - cat_height - 120 

dog_width = 100
dog_height = 40
dog_x = display_width - 50
dog_y = display_height - dog_height - 140

bird_width = 50
bird_height = 20 
bird_x = display_width - 50
bird_y = display_height - bird_height - 330

clock =pygame.time.Clock()

jumping = False
jumps = 30

scores = 0
scoring = False


class Animals:
    def __init__(self, x, y, width, height, speed, animal):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.animal = animal

    def move(self):
        global birds, dogs
        if self.x >= -self.width:
            if self.animal == 'dog':
                    if dogs == 77:
                        dogs = 0
                    display.blit(dog_img[dogs // 11], (self.x, self.y))
                    dogs += 1
            else:
                if birds == 88:
                    birds = 0
                display.blit(bird_img[birds // 11], (self.x, self.y))
                birds += 1
            self.x -= self.speed 
            return True
        else:
            self.x = display_width + 100 + random.randrange(-80, 60)
            return False

    def Repaint(self, radius, y, width, height, animal):
        global birds, dogs
        self.x = radius
        self.y = y
        self.width = width
        self.height = height
        self.animal = animal
        if self.animal == 'dog':
            if dogs == 77:
                dogs = 0
            display.blit(dog_img[dogs // 11], (self.x, self.y))
            dogs += 1
        else:
            if birds == 88:
                birds = 0
            display.blit(bird_img[birds // 11], (self.x, self.y))
            birds += 1


def Start():
    global jumping
    game = True
    animals_array = []
    Create_Animal(animals_array)
    land = pygame.image.load('Sprites\BackGround.png')
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] | keys[pygame.K_UP]:
            jumping = True
        if jumping:
            Jump()
        if scores == 25:
            Win()
            game = False
        Score(animals_array)
        display.blit(land, (0, 0))
        Print_text('Score: ' + str(scores), 10, 10)
        Draw_animals(animals_array)
        Draw_cat()
        # pygame.draw.rect(display, (247, 240, 22),(user_x, user_y, user_width, user_height))
        if Crash(animals_array):
            game = False
        pygame.display.update()
        clock.tick(80)
    return Game_Over()

def Jump():
    global cat_y, jumping, jumps
    if jumps >= -30:
        cat_y -= jumps / 2
        jumps -= 1
    else:
        jumps = 30
        jumping = False

def Create_Animal(array):
    # First
    global dog_y, bird_y
    choice = random.randrange(0, 2)
    if choice == 0:
        animal = 'dog'
        width = dog_width
        height = dog_height
        y = dog_y
    else:
        animal = 'bird'
        width = bird_width
        height = bird_height
        y = bird_y
    array.append(Animals(display_width + 20, y, width, height, 4, animal))
    # Second
    choice = random.randrange(0, 2)
    if choice == 0:
        animal = 'dog'
        width = dog_width
        height = dog_height
        y = dog_y
    else:
        animal = 'bird'
        width = bird_width
        height = bird_height
        y = bird_y
    array.append(Animals(display_width + 300, y, width, height, 4, animal))
    # Third
    choice = random.randrange(0, 2)
    if choice == 0:
        animal = 'dog'
        width = dog_width
        height = dog_height 
        y = dog_y
    else:
        animal = 'bird'
        width = bird_width
        height = bird_height
        y = bird_y
    array.append(Animals(display_width + 600, y, width, height, 4, animal))

def Distance(array):
    maximum = max(array[0].x, array[1].x, array[2].x)
    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 150 
    else:
        radius = maximum

    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(2, 3)
    else:
        radius += random.randrange(200, 400)
    return radius


def Draw_animals(array):
    global bird_y, dog_y
    for ani in array:
        check = ani.move()
        if not check:
            radius = Distance(array)

            choice = random.randrange(0, 2)
            if choice == 0:
                animal = 'dog'
                width = dog_width
                height = dog_height
                y = dog_y
            else:
                animal = 'bird'
                width = bird_width
                height = bird_height
                y = bird_y

            ani.Repaint(radius, y, width, height, animal)

def Draw_cat():
    global cats
    if cats == 66:
        cats = 0
    display.blit(cat_img[cats // 6], (cat_x, cat_y))
    cats += 1

def Crash(barriers):
    for barrier in barriers:
        if barrier.animal == 'dog':
            if cat_y + cat_height >= barrier.y:
                if barrier.x <= cat_x <= barrier.x + barrier.width:
                    return True 
                elif barrier.x <= cat_x + cat_width <= barrier.x + barrier.width:
                    return True
       # if barrier.animal == 'bird':
           # if (cat_y <= barrier.y + barrier.height):
            #   if (barrier.x <= cat_x <= barrier.x + barrier.width):
            #        return True
            #   elif barrier.x <= cat_x + cat_width <= barrier.x + barrier.width:
               #     return True
    return False

def Print_text(message, x, y, font_color = (255, 0 ,0), font_type = 'Sprites\holiday-home1.ttf', font_size = 40):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x,y))

def Game_Over():
    stop = True
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = False
        Print_text('Game Over. Enter to play again', 250, 200)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return True
        pygame.display.update()
        clock.tick(60)

def Win():
    win = True
    while win:
        for event in pygame.event.get():
            Print_text('You won! Your score = ' + str (scores), 250, 200)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return True
        pygame.display.update()
        clock.tick(60)

def Score(barriers):
    global scores, scoring
    if not scoring:
        for barrier in barriers:
            if barrier.animal == 'bird':
                if barrier.x <= cat_x + cat_width <= barrier.x + barrier.width:
                    if cat_y <= barrier.y + barrier.height:
                        scoring = True
                        barrier.x = display_width + 100 + random.randrange(-80, 60)
                        break
    else:
        if jumping == 0:
            scores += 1
            scoring = False
             
while Start():
    scores = 0
pygame.quit()
quit()
