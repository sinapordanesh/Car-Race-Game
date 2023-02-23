import math
import random
import pygame
import CarModule


class CarRace:

    def __init__(self):

        pygame.init()

        self.Crash_Sound = pygame.mixer.Sound('lose-m.wav')
        pygame.mixer.music.load('world-m.ogg')

        # ----------------------Objects-----------------
        self.Car_Class_Values = CarModule.Car(('scared.png', 64, 64))
        self.Screen_Class_Values = CarModule.Screen((800, 600), 'dodge')
        # self.Cube_Class_Values = CarModule.Cubes((random.randint(0, self.Screen_Class_Values.GetDisplaySize()[0])
        #                                           , -300)
        #                                          , (random.randint(50, 100)
        #                                             , random.randint(50, 100))
        #                                          , (random.randint(30, 220)
        #                                             , random.randint(30, 220)
        #                                             , random.randint(30, 220)))
        #
        # self.Cube_List = [self.Cube_Class_Values.GetCubePosition()
        #     , self.Cube_Class_Values.GetCubeSize()
        #     , self.Cube_Class_Values.GetCubeColor()]

        # self.Cube_List.append(self.Cube_Class_Values.GetCubeSize())
        # , self.Cube_Class_Values.GetCubePosition()
        # , self.Cube_Class_Values.GetCubeColor())

        # ----------------------Screen-------------------
        self.Display_Width = self.Screen_Class_Values.GetDisplaySize()[0]
        self.Display_High = self.Screen_Class_Values.GetDisplaySize()[1]
        self.Game_Display = pygame.display.set_mode((self.Display_Width, self.Display_High))

        # ----------------------Game---------------------
        self.Game_Name = self.Screen_Class_Values.GetGameName()
        # self.CarFeature = self.Car_Class_Values.CarFeature()

        self.Clock = pygame.time.Clock()

        self.Intro = True
        self.Run = True

        # -----------------Color-----------------------
        self.Red = (253, 34, 15)
        self.Green = (36, 244, 15)
        self.Blue = (28, 119, 255)
        self.Back_Ground = (255, 255, 255)
        # self.Green_Cold = pass

        # -----------------Cube-------------------------
        # self.Init_Cube_Speed = 8
        # self.MoveCube = self.Cube_List[0][1]

        # ----------------Car--------------------------
        self.CarImage = pygame.image.load(self.Car_Class_Values.CarFeature()[0])
        self.Car_Width = self.Car_Class_Values.CarFeature()[1]
        self.Car_High = self.Car_Class_Values.CarFeature()[2]
        self.Car_X_Pos = self.Display_Width * 0.45
        self.Car_Y_Pos = self.Display_High * 0.8
        self.Car_Speed = 0
        self.Init_Car_X_Pos_Change = 8

        # ---------------Score------------------------
        # self.Score_Init_Count = 0

    def SetCubeValues(self) -> []:
        self.Cube_Class_Values = CarModule.Cubes(
            (random.randint(0, (self.Screen_Class_Values.GetDisplaySize()[0] - 100))
             , -500)
            , (random.randint(50, 100)
               , random.randint(50, 100))
            , (random.randint(30, 220)
               , random.randint(30, 220)
               , random.randint(30, 220)))

        self.Cube_List = [self.Cube_Class_Values.GetCubePosition()
            , self.Cube_Class_Values.GetCubeSize()
            , self.Cube_Class_Values.GetCubeColor()]

        return self.Cube_List

    def GameIntro(self) -> None:

        pygame.mixer.music.stop()

        self.Gametitle(self.Game_Name)

        while self.Intro:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.Game_Display.fill(self.Back_Ground)
            self.MessageWrite(('freesansbold.ttf', 90), "Geniuse! Let's go", (self.Display_Width / 2),
                              (self.Display_High / 2))
            self.Mose_Pos = self.MousePosition()
            self.Cli_Pos = self.ClickPressPosition()
            self.Button('Go!', 150, 450, 100, 50, self.Green, self.Blue, self.Mose_Pos, self.Cli_Pos, self.RunGame)
            self.Button('Exit!', 550, 450, 100, 50, self.Red, self.Blue, self.Mose_Pos, self.Cli_Pos, quit)
            # print(self.SetCubeValues())
            pygame.display.update()

    def RunGame(self) -> None:

        pygame.mixer.music.play(-1)

        self.Car_Speed = 0
        self.Car_X_Pos = self.Display_Width * 0.45

        self.Init_Score_Count = 0
        self.Init_Cube_Speed = 8

        self.Gametitle(self.Game_Name)
        # self.CarPicture(self.CarFeature[0])

        self.SetCubeValues()
        self.Start_Cube_Y = self.Cube_List[0][1]

        while self.Run:

            self.Cli_Pos = self.ClickPressPosition()
            self.Mose_Pos = self.MousePosition()
            self.Handle = CarModule.Click.HandleClick(self)

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         quit()
            #
            #     elif event.type == pygame.KEYDOWN:
            #         if event.key == pygame.K_LEFT:
            #             self.Car_Speed = CarModule.Car.CarMove(self, self.Car_Speed, self.Car_X_Pos_Change, 1)
            #         elif event.key == pygame.K_RIGHT:
            #             self.Car_Speed = CarModule.Car.CarMove(self, self.Car_Speed, self.Car_X_Pos_Change, 2)
            #     elif event.type == pygame.KEYUP:
            #         self.Car_Speed = CarModule.Car.CarMove(self, self.Car_Speed, self.Car_X_Pos_Change, 3)
            #
            # self.Car_X_Pos += self.Car_Speed

            # print(self.Handle)

            # ------------------------------------------------Handle Click-----------------------------------------------
            if self.Handle == 1:
                self.Car_Speed = CarModule.Car.CarMove(self, self.Car_Speed, self.Init_Car_X_Pos_Change, 1)
            elif self.Handle == 2:
                self.Car_Speed = CarModule.Car.CarMove(self, self.Car_Speed, self.Init_Car_X_Pos_Change, 2)
            elif self.Handle == 3:
                self.Car_Speed = CarModule.Car.CarMove(self, self.Car_Speed, self.Init_Car_X_Pos_Change, 3)
            elif self.Handle == 0:
                pygame.quit()
                quit()

            self.Car_X_Pos = CarModule.Car.CarMoveLimit(self, self.Car_X_Pos, self.Car_Width, self.Display_Width)
            self.Car_X_Pos += self.Car_Speed

            # if self.Car_X_Pos >= self.Display_Width:
            #     self.Car_X_Pos = 0 - self.Car_Width
            # elif self.Car_X_Pos + self.Car_Width <= 0:
            #     self.Car_X_Pos = self.Display_Width

            # print(self.Car_X_Pos, self.Display_Width)

            # -----------------------------------------------------------------------------------------------------------

            self.Game_Display.fill(self.Back_Ground)
            self.Button('Menu', 0, 25, 65, 25, self.Blue, self.Red, self.Mose_Pos, self.Cli_Pos, self.GameIntro)

            # --------------------------------------------------Car-----------------------------------------------------
            self.CarPicture(self.CarImage, self.Car_X_Pos, self.Car_Y_Pos)
            # ----------------------------------------------------------------------------------------------------------

            self.CreateTextMessage(self.Init_Score_Count, 'Score :', 25, (0, 0), self.Red)

            # --------------------------------------------------Cube----------------------------------------------------

            self.Start_Cube_Y = CarModule.Cubes.MoveCube(self, self.Start_Cube_Y
                                                         , self.Init_Cube_Speed
                                                         , self.Display_High
                                                         , self.Cube_List[1][1])
            self.CubeCreator()

            if self.Start_Cube_Y >= self.Display_High:
                self.Init_Score_Count += 1
                self.SetCubeValues()
            # ----------------------------------------------------------------------------------------------------------

            # -----------------------------------------------Game--------------------------------------------------------
            self.Start_Cube_X = self.Cube_List[0][0]
            self.Cube_Width = self.Cube_List[1][0]
            self.Cube_High = self.Cube_List[1][1]

            self.Accident = CarModule.Car.CarCubeAccident(self, self.Car_X_Pos, self.Car_Y_Pos, self.Car_Width,
                                                          self.Car_High
                                                          , self.Start_Cube_X, self.Start_Cube_Y, self.Cube_Width,
                                                          self.Cube_High)
            if self.Accident is True:
                self.GameLose()

            #?????????????????????:
            # if CarModule.Cubes.GameDifficulties(self, self.Init_Score_Count, 5) is True:
            #     self.Init_Cube_Speed += 1

            # -----------------------------------------------------------------------------------------------------------

            # print(self.Accident)
            # pygame.display.flip()
            pygame.display.update()
            self.Clock.tick(90)

    def GameLose(self):

        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(self.Crash_Sound)

        self.MessageWrite(('freesansbold.ttf', 90), 'Game Over!', (self.Display_Width / 2), (self.Display_High / 2))

        while True:

            self.Handle = CarModule.Click.HandleClick(self)
            if self.Handle == 0:
                pygame.quit()
                quit()

            self.Mose_Pos = self.MousePosition()
            self.Cli_Pos = self.ClickPressPosition()

            self.Button('Play Again', 325, 450, 150, 50, self.Green, self.Blue, self.Mose_Pos, self.Cli_Pos,
                        self.RunGame)
            self.Button('Menu', 0, 25, 65, 25, self.Blue, self.Red, self.Mose_Pos, self.Cli_Pos, self.GameIntro)

            pygame.display.update()

    def Gametitle(self, txt: str) -> None:
        pygame.display.set_caption(txt)

    def CarPicture(self, _txt, _Pos_X: int, _Pos_Y: int) -> None:
        self.Game_Display.blit(self.CarImage, (_Pos_X, _Pos_Y))

    # def CarPicture(self, _txt, _Pos_X: int, _Pos_Y: int) -> None:
    #     self.Game_Display.blit(self.CarImage, (_Pos_X * 0.45, _Pos_Y * 0.8))

    def MousePosition(self) -> (int, int):
        return pygame.mouse.get_pos()

    def ClickPressPosition(self) -> (int, int, int):
        return pygame.mouse.get_pressed()

    def CreateTextMessage(self, _Count: int, _Msg: str, _FontSize: int, _Position: (int, int), _Text_Color) -> None:
        self.Font = pygame.font.SysFont(None, _FontSize)
        self.Text = self.Font.render(_Msg + str(_Count), True, _Text_Color)
        self.Game_Display.blit(self.Text, _Position)

    # def CubeCreator(self, _X: int, _Y: int, _W: int, _H: int, _Color: int) -> None:
    #     pygame.draw.rect(self.Game_Display, _Color, [_X, _Y, _W, _H])

    def CubeCreator(self) -> None:
        pygame.draw.rect(self.Game_Display
                         , self.Red
                         , [self.Cube_List[0][0]
                             , self.Start_Cube_Y
                             , self.Cube_List[1][0]
                             , self.Cube_List[1][1]])
        pygame.display.update()

    # def CubeRenew(self, _Y: int):
    #
    #     if self.Start_Cube_Y >= self.Screen_Class_Values.GetDisplaySize()[1]:
    #         self.Start_Cube_Y = 0 - self.Cube_List[1][1]
    #         self.SetCubeValues()

    def Button(self
               , _Msg: str
               , _X: int
               , _Y: int
               , _W: int
               , _H: int
               , _Inactive
               , _Active
               , _MousePos: (int, int)
               , _ClicPressPos: (int, int, int)
               , _Action=None) -> None:

        if CarModule.Screen.ButtonActivation(None, _X, _Y, _W, _H, _MousePos):
            pygame.draw.rect(self.Game_Display, _Active, (_X, _Y, _W, _H))

            if _ClicPressPos[0] == 1 and _Action is not None:
                _Action()

                # if _Action == '1' :
                #     self.RunGame()

        else:
            pygame.draw.rect(self.Game_Display, _Inactive, (_X, _Y, _W, _H))

        self.MessageWrite(('freesansbold.ttf', 20), _Msg, (_X + (_W / 2)), (_Y + (_H / 2)))

    def Text_Objects(self, _Text, _Font):
        self.TextSurface = _Font.render(_Text, True, (0, 0, 0))
        return self.TextSurface, self.TextSurface.get_rect()

    def MessageWrite(self, _Font: (str, int), _Msg: str, _X: float, _Y: float) -> None:
        self.TargetText = pygame.font.Font(_Font[0], _Font[1])
        self.TextSurf, self.TextRect = self.Text_Objects(_Msg, self.TargetText)
        self.TextRect.center = (_X, _Y)
        self.Game_Display.blit(self.TextSurf, self.TextRect)

    # def TextMessage(self, _Count:int, _Fix_Text:str, _Font_Size:int, _Color,_Position:(int, int)):
    #     self.Font = pygame.font.SysFont(None, _Font_Size)
    #     self.text


if __name__ == '__main__':
    CarRace().GameIntro()
