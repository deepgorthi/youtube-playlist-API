class PlaylistInfo:

    def __init__(self, id, title, duration):
        self.id = id
        self.title = title
        self.duration = duration

    def getId(self):
        return self.id
    
    def getTitle(self):
        return self.title

    def getDuration(self):
        return self.duration