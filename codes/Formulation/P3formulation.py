import numpy as np
from scipy.optimize import linprog

class P3formulation:

    def __init__(self, nonnegative = False):
        self.nonnegative = nonnegative
        
    def fit(self, X, y, quantiles, dec):
        n_samples = X.shape[0]
        p = X.shape[1]
        I = np.eye(n_samples)
        bub_one_quantile = np.concatenate((-y,np.zeros((n_samples,1)),y,np.zeros((n_samples,1))),axis=None)
        Aub_one_quantile = np.block([
                                        [-X,-I,np.zeros((n_samples,n_samples))],
                                        [np.zeros((n_samples,p)),-I,np.zeros((n_samples,n_samples))],
                                        [X,np.zeros((n_samples,n_samples)),-I],
                                        [np.zeros((n_samples,p)),np.zeros((n_samples,n_samples)),-I]
                                        ])
        c1 = np.concatenate((np.zeros((p,1)),quantiles[0]*np.ones((n_samples,1)),(1-quantiles[0])*np.ones((n_samples,1))))
        c2 = np.concatenate((np.zeros((p,1)),quantiles[1]*np.ones((n_samples,1)),(1-quantiles[1])*np.ones((n_samples,1))))
        c_P3 = np.concatenate((c1,c2))
        q = dec*abs(np.quantile(y,quantiles[1])-np.quantile(y,quantiles[0]))
        
        if self.nonnegative:
            A_P3 = np.block([[Aub_one_quantile,np.zeros(Aub_one_quantile.shape)],
                             [np.zeros(Aub_one_quantile.shape),Aub_one_quantile],
                             [X,np.zeros((n_samples,2*n_samples)),-X,np.zeros((n_samples,2*n_samples))],
                             [-X,np.zeros((n_samples,2*n_samples)),X,np.zeros((n_samples,2*n_samples))],
                             [-X,np.zeros((n_samples,2*n_samples)),np.zeros((n_samples,p)),np.zeros((n_samples,2*n_samples))],
                             [X,np.zeros((n_samples,2*n_samples)),-X,np.zeros((n_samples,2*n_samples))]])
            b_P3 = np.concatenate((bub_one_quantile,bub_one_quantile,q*np.ones((2*n_samples,1)),np.zeros((2*n_samples,1))),axis=None)
            
        else:
            A_P3 = np.block([[Aub_one_quantile,np.zeros(Aub_one_quantile.shape)],
                             [np.zeros(Aub_one_quantile.shape), Aub_one_quantile],
                             [X,np.zeros((n_samples,2*n_samples)),-X,np.zeros((n_samples,2*n_samples))],
                             [-X,np.zeros((n_samples,2*n_samples)),X,np.zeros((n_samples,2*n_samples))],
                             [X,np.zeros((n_samples,2*n_samples)),-X,np.zeros((n_samples,2*n_samples))]])
            b_P3 = np.concatenate((bub_one_quantile,bub_one_quantile,q*np.ones((2*n_samples,1)),np.zeros((1*n_samples,1))),axis=None)
  

        result = linprog(c_P3, A_ub = A_P3, b_ub = b_P3, bounds=(None, None))
        print("For dec = %f ,Optimization status: %d" %(dec, result.status))

        solution = result.x
        self.lowercoef = [solution[0:p]]
        self.uppercoef = [solution[p+2*n_samples:2*p+2*n_samples]]
        
        return self

    def predict(self, X):
        lower_coef = np.array(self.lowercoef)
        upper_coef = np.array(self.uppercoef)
        lower_pred = np.dot(X, lower_coef.T)
        upper_pred = np.dot(X, upper_coef.T)

        return lower_pred, upper_pred 