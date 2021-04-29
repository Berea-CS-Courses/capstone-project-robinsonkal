import pandas as pd


#new_df = pd.DataFrame()
#new_df['potential_dog_whistle'] = ""
#new_df['count_of_use']=""
#new_df['ratio_of_use']=""

df_fourchandata = pd.read_excel (r'C:\Users\robinsonkal\Desktop\File fourchan_Data_pol_run2_copy.xls')
print (df_fourchandata)

df_Reuter_Data = pd.read_excel (r'C:\Users\robinsonkal\Desktop\File Rueter_Data_cleaned_copy.xls')
print(df_Reuter_Data)

new_df=pd.merge(df_fourchandata, df_Reuter_Data, on="cleaned_word")
print(new_df)

new_df.to_csv(r'C:\Users\robinsonkal\Desktop\Comparison_data_second.csv', index = False)


