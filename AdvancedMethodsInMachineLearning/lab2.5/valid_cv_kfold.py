# -*- coding: utf-8 -*-
"""

    TOPIC: K-fold Cross-validation

"""

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

iris = datasets.load_iris()
lg = LogisticRegression(random_state=1)

res = cross_val_score(lg, iris.data, iris.target, cv=5)
print(res)
