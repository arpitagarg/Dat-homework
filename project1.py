
# coding: utf-8

# # Project 1_Arpita Garg
# 
# In this first project you will create a framework to scope out data science projects. This framework will provide you with a guide to develop a well-articulated problem statement and analysis plan that will be robust and reproducible.

# ## Questions related to `admissions.csv` dataset

# #### 1. Create a data dictionary 

# Answer: 
# 
# Variable | Description | Type of Variable
# ---| ---| ---
# Admit | 0 = no admission 1 = admission | categorical
# GPA | 0-4, 4 is highest | discrete 
# GRE | 200-800, 800 is highest | discrete 
# Prestige | 1-4, 1 is highest | discrete 
# 

# We would like to explore the association between X and Y 

# #### 2. What is the outcome?

# Answer:Student Admission Success Rate for prestige 1

# #### 3. What are the predictors/covariates? 

# Answer:Gre, Gpa, Prestige, Admit

# #### 4. What timeframe is this data relevant for?

# Answer: Not Mentioned in data

# #### 5. What is the hypothesis?

# Answer:Majority of the students with Prestige 1 have higher Gpa and Gre scores.

# #### 6. Using the above information, write a well-formed problem statement. 
# 

# Answer:Determine students with prestige 1 have a higher admission rate?

# ### Exploratory Analysis Plan

# Using the lab from a class as a guide, create an exploratory analysis plan. 

# #### 1. What are the goals of the exploratory analysis? 

# Answer: To analyze the range of GPA and GRE score for Prestige 1 students with success in admission.

# #### 2a. What are the assumptions regarding the distribution of the data? 

# Answer: The data is distributed across the same time period, given that no specific reference is made to time. Each data point represents 1 student. All data points have been collected from students from one school.

# #### 2b. How will you determine the distribution of your data? 

# Answer: By plotting the data points on the graph to understand the distribution of each feature

# #### 3a. How might outliers impact your analysis? 

# Answer: Datapoints stating that lower GPA, GRE and Presitige lead to a successful admission will neagatively impact our data because they could have different admission criteria like ethnicity and sports quota

# #### 3b. How will you test for outliers? 

# Answer: Plot the data points on the graph, cluster the data points to further check for outliers

# #### 4. What is your exploratory analysis plan?
# Using the above information, write an exploratory analysis plan that would allow you or a colleague to reproduce your analysis 1 year from now. 

# Answer: 
# 1.Understand the various predictors for accurate outcome
# 2.Data Organizing and Cleaning Data
# 3.Plotting the data, and checking for outliers
# 4.Checking the correlation between all factors to understand the relationship between data points
# 5.Create a graph (ex:histogram)to further analyze data on information needed

# ## Bonus Questions:
# 1. Outline your analysis method for predicting your outcome
# 2. Write an alternative problem statement for your dataset
# 3. Articulate the assumptions and risks of the alternative model

# Answer:
# 1. Cross Tab
# 2. Determine the average GMAT score that is accepted in school
# 3. a. No other criteria is used in accepting a student to school
#    b. All scores and acceptance rates refer to one time period 
