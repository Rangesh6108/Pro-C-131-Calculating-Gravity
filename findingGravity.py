import csv
import pandas as pd

rows=[]
with open("stars.csv",'r') as f:
    dataframe=csv.reader(f)
    for i in dataframe:
        rows.append(i)

headers=rows[0]
star_data=rows[1:]

df=pd.read_csv("stars.csv")

solar_mass=df["Mass"].tolist()
solar_radius=df["Radius"].tolist()
star_names=df["Star Name"].tolist()
distance=df["Distance"].tolist()

solar_mass.pop(0)
solar_radius.pop(0)
star_names.pop(0)
distance.pop(0)

mass_kgs=[]
for i in solar_mass:
    templist=float(i)*1.989e+30
    mass_kgs.append(templist)

# print(mass_kgs)

radius_mets=[]
for i in solar_radius:
    templist=float(i)*6.957e+8
    radius_mets.append(templist)

star_gravity=[]
for index, gravity in enumerate(star_names):
    tempgravity=(float(mass_kgs[index])*5.972e+24)/(float(radius_mets[index])*float(radius_mets[index])*6371000*6371000)*6.74e-11
    star_gravity.append(tempgravity)

# print(star_gravity)

df=pd.DataFrame(
    list(zip(star_names, distance, mass_kgs, radius_mets, star_gravity)),
    columns=["star_name","distance","mass","radius","gravity"]
)

df.to_csv("final.csv")