import pandas as pd

filename = "big-mac-full-index.csv"
df = pd.read_csv(filename)

print(df.columns)

#4. using iterrows()

for i,r in df.iterrows():
    print(r['name'], r['local_price'])

#6. Using apply ()
    
print(df.apply(lambda row: row['GDP_bigmac'], axis=1))

