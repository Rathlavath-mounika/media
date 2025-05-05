class Laptop:
    def __init__(self,brand,model,processor,ram,storage,price):
        self.brand=brand
        self.model=model
        self.processor=processor
        self.ram=ram
        self.storage=storage
        self.price=price
    def  about(self):
        return(f"{self.brand}{self.model},{self.processor},{self.ram}GB RAM, {self.storage}GB storage, price: ₹{self.price}")
laptop1=Laptop("Dell","inspiron15","intel i5",8,512,55000)
print(laptop1.about())
laptop2=Laptop("HP","pavilian15","Intel i7",16,1024,75000)
print(laptop2.about())
laptop3=Laptop("Lenovo","Ideapad slim3","AMD Ryzen 5",8, 512,48000)
print(laptop3.about())
laptop4=Laptop("ASUS","vivobook14","Intel i3",8,256,35000)
print(laptop4.about())
laptop5=Laptop("APPLE","macbook air m1","apple m1",8,256,92000)
print(laptop5.about())
laptop6=Laptop("Acer","aspire 7","AMD Ryzen 7",16,512,62000)
print(laptop6.about())
laptop7=Laptop("MSI","modern 14","intel i5",8,512,58000)
print(laptop7.about())
laptop8=Laptop("Samsung","galaxy book 2","intel i5",16,512,58000)
print(laptop8.about())
laptop9=Laptop("LG","gram 14","intel i5",8,256,78000)
print(laptop9.about())
laptop10=Laptop("Realme","book slim","intel i3",8,256,40000)
print(laptop10.about())
