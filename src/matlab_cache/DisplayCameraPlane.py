# Autogenerated with SMOP 
from smop.core import *
# DisplayCameraPlane.m

    
@function
def DisplayCameraPlane(C=None,R=None,windowScale=None,handleP=None,*args,**kwargs):
    varargin = DisplayCameraPlane.varargin
    nargin = DisplayCameraPlane.nargin

    R=R.T
# DisplayCameraPlane.m:3
    window11=dot(windowScale,cat([1],[1],[1]))
# DisplayCameraPlane.m:4
    window12=dot(windowScale,cat([- 1],[1],[1]))
# DisplayCameraPlane.m:4
    window21=dot(windowScale,cat([- 1],[- 1],[1]))
# DisplayCameraPlane.m:4
    window22=dot(windowScale,cat([1],[- 1],[1]))
# DisplayCameraPlane.m:4
    windowPrime11=dot(R,window11) + C
# DisplayCameraPlane.m:5
    windowPrime12=dot(R,window12) + C
# DisplayCameraPlane.m:5
    windowPrime21=dot(R,window21) + C
# DisplayCameraPlane.m:5
    windowPrime22=dot(R,window22) + C
# DisplayCameraPlane.m:5
    plot3(C[1],C[2],C[3],'ko')
    hold('on')
    plot3(cat(C[1],C[1] + dot(windowScale,R[1,2])),cat(C[2],C[2] + dot(windowScale,R[2,2])),cat(C[3],C[3] + dot(windowScale,R[3,2])),'g-')
    hold('on')
    plot3(cat(C[1],C[1] + dot(windowScale,R[1,1])),cat(C[2],C[2] + dot(windowScale,R[2,1])),cat(C[3],C[3] + dot(windowScale,R[3,1])),'r-')
    if nargin == 3:
        handleP=plot3(cat(windowPrime11[1],windowPrime12[1],windowPrime21[1],windowPrime22[1],windowPrime11[1],windowPrime21[1],windowPrime12[1],windowPrime22[1]),cat(windowPrime11[2],windowPrime12[2],windowPrime21[2],windowPrime22[2],windowPrime11[2],windowPrime21[2],windowPrime12[2],windowPrime22[2]),cat(windowPrime11[3],windowPrime12[3],windowPrime21[3],windowPrime22[3],windowPrime11[3],windowPrime21[3],windowPrime12[3],windowPrime22[3]),'k-')
# DisplayCameraPlane.m:13
    else:
        set(handleP,'XData',cat(windowPrime11[1],windowPrime12[1],windowPrime21[1],windowPrime22[1],windowPrime11[1],windowPrime21[1],windowPrime12[1],windowPrime22[1]),'YData',cat(windowPrime11[2],windowPrime12[2],windowPrime21[2],windowPrime22[2],windowPrime11[2],windowPrime21[2],windowPrime12[2],windowPrime22[2]),'ZData',cat(windowPrime11[3],windowPrime12[3],windowPrime21[3],windowPrime22[3],windowPrime11[3],windowPrime21[3],windowPrime12[3],windowPrime22[3]))
    
    grid('on')
    # axis equal