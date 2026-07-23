

from google.colab import files
uploaded = files.upload()

dataset = pd.read_csv('Dataset.csv')
datasetwithNaN = dataset
dataset

print(dataset.shape)
print(dataset.describe())


dataset.isna().any()


MeandatasetNotNan = dataset.price.fillna(dataset.price.mean())
MeandatasetNotNan

MediandatasetNotNan = dataset.price.fillna(dataset.price.median())
MediandatasetNotNan


dataset.describe()

percentile = dataset.price.quantile(1.0)
percentile

datasetNoOutlier = dataset[dataset.price<percentile]
datasetNoOutlier