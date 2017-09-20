class product:
  product={}
  updat={}
  buy={}
  #d={}
  #m={}
  def addproducts(self):
    product_name=input("enter a new product")
    quantity=input("enter that product quantity")
    self.product[product_name]=quantity
  
    
  def buyproduct(self,dic):
    # self.up={}
    # self.dep={}
    if bool(dic):
#135463q99u0
      
      for index, (key, value) in enumerate(dic.items()):
        self.updat[index+1]=[key,value]
        
        print(str(index+1)+"."+key+":"+str(value))
      print("you can choose any of the product to buy")  
      produc=input("which product u want to buy")
      produc=int(produc)
      quan=input("how much u want")
      quan=int(quan)
      for i in self.updat: 
        if i==produc:
          if int(self.updat[i][1])>=quan:
            self.updat[i][1]=int(self.updat[i][1])-int(quan)
            self.updat[i][1]=str(self.updat[i][1])
            
            self.buy[self.updat[i][0]]=quan
            self.buy.update(self.buy)
            for i in self.updat:
              print(str(i)+":"+str(self.updat[i][0])+":"+str(self.updat[i][1]))
          else:
            print("that much quantity is not available")
    else:
      print("no products added")
          
      self.updat.update(self.updat)       
  def listproduct(self) :
    
    if bool(self.buy):
       for i in self.buy:
        print(str(i)+":"+str(self.buy[i]))
    else:
      print("no product")
a=product()
print ("1.add new product with its stocks. 2. buy products 3. list the sold product quantity 4.quit")
l={}
f={}
v={}
b="y"
while b=="y":  
  n=input("choose the operation")
  
  
  if n=='1':
    e="y"
    while e=="y":
      
      a.addproducts()
      l.update(a.product)
      #print(l)
      e=input("add more products y or n")
  elif n=="2":   
    #print (l)
    a.buyproduct(l)
    f.update(a.updat)
    v.update(a.buy)
  elif n=="3":
    a.listproduct()
  elif n=="4":
    break
  b=input("you want to do any other operation y or n")  
  
  
  
  
  
  
