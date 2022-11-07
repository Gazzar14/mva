def one_sample_ttest(data, alpha = 0.05):
    """
    Tests hypothesis about the mean vector. use when sample size is smaller than 20p and the varaince-covariance marix is unknown  
    
    Keyword arguments: 
    data: data matrix
    alpha: significance level (default = 0.05)
    
    return:  pvalue, test-statistic
    """
    #function
    return 10

def one_sample_chi2test(data, alpha = 0.05):
    """
    Tests hypothesis about the mean vector. use when sample size is larger than 20p 
    
    Keyword arguments: 
    data: data matrix
    alpha: significance level (default = 0.05)

    return:  pvalue, test-statistic
    """
    #function
    return None
        

def two_sample_paired_ttest(data1, data2, alpha = 0.05):
    """
    Compares mean vectors of two dependent samples
    
    Keyword arguments: 
    data1: first sample data matrix
    data2: second sample data matrix
    
    return pvalue, test statistic"""    
    #function
    return None
    

def two_sample_ind_ttest(data1, data2, equal_var = True, alpha = 0.05):
    """
    Compares mean vector of two independent sample 
    
    keyword arguments:
    data1: first sample data matrix
    data2: second sample data matrix
    equal-var: assumes equal variance between two samples and uses pooled variance covariance matrix (default = True)
    
    return: pvalue, test statistic"""   
    #function
    return None
    

def sphercity_test(data, alpha = 0.05):
    """
    performs Maucly's sphercity test.
    Checks if variables are independent and have the same variance
    
    keyword arguments:
    data: data matrix
    alpha: significance level (default = 0.05)

    return:  pvalue, test-statistic
    """
    #function
    return None


def box_mtest(data1, data2, alpha = 0.05):
    """
    compares covariance beween two samples using Box's M-test
    keyword arguments:
    data1: first sample data matrix
    data2: second sample data matrix
    returns: pvalue, test statistic """
    #function
    return None
