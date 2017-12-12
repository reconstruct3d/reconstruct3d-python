'''****************************************************************************
*   ExploringSfMWithOpenCV
******************************************************************************
*   by Roy Shilkrot, Dec 2012
*   http:#www.morethantechnical.com/
******************************************************************************
*   Ch4 of the book "Mastering OpenCV with Practical Computer Vision Projects"
*   Copyright Packt Publishing 2012.
*   http:#www.packtpub.com/cool-projects-with-opencv/book
****************************************************************************'''

#include "IFeatureMatcher.h"

class RichFeatureMatcher : public IFeatureMatcherprivate:
	cv.Ptr<cv.FeatureDetector> detector
	cv.Ptr<cv.DescriptorExtractor> extractor
	
	std.vector<cv.Mat> descriptors
	
	std.vector<cv.Mat>& imgs; 
	std.vector<std.vector<cv.KeyPoint> >& imgpts
public:
	#c'tor
	RichFeatureMatcher(std.vector<cv.Mat>& imgs, 
					   std.vector<std.vector<cv.KeyPoint> >& imgpts)
	
	void MatchFeatures(int idx_i, idx_j, matches = NULL)
	
	std.vector<cv.KeyPoint> GetImagePoints(int idx) { return imgpts[idx];

