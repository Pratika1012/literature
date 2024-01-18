import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")




st.markdown("<h4 style='text-align: left;color:#305D87;font-family:georgia'>We have sampled and profiled a select subset of literature (n=68) to ensure enough variety in terms of coverage across studies in different regions around the globe, the type of wound, the type of study, year of publication, form of chitosan used, and study model</h4>", unsafe_allow_html=True)

# st.markdown("<p style='text-align: center; font-size: 20px;'><b>Structured Approaches to Strategic Solutions!</b></p>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center; font-size: 18px;'><i>Client Experience 2.0: We are working towards building a repository of key consulting resources to help you improve your client experience from the very first touch point</i></p>", unsafe_allow_html=True)

data=pd.read_excel("Literature Database.xlsx")
data.columns = data.iloc[0]
data = data[1:]



st.markdown(
    """
    <style>
    [data-testid="stSidebar"] > div:first-child {
        width: 300px;
    }
    
    </style>
    """,
    unsafe_allow_html=True,
    )


    
with st.sidebar:
   

    a=['All']          
    options1=st.multiselect('Select a Country', options=['All'] + list(data['Country'].unique().tolist()),default=a,key='country')
    options2=st.multiselect('Select an Indication', options=['All'] + list(data['Indication'].unique().tolist()),default=a,key='Indication')
    options3=st.multiselect('Select a Year of publication', options=['All'] + list(data['Year of publication'].unique().tolist()),default=a,key='Year of publication')
    options4=st.multiselect('Select a Form of chitosan', options=['All'] + list(data['Form of chitosan-based product'].unique().tolist()),default=a,key='Form of chitosan')
    options5=st.multiselect('Select a Type of study', options=['All'] + list(data['Type of study'].unique().tolist()),default=a,key='Type of study')
    options6=st.multiselect('Select a Study model', options=['All'] + list(data['Study model'].unique().tolist()),default=a,key='Study model')


st.markdown("""
    <style>
        
        .stMultiSelect > label {
            font-size:105%; 
            font-weight:bold; 
            color:white;
        } 
    </style>
    """, unsafe_allow_html=True)



len1=len(options1)
len2=len(options2)
len3=len(options3)
len4=len(options4)
len5=len(options5)
len6=len(options6)


if ("All" in options1) & (len1==1):

          filtered_df = data 

else:
         filtered_df = data[data['Country'].isin(options1)]


if (len2!=1) & (options2!="All"):        
    filtered_df = filtered_df[filtered_df['Indication'].isin(options2)]

if (len3!=1) & (options3!="All"): 
            filtered_df = filtered_df[filtered_df['Year of publication'].isin(options3)]

if (len4!=1) & (options4!="All"): 
            filtered_df = filtered_df[filtered_df['Form of chitosan-based product'].isin(options4)]


if (len5!=1) & (options5!="All"): 
            filtered_df = filtered_df[filtered_df['Type of study'].isin(options5)]


if (len6!=1) & (options6!="All"): 
            filtered_df = filtered_df[filtered_df['Study model'].isin(options6)]


# st.dataframe(
#     filtered_df,
#     column_config={
        
#         "Link": st.column_config.LinkColumn("Pdf URL"),
#         # "Name of the study": st.column_config.Column(
#         #     width=1150,
#         #     required=True,
#         # )
        
#     },
#     hide_index=True,
#     height=2500,
#     use_container_width=True,
# )
# # st.table(filtered_df)

# st.write(filtered_df.to_html(escape=False), unsafe_allow_html=True)
            

def make_hyperlink(url, text):
    return f'<a href="{url}" target="_blank">{text}</a>'

# Create a new column with clickable hyperlinks
filtered_df['Name of the study'] = filtered_df.apply(lambda row: make_hyperlink(row['Link'],row["Name of the study"] ), axis=1)
filtered_df.drop("Link",inplace=True,axis=1)
# Display the table with clickable hyperlinks using st.write

header_style = '''
    <style>
        table th {
            background-color:#293A4A ;
            color:white;
            text-align:center
        }

        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid red;  /* Set the border color here */
            padding: 8px;
            text-align: center;
        }
    </style>
'''
st.markdown(header_style, unsafe_allow_html=True)
st.write(filtered_df.style.hide(axis="index").to_html(escape=False, render_links=True), hide_index=True,unsafe_allow_html=True)





# Sample data with hyperlinks


