class Rectangle:
    #defining the attributes of my class
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.name="Rectangle"
      #defining this predefined fucntion for the print
    def __str__(self):
        return self.name+"(width="+str(self.width)+", height="+str(self.height)+")"
        
        
        #adding methodes
    def set_width(self,width):
        self.width=width
        
    def set_height(self,height):
        self.height=height
        
    def get_area(self):
        return self.width*self.height
        
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
        
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
        
    def get_picture(self):
        if (self.width>50 or self.height>50):
            return "Too big for picture."
        else:
            ch=""
            for g in range(self.height):
                for i in range (self.width):
                    ch=ch+"*"
                ch=ch+"\n"
            return ch
        
    def get_amount_inside(self,x):
        a=self.get_area()
        y=x.get_area()
        return int(a/y)



#the class square inherite from the super class rectangle
class Square(Rectangle):
    def __init__(self,side):
        Rectangle.__init__(self,side,side)
        self.name="Square"
        self.side=side
    def __str__(self):
        return self.name+"(side="+str(self.side)+")"
   
    def set_side(self,side):
        Rectangle.set_height(self, side)
        Rectangle.set_width(self,side)
        self.side=side
      #polymorphisme in this case (overriding existing               function)
    def set_width(self,side):
        self.side=side
    def set_height(self,side):
        self.side=side
        
    
    
    