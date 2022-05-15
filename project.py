import pandas as pd
import statistics as st
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import plotly.figure_factory as pff
import seaborn as sns
import random

# -----------------------------------------------------------------------------------------------------

df = pd.read_csv("savings.csv")
fig = px.scatter(df, y="quant_saved", color="rem_any")

# -----------------------------------------------------------------------------------------------------

import csv

with open('savings.csv', newline="") as f:
  reader = csv.reader(f)
  savings_data = list(reader)

savings_data.pop(0)

# -----------------------------------------------------------------------------------------------------

total_entries = len(savings_data)
total_people_given_reminder = 0
for data in savings_data:

  if int(data[3]) == 1:

    total_people_given_reminder += 1


fig = go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y=[total_people_given_reminder, (total_entries - total_people_given_reminder)]))

# -----------------------------------------------------------------------------------------------------

#Mean, median and mode of savings

all_savings = []
for data in savings_data:
  all_savings.append(float(data[0]))

print(f"Mean of savings - {st.mean(all_savings)}")
print(f"Median of savings - {st.median(all_savings)}")
print(f"Mode of savings - {st.mode(all_savings)}")

# -----------------------------------------------------------------------------------------------------

#Mean, median and mode of savings

reminded_savings = []
not_reminded_savings = []

for data in savings_data:

  if int(data[3]) == 1:

    reminded_savings.append(float(data[0]))

  else:

    not_reminded_savings.append(float(data[0]))

print("Results for people who were reminded to save")
print(f"Mean of savings - {st.mean(reminded_savings)}")
print(f"Median of savings - {st.median(reminded_savings)}")
print(f"Mode of savings - {st.mode(reminded_savings)}")

#To add new lines

print("\n\n")
print("Results for people who were not reminded to save")
print(f"Mean of savings - {st.mean(not_reminded_savings)}")
print(f"Median of savings - {st.median(not_reminded_savings)}")
print(f"Mode of savings - {st.mode(not_reminded_savings)}")

#Standard Deviation

print(f"Standard deviation of all the data -> {st.stdev(all_savings)}")
print(f"Standard deviation of people who were reminded -> {st.stdev(reminded_savings)}")
print(f"Standard deviation of people who were not reminded -> {st.stdev(not_reminded_savings)}")


# --------------------------------------- Data Story 2 ---------------------------------

age = []
savings = []

for a in savings_data :

    if float(a[5]) != 0 :

        age.append(float(a[5]))
        savings.append(float(a[0]))

correlation = np.corrcoef(age , savings)

print("---------------------------------------------------------------")
print("Correlation Coefficient betwwen Age And Savings : " , correlation[0,1])

# -----------------------------------------------------------------------------------------------------

graphh = pff.create_distplot([df["quant_saved"].tolist()] , ["Savings"] , show_hist = False)

# ------------------------------------------------------------------------

q1 = df["quant_saved"].quantile(0.25)
q3 = df["quant_saved"].quantile(0.75)
iqr = q3 - q1

print("q1 : " , q1)
print("q3 : " , q3)
print("iqr : " , iqr)

lowerWhisker = q1 - (1.5 * iqr)
upperWhisker = q3 + (1.5 * iqr)

print("-------------------------")
print("Lower Whisker : ", lowerWhisker )
print("Upper Whisker : ", upperWhisker )

# -----------------------------------------------------------------------

new_df = df[df["quant_saved"] < upperWhisker]

all_savings = new_df["quant_saved"]

print("---------------------------------------------------")
print(f"Mean of savings - {st.mean(all_savings)}")
print(f"Median of savings - {st.median(all_savings)}")
print(f"Mode of savings - {st.mode(all_savings)}")

graphh = pff.create_distplot([new_df["quant_saved"].tolist()] , ["Savings"] , show_hist = False)

# --------------------------------------------------------------------------------------------------------

sampling_mean_list = []

for i in range(1000):

  temp_list = []

  for j in range(100):

    temp_list.append(random.choice(all_savings))

  sampling_mean_list.append(st.mean(temp_list))

mean_sampling = st.mean(sampling_mean_list)

fig = pff.create_distplot([sampling_mean_list], ["Savings (Sampling)"], show_hist=False)

print("---------------------------------------------------")
print(f"Mean of Sampling Distribution - {mean_sampling}")
print(f"Standard deviation of the sampling data - {st.stdev(sampling_mean_list)}")



























