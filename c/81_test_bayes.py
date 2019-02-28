# -*- coding: utf-8 -*-
# @Time    : 2/27/19 10:31 AM
# @Author  : Anxi.xue
# @Email   : xueanxi@163.com

import numpy as np
X = np.random.randint(5, size=(6, 10))
print('X',X)
y = np.array([1, 2, 3, 4, 5, 6])
print('y',type(y))
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(X, y)
print(clf.predict(X[2:3]))