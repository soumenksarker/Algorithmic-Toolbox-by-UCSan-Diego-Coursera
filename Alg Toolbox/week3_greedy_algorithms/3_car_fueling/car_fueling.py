import math
def car_fueling(dist,miles,n,gas_stations):
    d=dist
    gs = [0]+gas_stations+[dist]
    m=miles
    r=0
    s=0
    if dist<=m:
        r=0
    else:
        i=1
        while(i<n+2):
          if gs[i]-gs[i-1]>miles:
             r= -1
             break
          else:
              m-=(gs[i]-s)
              if m<=0:
                 r+=1
                 if m==0:
                    s=gs[i]
                    m=miles
                    if i==n+1:
                        r-=1
                        break
                 else:
                    s=gs[i-1]
                    m=miles
              else:
                  m=miles
          i+=1
    return r

# Driver Code
if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(car_fueling(input_d, input_m, input_n, input_stops))

