import numpy as np
from math import *
import scipy.stats as st

def mm1queue(lam,mu,M):
    arrival_time=np.zeros(2*M)
    interarrivaltime=np.random.exponential(1/lam)
    arrival_time[0]=interarrivaltime
    for i in range(1,2*M):
        interarrivaltime=np.random.exponential(1/lam)
        k=arrival_time[i-1]+interarrivaltime
        if k<10**4:
            arrival_time[i]=k
        else:
            break
    arrival_time=arrival_time[arrival_time != 0]
    total_arrivals=arrival_time.shape[0]
    enter_service_time=np.zeros(total_arrivals)
    completion_time=np.zeros(total_arrivals)
    enter_service_time[0]=arrival_time[0]
    completion_time[0]=enter_service_time[0]+np.random.exponential(1/mu)
    for i in range(1,total_arrivals):
        service_time=np.random.exponential(1/mu)
        enter_service_time[i]=max(completion_time[i-1],arrival_time[i])
        k=enter_service_time[i]+service_time
        if k<10**4:
            completion_time[i]=k
        else:
            break
    totalenter=np.zeros(10*M)
    totalleave=np.zeros(10*M)
    here_now=np.zeros(10*M)
    for h in range(arrival_time.shape[0]):
        f=floor(arrival_time[h]*10)
        totalenter[f:]+=1
    
    for h in range(completion_time.shape[0]):
        f=floor(completion_time[h]*10)
        if (f==0): break
        totalleave[f:]+=1
        
    for a in range(10*M):
        here_now[a]=totalenter[a]-totalleave[a]
    return here_now
