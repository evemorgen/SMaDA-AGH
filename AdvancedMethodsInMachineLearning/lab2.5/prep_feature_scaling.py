# -*- coding: utf-8 -*-
"""

    TOPIC: Feature Scaling

"""

import pandas as pd

from sklearn import datasets

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

from sklearn.preprocessing import StandardScaler

#%% Set parameters.

n_neighbors = 3

#%% Load the dataset and prepare train/test subsets.

dataset = datasets.load_wine()
X_raw = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
y = pd.DataFrame(data=dataset.target, columns=['quality'])

# Make a train/test split using 30% test size.
X_train_raw, X_test_raw, y_train, y_test = train_test_split(X_raw, y,
                                                            test_size=0.30,
                                                            stratify=y,
                                                            random_state=42)
#%% Fit a kNN classifier on the unscaled data.


clf_raw = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X_train_raw, y_train.values.ravel())

y_test_pred_raw = clf_raw.predict(X_test_raw)

print('\n== CLASSIFICATION PERFORMANCE (raw) ==\n')
acc_raw = accuracy_score(y_test_pred_raw, y_test)
print('Accuracy (original): {:.3f}'.format(acc_raw), '\n')
print('Classification report:\n', classification_report(y_test, y_test_pred_raw))

#%% Standardize features by removing the mean and scaling to unit variance.

scaler = StandardScaler().fit(X_raw)
X_scaled = X_raw.copy()
X_scaled.iloc[:,:] = scaler.transform(X_raw)


#%% Fit a kNN classifier on the scaled data.
X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(X_scaled, y,
                                                            test_size=0.30,
                                                            stratify=y,
                                                            random_state=42)

clf_scaled = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X_train_scaled, y_train.values.ravel()) 

y_test_pred_scaled = clf_scaled.predict(X_test_scaled)

print('\n== CLASSIFICATION PERFORMANCE (scaled) ==\n')
acc_scaled = accuracy_score(y_test_pred_scaled, y_test)
print('Accuracy (original): {:.3f}'.format(acc_scaled), '\n')
print('Classification report:\n', classification_report(y_test, y_test_pred_scaled))
