# Autogenerated with SMOP 
from smop.core import *
# DisplayCorrespondence.m

    
@function
def DisplayCorrespondence(img=None,x=None,xp=None,*args,**kwargs):
    varargin = DisplayCorrespondence.varargin
    nargin = DisplayCorrespondence.nargin

    ## Display correspondence points between SIFT keypoints and reprojection
# img: image to display
# x: size of (n, 2). SIFT keypoints locations
# xp: size of (n, 2). Reprojection locations
    
    figure
    imshow(img)
    hold('on')
    err=0
# DisplayCorrespondence.m:9
    for i in arange(1,size(x,1)).reshape(-1):
        # Draw lines between corresponding SIFT keypoints and reprojection
        plot(cat(xp[i,1],x[i,1]),cat(xp[i,2],x[i,2]),'LineWidth',1,'Color','red')
        scatter(x[i,1],x[i,2],'o','LineWidth',1,'MarkerEdgeColor','blue','MarkerFaceColor','blue')
        err=err + (x[i,:] - xp[i,:]) ** 2
# DisplayCorrespondence.m:20
    
    # Display RMS error
    text(1170,20,sprintf('Error: %1.2f',sqrt(sum(err) / size(x,1))),'Color','white','FontSize',14)
    hold('off')
    return
    
if __name__ == '__main__':
    pass
    