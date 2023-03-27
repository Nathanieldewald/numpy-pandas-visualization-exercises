'''
1.How many negative numbers are there?

2.How many positive numbers are there?

3.How many even positive numbers are there?

4.If you were to add 3 to each data point, how many positive numbers would there be?

5.If you squared each number, what would the new mean and standard deviation be?

6.A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. 
This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.

7.Calculate the z-score for each data point. Recall that the z-score is given by:

8.Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.
'''

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

number_of_neg = np.sum(a<0)
print("1.How many negative numbers are there?",number_of_neg)

number_of_pos = np.sum(a>=0)
print("2.How many positive numbers are there?",number_of_pos)
print(a)
number_even = a[(a>0) & (a & 2 == 0)]
print("3.How many even positive numbers are there?",(number_even))

question4 = [a + 3]
#print(question4)
#question4 = len(question4[question4 >= 0])
#print("4.If you were to add 3 to each data point, how many positive numbers would there be?",question4)

#question5 = ((a**2)).nanstd()
#print("5.If you squared each number, what would the new mean and standard deviation be?", question5)