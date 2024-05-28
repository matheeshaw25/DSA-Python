class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self): #getter returns color
        return self.color    

    def set_color(self,color): #setter sets color
        self.color = color

cookie_one = Cookie('green')      
print(cookie_one.get_color())      

cookie_one.set_color('yellow')
print(cookie_one.get_color())
