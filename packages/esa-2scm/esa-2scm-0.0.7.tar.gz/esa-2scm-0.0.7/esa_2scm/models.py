import numpy as np
import pandas as pd
import scipy.stats as ss
from sklearn.metrics import r2_score
from typing import Union, List
from .syniv import SynIV




class BaseCM:
    
    _KNOWLEDGE = (None, 'x2->x1', 'x1->x2')
    
    def __init__(
        self, 
        x1: Union[np.ndarray, pd.Series, List], 
        x2: Union[np.ndarray, pd.Series, List],
        prior_knowledge: str = None,
        ):
        
        if np.ndim(x1) > 1 or np.ndim(x2) > 1:
            raise ValueError("Inputs for x1 and x2 must be 1-Dimensional")
        
        if len(x1) != len(x2):
            raise ValueError("Need equal sample sizes for x1 and x2")
        
        self._x1, self._x2 = np.array(x1) , np.array(x2)
                        
        if prior_knowledge in BaseCM._KNOWLEDGE:
            self._prior_knowledge = prior_knowledge
        else: raise ValueError("Valid expression for prior_knowledge: 'x2->x1' or 'x1->x2'")


class ESA2SCM(BaseCM):
    
    def __init__(self, x1, x2, prior_knowledge=None):
        super().__init__(x1, x2, prior_knowledge)


    @staticmethod
    def _estimate(x, z):
        if np.var(z, ddof=1) == 0:
            b = 0
        else:  
            b = np.cov(x, z)[0,1] / np.var(z, ddof=1)
        c = np.mean(x) - b * np.mean(z)
        x_hat = c + b * z
        return x_hat, b
    
    
    def fit(self, syniv_method: str = "esa", **kwargs):
        
        if self._prior_knowledge is not None:
            
            def estimate(x1, x2, prior_knowledge):
                x_hat, b = ESA2SCM._estimate(x1, x2)
                causal_dir = prior_knowledge
                score = r2_score(x1, x_hat)
                return x_hat, b, causal_dir, score
                        
            if self._prior_knowledge == 'x2->x1':
                self._x_hat, self._b, self._causal_dir_fixed, self._true_score = estimate(self._x1, self._x2, self._prior_knowledge)
                
            else:
                self._x_hat, self._b, self._causal_dir_fixed, self._true_score = estimate(self._x2, self._x1, self._prior_knowledge)

        else:
            estimate_syniv = SynIV.get_syniv(syniv_method)
            self._z1, self._z2 = estimate_syniv(self._x1, **kwargs), estimate_syniv(self._x2, **kwargs)
            
            self._x1_iv1sls, self._x2_iv1sls = ESA2SCM._estimate(self._x1, self._z1)[0], ESA2SCM._estimate(self._x2, self._z2)[0]
            self._x1_slsiv_corr_ = 'undefined (0 variance)' if np.var(self._x1_iv1sls) == 0 or np.var(self._x1) == 0 else np.corrcoef(self._x1_iv1sls, self._x1)[0][1] 
            self._x2_slsiv_corr_ = 'undefined (0 variance)' if np.var(self._x2_iv1sls) == 0 or np.var(self._x2) == 0 else np.corrcoef(self._x2_iv1sls, self._x2)[0][1]
            
            self._x1_iv2sls, self._b12 = ESA2SCM._estimate(self._x1, self._x2_iv1sls)
            self._x2_iv2sls, self._b21 = ESA2SCM._estimate(self._x2, self._x1_iv1sls)
            
            self._score, self._score_rev = round(r2_score(self._x1, self._x1_iv2sls), 5), round(r2_score(self._x2, self._x2_iv2sls), 5) 
            
            self._causal_dir = "x2->x1" if self._score > self._score_rev else "x1->x2" if self._score < self._score_rev else "undetermined"
            
            if self._causal_dir == "x2->x1":
                self._true_x_hat, self._true_causal_coef, self._true_score = self._x2_iv2sls, self._b12, self._score
            elif self._causal_dir == "x1->x2":
                self._true_x_hat, self._true_causal_coef, self._true_score = self._x1_iv2sls, self._b21, self._score_rev
            else:
                self._true_x_hat, self._true_causal_coef, self._true_score = np.nan, 0, 0
            
        return self
    
    
    def _summary(self):
        summary_idx = ["Causal Direction", "Goodness of Fit", "Causal Coefficient"]
        additional_idx = ["Corr (2SLS_IV-Explanatory)"]
        
        if self._prior_knowledge is not None:
            self._result = pd.DataFrame({self._prior_knowledge + " (Predetermined)": [self._prior_knowledge, self._true_score, self._b]}, index=summary_idx)
            return self._result
        
        summary_columns = ['x2->x1', 'x1->x2']
        summary_values = [str(self._causal_dir == 'x2->x1'), self._score, self._b12, self._x2_slsiv_corr_]
        summary_values_rev = [str(self._causal_dir == 'x1->x2'), self._score_rev, self._b21, self._x1_slsiv_corr_]
        self._result = pd.DataFrame({summary_columns[0]: summary_values, summary_columns[1]: summary_values_rev}, index=summary_idx+additional_idx)
        
        return self._result
    
    
    @property
    def x1(self):
        return self._x1
    
    @property
    def x2(self):
        return self._x2
    
    @property
    def z1(self):
        if hasattr(self, "_z1"):
            return self._z1
        raise AttributeError("Prior knowledge has been set")
    
    @property
    def z2(self):
        if hasattr(self, "_z2"):
            return self._z2
        raise AttributeError("Prior knowledge has been set")
    
    @property
    def causal_coef(self):
        if hasattr(self, "_b"):
            return self._b
        return self._true_causal_coef
    
    @property
    def causal_direction(self):
        if hasattr(self, "_causal_dir_fixed"):
            return self._causal_dir_fixed + ' (prior knowledge)'
        return self._causal_dir
    
    @property
    def score(self):
        return self._true_score
    
    @property
    def x_hat(self):
        if hasattr(self, "_x_hat"):
            return self._x_hat
        return self._true_x_hat
    
    @property
    def corr_x1_to_slsiv(self):
        if hasattr(self, "_x1_slsiv_corr_"):
            return self._x1_slsiv_corr_
        raise AttributeError("Prior knowledge has been set")
    
    @property
    def corr_x2_to_slsiv(self):
        if hasattr(self, "_x2_slsiv_corr_"):
            return self._x2_slsiv_corr_
        raise AttributeError("Prior knowledge has been set")
    
    @property
    def summary(self):
        return self._summary
    
