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

#include "AbstractFeatureMatcher.h"

class OFFeatureMatcher : public AbstractFeatureMatcher	std.vector<cv.Mat>& imgs; 
	std.vector<std.vector<cv.KeyPoint> >& imgpts
	
public:
	OFFeatureMatcher(bool _use_gpu,
					std.vector<cv.Mat>& imgs_, 
					 std.vector<std.vector<cv.KeyPoint> >& imgpts_)
	void MatchFeatures(int idx_i, idx_j, matches)
	std.vector<cv.KeyPoint> GetImagePoints(int idx) { return imgpts[idx];

