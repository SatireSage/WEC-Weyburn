import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BUTTONLIGHT = (170, 170, 170)
BUTTONDARK = (100, 100, 100)

boardSize = 0

res = (1000, 700)

winEight = (400, 400)
winTen = (500, 500)
winTwelve = (600, 600)
winFourteen = (700, 700)
winSixteen = (800, 800)

eightPiece = [[14, 10, 15, 11, 12, 15, 10, 14],
              [9, 9, 9, 9, 9, 9, 9, 9],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1],
              [6, 2, 7, 3, 4, 7, 2, 6]]


screen = pygame.display.set_mode(res)
pygame.display.set_caption("CHESS")
clock = pygame.time.Clock()

FONTSINGLE = pygame.font.SysFont('Corbel', 35)
FONTDOUBLE = pygame.font.SysFont('Corbel', 35)
eightBoard = FONTSINGLE.render('8x8', True, WHITE)
tenBoard = FONTDOUBLE.render('10x10', True, WHITE)
twelveBoard = FONTDOUBLE.render('12x12', True, WHITE)
fourteenBoard = FONTDOUBLE.render('14x14', True, WHITE)
sixteenBoard = FONTDOUBLE.render('16x16', True, WHITE)


def drawBoard(size):
    for y in range(0, size):
        if (y % 2) == 0:
            for x in range(0, (size//2)):
                pygame.draw.rect(screen, BLACK, [((50*2*x)+50), 50*y, 50, 50])
        else:
            for x in range(0, (size//2)):
                pygame.draw.rect(screen, BLACK, [(50*2*x), 50*y, 50, 50])


startScreen = True
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if startScreen == True:
                if 75 <= mouse[0] <= 225 and 500 <= mouse[1] <= 545:
                    boardSize = 8
                    startScreen = False
                    screen = pygame.display.set_mode(winEight)

                if 250 <= mouse[0] <= 400 and 500 <= mouse[1] <= 545:
                    boardSize = 10
                    startScreen = False
                    screen = pygame.display.set_mode(winTen)

                if 425 <= mouse[0] <= 575 and 500 <= mouse[1] <= 545:
                    boardSize = 12
                    startScreen = False
                    screen = pygame.display.set_mode(winTwelve)

                if 600 <= mouse[0] <= 750 and 500 <= mouse[1] <= 545:
                    boardSize = 14
                    startScreen = False
                    screen = pygame.display.set_mode(winFourteen)

                if 775 <= mouse[0] <= 925 and 500 <= mouse[1] <= 545:
                    boardSize = 16
                    startScreen = False
                    screen = pygame.display.set_mode(winSixteen)

    mouse = pygame.mouse.get_pos()

    if startScreen == True:
        screen.fill(WHITE)
        if 75 <= mouse[0] <= 225 and 500 <= mouse[1] <= 545:
            pygame.draw.rect(screen, BUTTONLIGHT, [75, 500, 150, 45])
        else:
            pygame.draw.rect(screen, BUTTONDARK, [75, 500, 150, 45])
        screen.blit(eightBoard, (130, 507))

        if 250 <= mouse[0] <= 400 and 500 <= mouse[1] <= 545:
            pygame.draw.rect(screen, BUTTONLIGHT, [250, 500, 150, 45])
        else:
            pygame.draw.rect(screen, BUTTONDARK, [250, 500, 150, 45])
        screen.blit(tenBoard, (287, 507))

        if 425 <= mouse[0] <= 575 and 500 <= mouse[1] <= 545:
            pygame.draw.rect(screen, BUTTONLIGHT, [425, 500, 150, 45])
        else:
            pygame.draw.rect(screen, BUTTONDARK, [425, 500, 150, 45])
        screen.blit(twelveBoard, (462, 507))

        if 600 <= mouse[0] <= 750 and 500 <= mouse[1] <= 545:
            pygame.draw.rect(screen, BUTTONLIGHT, [600, 500, 150, 45])
        else:
            pygame.draw.rect(screen, BUTTONDARK, [600, 500, 150, 45])
        screen.blit(fourteenBoard, (637, 507))

        if 775 <= mouse[0] <= 925 and 500 <= mouse[1] <= 545:
            pygame.draw.rect(screen, BUTTONLIGHT, [775, 500, 150, 45])
        else:
            pygame.draw.rect(screen, BUTTONDARK, [775, 500, 150, 45])
        screen.blit(sixteenBoard, (812, 507))

    else:
        screen.fill(WHITE)
        drawBoard(boardSize)

    pygame.display.flip()

clock.tick(60)
pygame.quit()
