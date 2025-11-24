import pandas

#df = pandas.DataFrame({"highscore" : 0},index=[0])
#print(df["highscore"].values[0])
#df.to_csv('info.csv', index=False)
df =  pandas.read_csv('info.csv')
print(df["highscore"].values[0])