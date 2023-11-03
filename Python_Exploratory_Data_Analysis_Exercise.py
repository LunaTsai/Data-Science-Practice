#!/usr/bin/env python
# coding: utf-8

# Draw a correlation heatmap to see the associations among different numerical variables. Which variables have the highest association? How about the lowest

# Try to answer these questions!
# Draw a correlation heatmap to see the associations among different numerical variables. Which variables have the highest association? How about the lowest?
# Draw a pairplot but by using HeartDisease variable for coloring. Do you observe anything interesting?
# Generate a contingency table for Sex and ChestPainType. How about Sex versus HeartDisease?
# Draw a countplot of ChestPainType but by using HeartDisease for coloring. What do you find interesting?
# Draw a boxplot of MaxHR across HeartDisease but by using Sex for coloring. What do you find interesting?
# Generate a decision tree with max_depth = 2 where the target variable is HeartDisease and the independent variables are all the numerical variables from Heart data set. Which variables are the most important in determining HeartDisease? Do you think our decision tree is a "good" classifier?

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd # for data import/data wrangling
import seaborn as sns # for statistical visualization


# In[6]:


heart = pd.read_csv('C:/Users/Luna Tsai/Desktop/heart.csv')

#calculate the correlation matrix on the numeric columns
#corr = penguins.select_dtypes('number').corr()

# plot the heatmap
#sns.heatmap(corr, annot = True)
heart.head()


# In[5]:


#Draw a correlation heatmap to see the associations among different numerical variables. 
#Which variables have the highest association? How about the lowest?
corr = heart.select_dtypes('number').corr()
sns.heatmap(corr, annot = True)


# In[9]:


sns.pairplot(heart, hue = "HeartDisease")


# In[32]:


heart.dtypes
#combine two columns???? ask
heart["sex_ChestPainType"] = heart.Sex + ', '+ heart.ChestPainType

heart.head()


# In[23]:


#How about Sex versus HeartDisease
pd.crosstab(heart['Sex'], heart['ChestPainType'])


# In[22]:


pd.crosstab(heart['Sex'], heart['HeartDisease'])


# In[24]:


#Draw a countplot of ChestPainType but by using HeartDisease for coloring. What do you find interesting?
sns.countplot(data =heart, x = "ChestPainType", hue = "HeartDisease")


# In[14]:


#Draw a boxplot of MaxHR across HeartDisease but by using Sex for coloring. What do you find interesting?
sns.boxplot(data = heart, x = "HeartDisease", y = "MaxHR",hue = "Sex")
#sns.boxplot(data = heart, x = "MaxHR", y = "HeartDisease",hue = "Sex")


# In[31]:


#Generate a decision tree with max_depth = 2 where the target variable is HeartDisease and the independent variables are all the numerical variables from Heart data set. 
#Which variables are the most important in determining HeartDisease? 
#Do you think our decision tree is a "good" classifier?
from sklearn import tree


#X= heart.loc['Age','RestingBP','Cholesterol','FastingBS','MaxHR','Oldpeak']
#y = heart.loc['HeartDisease'] #species #target variable that'll be used for species prediction
#model3 = tree.DecisionTreeClassifier(max_depth=2)
#model3 = model3.fit(X, y)

X  = heart.select_dtypes("number").drop(columns = 'HeartDisease')
#X = heart[['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak']]
y = heart['HeartDisease'] #species #target variable that'll be used for species prediction
y = heart.loc[:,"HeartDisease"]
model3 = tree.DecisionTreeClassifier(max_depth=2)
model3 = model3.fit(X, y)
tree.plot_tree(model3)

