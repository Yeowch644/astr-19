class FavAnimal:
    def __init__(self, arms, legs, eyes, tail, furry):
        self.arms = arms
        self.legs = legs
        self.eyes = eyes
        self.tail = tail
        self.furry = furry
    
    def description(self):
        print(f"My favorite animal has {self.eyes} eyes, with an average arm length of {self.arms} and leg length of {self.legs}.")
        if self.tail == True and self.furry == True:
            print("It also has a tail and fur.")
        elif self.tail == True and self.furry == False:
            print("It also has a tail but no fur.")
        elif self.tail == False and self.furry == True:
            print("It also has fur but no tail.")
        else:
            print("It has neither a tail nor fur.")
        

def main():
    Cat = FavAnimal(9.5, 10.5, 2, True, True)
    Cat.description()
    

if __name__=="__main__":
    main()