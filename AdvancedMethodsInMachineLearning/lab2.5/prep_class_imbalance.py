# -*- coding: utf-8 -*-
"""

    TOPIC: Class Imbalance Problem

"""

"""

NO balance-scale.data FILE PROVIDED


"""


import pandas as pd
import numpy as np
 
# Read the dataset.
df0 = pd.read_csv('balance-scale.data', 
                  names=['balance', 'var1', 'var2', 'var3', 'var4'])

#%% Analyze the original dataset.
 
print('Example observations:')
print(df0.head(n=3), '\n')

print('Number of instances in each class (raw):')
print(df0['balance'].value_counts(), '\n')

#%% Transform into binary classification.

df_raw = df0.copy()
df_raw['balance'] = [1 if b=='B' else 0 for b in df_raw.balance]
 
print('Number of instances in each class (K=2):')
print(df_raw['balance'].value_counts(), '\n')

#%% Predict using logistic regression on the original dataset.

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Separate input features (X) and the target variable (y).
X_raw = df_raw.drop('balance', axis=1)
y_raw = df_raw.balance
 
# Train the model.
clf_raw = LogisticRegression().fit(X_raw, y_raw)
 
# Predict on the training set.
y_pred_raw = clf_raw.predict(X_raw)

acc_original = accuracy_score(y_pred_raw, y_raw)
print('Accuracy (original): {:.3f}'.format(acc_original))
print('Predicted classes:', np.unique(y_pred_raw), '\n')

#%% Predict using logistic regression on the resampled dataset.

from sklearn.utils import resample

# Separate majority and minority classes
df_majority = df_raw[df_raw.balance == 0]
df_minority = df_raw[df_raw.balance == 1]
 
# Upsample minority class
df_minority_upsampled = resample(df_minority, 
                                 replace=True,     # sample with replacement
                                 n_samples=df_majority.shape[0],  # to match majority class
                                 random_state=123) # for reproducibility
 
# Combine majority class with upsampled minority class
df_upsampled = pd.concat([df_majority, df_minority_upsampled])
 
# Display new class counts
print('Number of instances in each class (K=2, upsampled):')
print(df_upsampled.balance.value_counts(), '\n')

# Separate input features (X) and target variable (y)
X_sample = df_upsampled.drop('balance', axis=1)
y_sample = df_upsampled.balance
 
# Train model
clf_sample = LogisticRegression().fit(X_sample, y_sample)
 
# Predict on training set
y_pred_sample = clf_sample.predict(X_sample)
 
print('Accuracy (resampled): {:.3f}'.format(accuracy_score(y_sample, y_pred_sample)))
print('Predicted classes:', np.unique(y_pred_sample), '\n')
