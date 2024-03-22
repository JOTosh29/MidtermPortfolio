import csv
import pandas as pd

data = pd.read_csv(r'C:\Users\Jim Owen\Downloads\panda_suicide_act\suicide.csv')
columns = ['country', 'sex', 'age', 'year', 'suicides_no', 'suicides/100k pop']

print("#1")
display(data[columns])
print("")

print("#2")
ph_suicide = data[data['country'] == "Philippines"]
display(ph_suicide[columns])
print("")

print("#3")
ph_suicide2011 = ph_suicide[ph_suicide['year'] == 2011]
display(ph_suicide2011[columns])
print("")

print("#4")
suicide2005 = data[data['year'] == 2005]
highest_suicide2005 = suicide2005[suicide2005['suicides/100k pop'] == suicide2005['suicides/100k pop'].max()]
display(highest_suicide2005[['country', 'sex', 'age', 'year', 'suicides/100k pop']])
print("")

print("5")
suicides_per_year = data.groupby('year').agg({'suicides_no': 'sum', 'suicides/100k pop': 'mean'})
display(suicides_per_year.sort_index(ascending=False))
print("")

print("@6")
male_data = data[data['sex'] == 'male']
female_data = data[data['sex'] == 'female']

male_suicides_no = male_data['suicides_no'].sum()
female_suicides_no = female_data['suicides_no'].sum()

male_mean_suicides100k = male_data['suicides/100k pop'].mean()
female_mean_suicides100k = female_data['suicides/100k pop'].mean()

result_df = pd.DataFrame({
    'Gender': ['Male', 'Female'],
    'Total Suicides': [male_suicides_no, female_suicides_no],
    'Mean Suicides/100k pop': [male_mean_suicides100k, female_mean_suicides100k]
})
display(result_df.sort_values(by='Total Suicides', ascending=False))
print("")

print("#7")
age_data = data.groupby('age').agg({'suicides_no': 'sum', 'suicides/100k pop': 'mean'})
display(age_data.sort_values(by='suicides_no', ascending=False))
print("")

print("#8")
country_year = data.groupby(['country', 'year']).agg({'suicides_no': 'sum'})
display(country_year.sort_values(by='suicides_no', ascending=False))
print("")

print("@9")
ph_summary = ph_suicide.groupby(['year', 'sex', 'age']).agg({'suicides_no': 'sum'})
display(ph_summary)
print("")

print("#10")
ph_yeardata = ph_suicide.groupby('year').agg({'suicides_no': 'sum'})
ph_max_year = ph_yeardata.idxmax()[0]
ph_max_suicides = ph_yeardata.max()[0]
display(pd.DataFrame({"Year with the highest combined suicides in Philippines": [ph_max_year], "Number of suicide cases in that year": [ph_max_suicides]}))

print("")
