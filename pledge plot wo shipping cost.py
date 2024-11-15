import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read KS csv

df  = pd.read_csv("C:\\Users\\cwoss\\Downloads\\data.csv")

funding_list = df['dumshit'].tolist()

# for i in funding_list:
#     global funds
#     try: 
#         funds = i
#         fund_chart = plt.funds(i)
#         df = fund_chart.history(period='2mo', interval='1d')
#     except Exception as e: #Add an except block to handle exceptions
#         print(f"An error occurred: {e}")
    
    
    
#Display the first few rows of the Dataframe

#print(df.head())


#Check the columns and data types

#print(df.info())

#Display basic statistics 

#print(df.describe())

#Accessing date (or dumshit)

df['dumshit'] = pd.to_datetime(df['dumshit']) #Convert 'dumshit' (date) to datetime format

#Clean 'Backing Minimum' by converting it to numeric, forcing invalid values to NaN
df['Backing Minimum'] = pd.to_numeric(df['Backing Minimum'], errors='coerce')

#Drop rows where 'Backing Minimum' or 'dumshit' are missing. Optional step. 

# df = df.dropna(subset=['Backing Minimum', 'dumshit'])
#Plotting the funding trend


plt.figure(figsize=(10,5)) 
plt.plot(df['dumshit'], df['Backing Minimum'], marker='o')
plt.title('Funding Trends Viz')
plt.xlabel('dumshit')
plt.ylabel('Backing Minimum')
plt.grid()
plt.show()