 
class ModelFacade:
    def __init__(self, image, *args, **kwargs):
        self.image = image

    def processImage(self):
        print("do something with " + str(self.image))
        return 0
