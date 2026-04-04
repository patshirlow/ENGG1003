def minpos(x):
   positives = [v for v in x if v > 0]
   mp = min(positives)
   idx = x.index(mp)
   return mp, idx
x = [1.624, -0.611, -1.072, 0.865, -2.301, 1.744, -0.761, 0.319, -0.249]
mp, idx = minpos(x)
print(x)
print(mp)
print(idx)  
