

def  fizz_buzz():
    i = 0
    for i in range(0,100):
     if i%3==0:
      print('fizz')
     if i%5==0:
      print('buzz')
     if i%5==0 and i%3==0:
      print('“FizzBuzz')    
     else:
      print(i)
    i+=1  
fizz_buzz()




i=0
while i<=100:
    i+=1
    if i%3==0:
      print('fizz')
    if i%5==0:
      print('buzz')
    if i%5==0 and i%3==0:
      print('“FizzBuzz')    
    else:
      print(i)


def fizz_buzz():    
    i = 0
    for i in range(0,100):
     if i%3==0:
      print(i , 'fizz')
     if i%5==0:
      print(i , 'buzz')
     if i%5==0 and i%3==0:
      print(i , 'FizzBuzz')    
     
    i+=1  
fizz_buzz()



def fizz_buzz(fizz=3,buzz=5,up_to=15):
  x = 0;
  result =[]
  while x in range(up_to+1):
    string = ""
    if x%fizz==0 and x != 0:
      string += "Fizz"
    if x%buzz==0 and x !=0:
      string += "Buzz"
    result.append((x,(str(x) if string == "" else string)))
    x+=1
  for i in result:
    print(f'{i[0]},{i[1]}')
  
fizz_buzz(3, 5, 45)