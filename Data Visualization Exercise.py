#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd # for data import/data wrangling
import seaborn as sns 


# In[3]:


storms = pd.read_csv('C:/Users/Luna Tsai/Desktop/storms.csv')
storms_cut = storms.iloc[0:159,:] # So only the first 159rows
#storms.head()
storms_cut.head()


# In[4]:


#Generate a histogram of pressure; how about different histograms of pressure based on each status
sns.histplot(storms_cut, x = "pressure")


# In[5]:


#Generate a boxplot of pressures for each storm
sns.boxplot(data=storms_cut, x="name", y="pressure")


# In[6]:


#Generate a countplot for each storm.
sns.countplot(storms_cut, x = "name")


# In[8]:


#Generate a scatter plot between wind and pressure depicting at the same time a linear line that fits the observations the best.
#sns.lmplot(x = "wind", y = "pressure ",
#           hue = "Sex", data = storms_cut)

sns.lmplot(x = "wind", y = "pressure" ,data = storms_cut)
#sns.lmplot(x = "wind", y = "pressure", hue = "name", data = storms_cut) 


# In[11]:


#Generate a scatter plot depicting the trajectories of each storm using lat and long column; which means the x-axis describes longitute 
#whereas the y-axis describes latitude information of the center of the storms. Add grid lines as well.
ax = sns.scatterplot(data=storms_cut, x="long", y="lat", hue = "name", style = "category")
sns.move_legend(ax, "upper right",bbox_to_anchor=(1.3, 1))
#plt.title('Passenger age versus ticket fare for each sex')
#plt.xlabel('Passenger age')
#plt.ylabel('Ticket fare')
#ax.set_xticks(range(0,81,20)) # x axis ticks
plt.grid()  #grid line
#sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
#plt.savefig("beautiful_plot.png")

