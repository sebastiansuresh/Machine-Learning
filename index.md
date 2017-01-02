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
 
### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/sebastiansuresh/Machine-Learning/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
