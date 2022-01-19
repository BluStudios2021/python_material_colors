'''
    A simple implementation of the material design colors in python
     - currently only supports 'rgb' format; more will be added soon
    
    Usage:

    from material_colors import MaterialColors
    
    Colors = MaterialColors('rgb')
    
    my_red_color = Colors.red()

    my_purple_color = Colors.purple(300)
'''

class MaterialColors():
    def __init__(self, mode = 'rgb'):
        # set the format in which the color gets returned
        self.setMode()

        # normal colors
        self._red         = {50: [(255, 235, 238)],
                            100: [(255, 205, 210)],
                            200: [(239, 154, 154)],
                            300: [(239, 154, 154)],
                            400: [(239, 83, 80)],
                            500: [(244, 67, 54)],
                            600: [(229, 57, 53)],
                            700: [(211, 47, 47)],
                            800: [(198, 40, 40)],
                            900: [(183, 28, 28)]}

        self._pink        = {50: [(252, 228, 236)],
                            100: [(248, 187, 208)],
                            200: [(244, 143, 177)],
                            300: [(240, 98, 146)],
                            400: [(236, 64, 122)],
                            500: [(233, 30, 99)],
                            600: [(216, 27, 96)],
                            700: [(194, 24, 91)],
                            800: [(173, 20, 87)],
                            900: [(136, 14, 79)]}

        self._purple      = {50: [(243, 229, 245)],
                            100: [(225, 190, 231)],
                            200: [(206, 147, 216)],
                            300: [(186, 104, 200)],
                            400: [(171, 71, 188)],
                            500: [(156, 39, 176)],
                            600: [(142, 36, 170)],
                            700: [(123, 31, 162)],
                            800: [(106, 27, 154)],
                            900: [(74, 20, 140)]}

        self._deep_purple = {50: [(237, 231, 246)],
                            100: [(209, 196, 233)],
                            200: [(179, 157, 219)],
                            300: [(149, 117, 205)],
                            400: [(126, 87, 194)],
                            500: [(103, 58, 183)],
                            600: [(94, 53, 177)],
                            700: [(81, 45, 168)],
                            800: [(69, 39, 160)],
                            900: [(49, 27, 146)]}

        self._indigo      = {50: [(232, 234, 246)],
                            100: [(197, 202, 233)],
                            200: [(159, 168, 218)],
                            300: [(121, 134, 203)],
                            400: [(92, 107, 192)],
                            500: [(63, 81, 181)],
                            600: [(57, 73, 171)],
                            700: [(48, 63, 159)],
                            800: [(40, 53, 147)],
                            900: [(26, 35, 126)]}

        self._blue        = {50: [(227, 242, 253)],
                            100: [(187, 222, 251)],
                            200: [(144, 202, 249)],
                            300: [(100, 181, 246)],
                            400: [(66, 165, 245)],
                            500: [(33, 150, 243)],
                            600: [(30, 136, 229)],
                            700: [(25, 118, 210)],
                            800: [(21, 101, 192)],
                            900: [(13, 71, 161)]}

        self._light_blue  = {50: [(225, 245, 254)],
                            100: [(179, 229, 252)],
                            200: [(129, 212, 250)],
                            300: [(129, 212, 250)],
                            400: [(41, 182, 246)],
                            500: [(3, 169, 244)],
                            600: [(3, 155, 229)],
                            700: [(2, 136, 209)],
                            800: [(2, 119, 189)],
                            900: [(1, 87, 155)]}

        self._cyan        = {50: [(224, 247, 250)],
                            100: [(178, 235, 242)],
                            200: [(128, 222, 234)],
                            300: [(77, 208, 225)],
                            400: [(38, 198, 218)],
                            500: [(0, 188, 212)],
                            600: [(0, 172, 193)],
                            700: [(0, 151, 167)],
                            800: [(0, 131, 143)],
                            900: [(0, 96, 100)]}

        self._teal        = {50: [(224, 242, 241)],
                            100: [(178, 223, 219)],
                            200: [(128, 203, 196)],
                            300: [(77, 182, 172)],
                            400: [(38, 166, 154)],
                            500: [(0, 150, 136)],
                            600: [(0, 137, 123)],
                            700: [(0, 121, 107)],
                            800: [(0, 105, 92)],
                            900: [(0, 77, 64)]}

        self._green       = {50: [(232, 245, 233)],
                            100: [(200, 230, 201)],
                            200: [(165, 214, 167)],
                            300: [(129, 199, 132)],
                            400: [(102, 187, 106)],
                            500: [(76, 175, 80)],
                            600: [(67, 160, 71)],
                            700: [(56, 142, 60)],
                            800: [(46, 125, 50)],
                            900: [(27, 94, 32)]}

        self._light_green = {50: [(241, 248, 233)],
                            100: [(220, 237, 200)],
                            200: [(197, 225, 165)],
                            300: [(174, 213, 129)],
                            400: [(156, 204, 101)],
                            500: [(139, 195, 74)],
                            600: [(124, 179, 66)],
                            700: [(104, 159, 56)],
                            800: [(85, 139, 47)],
                            900: [(51, 105, 30)]}

        self._lime        = {50: [(249, 251, 231)],
                            100: [(240, 244, 195)],
                            200: [(230, 238, 156)],
                            300: [(220, 231, 117)],
                            400: [(212, 225, 87)],
                            500: [(205, 220, 57)],
                            600: [(192, 202, 51)],
                            700: [(175, 180, 43)],
                            800: [(158, 157, 36)],
                            900: [(130, 119, 23)]}

        self._yellow      = {50: [(255, 253, 231)],
                            100: [(255, 249, 196)],
                            200: [(255, 245, 157)],
                            300: [(255, 241, 118)],
                            400: [(255, 238, 88)],
                            500: [(255, 235, 59)],
                            600: [(253, 216, 53)],
                            700: [(251, 192, 45)],
                            800: [(249, 168, 37)],
                            900: [(245, 127, 23)]}

        self._amber       = {50: [(255, 248, 225)],
                            100: [(255, 236, 179)],
                            200: [(255, 224, 130)],
                            300: [(255, 213, 79)],
                            400: [(255, 202, 40)],
                            500: [(255, 193, 7)],
                            600: [(255, 179, 0)],
                            700: [(255, 160, 0)],
                            800: [(255, 143, 0)],
                            900: [(255, 111, 0)]}

        self._orange      = {50: [(255, 243, 224)],
                            100: [(255, 224, 178)],
                            200: [(255, 204, 128)],
                            300: [(255, 183, 77)],
                            400: [(255, 167, 38)],
                            500: [(255, 152, 0)],
                            600: [(251, 140, 0)],
                            700: [(245, 124, 0)],
                            800: [(239, 108, 0)],
                            900: [(230, 81, 0)]}

        self._deep_orange = {50: [(251, 233, 231)],
                            100: [(255, 204, 188)],
                            200: [(255, 171, 145)],
                            300: [(255, 138, 101)],
                            400: [(255, 112, 67)],
                            500: [(255, 87, 34)],
                            600: [(244, 81, 30)],
                            700: [(230, 74, 25)],
                            800: [(216, 67, 21)],
                            900: [(191, 54, 12)]}

        self._brown       = {50: [(239, 235, 233)],
                            100: [(215, 204, 200)],
                            200: [(188, 170, 164)],
                            300: [(161, 136, 127)],
                            400: [(141, 110, 99)],
                            500: [(121, 85, 72)],
                            600: [(109, 76, 65)],
                            700: [(93, 64, 55)],
                            800: [(78, 52, 46)],
                            900: [(62, 39, 35)]}

        self._grey        = {50: [(250, 250, 250)],
                            100: [(245, 245, 245)],
                            200: [(238, 238, 238)],
                            300: [(224, 224, 224)],
                            400: [(189, 189, 189)],
                            500: [(158, 158, 158)],
                            600: [(117, 117, 117)],
                            700: [(97, 97, 97)],
                            800: [(66, 66, 66)],
                            900: [(33, 33, 33)]}

        self._blue_grey  = {50: [(236, 239, 241)],
                            100: [(207, 216, 220)],
                            200: [(176, 190, 197)],
                            300: [(144, 164, 174)],
                            400: [(120, 144, 156)],
                            500: [(96, 125, 139)],
                            600: [(84, 110, 122)],
                            700: [(69, 90, 100)],
                            800: [(55, 71, 79)],
                            900: [(38, 50, 56)]}


        # accent colors
        self._accent_red         = {100: [(255, 138, 128)],
                                    200: [(255, 82, 82)],
                                    400: [(255, 23, 68)],
                                    700: [(213, 0, 0)]}

        self._accent_pink        = {100: [(255, 128, 171)],
                                    200: [(255, 64, 129)],
                                    400: [(245, 0, 87)],
                                    700: [(197, 17, 98)]}

        self._accent_purple      = {100: [(234, 128, 252)],
                                    200: [(224, 64, 251)],
                                    400: [(213, 0, 249)],
                                    700: [(170, 0, 255)]}

        self._accent_deep_purple = {100: [(179, 136, 255)],
                                    200: [(124, 77, 255)],
                                    400: [(101, 31, 255)],
                                    700: [(98, 0, 234)]}

        self._accent_indigo      = {100: [(140, 158, 255)],
                                    200: [(83, 109, 254)],
                                    400: [(61, 90, 254)],
                                    700: [(48, 79, 254)]}

        self._accent_blue        = {100: [(130, 177, 255)],
                                    200: [(68, 138, 255)],
                                    400: [(41, 121, 255)],
                                    700: [(41, 98, 255)]}

        self._accent_light_blue  = {100: [(128, 216, 255)],
                                    200: [(64, 196, 255)],
                                    400: [(0, 176, 255)],
                                    700: [(0, 145, 234)]}

        self._accent_cyan        = {100: [(132, 255, 255)],
                                    200: [(24, 255, 255)],
                                    400: [(0, 229, 255)],
                                    700: [(0, 184, 212)]}

        self._accent_teal        = {100: [(167, 255, 235)],
                                    200: [(100, 255, 218)],
                                    400: [(29, 233, 182)],
                                    700: [(0, 191, 165)]}

        self._accent_green       = {100: [(185, 246, 202)],
                                    200: [(105, 240, 174)],
                                    400: [(0, 230, 118)],
                                    700: [(0, 200, 83)]}

        self._accent_light_green = {100: [(204, 255, 144)],
                                    200: [(178, 255, 89)],
                                    400: [(118, 255, 3)],
                                    700: [(100, 221, 23)]}

        self._accent_lime        = {100: [(244, 255, 129)],
                                    200: [(238, 255, 65)],
                                    400: [(198, 255, 0)],
                                    700: [(174, 234, 0)]}

        self._accent_yellow      = {100: [(255, 253, 231)],
                                    200: [(255, 255, 0)],
                                    400: [(255, 234, 0)],
                                    700: [(255, 214, 0)]}

        self._accent_amber       = {100: [(255, 229, 127)],
                                    200: [(255, 215, 64)],
                                    400: [(255, 196, 0)],
                                    700: [(255, 171, 0)]}

        self._accent_orange      = {100: [(255, 209, 128)],
                                    200: [(255, 171, 64)],
                                    400: [(255, 145, 0)],
                                    700: [(255, 109, 0)]}

        self._accent_deep_orange = {100: [(255, 158, 128)],
                                    200: [(255, 110, 64)],
                                    400: [(255, 61, 0)],
                                    700: [(221, 44, 0)]}



    # normal colors
    def red(self, val = 500):
        return self._red[val][self.mode]

    def pink(self, val = 500):
        return self._pink[val][self.mode]

    def purple(self, val = 500):
        return self._purple[val][self.mode]

    def deepPurple(self, val = 500):
        return self._deep_purple[val][self.mode]

    def indigo(self, val = 500):
        return self._indigo[val][self.mode]

    def blue(self, val = 500):
        return self._blue[val][self.mode]

    def lightBlue(self, val = 500):
        return self._light_blue[val][self.mode]

    def cyan(self, val = 500):
        return self._cyan[val][self.mode]

    def teal(self, val = 500):
        return self._teal[val][self.mode]

    def green(self, val = 500):
        return self._green[val][self.mode]

    def lightGreen(self, val = 500):
        return self._light_green[val][self.mode]

    def lime(self, val = 500):
        return self._lime[val][self.mode]

    def yellow(self, val = 500):
        return self._yellow[val][self.mode]

    def amber(self, val = 500):
        return self._amber[val][self.mode]

    def orange(self, val = 500):
        return self._orange[val][self.mode]

    def deepOrange(self, val = 500):
        return self._deep_orange[val][self.mode]

    def brown(self, val = 500):
        return self._brown[val][self.mode]

    def grey(self, val = 500):
        return self._grey[val][self.mode]

    def blueGrey(self, val = 500):
        return self._blue_grey[val][self.mode]


    # accent colors
    def _accentRed(self, val = 400):
        return self._accent_red[val][self.mode]

    def _accentPink(self, val = 400):
        return self._accent_pink[val][self.mode]

    def _accentPurple(self, val = 400):
        return self._accent_purple[val][self.mode]

    def _accentDeepPurple(self, val = 400):
        return self._accent_deep_purple[val][self.mode]

    def _accentIndigo(self, val = 400):
        return self._accent_indigo[val][self.mode]

    def _accentBlue(self, val = 400):
        return self._accent_blue[val][self.mode]

    def _accentLightBlue(self, val = 400):
        return self._accent_light_blue[val][self.mode]

    def _accentCyan(self, val = 400):
        return self._accent_cyan[val][self.mode]

    def _accentTeal(self, val = 400):
        return self._accent_teal[val][self.mode]

    def _accentGreen(self, val = 400):
        return self._accent_green[val][self.mode]

    def _accentLightGreen(self, val = 400):
        return self._accent_light_green[val][self.mode]

    def _accentLime(self, val = 400):
        return self._accent_lime[val][self.mode]

    def _accentYellow(self, val = 400):
        return self._accent_yellow[val][self.mode]

    def _accentAmber(self, val = 400):
        return self._accent_amber[val][self.mode]

    def _accentOrange(self, val = 400):
        return self._accent_orange[val][self.mode]

    def _accentDeepOrange(self, val = 400):
        return self._accent_deep_orange[val][self.mode]


    def setMode(self, mode):
        if mode == 'rgb':
            self.mode = 0
        else:
            print('[MaterialColors] - Error: No such mode as \'' + mode + '\' avaliable!')
            print('[MaterialColors] - Error: Mode was set to \'rgb\' !')
            self.mode = 0
