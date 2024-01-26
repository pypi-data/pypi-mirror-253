#  Hue Engine ©️
#  2023-2024 Setoichi Yumaden <setoichi.dev@gmail.com>
#
#  This software is provided 'as-is', without any express or implied
#  warranty.  In no event will the authors be held liable for any damages
#  arising from the use of this software.
#
#  Permission is granted to anyone to use this software for any purpose,
#  including commercial applications, and to alter it and redistribute it
#  freely, subject to the following restrictions:
#
#  1. The origin of this software must not be misrepresented; you must not
#     claim that you wrote the original software. If you use this software
#     in a product, an acknowledgment in the product documentation would be
#     appreciated but is not required.
#  2. Altered source versions must be plainly marked as such, and must not be
#     misrepresented as being the original software.
#  3. This notice may not be removed or altered from any source distribution.

import pygame as pg, pygetwindow as gw, sys, random, os, re, math
from pygame.locals import QUIT,KEYDOWN,KEYUP,MOUSEBUTTONDOWN,MOUSEBUTTONUP
from Hue.version import __versionTag__
from screeninfo import get_monitors

pgRect = pg.Rect
pgEvent = pg.Event
QuitEvent = pg.QUIT
KeyUpEvent = pg.KEYUP
pgSurface = pg.Surface
KeyDownEvent = pg.KEYDOWN
Vector2 = pg.math.Vector2
Clock = pg.time.Clock
ShowCursor = pg.mouse.set_visible
GetKeyPresses = pg.key.get_pressed
MouseButtonUpEvent = pg.MOUSEBUTTONUP
MouseButtonDownEvent = pg.MOUSEBUTTONDOWN

class BoolPair:
    def __init__(self, x:bool=False, y:bool=False) -> None:
        self.x = x
        self.y = y

class Keyboard:
    # Letter keys
    A = pg.K_a
    B = pg.K_b
    C = pg.K_c
    D = pg.K_d
    E = pg.K_e
    F = pg.K_f
    G = pg.K_g
    H = pg.K_h
    I = pg.K_i
    J = pg.K_j
    K = pg.K_k
    L = pg.K_l
    M = pg.K_m
    N = pg.K_n
    O = pg.K_o
    P = pg.K_p
    Q = pg.K_q
    R = pg.K_r
    S = pg.K_s
    T = pg.K_t
    U = pg.K_u
    V = pg.K_v
    W = pg.K_w
    X = pg.K_x
    Y = pg.K_y
    Z = pg.K_z

    # Number keys
    Num0 = pg.K_0
    Num1 = pg.K_1
    Num2 = pg.K_2
    Num3 = pg.K_3
    Num4 = pg.K_4
    Num5 = pg.K_5
    Num6 = pg.K_6
    Num7 = pg.K_7
    Num8 = pg.K_8
    Num9 = pg.K_9

    # Function keys
    F1 = pg.K_F1
    F2 = pg.K_F2
    F3 = pg.K_F3
    F4 = pg.K_F4
    F5 = pg.K_F5
    F6 = pg.K_F6
    F7 = pg.K_F7
    F8 = pg.K_F8
    F9 = pg.K_F9
    F10 = pg.K_F10
    F11 = pg.K_F11
    F12 = pg.K_F12

    # Special keys
    Space = pg.K_SPACE
    Escape = pg.K_ESCAPE
    Enter = pg.K_RETURN
    Tab = pg.K_TAB
    Shift = pg.K_LSHIFT  # Left Shift
    Ctrl = pg.K_LCTRL    # Left Control
    Alt = pg.K_LALT      # Left Alt
    RShift = pg.K_RSHIFT  # Right Shift
    RCtrl = pg.K_RCTRL    # Right Control
    RAlt = pg.K_RALT      # Right Alt

    # Arrow keys
    Up = pg.K_UP
    Down = pg.K_DOWN
    Left = pg.K_LEFT
    Right = pg.K_RIGHT

    # Numpad keys
    NumPad0 = pg.K_KP0
    NumPad1 = pg.K_KP1
    NumPad2 = pg.K_KP2
    NumPad3 = pg.K_KP3
    NumPad4 = pg.K_KP4
    NumPad5 = pg.K_KP5
    NumPad6 = pg.K_KP6
    NumPad7 = pg.K_KP7
    NumPad8 = pg.K_KP8
    NumPad9 = pg.K_KP9
    NumPadDivide = pg.K_KP_DIVIDE
    NumPadMultiply = pg.K_KP_MULTIPLY
    NumPadSubtract = pg.K_KP_MINUS
    NumPadAdd = pg.K_KP_PLUS
    NumPadEnter = pg.K_KP_ENTER
    NumPadDecimal = pg.K_KP_PERIOD

    # Modifier keys
    LShift = pg.K_LSHIFT
    RShift = pg.K_RSHIFT
    LCtrl = pg.K_LCTRL
    RCtrl = pg.K_RCTRL
    LAlt = pg.K_LALT
    RAlt = pg.K_RALT
    LMeta = pg.K_LMETA
    RMeta = pg.K_RMETA
    LSuper = pg.K_LSUPER  # Windows key for left
    RSuper = pg.K_RSUPER  # Windows key for right

    # Miscellaneous keys
    CapsLock = pg.K_CAPSLOCK
    NumLock = pg.K_NUMLOCK
    ScrollLock = pg.K_SCROLLOCK
    PrintScreen = pg.K_PRINT
    Pause = pg.K_PAUSE
    Insert = pg.K_INSERT
    Delete = pg.K_DELETE
    Home = pg.K_HOME
    End = pg.K_END
    PageUp = pg.K_PAGEUP
    PageDown = pg.K_PAGEDOWN

    # Symbol keys
    Grave = pg.K_BACKQUOTE  # `~
    Minus = pg.K_MINUS      # -_
    Equals = pg.K_EQUALS    # =+
    LeftBracket = pg.K_LEFTBRACKET   # [{
    RightBracket = pg.K_RIGHTBRACKET # ]}
    Backslash = pg.K_BACKSLASH       # \|
    Semicolon = pg.K_SEMICOLON       # ;:
    Quote = pg.K_QUOTE               # '"
    Comma = pg.K_COMMA               # ,<
    Period = pg.K_PERIOD             # .>
    Slash = pg.K_SLASH               # /?
    BackSpace = pg.K_BACKSPACE
    Tab = pg.K_TAB
    Enter = pg.K_RETURN
    Menu = pg.K_MENU

class Controller:
    # Buttons
    A = pg.CONTROLLER_BUTTON_A
    B = pg.CONTROLLER_BUTTON_B
    X = pg.CONTROLLER_BUTTON_X
    Y = pg.CONTROLLER_BUTTON_Y
    Back = pg.CONTROLLER_BUTTON_BACK
    Guide = pg.CONTROLLER_BUTTON_GUIDE
    Start = pg.CONTROLLER_BUTTON_START
    LeftStick = pg.CONTROLLER_BUTTON_LEFTSTICK
    RightStick = pg.CONTROLLER_BUTTON_RIGHTSTICK
    LeftShoulder = pg.CONTROLLER_BUTTON_LEFTSHOULDER
    RightShoulder = pg.CONTROLLER_BUTTON_RIGHTSHOULDER
    DpadUp = pg.CONTROLLER_BUTTON_DPAD_UP
    DpadDown = pg.CONTROLLER_BUTTON_DPAD_DOWN
    DpadLeft = pg.CONTROLLER_BUTTON_DPAD_LEFT
    DpadRight = pg.CONTROLLER_BUTTON_DPAD_RIGHT

    # Axes
    LeftX = pg.CONTROLLER_AXIS_LEFTX
    LeftY = pg.CONTROLLER_AXIS_LEFTY
    RightX = pg.CONTROLLER_AXIS_RIGHTX
    RightY = pg.CONTROLLER_AXIS_RIGHTY
    TriggerLeft = pg.CONTROLLER_AXIS_TRIGGERLEFT
    TriggerRight = pg.CONTROLLER_AXIS_TRIGGERRIGHT
    
    def init(self) -> None:
        pg.joystick.init()

class Mouse:
    LeftClick = 1
    WheelClick = 2
    RightClick = 3
    WheelUp = 4
    WheelDown = 5

class FPSMonitor:
    def __init__(self) -> None:
        """
        Initializes the FPSMonitor object.

        Attributes:
            peak_fps (float): The highest FPS value reached.
            total_frames (int): The total number of frames that have been rendered.
            total_fps (float): The sum of all FPS values, used to calculate the average FPS.
        """
        self.peakFps = 0.0
        self.totalFrames = 0
        self.totalFps = 0.0

    def update(self, currentFps:float) -> None:
        """
        Updates the FPS values with the current FPS.

        Args:
            current_fps (float): The current FPS value from pg.time.Clock().get_fps().
        """
        # Update the peak FPS if the current FPS is higher than the previously recorded peak
        self.peakFps = max(self.peakFps, currentFps)

        # Increment the total frames and add the current FPS to the total_fps
        self.totalFrames += 1
        self.totalFps += currentFps

    def getCurrentFps(self, clock) -> float:
        """
        Retrieves the current FPS from the provided frame clock.

        Args:
            clock (pg.time.Clock): The frame clock object.

        Returns:
            float: The current FPS value.
        """
        return clock.get_fps()

    def getPeakFps(self) -> float:
        """
        Returns the peak FPS value.

        Returns:
            float: The highest FPS value reached.
        """
        return self.peakFps

    def getAverageFps(self) -> float:
        """
        Calculates and returns the average FPS value.

        Returns:
            float: The average FPS value.
        """
        return self.totalFps / self.totalFrames if self.totalFrames > 0 else 0.0

    def getFpsData(self, clock) -> str:
        """
        Returns the current, peak, and average FPS values.

        Args:
            clock (pg.time.Clock): The frame clock object.

        Returns:
            str: A string containing the current FPS, peak FPS, and average FPS.
        """
        currentFps = self.getCurrentFps(clock)
        self.update(currentFps)
        peakFps = self.getPeakFps()
        averageFps = self.getAverageFps()
        return f"FPS | current | {int(currentFps)} | peak | {int(peakFps)} | avg. | {int(averageFps)}"

class DebugInterface:
    def __init__(self, displaySurface:pgSurface, position:Vector2, gameClock:Clock, interfaceSize:Vector2=(180,80), fontSize:int=24) -> None:
        self.scope = []
        self.fontSize = fontSize
        self.displaySurface = displaySurface
        self.font = pg.font.Font(size=fontSize)
        self.interfaceRect = pgRect((position.x, position.y), interfaceSize)
        self._monitor = FPSMonitor()
        self._clock = gameClock

    def AddToInterface(self, Info) -> None:
        if Info not in self.scope:
            self.scope.append(str(Info))

    def SetFontSize(self, fontSize:int=24):
        self.fontSize = fontSize
        self.font = pg.font.Font(size=fontSize)

    def VisualOutput(self) -> None:
        self.AddToInterface(self._monitor.getFpsData(self._clock))
        for i,j in enumerate(self.scope):
            debugInfo = self.font.render(str(j), antialias=True, color=[255,255,255], bgcolor=[0,0,0])
            self.displaySurface.blit(debugInfo,(self.interfaceRect.x,self.interfaceRect.y+(i*(debugInfo.get_height() + 8))))
        self.scope.clear()

def CreateWindow(windowSize:Vector2=Vector2(800,600), FLAG:list|tuple|int=[]) -> pgSurface:
    return pg.display.set_mode((windowSize.x,windowSize.y), *FLAG)

def CreateClock() -> pg.time.Clock:
    return pg.time.Clock()

def GetEvents(quitFlag:bool|int) -> list:
    if (quitFlag):
        pg.quit()
        print("Hue Engine Exited!\n")
        sys.exit()
    for e in pg.event.get():
        if e.type == QUIT:
            pg.quit()
            print("Hue Engine Exited!\n")
            sys.exit()
        if e.type == KEYDOWN or e.type == KEYUP:
            return [e.type, e.key]
        if e.type == MOUSEBUTTONDOWN or e.type == MOUSEBUTTONUP:
            return [e.type, e.button]

def GetKeyState() -> tuple|pg.key.ScancodeWrapper:
    return pg.key.get_pressed()

def SendFrame() -> None:
    pg.display.flip()

def Exit(e:pgEvent) -> None:
    if (e and e[0] == pg.QUIT):
        print("\Hue Engine Exited!\n")
        pg.quit()
        sys.exit()

def RandomColor() -> list:
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    return [r,g,b]

def FillSurface(surf:pgSurface, color:tuple|list=RandomColor()) -> bool:
    if (surf.fill(color)):
        return True;
    return False;

def NaturalKey(string_) -> int|str:
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

def SetTitle(title:str=f"{__versionTag__}") -> None:
    pg.display.set_caption(title)

def GetMousePosition() -> Vector2:
    return Vector2(*pg.mouse.get_pos())

def Blit(destSurf:pgSurface, toBlit:pgSurface, position:Vector2) -> None:
    if not position: destSurf.blit(toBlit, toBlit.get_rect())
    else: destSurf.blit(toBlit, (position.x, position.y))

def LoadSurface(path: str) -> pgSurface:
    canonicalizedPath = path.replace('/', os.sep).replace('\\', os.sep)
    image = pg.image.load(canonicalizedPath).convert_alpha()
    return image

def LoadSurfaceDir(path: str) -> list:
    surfaceList = []
    for _, __, imageFiles in os.walk(path):
        sortedFiles = sorted(imageFiles, key=NaturalKey)
        for image in sortedFiles:
            fullPath = path + '/' + image
            imageSurface = LoadSurface(fullPath)
            surfaceList.append(imageSurface)

    return surfaceList

def LoadSurfaceDirNum(path: str) -> list:
    surfaceList = []
    fileList = []
    for _, __, imageFiles in os.walk(path):
        for index, image in enumerate(imageFiles):
            fileList.append(image)
        # sort images based on numerical values in the image names: run1.png will always come before run12.png as walk doesnt sort files returned.
        fileList.sort(key=lambda image: int(
            ''.join(filter(str.isdigit, image))))
        for index, image in enumerate(fileList):
            fullPath = path + '/' + image
            imageSurface = LoadSurface(fullPath).convert_alpha()
            imageSurface.set_colorkey([0, 0, 0])
            surfaceList.append(imageSurface)
    return surfaceList

def ScaleSurface(surf:pgSurface, size:list|tuple) -> pgSurface:
    newSurface = pg.transform.scale(surface=surf,size=size)
    return pgSurface(size[0], size[1], newSurface.get_rect().topleft)

def ScaleSurfaces(surfs: list, size: tuple) -> list:
    scaled_images = []
    for surf in surfs:
        scaled_images.append(ScaleSurface(surf, size))
    return scaled_images

def SurfaceCutout(surf: pgSurface, cutSize: int) -> list:
    surface = surf
    surfNumX = int(surface.get_size()[0] / cutSize)
    surfNumY = int(surface.get_size()[1] / cutSize)

    cutSurfs = []
    for row in range(surfNumY):
        for col in range(surfNumX):
            x = col * cutSize
            y = row * cutSize
            newSurf = pgSurface(
                (cutSize, cutSize), flags=pg.SRCALPHA)
            newSurf.blit(surface, (0, 0), pg.Rect(
                x, y, cutSize, cutSize))
            cutSurfs.append(newSurf)

    return cutSurfs

def LoadSurfaceCutout(path: str, cutSize: int) -> list:
    surface = LoadSurface(path)
    surfNumX = int(surface.get_size()[0] / cutSize)
    surfNumY = int(surface.get_size()[1] / cutSize)
    cutSurfs = []
    for row in range(surfNumY):
        for col in range(surfNumX):
            x = col * cutSize
            y = row * cutSize
            newSurf = pgSurface((cutSize, cutSize), flags=pg.SRCALPHA).convert_alpha()
            newSurf.blit(surface, (0, 0), pg.Rect(x, y, cutSize, cutSize))
            cutSurfs.append(newSurf)
    return cutSurfs

_textLibrary = {}
def RenderText(surf:pg.Surface, ttfPath:str=None, text:str="text", position:pg.math.Vector2=pg.math.Vector2, size:int=30, color:list|tuple=(255,255,255), bgColor=None, center=True) -> None:
    global _textLibrary
    textSurf = _textLibrary.get(f"{text}{color}{size}")
    if textSurf is None:
        if ttfPath != None:
            font = pg.font.Font(ttfPath, size)
        else:
            font = pg.font.Font(None, size)
        textSurf = font.render(text, True, color, bgColor)
        _textLibrary[f"{text}{color}{size}"] = textSurf
    x, y = position
    if center:
        surf.blit(textSurf, (x - (textSurf.get_width() // 2), y - (textSurf.get_height() // 2)))
    else:
        surf.blit(textSurf, (x, y))

def SineWaveValue() -> int:
    value = math.sin(pg.time.get_ticks())
    if value >= 0:
        return 255
    else:
        return 0

def Clamp(num: int, minValue: int, maxValue: int) -> int:
    return max(min(num, maxValue), minValue)

def DistTo(originVector, targetVector) -> Vector2:
    deltaX = targetVector.x - originVector.x
    deltaY = targetVector.y - originVector.y
    return Vector2((deltaX), (deltaY))

def GetMousePosition() -> Vector2:
    return Vector2(pg.mouse.get_pos())

def SetWindowPos(windowTitle:str, x:int, y:int) -> None:
    try:
        window = gw.getWindowsWithTitle(windowTitle)[0]
        window.moveTo(x, y)
    except IndexError:
        print("Window not found!")

def GetMonitorSize() -> Vector2:
    [monitor := m for m in get_monitors()]
    return Vector2(monitor.width,monitor.height)

def GetMonitorInfo() -> list:
    info = []
    [info.append(m) for m in get_monitors()]
    return info

def SetIcon(iconPath:str) -> None:
    try:
        icon = LoadSurface(iconPath)
        pg.display.set_icon(icon)
    except (TypeError):
        print("ERROR SETTING ICON!!!\n")
