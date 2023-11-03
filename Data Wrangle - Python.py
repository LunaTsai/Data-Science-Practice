#!/usr/bin/env python
# coding: utf-8

# # Welcome to the Data Wrangling in Python workshop!
# 
# Data wrangling is a crucial step in the preparation of data before performing analyses. This workshop is designed to teach how to manipulate Pandas Dataframe in Python. We will cover data structure, data manipulation, and simple data analysis. 
# At the end of this workshop, you will be able to:
# 
# - Import csv file
# - Glimpse your data set and print summaries 
# - Select necessary columns & drop unnecessary columns
# - Filter rows (observations) satisfying conditions
# - Change column names & order of columns
# - Add new columns to the current data set using its values
# - Make your data set wider/narrower
# - Derive conclusions from your data wrangling
# 
# #"group" is very important

# ## Let us start from loading necessary packages!

# In[3]:


import numpy as np # incase repetition, linear algerbra
import pandas as pd #multiple dimiensions


# ## NumPy (numerical Python) vs Pandas 

# |      | NumPy    | Pandas    |
# |:----:|:--------:|:--------:|
# |Purpose|  Working with arrays and matrices of numerical data  | Structured data (tabular)|
# |Data Structures|  ndarray   |  DataFrame (2-dim'l), Series (1-dim'l) | 
# |  Features  |  Linear algebra, linear transformations (ex. PCA)   |  Data cleaning, manipulations (aggregations, regrouping, reshaping) | 

# ## Today's data: Estimates of the components of interprovincial migration, quarterly (from Statistics Canada)
# 
# Today we'll deal with a data set from Statistics Canada on the estimates of the componenents of interprovincial migration on a quarterly basis (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710002001). In the shared folder, you should be able to see the csv file called "migration.csv". "migration_description.csv" contains detailed description of the data set. Roughly speaking, this dataset includes total number of in-migrants and out-migrants in each province over time.
# 
# Let us start from importing the data set.

# ## 1. Import data set

# In[4]:


migration = pd.read_csv('cmigration.csv')


# In[1]:


mig_org =  pd.read_csv('C:/Users/Luna Tsai/Desktop/migration.csv') #save the original data set just in case


# It's always a good habit to glimpse first the data set you are reading:

# In[5]:


migration.head()


# How big is our dataset?

# In[6]:


migration.shape


# ## 2. Understanding data a little bit more

# After seeing the first few rows of the migration data set as well as the column names, you might already have a couple of questions to be answered. For example, What's the time period over which the data was taken? In the *GEO* column, it looks like we have names of provinces and territories but am I sure about this (i.e. how to print distinct values of the column)? What are the maximum/minimum values of the *Value* column?

# ### unique() function: print distinct values

# In[7]:


migration["GEO"].unique()


# In[8]:


migration["Interprovincial migration"].unique()


# In[9]:


min(migration["VALUE"])


# In[10]:


max(migration["VALUE"])


# In[14]:


migration["VALUE"].describe()


# We can summarize the *VALUE* column by province as well:

# In[11]:


#summarize VALUE by GEO
migration.groupby('GEO')['VALUE'].describe()


# Can we do the same thing for the "REF_DATE" column?

# In[12]:


migration["REF_DATE"].describe()


# Why does it look different than the "VALUE" column? The answer stays in the *data type* of the columns.

# In[13]:


migration.dtypes


# Let us change the "REF_DATA" column to have another data type called *datetime*; it seems that each entry has the format "yyyy-mm". 

# In[14]:


migration_date = pd.to_datetime(migration['REF_DATE'], format='%Y-%m')
#pd.to_datetime(migration['REF_DATE'], format='%Y-%m').apply(lambda x: x.strftime('%Y-%m'))
migration_date


# In[15]:


migration_date.describe()


# ## 3. How to select/drop columns (to be corrected)

# It seems that we have many columns whose information is not really useful to us. We can remove these columns.

# In[16]:


migration.columns


# In[17]:


migration.drop(columns='DGUID', inplace=True) #"inplace = True" modifies the original DataFrame in-place


# In[18]:


migration.columns


# In[19]:


migration.drop(columns = ['UOM', 'UOM_ID', 'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'STATUS', 'SYMBOL',
                         'TERMINATED', 'DECIMALS'], inplace = True)


# In[20]:


migration.columns


# We could've selected columns using `.loc` or `.iloc` function. `.loc` uses column/row names, whereas `.iloc` uses column/row indices.

# In[21]:


mig_org.loc[:, ['REF_DATE', 'GEO', 'Interprovincial migration', 'VALUE']]
# The first : refers to the all rows of the data frame


# In[22]:


mig_org.iloc[:, [0,1,3,10]] # use indices instead of column names


# ## 4. How to split the 'REF_DATE' column?

# How could we split the year/month/day into separate columns? 

# In[23]:


migration[['year','month']] = migration['REF_DATE'].str.split('-',expand=True) #string split by the delimiter '-'


# In[30]:


migration


# In[24]:


migration.drop(columns='REF_DATE', inplace=True)


# In[25]:


migration.head()


# ## 5. How to change column names & column order

# How to change the column order?

# In[26]:


migration = migration[['year', 'month', 'GEO', 'Interprovincial migration', 'VALUE']]
migration.head()


# How could we change the column name 'VALUE' to 'number'?

# In[27]:


migration.rename(columns={'VALUE': 'number'}, inplace=True)
migration.head()


# ## 6. Filtering rows by "masking"

# ### Logical operators in Python

# | Operator | Function     |
# |----------|--------------|
# | ==       | Equal        |
# | !=       | Not Equal    |
# | >        | Bigger than  |
# | <        | Smaller than |
# | &        | And          |
# | \|       | Or           |
#     

# In[28]:


3 == 4


# In[29]:


4>3


# In[30]:


a = np.array([1,2,3])
b = np.array([1,2,4])
a!=b


# In[31]:


np.sum(a!=b)


# So by using these logical operators, we can "mask" rows that do not satisfy certain conditions. Our goal is to remove the value "Canada" from the *GEO* column.

# In[35]:


migration["GEO"] != "Canada"


# In[28]:


np.sum(migration["GEO"] == "Canada") # number of rows whose value in the GEO column is Canada


# Or we can print the counts of distinct values from a column using `value_counts`.

# In[29]:


migration["GEO"].value_counts()


# In[30]:


mig_filtered = migration[migration["GEO"] != "Canada"]


# In[31]:


mig_filtered.head()


# ## 7. Sorting 
# 
# Let us sort the rows by the value of the "number" column.

# In[32]:


mig_sorted = mig_filtered.sort_values(by='number', ascending = False)
mig_sorted


# ## 8. Make your data look wider? longer?: pivot vs melt

# In[34]:


mig_filtered.pivot(index = ['year', 'month', 'GEO'], columns = 'Interprovincial migration', values='number')


# In[35]:


mig_wider_month = mig_filtered.pivot(index = ['year', 'GEO', 'Interprovincial migration'], columns = 'month', values='number')
mig_wider_month


# In[36]:


mig_wider_month.columns


# In[37]:


mig_wider_month = mig_wider_month.reset_index()
mig_wider_month


# In[38]:


mig_wider_month.columns


# In[39]:


mig_wider_month.melt(id_vars=['year', 'GEO', 'Interprovincial migration'], var_name='month', value_name='number')


# ## 9. Add a new column using the data from the current data set & with ifelse condition

# In[40]:


mig_in_out = mig_filtered.pivot(index = ['year', 'month', 'GEO'], columns = 'Interprovincial migration', values='number')
mig_in_out = mig_in_out.reset_index() #reset column name
mig_in_out


# In[42]:


mig_in_out['migrants_total'] = mig_in_out['In-migrants'] + mig_in_out['Out-migrants']


# In[43]:


mig_in_out


# In[44]:


# adding a column using ifelse
mig_in_out['migrants_flux'] = np.where(mig_in_out['In-migrants']>mig_in_out['Out-migrants'], "positive", "negative")


# In[45]:


mig_in_out


# ## 10. Derive (tentative) conclusions from the data set

# Q. Number of total immigrants by province over the entire period?

# In[47]:


mig_in_out.groupby('GEO')['migrants_total'].sum()


# Q. Count the number of positive/negative flux of migrants by each province?

# In[52]:


mig_flux = mig_in_out.groupby(['GEO','migrants_flux'])['month'].count() #important takeaway
mig_flux


# In[53]:


type(mig_flux)


# In[55]:


mig_flux.columns


# In[56]:


mig_flux.index


# In[57]:


mig_flux_df = pd.DataFrame(mig_flux)
mig_flux_df = mig_flux_df.reset_index()
mig_flux_df


# In[59]:


mig_flux_df.columns


# Q. From `mig_flux_df`, how can we calculate immediately which province/territory had the biggest differences in the number of months of net positive/negative flux of migrants?

# In[65]:


mig_flux_df = mig_flux_df.pivot(index = 'GEO', columns = 'migrants_flux', values='month')
mig_flux_df['diff'] = mig_flux_df['positive'] - mig_flux_df['negative']
mig_flux_df


# ## Let us work on another data set as an exercise!

# **billboard** data set shows song rankings for Billboard top 100 in the year 2000. The data set is from the "Whiteburn"project, https://waxy.org/2008/05/the_whitburn_project/. This is a data set with variables:
# 
#      - artist: artist name
#      - track: song name
#      - date.entered: date the song entered the top 100
#      - wk1-wk76: Rank of the song in each week after it entered
# 
# Let me import the data set for you, and from there you should work on the following exercise problems I created!

# # Exercise problems
# 
# 0. Print the first five rows of the `billboard` data set.
# 1. What's the dimension (number of rows and columns) of the data set?
# 2. What are the column names?
# 3. What's the data type of each column?
# 4. What are the unique values of the `date.entered` column?
# 5. How many counts of unique values of the `artist` column?????
# 6. Print summary statistics of the `wk1` column.
# 7. Filter the dataset in a way that only `Houston, Whitney` shows up in the artist column. Save the filtered data set to `Whitney_Houston`.
# 8. Sort `Whitney_Houston` based on the descending order of the `date.entered` column.
# 9. Select all the columns only upto `wk9`. Save it into `Whitney_Houston` again.
# 10. From `Whitney_Houston`, make a summary table that generates mean of Whitney's rank of her songs for each week.
# 11. From `Whiteney_Houston`, make a new data frame that still maintains `artist`,`track`,`date.entered` columns but a new column called `week` contains column names from `wk1` to `wk9` and another new column called `rank` contains the rank for each combination of track and week (so our data set now looks *longer* than `Whitney_Houston`). Save the data set into `Whitney_Houston_long`.
# 12. From `Whiteny_Houston_long`, derive the average rank of each track and conclude which track of Whitney Houston had the highest (so the smallest in terms of number) rank on average.

# In[4]:


billboard = pd.read_csv("C:/Users/Luna Tsai/Desktop/billboard.csv")


# In[5]:


billboard.head()


# In[6]:


billboard.columns


# In[7]:


billboard.dtypes


# In[8]:


billboard['date.entered'].unique()


# In[10]:


billboard['artist'].value_counts()


# In[80]:


billboard['wk1'].describe()


# In[56]:


np.sum(billboard['wk1'])


# In[72]:


Whitney_Houston = billboard[billboard['artist'] == 'Houston, Whitney']
Whitney_Houston.head()


# In[73]:


Whitney_Houston_sorted = Whitney_Houston.sort_values(by='date.entered', ascending = False)


# In[74]:


Whitney_Houston_sorted


# In[81]:


#Select all the columns only upto `wk9`. Save it into `Whitney_Houston` again.
Whitney_Houston = Whitney_Houston.iloc[:,0:12] # or Whitney_Houston.loc[:'artist']


# In[82]:


Whitney_Houston


# In[88]:


Whitney_Houston.loc[:,'wk1':'wk9'].mean()


# In[83]:


Whitney_Houston.loc[:,'wk1':'wk9'].mean(axis =1)


# In[85]:


#Q11
Whitney_Houston_long = Whitney_Houston.melt(id_vars=['artist', 'track', 'date.entered'], var_name='week', value_name='rank').sort_values(by = ['track','week'])


# In[86]:


Whitney_Houston_long


# In[87]:


Whitney_Houston_long.groupby('track')['rank'].mean()

