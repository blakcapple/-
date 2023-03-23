import numpy as np
def average_pooling_forward(x, pool_param):
    N, C, H, W = x.shape
    HH, WW, stride = pool_param['pool_height'], pool_param['pool_width'], pool_param['stride']
    H_out=(H-HH)/stride+1
    W_out=(W-WW)/stride+1
    out=np.zeros((N,C,H_out,W_out))
    
    for i in H_out:
        for j in W_out:
             x_mask=x[:,:,i*stride:i*stride+HH,j*stride:j*stride+WW]
             out[:,:,i,j]=np.average(x_mask,axis=(2,3))
    return out