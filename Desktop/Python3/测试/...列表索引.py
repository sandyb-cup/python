import numpy as np
np.random.seed(1)
W = np.random.randn(2,2,3,8)

print(W[...,2].shape)

print("``````````````````")
print(W[:,:,:,1].shape)



