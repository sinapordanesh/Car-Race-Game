import math
import random
import pygame


class Car:

    def __init__(self, _Car_Feature: (str, int, int)):
        self.Car_Name = _Car_Feature[0]
        self.Car_Width = _Car_Feature[1]
        self.Car_High = _Car_Feature[2]

        # self.Car_X_Pos = _Car_X_Pos

    def CarFeature(self) -> (str, int, int):
        return self.Car_Name, self.Car_Width, self.Car_High

    def CarMove(self, _Car_Speed: int, _Car_X_Pos_Change: int, _Condition: int) -> int:

        if _Condition == 1:
            _Car_Speed = -_Car_X_Pos_Change

        elif _Condition == 2:
            _Car_Speed = _Car_X_Pos_Change

        elif _Condition == 3:
            _Car_Speed = 0

        return _Car_Speed

    # def CarMove(self, _Car_Speed: int, _Car_X_Pos_Change: int, _Condition: int) -> int:
    #
    #     if _Condition == 1:
    #         _Car_Speed = -_Car_X_Pos_Change
    #
    #     elif _Condition == 2:
    #         _Car_Speed = _Car_X_Pos_Change
    #
    #     elif _Condition == 3:
    #         _Car_Speed = 0
    #
    #     return _Car_Speed

    def CarMoveLimit(self, _Car_X_Pos: int, _Car_Width: int, _Display_Width):

        if _Car_X_Pos >= _Display_Width:
            _Car_X_Pos = 0 - _Car_Width
        elif _Car_X_Pos + _Car_Width <= 0:
            _Car_X_Pos = _Display_Width

        return _Car_X_Pos

    def CarCubeAccident(self, _Car_X_Pos: float, _Car_Y_Pos: float, _Car_W: float, _Car_H: float
                        , _Cube_X_Pos: float, _Cube_Y_Pos: float, _Cube_W: float, _Cube_H: float) -> bool:

        if (_Cube_Y_Pos <= _Car_Y_Pos <= _Cube_Y_Pos + _Cube_H) or \
                (_Cube_Y_Pos <= _Car_Y_Pos + _Car_H <= _Cube_Y_Pos + _Cube_H):
            if (_Cube_X_Pos <= _Car_X_Pos <= _Cube_X_Pos + _Cube_W) or \
                    (_Cube_X_Pos <= _Car_X_Pos + _Car_W <= _Cube_X_Pos + _Cube_W):
                return True


class Cubes:
    def __init__(self, _Cube_Pose: (int, int)
                 , _Cube_Size: (int, int)
                 , _Cube_Color: (int, int, int)):
        self.Cube_X = _Cube_Pose[0]
        self.Cube_Y = _Cube_Pose[1]

        self.Cube_W = _Cube_Size[0]
        self.Cube_H = _Cube_Size[1]

        self.Cube_Color_R = _Cube_Color[0]
        self.Cube_Color_G = _Cube_Color[1]
        self.Cube_Color_B = _Cube_Color[2]

    def GetCubePosition(self) -> (int, int):
        return self.Cube_X, self.Cube_Y

    def GetCubeSize(self) -> (int, int):
        return self.Cube_W, self.Cube_H

    def GetCubeColor(self) -> (int, int, int):
        return self.Cube_Color_R, self.Cube_Color_G, self.Cube_Color_B

    def MoveCube(self, _Pos_Y: int, _Speed: int, _Display_High: (int, int), _Cube_high: int) -> int:

        if _Pos_Y < _Display_High:
            _Pos_Y += _Speed
            return _Pos_Y

        elif _Pos_Y >= _Display_High:
            _Pos_Y = 0 - _Cube_high
            return _Pos_Y

    def GameDifficulties(self, _Object_Numbers: int, _Difficulties_Grade: int) -> bool:
        if _Object_Numbers % _Difficulties_Grade == 0:
            return True


class Screen:
    def __init__(self, _Display_Size: (int, int)
                 , _Game_Name: str):
        self.Display_width = _Display_Size[0]
        self.Display_high = _Display_Size[1]

        self.Game_Name = _Game_Name

    def GetDisplaySize(self) -> (int, int):
        return self.Display_width, self.Display_high

    def GetGameName(self) -> str:
        return self.Game_Name

    def ButtonActivation(self, _X: int, _Y: int, _W: int, _H: int, _MosPos: (int, int)) -> bool:
        if _X < _MosPos[0] < _X + _W and _Y < _MosPos[1] < _Y + _H:
            return True

    # def Button(self
    #            , _Msg: str
    #            , _X: int
    #            , _Y: int
    #            , _W: int
    #            , _H: int
    #            , _Inactive
    #            , _Active
    #            , _MousePos: (int, int)
    #            , _ClicPressPos: (int, int)
    #            , _Action=None):
    #     pass
    #
    # def Text_Objects(self, _Text, _Font):
    #
    #     self.TextSurface = _Font.render(_Text, True, (0, 0, 0))
    #     return self.TextSurface, self.TextSurface.get_rect()
    #
    # def MessageWrite(self, _Font: (str, int), _Msg: str, _X: float, _Y: float):
    #
    #     self.TargetText = pygame.font.Font(_Font[0], _Font[1])
    #     self.TextSurf, self.TextRect = self.Text_Objects(_Msg, self.TargetText)
    #     self.TextRect.center = (_X, _Y)


class Click:

    def __init__(self) -> None:
        pass

    def HandleClick(self) -> int:
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                return 0
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_LEFT:
                    return 1
                elif self.event.key == pygame.K_RIGHT:
                    return 2
            elif self.event.type == pygame.KEYUP:
                if self.event.key == pygame.K_LEFT or self.event.key == pygame.K_RIGHT:
                    return 3

# class Click:
#
#     def __init__(self) -> None:
#         pass
#
#     def Quit(self) -> bool:
#         for self.event in pygame.event.get():
#             if self.event.type == pygame.QUIT:
#                 return True
#
#     def ClickDown(self) -> int:
#         for self.event in pygame.event.get():
#             if self.event.type == pygame.KEYDOWN:
#                 if self.event.key == pygame.K_LEFT:
#                     return 1
#                 elif self.event.key == pygame.K_RIGHT:
#                     return 2
#             elif self.event.type == pygame.KEYUP:
#                 if self.event.key == pygame.K_LEFT or self.event.key == pygame.K_RIGHT:
#                     return 3
