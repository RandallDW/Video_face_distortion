import numpy as NP
import numpy.ma as ma
def build_face_mask(w,h) :
	left = int(w/5);
	right = left
	fill = w-right-left
	row = NP.r_[left*[0],fill*[1],right*[0]]
#	print(row)
#	re = NP.r_[left*[0,0],fill*[1],right*[0,0]]
#	half = int(h/2)
#	if h%2 ==0 :
#		out= NP.row_stack(half*(row,row))
#	else:
#		out= NP.row_stack(half*(row,row))
#		out= NP.row_stack((out,row))
#	print(out)
	out = row 
	for x in range (1,h):
		if x <= h*0.125 and left>=1:
			left = left-1
			right = left
			fill = w-right-left
			row = NP.r_[left*[0],fill*[1],right*[0]]
			out = NP.row_stack((out,row))
		elif x >= (0.8*h) : 
			left = left+1
			right = left
			fill = w-right-left
			row = NP.r_[left*[0], fill*[1],right*[0]]
			out = NP.row_stack((out,row))
		else:
			row = NP.r_[left*[0], fill*[1], right*[0]]
			out = NP.row_stack((out,row))
#		print(out)
	return out
#if __name__=='__main__':
#	build_face_mask(20,10)


