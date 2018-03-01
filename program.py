import math
def dist(a,b,x,y):
    return abs(x-a)+abs(y-b)

def is_faisible(time,car_x,car_y,a,b,x,y,s,f):
    dist_car_to_ride = dist(car_x,car_y,a,b)
    total_len = time+dist_car_to_ride+max(0,s-(time+dist_car_to_ride))+dist(a,b,x,y)
    return total_len < f

def find_nearest_available_car(time, a,b,x,y,s,f):
    min_dist = math.inf
    min_car = -1
    for i,car in enumerate(cars_pos):
        if (cars_status[i]==-1 or cars_status[i]<=time) and is_faisible(time,car[0],car[1],a,b,x,y,s,f):
            current_dist = dist(car[0],car[1],x,y)
            if current_dist < min_dist:
                min_dist = current_dist
                min_car = i
    #print(min_car, a,b,x,y)
    return min_car

def check_arrive_on_time():
    pass

R, C, F, N, B, T = [int(i) for i in input().split()]
rides = []

cars = [[] for i in range(F)]
cars_status = [-1 for i in range(F)]
cars_pos = [(0,0) for i in range(F)]
available = F

time = 0
index = 0
for _ in range(N):
    a,b,x,y,s,f = [int(i) for i in input().split()]
    rides.append((a,b,x,y,s,f,index))
    index+=1

rides = sorted(rides,key=lambda x:x[4])
#rides_done = set()
while time<T:
    #print(cars_status)
    rides_to_remove = []
    next_iter = time+1
    for ride_id in range(len(rides)):
        #if available==0:
        #    break

        #if ride_id not in rides_done:
        a,b,x,y,s,f,idx = rides[ride_id]
        if time>=f:
            rides_to_remove.append(ride_id)
            #rides_done.add(ride_id)
        else:
            car_id = find_nearest_available_car(time,a,b,x,y,s,f)
            if car_id>=0:
                dist_car_to_ride = dist(cars_pos[car_id][0],cars_pos[car_id][1],a,b)
                cars_status[car_id] = time+dist_car_to_ride+max(0,s-(time+dist_car_to_ride))+dist(a,b,x,y)
                #available-=1
                cars[car_id].append(idx)
                cars_pos[car_id]=(x,y)
                #rides_done.add(ride_id)
                rides_to_remove.append(ride_id)
                next_iter = min(next_iter,cars_status[car_id])

    #for i,car_s in enumerate(cars_status):
    #    if time>= car_s:
    #        cars_status[i]=-1
    #    available+=1
    #print("len : "+str(len(rides)) + " remove : "+ str(rides_to_remove))
    for i in rides_to_remove[::-1]:
        del rides[i]
    #print("len : "+str(len(rides)))
    time=next_iter

for car in cars:
    print(str(len(car)) + " " + " ".join([str(i) for i in car]))
