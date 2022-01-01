from PIL import Image, ImageColor

X = 0
Y = 1

R = 0
G = 1
B = 2


class ImageInitializationError(Exception):
    def __init__(self, message="Must supply a filename"):
        self.message = message
        super().__init__(self.message)


class Pixel:
    def __init__(self, location, image):
        self.location = location
        self.image = image

    @property
    def red(self):
        rgb = self.image.getpixel(self.location)
        return rgb[R]

    @red.setter
    def red(self, value):
        rgb = self.image.getpixel(self.location)
        self.image.putpixel(self.location, (int(value), rgb[G], rgb[B]))

    @property
    def green(self):
        rgb = self.image.getpixel(self.location)
        return rgb[G]

    @green.setter
    def green(self, value):
        rgb = self.image.getpixel(self.location)
        self.image.putpixel(self.location, (rgb[R], int(value), rgb[B]))

    @property
    def blue(self):
        rgb = self.image.getpixel(self.location)
        return rgb[B]

    @blue.setter
    def blue(self, value):
        rgb = self.image.getpixel(self.location)
        self.image.putpixel(self.location, (rgb[R], rgb[G], int(value)))


class SimpleImage:

    def __init__(self, filename: str, image=None):
        if filename:
            self.image = Image.open(filename)
        elif image:
            self.image = image
        else:
            raise ImageInitializationError
        self.pixels = self.image.load()
        self.location = (0, 0)

    @classmethod
    def from_image(cls, image):
        pass

    @property
    def height(self):
        return self.image.height

    @property
    def width(self):
        return self.image.width

    def __iter__(self):
        return self

    def __next__(self):
        loc = self.location
        self.location = (self.location[X] + 1, self.location[Y])
        if self.location[X] >= self.width:
            self.location = (0, self.location[Y] + 1)
        if self.location[Y] >= self.height:
            raise StopIteration
        return Pixel(loc, self.image)

    def show(self):
        self.image.show()

    def get_pixel(self, x, y):
        return Pixel((x, y), self.image)

    @staticmethod
    def blank(width, height):
        image = Image.new(mode="RGB", size=(width, height), color="white")
        i = SimpleImage(filename=None, image=image)
        return i
