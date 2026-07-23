
=

from google.colab import files
uploaded = files.upload()

dataset = pd.read_csv('dataset.csv')
print(dataset.shape)
print(dataset.head(5))

"""### Considering Temperature below 24 as Cold Climate and above 24 as Hot Climate in our dataset"""

dataset['Temp_Cat'] = dataset['Temprature'].apply(lambda x : 0 if x < 24 else 1)
datasetModified = dataset[['Confirmed', 'Temp_Cat']]
print(datasetModified.head(5))

d1 = datasetModified[(datasetModified['Temp_Cat']==1)]['Confirmed']
d2 = datasetModified[(datasetModified['Temp_Cat']==0)]['Confirmed']

m1, m2 = d1.mean(), d2.mean()
sd1, sd2 = d1.std(), d2.std()
n1, n2 = d1.shape[0], d2.shape[0]

from numpy import sqrt, abs, round
from scipy.stats import norm
def model(X1, X2, sigma1, sigma2, N1, N2): #Two sample Z test
    ovr_sigma = sqrt(sigma1**2/N1 + sigma2**2/N2)
    z = (X1 - X2)/ovr_sigma
    pval = 2*(1 - norm.cdf(abs(z)))
    return z, pval
z, p = model(m1, m2, sd1, sd2, n1, n2)

z_score = np.round(z,8)
p_val = np.round(p,6)

if (p_val<0.05):
    Hypothesis_Status = 'Reject Null Hypothesis : Significant'
else:
    Hypothesis_Status = 'Do not reject Null Hypothesis : Not Significant'

print (p_val)
print (Hypothesis_Status)