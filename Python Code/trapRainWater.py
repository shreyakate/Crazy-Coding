def trapRainWater(height):
	 l, r, tmp, water = 0,len(height)-1,0,0
	 lmax, rmax= height[l], height[r]

	 while l<r:
	 	if height[l]<=height[r]:
	 		curr = height[l]
	 		lmax = max(lmax, curr)
	 		water += lmax - curr
	 		l += 1
	 	else:
	 		curr = height[r]
	 		rmax = max(rmax, curr)
	 		water += rmax - curr
	 		r -= 1
	 return  water

print trapRainWater([0,1,0])



