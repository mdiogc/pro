class File:
    def __init__(self, path):
        self.path = path
        self.contents = []

    def add_content(self, content):
        self.contents.append(content)

    @property
    def size(self):
        return len(self.contents)

    @property
    def info(self):
        return f"{self.path} [size={self.size}B]"

class MediaFile(File):
    def __init__(self, path, codec, geoloc, duration):
        super().__init__(path)
        self.codec = codec
        self.geoloc = geoloc
        self.duration = duration

    @property
    def info(self):
        return f"{self.path} [size={self.size}B]\nCodec: {self.codec}\nGeolocalization: {self.geoloc}\nDuration: {self.duration}s"

class VideoFile(MediaFile):
    def __init__(self, path, codec, geoloc, duration, dimensions):
        super().__init__(path, codec, geoloc, duration)
        self.dimensions = dimensions

    @property
    def info(self):
        return f"{self.path} [size={self.size}B]\nCodec: {self.codec}\nGeolocalization: {self.geoloc}\nDuration: {self.duration}s\nDimensions: {self.dimensions}"
