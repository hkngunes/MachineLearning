########################
##### Prepare Data #####
X = [1,2,3,4,5,6,7,8,9,10]
Y = [1,1.2,2.1,3.3,3.7,4.9,6.1,7.3,8.0,9.2]
##### Prepare Data #####
########################

##############################
##### Prepare Parameters #####
def arrange_t1():
    XPOS = list(map(lambda x:x>0,X))
    isXPOS = sum(XPOS) > m
    YPOS = list(map(lambda y:y>0,Y))
    isYPOS = sum(YPOS) > m
    if(isXPOS != isYPOS):
        return -1
    return 1
m = len(X)
t1 = arrange_t1()
t0 = 0
c0 = 0.1/(2*m)
c1 = 0.1/(2*m*m)
err=1
epsilon = 0.001
max_iter = 10000
##### Prepare Parameters #####
##############################

########################
##### GD Algorithm #####
iter_count=0
while iter_count < 10000 and err > 0.001:
    iter_count+=1
    next_t0 = t0 - c0*sum(list(map(lambda x,y:t0+t1*x-y, X,Y)))
    next_t1 = t1 - c1*sum(list(map(lambda x,y:x*(t0+t1*x-y), X,Y)))
    t0=next_t0
    t1=next_t1
    err = sum(list(map(lambda x,y:t0+t1*x-y, X,Y)))/m
##### GD Algorithm #####
########################

###########################
##### Dispaly Results #####
import matplotlib.pyplot as plt
M=list(map(lambda x:t0+t1*x,X))
plt.title("Iteration: "+str(iter_count)+"   Err: "+str(err))
plt.plot(X,Y,"r")
plt.plot(X,M,"b")
plt.show()
##### Dispaly Results #####
###########################
