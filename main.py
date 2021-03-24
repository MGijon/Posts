"""Model Selection practice for clasasification model."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris           # Load the dataset

plt.style.use('ggplot')

data = load_iris()
X = data['data']
y = data['target']
names = data['target_names']
feature_names = data['feature_names']

print(type(data))