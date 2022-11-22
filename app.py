# import libraries
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# app ki heading
st.write("""
# Summary of the dataset 
""")

df = pd.read_csv('kaggle_survey_2022_responses.csv')


df1= df

# Merging platform selection columns
df1['Platform'] = df[df.columns[5:17]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)
# Merging first_platform selection columns 
df1['First_Platform'] = df[df.columns[18:24]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging research_include_ml selection columns
df1['Research_include_ML'] = df[df.columns[26:29]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging Programming language selection columns
df1['Programming_language'] = df[df.columns[30:46]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging IDE selection columns
df1['IDE'] = df[df.columns[46:59]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging hosted notebooks selection columns
df1['Hosted_Notebooks'] = df[df.columns[59:75]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging Visualization libraries selection columns
df1['Visualization_libraries'] = df[df.columns[75:90]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging ML framework used on regular basis selection columns
df1['ML_framework_regular'] = df[df.columns[91:106]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging ML algorithms selection columns
df1['ML_algo'] = df[df.columns[106:120]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging Computer vision methods selection columns
df1['Computer_Vision_method'] = df[df.columns[120:128]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging NLP selection columns
df1['NLP'] = df[df.columns[128:134]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging pre trained models selection columns
df1['Pre_Trained_Model'] = df[df.columns[134:144]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging important activities at work selection columns
df1['important_activities_at_work'] = df[df.columns[150:158]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging cloud computing platforms selection columns
df1['cloud_computing_platform'] = df[df.columns[160:172]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging cloud computing products selection columns
df1['cloud_computing_products'] = df[df.columns[173:178]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging data storage products selection columns
df1['data_storage_products'] = df[df.columns[178:186]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging data products selection columns
df1['data_products'] = df[df.columns[186:202]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging business intelligence tools selection columns
df1['business_intelligence_tools'] = df[df.columns[202:217]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging managed ml models selection columns
df1['Managed_ML-models'] = df[df.columns[217:230]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging automated ml tools selection columns
df1['Automated_ML_tools'] = df[df.columns[230:238]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging automated ml tools selection columns
df1['Products_for_ML_model'] = df[df.columns[238:250]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging automated ml tools selection columns
df1['Tools_to_monitor'] = df[df.columns[250:265]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging ethical AI products selection columns
df1['Ethical_AI_products'] = df[df.columns[265:274]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging specialized hardware selection columns
df1['Specialized_hardware'] = df[df.columns[274:283]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# Merging favourite media sources selection columns
df1['Fav_media_sources'] = df[df.columns[284:296]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

# df1 into dataframe
df1 = pd.DataFrame({"platforms":df1['Platform'],"first_platform":df1["First_Platform"],"research_include_ml":df1['Research_include_ML'],"programming_language":df1["Programming_language"],"ide":df1["IDE"],"hosted_notebooks":df1["Hosted_Notebooks"],"visualization_libraries":df1["Visualization_libraries"],"ml_framework_regular":df1["ML_framework_regular"],"ml_algo":df1["ML_algo"],"computer_vision_method":df1["Computer_Vision_method"],"nlp":df1["NLP"],"pre_trained_model":df1["Pre_Trained_Model"],"important_activities_at_work":df1["important_activities_at_work"],"cloud_computing_platform":df1["cloud_computing_platform"],'cloud_computing_products':df1['cloud_computing_products'],"data_storage_products":df1["data_storage_products"],"data_products":df1["data_products"],"business_intelligence_tools":df1["business_intelligence_tools"],"managed_ml-models":df1["Managed_ML-models"],"automated_ml_tools":df1["Automated_ML_tools"],"products_for_ml_model":df1["Products_for_ML_model"],"tools_to_monitor":df1["Tools_to_monitor"],"ethical_ai_products":df1["Ethical_AI_products"],"specialized_hardware":df1["Specialized_hardware"],"fav_media_soruces":df1["Fav_media_sources"]})

df['For how many years have you used machine learning methods?'].fillna('I prefer not to answer',inplace=True)
df['What is your current yearly compensation (approximate $USD)?'].fillna('I prefer not to answer',inplace=True)



# Adding single columns as well
df1['gender'] = df['What is your gender? - Selected Choice']
df1['country'] = df['In which country do you currently reside?']
df1['experience'] = df['For how many years have you been writing code and/or programming?']
df1['title_of_current_role'] = df['Select the title most similar to your current role (or most recent title if retired): - Selected Choice']
df1['current_employer'] = df['In what industry is your current employer/contract (or your most recent employer if retired)? - Selected Choice']
df1['size_of_company'] = df['What is the size of the company where you are employed?']
df1['incorporation_of_ml_methods'] = df['Does your current employer incorporate machine learning methods into their business?']
df1['cloud_platforms_with_best_developer_experience'] = df['Of the cloud platforms that you are familiar with, which has the best developer experience (most enjoyable to use)? - Selected Choice']
df1['Usage_of_tpu'] = df['Approximately how many times have you used a TPU (tensor processing unit)?']
df1['duration'] = df['Duration (in seconds)']


# plotting the data
df3=df.groupby('In which country do you currently reside?',as_index=False)[['What is your gender? - Selected Choice']].count().sort_values(by='What is your gender? - Selected Choice',ascending=False).reset_index(drop=True)
df3['Gender'] = df1['gender']
df3['age']=df['What is your age (# years)?']
df3['country'] = df1['country']
df3['first_platform'] = df1['first_platform']
df3['ml_experience'] = df['For how many years have you used machine learning methods?']
df3['salary'] = df['What is your current yearly compensation (approximate $USD)?']
df3['Gender_Count']=df3['What is your gender? - Selected Choice']
df3['platform'] = df1['platforms']
fig = px.sunburst(data_frame=df3,path=[df3['Gender'], df3['age'],df3['country'],df3['ml_experience'],df3['salary'],df3['platform'],df3['first_platform']],values=df3['Gender_Count'],color_discrete_sequence=["deepskyblue", "mediumturquoise","aquamarine", "greenyellow","limegreen"],width=3000, height=1500,
                title='<b>Summary')
fig.update_layout( plot_bgcolor='#FEF2F2', paper_bgcolor='#e9f5f5')
st.pyplot(fig.show())
