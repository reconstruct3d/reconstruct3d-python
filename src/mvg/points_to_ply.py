def points_to_ply(filename, coordinates, colors):

	with open(filename + '.ply', 'w') as outfile:
	    outfile.write('ply\n')
	    outfile.write('format binary_little_endian 1.0\n')
	    outfile.write('element vertex %d\n' % coordinates.shape[0])
	    outfile.write('property float x\n')
	    outfile.write('property float y\n')
	    outfile.write('property float z\n')
	    outfile.write('property uchar red\n')
	    outfile.write('property uchar green\n')
	    outfile.write('property uchar blue\n')

	    print(colors.astype('str'))
	    outfile.write(str(colors.tolist()))
