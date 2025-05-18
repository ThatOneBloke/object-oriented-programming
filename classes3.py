class Phone:
    def __init__(self, color, size):

        self.hascamera = True
        self.hasscreen = True
        self.isflexible = False
        self.color = color
        self.size = size
        self.apps = "google"
    
apple = Phone("black", "large")
google = Phone("white", "medium")
samsung = Phone("blue", "small")

print(apple.size, google.color, samsung.color, google.size)