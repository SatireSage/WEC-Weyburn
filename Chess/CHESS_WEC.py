import pygame

IMAGES = {}


def GamePieces():
    pieces = ['bq', 'bk', 'br', 'bn', 'bb', 'bv', 'bp',
              'wq', 'wk', 'wr', 'wn', 'wb', 'wv', 'wp', ]
    for piece in pieces:
        IMAGES[piece] = pygame.image.load("ChessPieces/" + piece + ".png")


bkg = pygame.image.load("ChessPieces/Weyburn_Chess.jpg")

pygame.init()
GamePieces()

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

BaseState8 = [['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
              ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
              ['--', '--', '--', '--', '--', '--', '--', '--'],
              ['--', '--', '--', 'bv', 'bv', '--', '--', '--'],
              ['--', '--', '--', 'wv', 'wv', '--', '--', '--'],
              ['--', '--', '--', '--', '--', '--', '--', '--'],
              ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
              ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']]

BaseState10 = [['br', 'bn', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'bn', 'br'],
               ['bv', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bv'],
               ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--'],
               ['wv', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wv'],
               ['wr', 'wn', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wn', 'wr']]

BaseState12 = [['br', 'bn', 'bn', 'bb', 'bb', 'bq', 'bk', 'bb', 'bb', 'bn', 'bn', 'br'],
               ['bp', 'bp', 'bp', 'bp', 'bp', 'bp',
                'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
               ['--', '--', '--', '--', '--', '--',
                '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--',
                '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--',
                '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--',
                '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--',
                '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--',
                '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--',
                '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--',
                '--', '--', '--', '--', '--', '--'],
               ['wp', 'wp', 'wp', 'wp', 'wp', 'wp',
                'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
               ['wr', 'wn', 'wn', 'wb', 'wb', 'wq', 'wk', 'wb', 'wb', 'wn', 'wn', 'wr']]

BaseState14 = [['br', 'bb', 'bn', 'br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br', 'bn', 'bb', 'br'],
               ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp',
                   'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', ],
               ['--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--'],
               ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp',
                   'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
               ['wr', 'wb', 'wn', 'wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr', 'wn', 'wb', 'wr']]

BaseState16 = [['br', 'bb', 'bn', 'br', 'bn', 'bb', 'bq', 'bq', 'bk', 'bq', 'bb', 'bn', 'br', 'bn', 'bb', 'br'],
               ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp',
                   'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
               ['--', '--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--', '--'],
               ['--', '--', '--', '--', '--', '--', '--', '--',
                   '--', '--', '--', '--', '--', '--', '--', '--'],
               ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp',
                   'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
               ['wr', 'wb', 'wn', 'wr', 'wn', 'wb', 'wq', 'wq', 'wk', 'wq', 'wb', 'wn', 'wr', 'wn', 'wb', 'wr']]


def drawPieces(filename, x, y):
    screen.blit(filename, (x, y))


def cyclePieces8(size):
    for y in range(0, size):
        for x in range(0, size):
            BoardState8 = BaseState8[y][x]
            if BoardState8 != '--':
                drawPieces(IMAGES[BoardState8], (x*50), (y*50))


def cyclePieces10(size):
    for y in range(0, size):
        for x in range(0, size):
            BoardState10 = BaseState10[y][x]
            if BoardState10 != '--':
                drawPieces(IMAGES[BoardState10], (x*50), (y*50))


def cyclePieces12(size):
    for y in range(0, size):
        for x in range(0, size):
            BoardState12 = BaseState12[y][x]
            if BoardState12 != '--':
                drawPieces(IMAGES[BoardState12], (x*50), (y*50))


def cyclePieces14(size):
    for y in range(0, size):
        for x in range(0, size):
            BoardState14 = BaseState14[y][x]
            if BoardState14 != '--':
                drawPieces(IMAGES[BoardState14], (x*50), (y*50))


def cyclePieces16(size):
    for y in range(0, size):
        for x in range(0, size):
            BoardState16 = BaseState16[y][x]
            if BoardState16 != '--':
                drawPieces(IMAGES[BoardState16], (x*50), (y*50))


screen = pygame.display.set_mode(res)
pygame.display.set_caption("Weyburn Chess")
clock = pygame.time.Clock()

FONTSINGLE = pygame.font.SysFont('Corbel', 35)
FONTDOUBLE = pygame.font.SysFont('Corbel', 35)
eightBoard = FONTSINGLE.render('8x8', True, WHITE)
tenBoard = FONTDOUBLE.render('10x10', True, WHITE)
twelveBoard = FONTDOUBLE.render('12x12', True, WHITE)
fourteenBoard = FONTDOUBLE.render('14x14', True, WHITE)
sixteenBoard = FONTDOUBLE.render('16x16', True, WHITE)
FONTEIGHT = pygame.font.SysFont('Academy Engraced LET', 35)
but1 = FONTEIGHT.render('Novice', True, (105, 201, 26))
but2 = FONTEIGHT.render('Beginner', True, (217, 217, 24))
but3 = FONTEIGHT.render('Competent', True, (219, 130, 22))
but4 = FONTEIGHT.render('Proficient', True, (227, 67, 18))
but5 = FONTEIGHT.render('Expert', True, (149, 17, 189))
FONTCOPYRIGHT = pygame.font.SysFont('Academy Engraved LET', 25)
cop = FONTCOPYRIGHT.render('© Weyburn 2021', True, WHITE)


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
        screen.blit(bkg, (0, 0))
        screen.blit(cop, (2, 684))
        screen.blit(but1, (110, 550))
        screen.blit(but2, (272, 550))
        screen.blit(but3, (436, 550))
        screen.blit(but4, (615, 550))
        screen.blit(but5, (812, 550))
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
        if boardSize == 8:
            cyclePieces8(boardSize)
        elif boardSize == 10:
            cyclePieces10(boardSize)
        elif boardSize == 12:
            cyclePieces12(boardSize)
        elif boardSize == 14:
            cyclePieces14(boardSize)
        elif boardSize == 16:
            cyclePieces16(boardSize)

    pygame.display.flip()

clock.tick(60)
pygame.quit()
