import sys
import numpy as np


def pca(data,k):
	row,col=data.shape
	means=np.mean(data,axis=0)
	data=data-means
	data_cov=np.cov(data,rowvar=0)

	eigenval,eigenvectors=np.linalg.eig(data_cov)
	eigenval_indices=np.argsort(eigenval)[::-1]
	eigenval[:]=eigenval[eigenval_indices]
	eigenvectors[:]=eigenvectors[:,eigenval_indices]
	eigenvectors_trunc=np.ones((col,k))
	print eigenvectors[:,0:2]
	Z=np.ones((row,k))
	for i in xrange(0,col):
		eigenvectors_trunc[i:]=eigenvectors[i,0:k]
	for i in xrange(0,len(data)):
		Z[i]=np.dot(eigenvectors_trunc.T,data[i])
	cov_new=np.cov(Z,rowvar=0)
	eigenvalue,eigenvector=np.linalg.eig(cov_new)


def main():
	data=np.loadtxt(sys.argv[1],dtype='float', delimiter="\t")
	k=int(sys.argv[2])
	pca(data,k)



if __name__ == "__main__":
    main()