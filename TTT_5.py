import pygame, sys, random, copy
from pygame.locals import *

RESOLUTION = (720, 480)
BOARDDIMENSIONS = (3, 3)
XMARGIN = int((RESOLUTION[0] - (BOARDDIMENSIONS[0] * (190 + 15))) / 2)
YMARGIN = int((RESOLUTION[0] - (BOARDDIMENSIONS[1] * (190 + 15))) / 2)

BGCOLOR = [255, 255, 255]  # background
BGCOLOR2 = [150, 150, 170]  # button background
LINECOLOR = [255, 50, 50]  # Highlight line color
LINECOLOR2 = [10, 10, 10]  # Line color
XCOLOR = [100, 100, 255]  # Color of 'X'
YCOLOR = [255, 100, 100]  # Color of 'Y'

MOUSE_X = 0
MOUSE_Y = 0
mouseClicked = False
difficulty = 0

def main():
    global CLOCK, DISPLAYSURF
    pygame.init()
    CLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((RESOLUTION[0], RESOLUTION[0]))
    mainFont = pygame.font.SysFont('Lucida Console', 200)
    smallFont = pygame.font.SysFont('Lucida Console', 40)
    logoFont = pygame.font.SysFont('Lucida Console', 80)
    pygame.display.set_caption('X-O-X')
    gamevars = [mainFont, smallFont]
    global mouseClicked
    global MOUSE_X
    global MOUSE_Y

    logo = pygame.image.load("LOGO.png")

    DISPLAYSURF.fill(tuple(BGCOLOR))
    while True:

        mouseClicked = False
        DISPLAYSURF.fill(tuple(BGCOLOR))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                MOUSE_X, MOUSE_Y = event.pos
            elif event.type == MOUSEBUTTONUP:
                MOUSE_X, MOUSE_Y = event.pos
                mouseClicked = True

        DISPLAYSURF.blit(logo, (280, 40))
        LOGO(logoFont)

        if drawButtonA(smallFont, 'vs. CPU', 350):
            vsCPU(gamevars)

        elif drawButtonA(smallFont, 'vs. Player', 410):
            gamePVP(gamevars)

        elif drawButtonA(smallFont, 'Theme Picker', 470):
            themePicker(gamevars)

        elif drawButtonA(smallFont, 'Quit', 530):
            pygame.quit()
            sys.exit()

        pygame.display.update()
        CLOCK.tick(30)


def vsCPU(gamevars):
    global mouseClicked
    global MOUSE_X
    global MOUSE_Y
    global difficulty

    mainFont = gamevars[0]
    smallFont = gamevars[1]

    DISPLAYSURF.fill(tuple(BGCOLOR))
    while True:
        mouseClicked = False
        DISPLAYSURF.fill(tuple(BGCOLOR))

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                MOUSE_X, MOUSE_Y = event.pos
            elif event.type == MOUSEBUTTONUP:
                MOUSE_X, MOUSE_Y = event.pos
                mouseClicked = True

        if returnToMenuButton(smallFont):
            return
        elif drawButtonA(smallFont, 'Easy', 290):
            difficulty = 0
            break
        elif drawButtonA(smallFont, 'Medium', 350):
            difficulty = 1
            break
        elif drawButtonA(smallFont, 'Impossible', 410):
            difficulty = 2
            break
        pygame.display.update()
        CLOCK.tick(30)
    gameCPU(gamevars)
    return


def themePicker(gamevars):
    global mouseClicked
    global MOUSE_X
    global MOUSE_Y

    mainFont = gamevars[0]
    smallFont = gamevars[1]

    DISPLAYSURF.fill(tuple(BGCOLOR))
    while True:
        mouseClicked = False
        DISPLAYSURF.fill(tuple(BGCOLOR))

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                MOUSE_X, MOUSE_Y = event.pos
            elif event.type == MOUSEBUTTONUP:
                MOUSE_X, MOUSE_Y = event.pos
                mouseClicked = True

        if returnToMenuButton(smallFont):
            return
        elif drawButtonA(smallFont, 'Classic', 290):
            setThemeClassic()
        elif drawButtonA(smallFont, 'Darcula', 350):
            setThemeDarcula()
        elif drawButtonA(smallFont, 'Camouflage', 410):
            setThemeCamouflage()
        elif drawButtonA(smallFont, 'Bubble Gum', 470):
            setThemeBubbleGum();
        elif drawButtonA(smallFont, 'Captain Dead Pool', 530):
            setThemeCaptainDeadPool()
        pygame.display.update()
        CLOCK.tick(30)


def setThemeClassic():
    global BGCOLOR
    global BGCOLOR2
    global LINECOLOR
    global LINECOLOR2
    global XCOLOR
    global YCOLOR

    BGCOLOR = [255, 255, 255]  # background
    BGCOLOR2 = [150, 150, 170]  # button background
    LINECOLOR = [255, 50, 50]  # Highlight line color
    LINECOLOR2 = [10, 10, 10]  # Line color
    XCOLOR = [100, 100, 255]  # Color of 'X'
    YCOLOR = [255, 100, 100]  # Color of 'Y'


def setThemeDarcula():
    global BGCOLOR
    global BGCOLOR2
    global LINECOLOR
    global LINECOLOR2
    global XCOLOR
    global YCOLOR

    BGCOLOR = [25, 25, 25]  # background
    BGCOLOR2 = [10, 10, 10]  # button background
    LINECOLOR = [100, 25, 25]  # Highlight line color
    LINECOLOR2 = [75, 75, 75]  # Line color
    XCOLOR = [25, 25, 100]  # Color of 'X'
    YCOLOR = [100, 25, 25]  # Color of 'Y'


def setThemeCamouflage():
    global BGCOLOR
    global BGCOLOR2
    global LINECOLOR
    global LINECOLOR2
    global XCOLOR
    global YCOLOR

    BGCOLOR = [5, 30, 5]  # background
    BGCOLOR2 = [10, 50, 10]  # button background
    LINECOLOR = [25, 100, 25]  # Highlight line color
    LINECOLOR2 = [5, 75, 5]  # Line color
    XCOLOR = [25, 75, 25]  # Color of 'X'
    YCOLOR = [25, 50, 25]  # Color of 'Y'


def setThemeBubbleGum():
    global BGCOLOR
    global BGCOLOR2
    global LINECOLOR
    global LINECOLOR2
    global XCOLOR
    global YCOLOR

    BGCOLOR = [240, 100, 255]  # background
    BGCOLOR2 = [190, 90, 200]  # button background
    LINECOLOR = [255, 200, 200]  # Highlight line color
    LINECOLOR2 = [80, 40, 80]  # Line color
    XCOLOR = [150, 50, 220]  # Color of 'X'
    YCOLOR = [220, 50, 140]  # Color of 'Y'


def setThemeCaptainDeadPool():
    global BGCOLOR
    global BGCOLOR2
    global LINECOLOR
    global LINECOLOR2
    global XCOLOR
    global YCOLOR

    BGCOLOR = [200, 0, 0]  # background
    BGCOLOR2 = [120, 50, 50]  # button background
    LINECOLOR = [0, 0, 0]  # Highlight line color
    LINECOLOR2 = [30, 10, 10]  # Line color
    XCOLOR = [0, 0, 0]  # Color of 'X'
    YCOLOR = [0, 0, 0]  # Color of 'Y'


def gameCPU(gamevars):

    global difficulty
    mainFont = gamevars[0]
    smallFont = gamevars[1]
    PLAYERVICTORY = False
    COMPUTERVICTORY = False
    doEachTurn = False
    global mouseClicked
    global MOUSE_X
    global MOUSE_Y


    PlayerScore = 0
    ComputerScore = 0

    mainBoard = makeEachBoxFalse(False)
    usedBoxes = makeEachBoxFalse(False)
    lifeOfBox = makeEachBoxFalse(False)
    playerTurnDone = False

    DISPLAYSURF.fill(tuple(BGCOLOR))
    drawLines()

    while True:
        mouseClicked = False

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                MOUSE_X, MOUSE_Y = event.pos
            elif event.type == MOUSEBUTTONUP:
                MOUSE_X, MOUSE_Y = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(MOUSE_X, MOUSE_Y)
        if boxx != None and boxy != None:

            if not usedBoxes[boxx][boxy] and mouseClicked and playerTurnDone == False:
                usedBoxes[boxx][boxy] = True
                mainBoard[boxx][boxy] = 'X'
                playerTurnDone = True
                doEachTurn = True


            elif playerTurnDone == True:
                pygame.time.wait(500)
                if difficulty == 0:
                    boxx, boxy = computerTurnWithAIEasy(usedBoxes, mainBoard)
                elif difficulty == 1:
                    boxx, boxy = computerTurnWithAIMedium(usedBoxes, mainBoard)
                elif difficulty == 2:
                    boxx, boxy = computerTurnWithAIImpossibleTwist(usedBoxes, mainBoard, lifeOfBox)
                usedBoxes[boxx][boxy] = True
                mainBoard[boxx][boxy] = 'O'
                playerTurnDone = False
                doEachTurn = True


        if doEachTurn:
            lifeOfBox[boxx][boxy] = 5
            lifeManagementBox(mainBoard, usedBoxes, lifeOfBox)
            DISPLAYSURF.fill(tuple(BGCOLOR))
            drawLines()
            for boxx in range(0, BOARDDIMENSIONS[0]):
                for boxy in range(0, BOARDDIMENSIONS[1]):
                    if mainBoard[boxx][boxy] == 'X':
                        markBoxX(boxx, boxy, mainFont)
                    elif mainBoard[boxx][boxy] == 'O':
                        markBoxO(boxx, boxy, mainFont)
            doEachTurn = False
            pygame.display.update()

        PLAYERVICTORY, COMPUTERVICTORY = gameWon(mainBoard)

        if PLAYERVICTORY:
            pygame.time.wait(500)
            highlightWin(mainBoard)
            pygame.display.update()
            usedBoxes, mainBoard, playerTurnDone, PLAYERVICTORY, COMPUTERVICTORY = boardReset(usedBoxes, mainBoard,
                                                                                              playerTurnDone,
                                                                                              PLAYERVICTORY,
                                                                                              COMPUTERVICTORY)
            PlayerScore += 1
            DISPLAYSURF.fill(tuple(BGCOLOR))
            drawLines()

        elif COMPUTERVICTORY:
            pygame.time.wait(500)
            highlightWin(mainBoard)
            pygame.display.update()
            usedBoxes, mainBoard, playerTurnDone, PLAYERVICTORY, COMPUTERVICTORY = boardReset(usedBoxes, mainBoard,
                                                                                              playerTurnDone,
                                                                                              PLAYERVICTORY,
                                                                                              COMPUTERVICTORY)
            ComputerScore += 1
            DISPLAYSURF.fill(tuple(BGCOLOR))
            drawLines()

        else:
            if gameOver(usedBoxes, mainBoard):
                usedBoxes, mainBoard, playerTurnDone, PLAYERVICTORY, COMPUTERVICTORY = boardReset(usedBoxes, mainBoard,
                                                                                                  playerTurnDone,
                                                                                                  PLAYERVICTORY,
                                                                                                  COMPUTERVICTORY)
                DISPLAYSURF.fill(tuple(BGCOLOR))
                drawLines()

        drawScoreBoard(smallFont, PlayerScore, 'Computer', ComputerScore)
        if returnToMenuButton(smallFont):
            return

        pygame.display.update()
        CLOCK.tick(30)


def gamePVP(gamevars):

    global difficulty
    mainFont = gamevars[0]
    smallFont = gamevars[1]
    PLAYER1VICTORY = False
    PLAYER2VICTORY = False
    global mouseClicked
    global MOUSE_X
    global MOUSE_Y


    Player1Score = 0
    Player2Score = 0

    mainBoard = makeEachBoxFalse(False)
    usedBoxes = makeEachBoxFalse(False)

    playerTurnDone = False

    DISPLAYSURF.fill(tuple(BGCOLOR))
    drawLines()

    while True:

        mouseClicked = False

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                MOUSE_X, MOUSE_Y = event.pos
            elif event.type == MOUSEBUTTONUP:
                MOUSE_X, MOUSE_Y = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(MOUSE_X, MOUSE_Y)
        if boxx != None and boxy != None:

            if not usedBoxes[boxx][boxy] and mouseClicked and playerTurnDone == False:
                markBoxX(boxx, boxy, mainFont)
                usedBoxes[boxx][boxy] = True
                mainBoard[boxx][boxy] = 'X'
                playerTurnDone = True
                pygame.display.update()

            elif not usedBoxes[boxx][boxy] and mouseClicked and playerTurnDone == True:
                markBoxO(boxx, boxy, mainFont)
                usedBoxes[boxx][boxy] = True
                mainBoard[boxx][boxy] = 'O'
                playerTurnDone = False
                pygame.display.update()

        PLAYER1VICTORY, PLAYER2VICTORY = gameWon(mainBoard)

        if PLAYER1VICTORY:
            pygame.time.wait(500)
            highlightWin(mainBoard)
            pygame.display.update()
            usedBoxes, mainBoard, playerTurnDone, PLAYERVICTORY, COMPUTERVICTORY = boardReset(usedBoxes, mainBoard,
                                                                                              playerTurnDone,
                                                                                              PLAYER1VICTORY,
                                                                                              PLAYER2VICTORY)
            Player1Score += 1
            DISPLAYSURF.fill(tuple(BGCOLOR))
            drawLines()

        elif PLAYER2VICTORY:
            pygame.time.wait(500)
            highlightWin(mainBoard)
            pygame.display.update()
            usedBoxes, mainBoard, playerTurnDone, PLAYERVICTORY, COMPUTERVICTORY = boardReset(usedBoxes, mainBoard,
                                                                                              playerTurnDone,
                                                                                              PLAYER1VICTORY,
                                                                                              PLAYER2VICTORY)
            Player2Score += 1
            DISPLAYSURF.fill(tuple(BGCOLOR))
            drawLines()

        else:
            if gameOver(usedBoxes, mainBoard):
                usedBoxes, mainBoard, playerTurnDone, PLAYERVICTORY, COMPUTERVICTORY = boardReset(usedBoxes, mainBoard,
                                                                                                  playerTurnDone,
                                                                                                  PLAYER1VICTORY,
                                                                                                  PLAYER2VICTORY)
                DISPLAYSURF.fill(tuple(BGCOLOR))
                drawLines()

        drawScoreBoard(smallFont, Player1Score, 'Player2', Player2Score)
        if returnToMenuButton(smallFont):
            return

        pygame.display.update()
        CLOCK.tick(30)


def drawLines():
    left = XMARGIN + 190
    top = YMARGIN
    width = 15
    height = (190 + 15) * BOARDDIMENSIONS[1]

    vertRect1 = pygame.Rect(left, top, width, height)
    pygame.draw.rect(DISPLAYSURF, LINECOLOR2, vertRect1)

    vertRect2 = pygame.Rect(left + 190 + 15, top, width, height)
    pygame.draw.rect(DISPLAYSURF, LINECOLOR2, vertRect2)

    left = XMARGIN
    top = YMARGIN + 190
    width = (190 + 15) * BOARDDIMENSIONS[0]
    height = 15

    horizRect1 = pygame.Rect(left, top, width, height)
    pygame.draw.rect(DISPLAYSURF, LINECOLOR2, horizRect1)

    horizRect2 = pygame.Rect(left, top + 190 + 15, width, height)
    pygame.draw.rect(DISPLAYSURF, LINECOLOR2, horizRect2)


def makeEachBoxFalse(val):
    usedBoxes = []
    for i in range(BOARDDIMENSIONS[0]):
        usedBoxes.append([val] * BOARDDIMENSIONS[1])
    return usedBoxes


def getBoxAtPixel(x, y):
    for boxx in range(BOARDDIMENSIONS[0]):
        for boxy in range(BOARDDIMENSIONS[1]):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, 190, 190)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)


def leftTopCoordsOfBox(boxx, boxy):
    left = boxx * (190 + 15) + XMARGIN
    top = boxy * (190 + 15) + YMARGIN
    return left, top


def centerxAndCenteryOfBox(boxx, boxy):
    centerx = boxx * (190 + 15) + XMARGIN + (190 / 2)
    centery = boxy * (190 + 15) + YMARGIN + (190 / 2) + 5
    return centerx, centery


def markBoxX(boxx, boxy, mainFont):
    centerx, centery = centerxAndCenteryOfBox(boxx, boxy)
    mark = mainFont.render('X', True, XCOLOR)
    markRect = mark.get_rect()
    markRect.centerx = centerx
    markRect.centery = centery
    DISPLAYSURF.blit(mark, markRect)


def markBoxO(boxx, boxy, mainFont):
    centerx, centery = centerxAndCenteryOfBox(boxx, boxy)
    mark = mainFont.render('O', True, YCOLOR)
    markRect = mark.get_rect()
    markRect.centerx = centerx
    markRect.centery = centery
    DISPLAYSURF.blit(mark, markRect)


def computerTurnWithAIImpossibleTwist(usedBoxes, mainBoard, lifeOfBox):
    for boxx in range(BOARDDIMENSIONS[0]):
        for boxy in range(BOARDDIMENSIONS[1]):
            mainBoardCopy = copy.deepcopy(mainBoard)
            if usedBoxes[boxx][boxy] == False:
                mainBoardCopy[boxx][boxy] = 'O'
                PLAYERVICTORY, COMPUTERVICTORY = gameWon(mainBoardCopy)

                if COMPUTERVICTORY == True:
                    return boxx, boxy

    mainBoardCopyP = copy.deepcopy(mainBoard)
    usedBoxesCopy = copy.deepcopy(usedBoxes)
    for boxx in range(BOARDDIMENSIONS[0]):
        for boxy in range(BOARDDIMENSIONS[0]):
            if lifeOfBox[boxx][boxy] == 0:
                mainBoardCopyP[boxx][boxy] = False
                usedBoxesCopy[boxx][boxy] = False
    for boxx in range(BOARDDIMENSIONS[0]):
        for boxy in range(BOARDDIMENSIONS[0]):
            mainBoardCopy = copy.deepcopy(mainBoardCopyP)
            if usedBoxesCopy[boxx][boxy] == False:
                mainBoardCopy[boxx][boxy] = 'X'
                PLAYERVICTORY, COMPUTERVICTORY = gameWon(mainBoardCopy)

                if PLAYERVICTORY == True:
                    return boxx, boxy

    mainBoardCopy = copy.deepcopy(mainBoard)

    if mainBoardCopy[1][1] == False:
        return 1, 1

    if ((mainBoardCopy[0][0] == mainBoardCopy[2][2] == 'X') or
            (mainBoardCopy[0][2] == mainBoardCopy[2][0] == 'X')):
        if mainBoardCopy[1][2] == False:
            return 1, 2

    if mainBoard[1][0] == 'X':
        if mainBoard[0][1] == 'X':
            if mainBoard[0][0] == False:
                return 0, 0

    if mainBoard[1][0] == 'X':
        if mainBoard[2][1] == 'X':
            if mainBoard[2][0] == False:
                return 2, 0

    if mainBoard[0][1] == 'X':
        if mainBoard[1][2] == 'X':
            if mainBoard[0][2] == False:
                return 0, 2

    if mainBoard[2][1] == 'X':
        if mainBoard[1][2] == 'X':
            if mainBoard[2][2] == False:
                return 2, 2

    if (mainBoard[0][2] == 'X'):
        if (mainBoard[2][1] == 'X'):
            if mainBoard[1][2] == False:
                return 1, 2
        elif (mainBoard[1][0]):
            if mainBoard[0][1] == False:
                return 0, 1

    if mainBoard[2][2] == 'X':
        if mainBoard[0][1] == 'X':
            if mainBoard[1][2] == False:
                return 1, 2
        elif mainBoard[1][0] == 'X':
            if mainBoard[2][1] == False:
                return 2, 1

    if mainBoard[0][0] == 'X':
        if mainBoard[2][1] == 'X':
            if mainBoard[1][0] == False:
                return 1, 0
        elif mainBoard[1][2] == 'X':
            if mainBoard[0][1] == False:
                return 0, 1

    if mainBoard[2][0] == 'X':
        if mainBoard[1][2] == 'X':
            if mainBoard[2][1] == False:
                return 2, 1
        elif mainBoard[0][1] == 'X':
            if mainBoard[1][0] == False:
                return 1, 0

    xlist = [0, 2, 0, 2]
    ylist = [0, 2, 0, 2]

    random.shuffle(xlist)
    random.shuffle(ylist)

    for x in xlist:
        for y in ylist:
            if mainBoardCopy[x][y] == False:
                return x, y

    for boxx in range(BOARDDIMENSIONS[0]):
        for boxy in range(BOARDDIMENSIONS[1]):
            if mainBoardCopy[boxx][boxy] == False:
                return boxx, boxy


def computerTurnWithAIMedium(usedBoxes, mainBoard):
    for boxx in range(BOARDDIMENSIONS[0]):
        for boxy in range(BOARDDIMENSIONS[1]):
            mainBoardCopy = copy.deepcopy(mainBoard)
            if usedBoxes[boxx][boxy] == False:
                mainBoardCopy[boxx][boxy] = 'O'
                PLAYERVICTORY, COMPUTERVICTORY = gameWon(mainBoardCopy)

                if COMPUTERVICTORY == True:
                    return boxx, boxy

    for boxx in range(BOARDDIMENSIONS[0]):
        for boxy in range(BOARDDIMENSIONS[0]):
            mainBoardCopy = copy.deepcopy(mainBoard)
            if usedBoxes[boxx][boxy] == False:
                mainBoardCopy[boxx][boxy] = 'X'
                PLAYERVICTORY, COMPUTERVICTORY = gameWon(mainBoardCopy)

                if PLAYERVICTORY == True:
                    return boxx, boxy

    while True:
        boxx = random.randint(0,2)
        boxy = random.randint(0,2)

        if usedBoxes[boxx][boxy] == False:
            return boxx, boxy


def computerTurnWithAIEasy(usedBoxes, mainBoard):
    while True:
        boxx = random.randint(0,2)
        boxy = random.randint(0,2)

        if usedBoxes[boxx][boxy] == False:
            return boxx, boxy


def gameWon(mainBoard):
    if ((mainBoard[0][0] == mainBoard[1][0] == mainBoard[2][0] == 'X') or
            (mainBoard[0][1] == mainBoard[1][1] == mainBoard[2][1] == 'X') or
            (mainBoard[0][2] == mainBoard[1][2] == mainBoard[2][2] == 'X') or
            (mainBoard[0][0] == mainBoard[0][1] == mainBoard[0][2] == 'X') or
            (mainBoard[1][0] == mainBoard[1][1] == mainBoard[1][2] == 'X') or
            (mainBoard[2][0] == mainBoard[2][1] == mainBoard[2][2] == 'X') or
            (mainBoard[0][0] == mainBoard[1][1] == mainBoard[2][2] == 'X') or
            (mainBoard[0][2] == mainBoard[1][1] == mainBoard[2][0] == 'X')):

        PLAYERVICTORY = True
        COMPUTERVICTORY = False
        return PLAYERVICTORY, COMPUTERVICTORY


    elif ((mainBoard[0][0] == mainBoard[1][0] == mainBoard[2][0] == 'O') or
          (mainBoard[0][1] == mainBoard[1][1] == mainBoard[2][1] == 'O') or
          (mainBoard[0][2] == mainBoard[1][2] == mainBoard[2][2] == 'O') or
          (mainBoard[0][0] == mainBoard[0][1] == mainBoard[0][2] == 'O') or
          (mainBoard[1][0] == mainBoard[1][1] == mainBoard[1][2] == 'O') or
          (mainBoard[2][0] == mainBoard[2][1] == mainBoard[2][2] == 'O') or
          (mainBoard[0][0] == mainBoard[1][1] == mainBoard[2][2] == 'O') or
          (mainBoard[0][2] == mainBoard[1][1] == mainBoard[2][0] == 'O')):

        PLAYERVICTORY = False
        COMPUTERVICTORY = True
        return PLAYERVICTORY, COMPUTERVICTORY


    else:
        PLAYERVICTORY = False
        COMPUTERVICTORY = False
        return PLAYERVICTORY, COMPUTERVICTORY


def gameOver(usedBoxes, mainBoard):
    for boxx in range(BOARDDIMENSIONS[0]):
        for boxy in range(BOARDDIMENSIONS[1]):
            if usedBoxes[boxx][boxy] == False:
                return False

    else:
        return True


def boardReset(usedBoxes, mainBoard, playerTurnDone, PLAYERVICTORY, COMPUTERVICTORY):
    pygame.time.wait(1000)
    usedBoxes = makeEachBoxFalse(False)
    mainBoard = makeEachBoxFalse(False)
    playerTurnDone = False
    PLAYERVICTORY = COMPUTERVICTORY = False

    return usedBoxes, mainBoard, playerTurnDone, PLAYERVICTORY, COMPUTERVICTORY


def highlightWin(mainBoard):
    scenario1 = 1
    scenario2 = 2
    scenario3 = 3
    scenario4 = 4
    scenario5 = 5
    scenario6 = 6
    scenario7 = 7
    scenario8 = 8

    if mainBoard[0][0] == mainBoard[1][0] == mainBoard[2][0] and (mainBoard[0][0] == 'X' or mainBoard[0][0] == 'O'):
        highLightBoxes(mainBoard, scenario1)


    if mainBoard[0][1] == mainBoard[1][1] == mainBoard[2][1] and (mainBoard[0][1] == 'X' or mainBoard[0][1] == 'O'):
        highLightBoxes(mainBoard, scenario2)


    if mainBoard[0][2] == mainBoard[1][2] == mainBoard[2][2] and (mainBoard[0][2] == 'X' or mainBoard[0][2] == 'O'):
        highLightBoxes(mainBoard, scenario3)


    if mainBoard[0][0] == mainBoard[0][1] == mainBoard[0][2] and (mainBoard[0][0] == 'X' or mainBoard[0][0] == 'O'):
        highLightBoxes(mainBoard, scenario4)


    if mainBoard[1][0] == mainBoard[1][1] == mainBoard[1][2] and (mainBoard[1][0] == 'X' or mainBoard[1][0] == 'O'):
        highLightBoxes(mainBoard, scenario5)


    if mainBoard[2][0] == mainBoard[2][1] == mainBoard[2][2] and (mainBoard[2][0] == 'X' or mainBoard[2][0] == 'O'):
        highLightBoxes(mainBoard, scenario6)


    if mainBoard[0][0] == mainBoard[1][1] == mainBoard[2][2] and (mainBoard[0][0] == 'X' or mainBoard[0][0] == 'O'):
        highLightBoxes(mainBoard, scenario7)


    if mainBoard[2][0] == mainBoard[1][1] == mainBoard[0][2] and (mainBoard[2][0] == 'X' or mainBoard[2][0] == 'O'):
        highLightBoxes(mainBoard, scenario8)


def highLightBoxes(mainBoard, scenario):
    if scenario == 1:
        startPos = (XMARGIN + (190 / 2), YMARGIN + (190 / 2))
        endPos = (XMARGIN + 190 + 15 + 190 + 15 + (190 / 2), YMARGIN + (190 / 2))

        pygame.draw.line(DISPLAYSURF, LINECOLOR, startPos, endPos, 10)

    elif scenario == 2:
        startPos = (XMARGIN + (190 / 2), YMARGIN + 190 + 15 + (190 / 2))
        endPos = (
            XMARGIN + (190 / 2) + 190 + 15 + 190 + 15,
            YMARGIN + 190 + 15 + (190 / 2))

        pygame.draw.line(DISPLAYSURF, LINECOLOR, startPos, endPos, 10)

    elif scenario == 3:
        startPos = (XMARGIN + (190 / 2), YMARGIN + 190 + 15 + 190 + 15 + (190 / 2))
        endPos = (XMARGIN + (190 / 2) + 190 + 15 + 190 + 15,
                  YMARGIN + 190 + 15 + 190 + 15 + (190 / 2))

        pygame.draw.line(DISPLAYSURF, LINECOLOR, startPos, endPos, 10)

    elif scenario == 4:
        startPos = (XMARGIN + (190 / 2), YMARGIN + (190 / 2))
        endPos = (XMARGIN + (190 / 2), YMARGIN + 190 + 15 + 190 + 15 + (190 / 2))

        pygame.draw.line(DISPLAYSURF, LINECOLOR, startPos, endPos, 10)

    elif scenario == 5:
        startPos = (XMARGIN + 190 + 15 + (190 / 2), YMARGIN + (190 / 2))
        endPos = (
            XMARGIN + 190 + 15 + (190 / 2),
            YMARGIN + 190 + 15 + 190 + 15 + (190 / 2))

        pygame.draw.line(DISPLAYSURF, LINECOLOR, startPos, endPos, 10)

    elif scenario == 6:
        startPos = (XMARGIN + 190 + 15 + 190 + 15 + (190 / 2), YMARGIN + (190 / 2))
        endPos = (XMARGIN + 190 + 15 + 190 + 15 + (190 / 2),
                  YMARGIN + 190 + 15 + 190 + 15 + (190 / 2))

        pygame.draw.line(DISPLAYSURF, LINECOLOR, startPos, endPos, 10)

    elif scenario == 7:
        startPos = (XMARGIN + (190 / 2), YMARGIN + (190 / 2))
        endPos = (XMARGIN + 190 + 15 + 190 + 15 + (190 / 2),
                  YMARGIN + 190 + 15 + 190 + 15 + (190 / 2))

        pygame.draw.line(DISPLAYSURF, LINECOLOR, startPos, endPos, 10)

    elif scenario == 8:
        startPos = (XMARGIN + 190 + 15 + 190 + 15 + (190 / 2), YMARGIN + (190 / 2))
        endPos = (XMARGIN + (190 / 2), YMARGIN + 190 + 15 + 190 + 15 + (190 / 2))

        pygame.draw.line(DISPLAYSURF, LINECOLOR, startPos, endPos, 10)


def drawScoreBoard(smallFont, playerScore, other , otherScore):
    scoreBoard = smallFont.render('|Player: ' + str(playerScore) + ' | ' + other + ': ' + str(otherScore) + '|', True, LINECOLOR2, BGCOLOR2)
    scoreBoardRect = scoreBoard.get_rect()
    scoreBoardRect.x = 0
    scoreBoardRect.y = 0
    DISPLAYSURF.blit(scoreBoard, scoreBoardRect)


def drawButtonA(smallFont, text, Y):
    left = True
    while len(text) < 19:
        if left:
            text = ' ' + text
            left = False
        else:
            text = text + ' '
            left = True
    if 130 < MOUSE_X < 590 and Y < MOUSE_Y < Y+40:
        button = smallFont.render(text, True, LINECOLOR2, lighterColor(BGCOLOR2))
        if mouseClicked:
            return True
    else:
        button = smallFont.render(text, True, LINECOLOR2, BGCOLOR2)


    buttonRect = button.get_rect()
    buttonRect.x = 130
    buttonRect.y = Y
    DISPLAYSURF.blit(button, buttonRect)
    return False


def returnToMenuButton(smallFont):
    if 0 < MOUSE_X < 340 and 670 < MOUSE_Y < 720:
        button = smallFont.render('Return to Menu', True, LINECOLOR2, lighterColor(BGCOLOR2))
        if mouseClicked:
            return True
    else:
        button = smallFont.render('Return to Menu', True, LINECOLOR2, BGCOLOR2)


    buttonRect = button.get_rect()
    buttonRect.x = 0
    buttonRect.y = 670
    DISPLAYSURF.blit(button, buttonRect)
    return False



def LOGO(logoFont):

    button = logoFont.render('TIC-TAC-TOE', True, LINECOLOR2, BGCOLOR)
    buttonRect = button.get_rect()
    buttonRect.x = 100
    buttonRect.y = 200
    DISPLAYSURF.blit(button, buttonRect)


def lighterColor(color):
    tcolor = copy.deepcopy(color)
    tcolor[0] += 30
    tcolor[1] += 30
    tcolor[2] += 30
    for i in range(0, 3):
        if tcolor[i] > 255:
            tcolor[i] = 255
    return tcolor


def lifeManagementBox(mainBoard, usedBoxes, lifeOfBox):
    for boxx in range(0, BOARDDIMENSIONS[0]):
        for boxy in range(0, BOARDDIMENSIONS[1]):
            if lifeOfBox[boxx][boxy] == 0:
                mainBoard[boxx][boxy] = False
                usedBoxes[boxx][boxy] = False
            else:
                lifeOfBox[boxx][boxy] -= 1

if __name__ == '__main__':
    main()