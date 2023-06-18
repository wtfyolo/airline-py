import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mp

df = pd.read_csv(r"C:\Users\Xeon\Desktop\Airline_Customer.csv")
#print(df)
df = df[df['Type of Travel'] != '122']
#remove 122 from type of travel
columns_to_check = ["Inflight wifi service","Departure/Arrival time convenient",\
"Ease of Online booking","Food and drink","Online boarding",\
"Seat comfort","Inflight entertainment","On-board service","Leg room service",\
"Checkin service","Baggage handling","Inflight service","Cleanliness"]
#introduce column as array
for column in columns_to_check:
    df = df[df[column] != 0]
    df = df.dropna(subset=[column])
#remove 0 and NaN from satisfaction columns
df.dropna(subset=['Departure Delay in Minutes'])
df.dropna(subset=['Arrival Delay in Minutes'])
bins = [0,10,20,30,40,50,60,100]  # Define the bin edges
# Create names for the groups
#------------------------------------------------------------------
#question 4
group_names = ['<10', '10-20', '20-30', '30-40', '40-50','50-60','>60']
df['agegroup'] = pd.cut(df['Age'], bins,labels=group_names)
#we want to count the number of observations for each category
#print(pd.value_counts(df['agegroup']))

#satisfied_responses = df[df['satisfaction'] == 'satisfied']
#neutral_responses = df[df['satisfaction'] == 'neutral or dissatisfied']

#satisfied_counts = satisfied_responses['agegroup'].value_counts()
#neutral_counts = neutral_responses['agegroup'].value_counts()
# Extract the bin names and counts
#age_groups = satisfied_counts.index.tolist()
#counts = satisfied_counts.values.tolist()
#counts2 = neutral_counts.values.tolist()
# Create the figure and subplots
#fig, ax = plt.subplots(figsize=(9, 6))
#ax.bar(group_names, counts)
#ax.bar(group_names, counts2)

# Set the title and labels
#ax.set_title('Satisfaction by Age Group')
#ax.set_xlabel('Age Group')
#ax.set_ylabel('Count')
#plt.show()
#------------------------------------------------------------------
# group labels
#totalresponses = df['satisfaction']
#agegroup_counts = totalresponses['agegroup'].value_counts()

#satisfied_responses = df[df['satisfaction'] == 'satisfied']
#neutral_responses = df[df['satisfaction'] == 'neutral']

# Extract the count of 'neutral' and 'satisfied' responses for each age group
#neutral_counts = neutral_responses['neutral'].value_counts()
#satisfied_counts = satisfied_responses['satisfied'].value_counts()

#Extract the age group labels and their corresponding counts
#counts1 = neutral_counts.values.tolist()
#counts2 = satisfied_counts.values.tolist()

# Create the bar chart
#bar_width = 0.35
#index = range(len(counts1))

#plt.bar(index, counts1, bar_width, label='Neutral')
#plt.bar(index, counts2, bar_width, bottom=neutral_counts, label='Satisfied')

# Set the x-axis tick positions and labels
#plt.xticks(index, counts1)

# Set the title, x-axis label, and y-axis label
#plt.title('Responses by Age Group')
#plt.xlabel('Age Group')
#plt.ylabel('Count')

# Add a legend
#plt.legend()

# Show the plot
#plt.show()

#satisfied_responses = df[df['satisfaction'] == 'satisfied']
#neutral_responses = df[df['satisfaction'] == 'neutral or dissatisfied']

#female_responses = df[df['gender'] == 'female']
#male_responses = df[df['gender'] == 'male']

#satisfied_counts = satisfied_responses['female_responses'].value_counts()
#satisfied_counts = satisfied_responses['male_responses'].value_counts()

#neutral_counts = neutral_responses['gender'].value_counts()

# Extract the bin names and counts
#age_groups = satisfied_counts.index.tolist()
#counts = satisfied_counts.values.tolist()
#counts2 = neutral_counts.values.tolist()

# Create the figure and subplots
#fig, ax = plt.subplots(figsize=(9, 6))
#ax.bar(group_names, counts)
#ax.bar(group_names, counts2)
#-------------------------------------------------------------
#question 5
print('Inflight wifi service')
print ('num values:',df['Inflight wifi service'].count()) # number of values
print ('mean :',df['Inflight wifi service'].mean()) # arithmetic average
print ('std :', df['Inflight wifi service'].std()) # standard deviation
print ('min : ', df['Inflight wifi service'].min()) # minimum
print ('max :',df['Inflight wifi service'].max()) # maximum
print ('quartile (0.25):', df['Inflight wifi service'].quantile(.25)) # first quartile
print ('quartile (0.5):',df['Inflight wifi service'].quantile(.5)) # second quartile
print ('quartile (0.75):', df['Inflight wifi service'].quantile(.75)) # third quartile
print ('median:', df['Inflight wifi service'].median()) #find mean
print ('variance:', df['Inflight wifi service'].var()) #show vaiance
# We can look at some statistics
#----------------------------------------------------------
print('')
print('Ease of Online booking')
print ('num values:',df['Ease of Online booking'].count()) # number of values
print ('mean :',df['Ease of Online booking'].mean()) # arithmetic average
print ('std :', df['Ease of Online booking'].std()) # standard deviation
print ('min : ', df['Ease of Online booking'].min()) # minimum
print ('max :',df['Ease of Online booking'].max()) # maximum
print ('quartile (0.25):', df['Ease of Online booking'].quantile(.25)) # first quartile
print ('quartile (0.5):',df['Ease of Online booking'].quantile(.5)) # second quartile
print ('quartile (0.75):', df['Ease of Online booking'].quantile(.75)) # third quartile
print ('median:', df['Ease of Online booking'].median()) #find mean
print ('variance:', df['Ease of Online booking'].var()) #show vaiance
# We can look at some statistics
#-----------------------------------------------------
print('')
print('Departure/Arrival time convenient')
print ('num values:',df['Departure/Arrival time convenient'].count()) # number of values
print ('mean :',df['Departure/Arrival time convenient'].mean()) # arithmetic average
print ('std :', df['Departure/Arrival time convenient'].std()) # standard deviation
print ('min : ', df['Departure/Arrival time convenient'].min()) # minimum
print ('max :',df['Departure/Arrival time convenient'].max()) # maximum
print ('quartile (0.25):', df['Departure/Arrival time convenient'].quantile(.25)) # first quartile
print ('quartile (0.5):',df['Departure/Arrival time convenient'].quantile(.5)) # second quartile
print ('quartile (0.75):', df['Departure/Arrival time convenient'].quantile(.75)) # third quartile
print ('median:', df['Departure/Arrival time convenient'].median()) #find mean
print ('variance:', df['Departure/Arrival time convenient'].var()) #show vaiance
# We can look at some statistics
#----------------------------------------------------------------------
#question 6
["Inflight wifi service","Departure/Arrival time convenient",\
"Ease of Online booking","Food and drink","Online boarding",\
"Seat comfort","Inflight entertainment","On-board service","Leg room service",\
"Checkin service","Baggage handling","Inflight service","Cleanliness"]
avg_rating = df['Inflight wifi service'].mean()
df['Inflight wifi service avg']=avg_rating
print('')
print(df['Inflight wifi service avg'])



#------------------------------------------------------------------------
