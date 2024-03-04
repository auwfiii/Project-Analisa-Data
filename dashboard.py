import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
all_df = pd.read_csv('all_data.csv')

# Title and Subtitle
st.title('Bike Sharing Data Analysis Dashboard')
st.subheader('by Alfianita Ingsiany')

# Sidebar
st.sidebar.header('User Information')
st.sidebar.text('Name: Alfianita Ingsiany')
st.sidebar.text('Email: alfianitaingsiany03@gmail.com')
st.sidebar.text('ID Dicoding: alfianita04')

# Data Wrangling
## Display the head of the data
st.header('Data Overview')
st.write(all_df.head())

# Data Analysis and Visualization
## Question 1: User Behavior on Weekdays vs Weekends
st.header('Question 1: User Behavior on Weekdays vs Weekends')
fig_weekdays_vs_weekends = plt.figure(figsize=(12, 6))
sns.boxplot(x='weekday_day', y='cnt_day', data=all_df, showfliers=False)
plt.title('User Behavior Based on Weekdays and Weekends')
plt.xlabel('Day (0: Sunday, 1: Monday, ..., 6: Saturday)')
plt.ylabel('Bike Usage Count')
st.pyplot(fig_weekdays_vs_weekends)

## Question 2: Impact of Weather Factors on Bike Usage
st.header('Question 2: Impact of Weather Factors on Bike Usage')

# Scatter plot for Temperature vs. Bike Rental Count with Weathersit and Windspeed
fig_weather_impact = plt.figure(figsize=(14, 18))
axes = fig_weather_impact.subplots(nrows=3, ncols=1)

## Temperature
sns.scatterplot(x='temp_day', y='cnt_day', data=all_df, hue='weathersit_day', palette='viridis', size='windspeed_day', ax=axes[0])
axes[0].set_title('Temperature Impact on Bike Usage')
axes[0].set_xlabel('Temperature (Normalized)')
axes[0].set_ylabel('Bike Usage Count')
axes[0].legend(title='Weathersit')

## Humidity
sns.scatterplot(x='hum_day', y='cnt_day', data=all_df, hue='weathersit_day', palette='viridis', size='windspeed_day', ax=axes[1])
axes[1].set_title('Humidity Impact on Bike Usage')
axes[1].set_xlabel('Humidity (Normalized)')
axes[1].set_ylabel('Bike Usage Count')
axes[1].legend(title='Weathersit')

## Windspeed
sns.scatterplot(x='windspeed_day', y='cnt_day', data=all_df, hue='weathersit_day', palette='viridis', size='temp_day', ax=axes[2])
axes[2].set_title('Windspeed Impact on Bike Usage')
axes[2].set_xlabel('Windspeed (Normalized)')
axes[2].set_ylabel('Bike Usage Count')
axes[2].legend(title='Weathersit')

st.pyplot(fig_weather_impact)

# Conclusion
st.header('Conclusion')
st.markdown("""
### Conclusion Question 1:

1. On weekdays, there is a significant daily variation, with some days having higher or lower bike usage than others.
2. On weekends, there is a noticeable pattern or change in bike usage behavior, which may be related to holiday habits.
3. It can be concluded that there is a significant difference in bike usage behavior between weekdays (Monday-Friday) and weekends (Saturday-Sunday). The boxplot shows that the distribution of bike usage varies among days in a week.

### Conclusion Question 2:

1. There is a positive correlation between temperature and bike usage. The higher the temperature, the higher the bike usage. However, the correlation with humidity is not very significant.
2. The correlation between windspeed and bike usage appears to be not significant. This suggests that windspeed may not be a major factor affecting bike usage behavior.
3. It can be concluded that temperature seems to be the dominant factor influencing bike usage, while humidity and windspeed have a smaller impact.
""")

# Save the dashboard
button = st.download_button('Save Dashboard as HTML', 'Bike_Sharing_Dashboard.html', key='download_button')
