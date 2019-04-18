import matplotlib.pyplot as plt
import numpy as np

mean = [0,0]
cov  = [[2,2.5],[1,2]] # diagonal covariance, points lie on x or y-axis
cov0 = [[2,0],[0,2]]
x,y = np.random.multivariate_normal(mean,cov,100).T
yn  = -y
x2,y2 = np.random.multivariate_normal(mean,cov0,100).T

for i,j in zip(x2,y2):
    print i,'\t',j



f, (ax1, ax2, ax3) = plt.subplots(1,3,sharey=True)
ax1.plot(x2,y2,'go')
ax2.plot(x,y,'o')
ax3.plot(x,yn,'ro')

ax1.set_title('uncorrelated')
ax2.set_title('correlated')
ax3.set_title('anticorrelated')

plist = [ax1,ax2,ax3]
for m in plist:
    m.set_xlabel('v')
    m.set_ylabel('u')
    
f.subplots_adjust(hspace=0)
#plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.show()

