import math
MAX,MIN=1000,-1000
def alphabeta(depth,idx,maximise,vals,alpha,beta):
	if depth==3:
		return values[idx]
	
	if maximise:
		best=MIN
		for i in range(0,2):
			val=alphabeta(depth+1,idx*2+i,False,vals,alpha,beta)
			best=max(best,val)
		if best<beta:
			alpha=max(alpha,best)
		return best
	else:
		best=MAX
		for i in range(0,2):
			val=alphabeta(depth+1,idx*2+i,True,vals,alpha,beta)
			best=min(best,val)
		if best>alpha:
			best=min(beta,best)
	return best	
	
if __name__=="__main__":
	values=[3,5,6,9,1,2,0,-1]
	print(f"REsult={alphabeta(0,0,True,values,MIN,MAX)}")
			
