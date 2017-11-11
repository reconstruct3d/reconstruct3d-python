# Autogenerated with SMOP 
from smop.core import *
# LinearPnP.m

    
@function
def LinearPnP(X=None,x=None,K=None,*args,**kwargs):
    varargin = LinearPnP.varargin
    nargin = LinearPnP.nargin

    ## LinearPnP
# Getting pose from 2D-3D correspondences
# Inputs:
#     X - size (N x 3) matrix of 3D points
#     x - size (N x 2) matrix of 2D points whose rows correspond with X
#     K - size (3 x 3) camera calibration (intrinsics) matrix
# Outputs:
#     C - size (3 x 1) pose transation
#     R - size (3 x 1) pose rotation
    
    # IMPORTANT NOTE: While theoretically you can use the x directly when solving
# for the P = [R t] matrix then use the K matrix to correct the error, this is
# more numeically unstable, and thus it is better to calibrate the x values
# before the computation of P then extract R and t directly
    
    X=matlabarray(cat(X,ones(size(X,1),1)))
# LinearPnP.m:18
    A=zeros(dot(3,size(X,1)),12)
# LinearPnP.m:19
    for i in arange(1,size(X,1)).reshape(-1):
        Xt=X[i,:]
# LinearPnP.m:22
        x_temp=matlabarray(cat(x[i,:],1))
# LinearPnP.m:23
        xx=numpy.linalg.solve(K,x_temp.T)
# LinearPnP.m:24
        j=dot((i - 1),3) + 1
# LinearPnP.m:25
        A[j:j + 2,:]=dot(cat([0,- 1,xx[2]],[1,0,- xx[1]],[- xx[2],xx[1],0]),cat([Xt,zeros(1,4),zeros(1,4)],[zeros(1,4),Xt,zeros(1,4)],[zeros(1,4),zeros(1,4),Xt]))
# LinearPnP.m:26
    
    __,__,v=svd(A,nargout=3)
# LinearPnP.m:30
    P_temp=v[:,end()]
# LinearPnP.m:31
    P=reshape(P_temp,4,3).T
# LinearPnP.m:32
    R=P[:,1:3]
# LinearPnP.m:33
    uu,dd,vv=svd(R,nargout=3)
# LinearPnP.m:34
    if det(dot(uu,vv.T)) > 0:
        R=dot(uu,vv.T)
# LinearPnP.m:36
        T=P[:,4] / dd[1,1]
# LinearPnP.m:37
    else:
        R=dot(- uu,vv.T)
# LinearPnP.m:39
        T=- P[:,4] / dd[1,1]
# LinearPnP.m:40
    
    C=dot(- R.T,T)
# LinearPnP.m:42