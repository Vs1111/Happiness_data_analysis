import streamlit as st
import pandas as pd
import helper
import openpyxl
global df
user_menu = st.sidebar.radio( 'Select An Option',('OVERALL ANALYSIS','WORLD-HAPPINESS -TALLY','COUNTRY-WISE ANALYSIS','ANALYSIS BY YEAR',
                                                  'ANALYSIS BY HAPPINESS SCORE','ANALYSIS BY REGION','Pre-COVID vs COVID World Happiness'))
if user_menu == 'OVERALL ANALYSIS':
 st.sidebar.header("Medal Tally")
 df = pd.read_csv("world-happiness-report-2015-2022-cleaned.csv",encoding="unicode_escape")
 df = df.drop(['Unamed'], axis=1)
 df = df.round(2)
 df= df[[ 'Happiness Rank','Year', 'Country','Happiness_Score']]
 df = df.set_index('Happiness Rank')
 years,country = helper.country_year_list(df)
 selected_year = st.sidebar.selectbox("Select Year",years)
 selected_country = st.sidebar.selectbox("Select Country", country)
 if selected_year == 'Overall' and selected_country == 'Overall':
     st.title("Overall Tally")
     temp_df = df
     st.dataframe(temp_df)
 if selected_year != 'Overall' and selected_country == 'Overall':
     st.title( str(selected_year) + " "+"Happiness Score")
     temp_df = df[df['Year'] == selected_year]
     st.dataframe(temp_df)
 if selected_year == 'Overall' and selected_country != 'Overall':
     st.title(selected_country + " "+"Happiness Score")
     temp_df = df[df['Country'] == selected_country]
     st.dataframe(temp_df)
 if selected_year != 'Overall' and selected_country != 'Overall':
     st.title(selected_country + " performance in " + str(selected_year) + " "+"Happiness Score")
     temp_df = df[(df['Year'] == selected_year) & (df['Country'] == selected_country)]
     st.dataframe(temp_df)
if user_menu == 'WORLD-HAPPINESS -TALLY':
    st.sidebar.header("WORLD-HAPPINESS -TALLY")
    df = pd.read_csv("world-happiness-report-2015-2022-cleaned.csv", encoding="unicode_escape")
    df = df.drop(['Unamed'], axis=1)
    df = df.round(2)
    df = df[['Region_name','Happiness Rank', 'Year', 'Country','Happiness_Score']]
    df = df.set_index('Happiness Rank')
    years, country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year", years)
    Region_name = df['Region_name'].unique().tolist()
    Region_name.sort()
    Region_name.insert(0, 'Overall')
    selected_Region_name = st.sidebar.selectbox("Select Region-name", Region_name)
    if selected_year == 'Overall' and  selected_Region_name =='Overall':
        st.title("overall performance")
        st.dataframe(df)
    if selected_year == 'Overall' and  selected_Region_name !='Overall':
        st.title(selected_Region_name + " overall performance")
        temp_df = df[df['Region_name'] == selected_Region_name]
        st.dataframe(temp_df)
    if selected_year != 'Overall' and  selected_Region_name !='Overall' :
        st.title(selected_Region_name + 'and' + str(selected_year) + " "+"Happiness Score")
        temp_df = df[(df['Year'] == selected_year) & (df['Region_name'] == selected_Region_name)]
        st.dataframe(temp_df)
    if selected_year != 'Overall' and  selected_Region_name == 'Overall':
        st.title(str(selected_year) + " "+"Happiness Score")
        temp_df = df[(df['Year'] == selected_year)]
        st.dataframe(temp_df)
if user_menu == 'COUNTRY-WISE ANALYSIS':
                df = pd.read_csv("world-happiness-report-2015-2022-cleaned.csv", encoding="unicode_escape")
                COUNTRY = df['Country'].unique().tolist()
                COUNTRY.sort()
                selected_COUNTRY = st.sidebar.selectbox("Select Country", COUNTRY)
                import plotly.express as px
                import numpy as np
                df = pd.read_csv("world-happiness-report-2015-2022-cleaned.csv",encoding="unicode_escape")
                df = df.drop(['Unamed'], axis=1)
                df = df[['Happiness Rank', 'Year', 'Region_name', 'Country', 'Happiness_Score']]
                df2 = df[(df['Country'] ==selected_COUNTRY )]
                df2.index = np.arange(1, len(df2) + 1)
                st.table(df2)
                st.title("Happiness vs COUNTRY")
                fig = px.bar(df2, x='Year',y='Happiness_Score', text_auto=True)
                st.write(fig)
                st.title("ANALYSIS OF ECONOMY BY Country ")
                df = pd.read_csv("world-happiness-report-2015-2022-cleaned.csv",encoding="unicode_escape")
                df2 = df[['Year', 'Country', 'Economy_GDP_ per_ Capita']]
                df2 = (df2[df2.Year != 2022])
                df2 = df2[(df2['Country'] == selected_COUNTRY)]
                fig = px.bar(df2, x='Year', y='Economy_GDP_ per_ Capita', text_auto=True)
                st.write(fig)
                st.title("ANALYSIS OF Family BY COUNTRY ")
                df = pd.read_csv("world-happiness-report-2015-2022-cleaned.csv",encoding="unicode_escape")
                df2 = df[['Year', 'Country', 'Family (Social Support)']]
                df2 = (df2[df2.Year != 2022])
                df2 = df2[(df2['Country'] == selected_COUNTRY)]
                fig = px.bar(df2, x='Year', y='Family (Social Support)', text_auto=True)
                st.write(fig)
                st.title("ANALYSIS OF Freedom BY COUNTRY ")
                df = pd.read_csv("world-happiness-report-2015-2022-cleaned.csv",encoding="unicode_escape")
                df2 = df[['Year', 'Country', 'Freedom']]
                df2 = (df2[df2.Year != 2022])
                df2 = df2[(df2['Country'] == selected_COUNTRY)]
                fig = px.bar(df2, x='Year', y='Freedom', text_auto=True)
                st.write(fig)
                st.title("ANALYSIS OF Trust BY COUNTRY ")
                df = pd.read_csv("world-happiness-report-2015-2022-cleaned.csv",encoding="unicode_escape")
                df2 = df[['Year', 'Country', 'Trust (Government Corruption)']]
                df2 = (df2[df2.Year != 2022])
                df2 = df2[(df2['Country'] == selected_COUNTRY)]
                fig = px.bar(df2, x='Year', y='Trust (Government Corruption)',text_auto=True)
                st.write(fig)
                st.title("ANALYSIS OF Generosity BY COUNTRY ")
                df = pd.read_csv("world-happiness-report-2015-2022-cleaned.csv",encoding="unicode_escape")
                df2 = df[['Year', 'Country', 'Generosity']]
                df2 = (df2[df2.Year != 2022])
                df2 = df2[(df2['Country'] == selected_COUNTRY)]
                fig = px.bar(df2, x='Year', y='Generosity', text_auto=True)
                st.write(fig)
                st.title("ANALYSIS OF Health BY COUNTRY ")
                df = pd.read_csv("world-happiness-report-2015-2022-cleaned.csv",encoding="unicode_escape")
                df2 = df[['Year', 'Country', 'Health (Life Expectancy)']]
                df2 = (df2[df2.Year != 2022])
                df2 = df2[(df2['Country'] == selected_COUNTRY)]
                fig = px.bar(df2, x='Year', y='Health (Life Expectancy)', text_auto=True)
                st.write(fig)
if user_menu == 'ANALYSIS BY YEAR':
    import plotly.express as px
    st.title("ANALYSIS OF  Happiness BY YEAR ")
    var1 = pd.read_excel("YEAR.xlsx", sheet_name='Sheet6')
    var1['HAPINESS_SCORE'] = var1['HAPINESS_SCORE'].astype(int)
    fig = px.pie(var1, values='HAPINESS_SCORE', names='YEAR', color_discrete_sequence=px.colors.sequential.RdBu, )
    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)
    st.title("ANALYSIS OF  ECONOMY BY YEAR ")
    var1 = pd.read_excel("YEAR.xlsx", sheet_name='Sheet8')
    fig = px.pie(var1, values='ECONOMY', names='Year', color_discrete_sequence=px.colors.sequential.RdBu, )
    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)
    st.title("ANALYSIS OF Social Support BY YEAR ")
    var1 = pd.read_excel("YEAR.xlsx", sheet_name='Sheet9')
    fig = px.pie(var1, values='Family (Social Support)', names='Year', color_discrete_sequence=px.colors.sequential.RdBu, )
    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)
    st.title("ANALYSIS OF Health_Life_Expectancy BY YEAR ")
    var1 = pd.read_excel("YEAR.xlsx", sheet_name='Sheet10')
    fig = px.pie(var1, values='Health', names='Year',color_discrete_sequence=px.colors.sequential.RdBu, )
    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)
    st.title("ANALYSIS OF Freedom BY YEAR ")
    var1 = pd.read_excel("YEAR.xlsx", sheet_name='Sheet11')
    fig = px.pie(var1, values='Freedom', names='Year', color_discrete_sequence=px.colors.sequential.RdBu, )
    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)
    st.title("ANALYSIS OF Trust (Government Corruption) BY YEAR ")
    var1 = pd.read_excel("YEAR.xlsx", sheet_name='Sheet12')
    fig = px.pie(var1, values='Trust', names='Year', color_discrete_sequence=px.colors.sequential.RdBu, )
    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)
    st.title("ANALYSIS OF Generosity BY YEAR ")
    var1 = pd.read_excel("YEAR.xlsx", sheet_name='Sheet13')
    fig = px.pie(var1, values='Generosity', names='Year', color_discrete_sequence=px.colors.sequential.RdBu, )
    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)

if user_menu == 'ANALYSIS BY HAPPINESS SCORE':
    import matplotlib.pyplot as plt
    df = pd.read_csv("world-happiness-report-2015-2022-cleaned.csv", encoding="unicode_escape")
    df = df.drop(['Unamed'], axis=1)
    st.title("Happiness vs Economy")
    y = df['Happiness_Score']
    x = df['Economy_GDP_ per_ Capita']
    plt.subplot(1, 2, 1)
    fig = plt.figure(figsize=(10, 4),dpi=.5, facecolor='w', edgecolor='k')
    plt.scatter(x, y)
    plt.xlabel('Economy', fontsize=18)
    plt.ylabel('Happiness_Score', fontsize=16)
    st.balloons()
    st.pyplot(fig)
    st.title("Happiness vs Family")
    y = df['Happiness_Score']
    x = df['Family (Social Support)']
    plt.subplot(1, 2, 1)
    st.balloons()
    fig =plt.figure(figsize=(10, 5), dpi=.5, facecolor='w', edgecolor='k')
    plt.scatter(x, y)
    plt.xlabel('Family', fontsize=18)
    plt.ylabel('Happiness_Score', fontsize=16)
    st.pyplot(fig)
    st.title("Happiness vs Health")
    y = df['Happiness_Score']
    x = df['Health (Life Expectancy)']
    plt.subplot(1, 2, 1)
    fig=plt.figure(figsize=(10,5), dpi=.5, facecolor='w', edgecolor='k')
    plt.scatter(x, y)
    plt.xlabel('Health', fontsize=18)
    plt.ylabel('Happiness_Score', fontsize=16)
    st.pyplot(fig)
    st.title("Happiness vs Freedom")
    y = df['Happiness_Score']
    x = df['Freedom']
    plt.subplot(1, 2, 1)
    fig=plt.figure(figsize=(10,5), dpi=.5, facecolor='w', edgecolor='k')
    plt.scatter(x, y)
    plt.xlabel('Freedom', fontsize=18)
    plt.ylabel('Happiness_Score', fontsize=16)
    st.pyplot(fig)
    st.title("Happiness vs Government Corruption")
    y = df['Happiness_Score']
    x = df['Trust (Government Corruption)']
    plt.subplot(1, 2, 1)
    fig=plt.figure(figsize=(10, 5), dpi=.5, facecolor='w', edgecolor='k')
    plt.scatter(x, y)
    plt.xlabel('Government Corruption', fontsize=18)
    plt.ylabel('Happiness_Score', fontsize=16)
    st.pyplot(fig)
    st.title("Happiness vs Generosity")
    y = df['Happiness_Score']
    x = df['Generosity']
    plt.subplot(1, 2, 1)
    fig=plt.figure(figsize=(10, 5), dpi=.5, facecolor='w', edgecolor='k')
    plt.scatter(x, y)
    plt.xlabel('Generosity', fontsize=18)
    plt.ylabel('Happiness_Score', fontsize=16)
    st.pyplot(fig)
if user_menu =='ANALYSIS BY REGION':
    import pandas as pd
    import plotly.express as px
    st.title("ANALYSIS OF HAPINESS SCORE BY REGION ")
    df = pd.read_excel("REGION.xlsx", sheet_name='Sheet2')
    fig = px.bar(df, x='Happiness_Score', y='Region_name', orientation='h')
    st.write(fig)
    st.title("ANALYSIS OF Economy_GDP_per_Capita BY REGION ")
    df = pd.read_excel("REGION.xlsx", sheet_name='Sheet3')
    fig = px.bar(df, x='Economy',y='Region_name', orientation='h', text_auto=True)
    st.write(fig)
    st.title("ANALYSIS OF Family (Social Support) BY REGION ")
    df = pd.read_excel("REGION.xlsx", sheet_name='Sheet4')
    fig = px.bar(df, x='Family', y='Region_name', orientation='h', text_auto=True)
    st.write(fig)
    st.title("ANALYSIS OF Health (Life Expectancy) BY REGION ")
    df = pd.read_excel("REGION.xlsx", sheet_name='Sheet5')
    fig = px.bar(df, x='Health',y='Region_name', orientation='h', text_auto=True)
    st.write(fig)
    st.title("ANALYSIS OF Freedom BY REGION ")
    df = pd.read_excel("REGION.xlsx", sheet_name='Sheet6')
    fig = px.bar(df, x='Freedom',y='Region_name', orientation='h', text_auto=True)
    st.write(fig)
    st.title("ANALYSIS OF Trust (Government Corruption) BY REGION ")
    df = pd.read_excel("REGION.xlsx", sheet_name='Sheet7')
    fig = px.bar(df,x='Trust1 ',y='Region_name',orientation='h',text_auto=True)
    st.write(fig)
    st.title("ANALYSIS OF Generosity BY REGION ")
    df = pd.read_excel("REGION.xlsx", sheet_name='Sheet8')
    fig = px.bar(df, x='Generosity',y='Region_name', orientation='h', text_auto=True)
    st.write(fig)
if user_menu =='Pre-COVID vs COVID World Happiness':
    import pandas as pd
    df = pd.read_excel("covid.xlsx", sheet_name='Sheet4')
    import numpy as np
    df.index = np.arange(1, len(df) + 1)
    COUNTRY = df['Country'].unique().tolist()
    COUNTRY.sort()
    selected_COUNTRY = st.sidebar.selectbox("Select Country", COUNTRY)
    df = df[(df['Country'] == selected_COUNTRY)]
    st.table(df)