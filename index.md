## Handwritting recognition   

In this project I have used the handwritten digits data set provided by scikit learn to train and test my machine learning algorithim. The data sets that are imported will act as training data for the algorithim. Since this is a supervised learing problem the algorithim will use the training data set to classify the different handwritten values.
I used Python to impliment the machine learning algorithim.

First the different modules were imported. 
```
import matplotlib.pyplot as plt
import numpy
from sklearn import datasets
from sklearn import svm
```
The handwriting data sets are loaded.

```
digits = datasets.load_digits()
```

The following code analyzes the data for classification 
```
clf = svm.SVC(gamma=0.001, C=100)
 ```
 
 The data is fitted to a model and learns from the model
 ```
 clf.fit(x,y)
 ```
 
 The following line of code prints out the prediction after learning the model
 ```
 print('Prediction', clf.predict(digits.data[-6]))
 ```
 
 The oputput for the testing value [-5] is 4
 
 ![image](https://github.com/sebastiansuresh/Machine-Learning/blob/master/prediction.png)
 
 From the below image it can be seen that the algorithim was succesfull in learning the various values of the handwritten numbers and predicting the corect number that was inputted.
 
 ![image] (https://github.com/sebastiansuresh/Machine-Learning/blob/master/Number.png)


