import matplotlib.pyplot as plt
import numpy
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()


clf = svm.SVC(gamma=0.001, C=100)

x,y = digits.data[:-10], digits.target[:-10] #storing all the digits data examples

#testing set
clf.fit(x,y)

print('Prediction', clf.predict(digits.data[-6]))
plt.imshow(digits.images[-6],cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()

