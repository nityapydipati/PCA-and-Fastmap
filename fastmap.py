from __future__ import division
import sys
import numpy as np



def fastmap(data,list_obj,obj):
	obj_A=obj[0]
	obj_B=obj[1]
	row,col=data.shape
	new_dist=np.zeros((row,col))
	d_ab=obj[2]
	x=[]
	for j in xrange(0,len(list_obj)):
		d_a=0
		d_b=d_ab
		
		for i in xrange(0,len(data)):
			

			if(((data[i][1]==obj_A and data[i][0]==list_obj[j]) or (data[i][1]==list_obj[j] and data[i][0]==obj_A)) and list_obj[j]!=obj_A):

				d_a=data[i][2]
				
			elif(((data[i][1]==obj_B and data[i][0]==list_obj[j]) or (data[i][1]==list_obj[j] and data[i][0]==obj_B)) and list_obj[j]!=obj_B): 
				
				d_b=data[i][2]
				
		
		if(list_obj[j]!=obj_A and list_obj[j]!=obj_B):
			x.append((np.square(d_a)+np.square(d_ab)-np.square(d_b)) / (2*d_ab))
		elif(list_obj[j]==obj_A):
			x.append(d_a)
		elif(list_obj[j]==obj_B):
			x.append(d_b)
	return x
	

def main():
	data=np.loadtxt(sys.argv[1],dtype='float', delimiter="\t")
	k=sys.argv[2]
	final=[]
	
	for i in xrange(0,k):
		indexmin=np.argmax(data[:,2])
		obj=data[indexmin]
		list_obj=[]
		for i in xrange(0,len(data)):
			for j in xrange(0,2):
				if(data[i][j] not in list_obj):
					list_obj.append(data[i][j])
		x=fastmap(data,list_obj,obj)
		
		final.append(x)
		
		for j in xrange(0,len(data)):
			
			data[j][2]=(np.sqrt((np.square(data[j][2])-np.square(x[int(data[j][0])-1]-x[int(data[j][1])-1]))))
		print data
	print np.array(final).T
		

		


if __name__ == "__main__":
    main()