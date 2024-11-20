import math
T0=10.7
TF=-22.2
t10=7.1
t20=4.2
t30=2.8

alfa= (-0.1)*math.log((T0-TF)/(t10-TF))
alfa20=(-0.05)*math.log((T0-TF)/(t20-TF))
alfa30=(-1/30)*math.log((T0-TF)/(t30-TF))


tmin1 = (-1)/alfa* math.log((T0-TF)/((-1)-TF))
t20min1 = (-1)/alfa20* math.log((T0-TF)/((-1)-TF))
t30min1 = (-1)/alfa30* math.log((T0-TF)/((-1)-TF))

print(tmin1, t20min1, t30min1)
