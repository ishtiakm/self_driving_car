
p=[0.167,0.167,0.167,0.167,0.167,0.167] # change this according to your inital belief
world=['green','red','red','green','red','green'] # Initialize your world
measurement=['green','red','red','red','green'] # Put the measurements sensed by your car
motion=[1,1,0,1,1] # Put the motion performed by the car
s_right=0.8 # accuracy of sensors
mov_right=0.9 # accuracy of motion

##Dont change code below
def sense(p,z):
  q=[]
  for i in range(len(p)):
    h=(z==world[i])
    q.append(p[i]*(h*s_right+(1-h)*(1-s_right)))
  s=sum(q)
  for i in range(len(q)):
    q[i]=q[i]/s
  return q
def mov(p,U):
  q=[]
  n=len(p)
  
  for i in range(len(p)):
    s=0
    s=s+(1-mov_right)*p[i]
    s=s+mov_right*p[(i-U)%n]
    q.append(s)
  return q
  
  
  
  
##Dont change code above 

for i in range(len(motion)):
  p=sense(p,measurement[i])
  p=mov(p,motion[i])
print(p)
