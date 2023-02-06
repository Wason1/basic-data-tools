import os
import pandas as pd

# specify the folder path
folder_path = r'C:\\combine'

# specify the file path to save the concatenated dataframe
file_path = r'C:\\combine\\dataout.csv'

# create an empty list to store the dataframes
df_list = []

print('reading data')
# loop through all the files in the folder
for filename in os.listdir(folder_path):
    # check if the file is an Excel file
    if filename.endswith(".xlsx"):
        # read the Excel file as text
        df = pd.read_excel(os.path.join(folder_path, filename), dtype=str, engine='openpyxl')
        # append the dataframe to the list
        df_list.append(df)

# concatenate all the dataframes in the list
concatenated_df = pd.concat(df_list)

'''
# set the chunksize to 1000 rows
chunksize = 1000
print('writing data')
# write the data in chunks
for i in range(0, len(concatenated_df), chunksize):
    concatenated_df[i:i+chunksize].to_excel(file_path, index=False, engine='openpyxl', startrow=i)
'''

concatenated_df.to_csv(file_path)
print('DONE!!!!!!!!!')