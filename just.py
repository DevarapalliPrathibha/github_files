import pandas as pd
df = pd.read_csv("C:/Users/user718/PycharmProjects/pythonProject/advance_project/pokemon_data.csv")
#de = pd.read
print(df)


#df_csv=pd.read_csv('pokemon_data.csv')
#print(df_csv)
print(df.head(5))

df_txt=pd.read_csv('pokemon_data.csv')
print(df_txt)

print(df[["Name","Type 1","HP"]])

print(df.iloc[2,1])
print(df.sort_values(["Speed"],ascending=True))
print(df.sort_values(["Type 1","Speed"],ascending=[1,0]))

#changes to data
df['Total']=df['HP']+df['Attack']+df['Sp. Atk']+df['Speed']
print(df)
df = df.drop(columns=["Total"])
print(df)

df["Total"]=df.iloc[:,4:10].sum(axis=1)
print(df)

cols=list(df.columns)
print(cols)

df =df[cols[0:4]+[cols[-1]]+cols[4:12]]
print(df)
