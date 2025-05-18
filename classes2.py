class Phone:
    hascamera = True
    hasscreen = True
    isflexible = False
    apps = "google"
    
    def appstore(self):
        print("you can buy games")
    def calling(self):
        print("you can call others")
    def flip_phone(self):
        print("you can flip your screen open") 
    
apple = Phone()
google = Phone()
samsung = Phone()

print(apple.hascamera, apple.apps, apple.isflexible)
print(samsung.hasscreen, samsung.apps, samsung.hascamera)

apple.appstore()
google.calling()
google.flip_phone()