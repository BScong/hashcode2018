import math
def dist(a,b,x,y):
    return abs(x-a)+abs(y-b)

def find_best_ride(time, car_x, car_y):
    min_metric = math.inf
    min_ride = -1
    for i in range(min(8*F,len(rides))):
        a,b,x,y,s,f,idx,d,c = rides[i]
        possible_metric = (f-time-d)
        dist_to_start = dist(car_x,car_y, a,b)
        metric = dist_to_start*possible_metric*c
        if s-time-dist_to_start>=0:
            metric = metric/B
        if (possible_metric > 0 or (possible_metric == 0 and dist_to_start == 0)) and metric < min_metric:
            min_metric=metric
            min_ride = i

    return min_ride

R, C, F, N, B, T = [int(i) for i in input().split()]
rides = []

cars = [[] for i in range(F)]
cars_status = [-1 for i in range(F)]
cars_pos = [(0,0) for i in range(F)]

index = 0
for _ in range(N):
    a,b,x,y,s,f = [int(i) for i in input().split()]
    d = dist(a,b,x,y)
    rides.append((a,b,x,y,s,f,index,d,float(f)/d))
    index+=1

rides = sorted(rides,key=lambda x:x[5])
time = 0
while time<T:
    for i,car_pos in enumerate(cars_pos):
        if cars_status[i]==-1 or time>=cars_status[i]:
            ride_id = find_best_ride(time, car_pos[0],car_pos[1])
            if ride_id >= 0:
                a,b,x,y,s,f,idx,d,c = rides[ride_id]
                dist_car_to_ride = dist(car_pos[0],car_pos[1],a,b)
                cars_status[i] = time+dist_car_to_ride+max(0,s-(time+dist_car_to_ride))+dist(a,b,x,y)
                cars[i].append(idx)
                cars_pos[i]=(x,y)
                del rides[ride_id]

    time+=1

for car in cars:
    print(str(len(car)) + " " + " ".join([str(i) for i in car]))
