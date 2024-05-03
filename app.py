import streamlit as st
import pandas as pd


# Sample dataframe
data = pd.read_csv('Metrics_Table.csv')
df = pd.DataFrame(data)


def display_content(organ):
    st.write(f"Selected Organ: {organ}")

    if organ == 'Abdomen':
        st.image("abdomen_normal.png", caption='Dataset sample - Abdomen', use_column_width=True)
        st.image("abdomen_generated.png", caption='Output generated - Abdomen 1', use_column_width=30)
        st.image("abdomen_generated1.png", caption='Output generated - Abdomen 2', use_column_width=30)
        st.image("abdomen_generated2.png", caption='Output generated - Abdomen 3', use_column_width=30)
        st.image("abdomen_generated3.png", caption='Output generated - Abdomen 4', use_column_width=30)
        st.image("abdomen_generated4.png", caption='Output generated - Abdomen 5', use_column_width=30)


    elif organ == 'Breast':
        st.image("breast_normal.png", caption='Dataset sample - Breast', use_column_width=True)
        st.image("breast_generated.png", caption='Output generated - Breast 1', use_column_width=30)
        st.image("breast_generated1.png", caption='Output generated - Breast 2', use_column_width=30)
        st.image("breast_generated2.png", caption='Output generated - Breast 3', use_column_width=30)
        st.image("breast_generated3.png", caption='Output generated - Breast 4', use_column_width=30)
        st.image("breast_generated4.png", caption='Output generated - Breast 5', use_column_width=30)

    elif organ == 'Chest':
        st.image("chest_normal.png", caption='Dataset sample - Chest', use_column_width=True)
        st.image("chest_generated5.png", caption='Output generated - Chest 1', use_column_width=30)
        st.image("chest_generated1.png", caption='Output generated - Chest 2', use_column_width=30)
        st.image("chest_generated2.png", caption='Output generated - Chest 3', use_column_width=30)
        st.image("chest_generated3.png", caption='Output generated - Chest 4', use_column_width=30)
        st.image("chest_generated4.png", caption='Output generated - Chest 5', use_column_width=30)

    elif organ == 'Head':
        st.image("head_normal.png", caption='Dataset sample - Head', use_column_width=True)
        st.image("head_generated.png", caption='Output generated - Head 1', use_column_width=30)
        st.image("head_generated1.png", caption='Output generated - Head 2', use_column_width=30)
        st.image("head_generated2.png", caption='Output generated - Head 3', use_column_width=30)
        st.image("head_generated3.png", caption='Output generated - Head 4', use_column_width=30)
        st.image("head_generated4.png", caption='Output generated - Head 5', use_column_width=30)

    elif organ == 'Hand':
        st.image("hand_normal.png", caption='Dataset sample - Hand', use_column_width=True)
        st.image("hand_generated.png", caption='Output generated - Hand 1', use_column_width=30)
        st.image("hand_generated1.png", caption='Output generated - Hand 2', use_column_width=30)
        st.image("hand_generated2.png", caption='Output generated - Hand 3', use_column_width=30)
        st.image("hand_generated3.png", caption='Output generated - Hand 4', use_column_width=30)
        st.image("hand_generated4.png", caption='Output generated - Hand 5', use_column_width=30)



st.title('MULTIMEDIA FORENSICS FOR CYBER SECURITY AND DATA TAMPERING')
st.write('### CSE3502 J Component by 20MIS0183 and 20MIS0190')
# Display the dataframe as a table
st.write('### Result Summary')
st.write(df)

st.write('### Select organ to generate & test synthetic images')

# Dropdown menus for dataset and model selection
# dataset = st.selectbox('Dataset', ['Mendeley', 'Kaggle'])
organ = st.selectbox('Organ', ['Breast','Chest','Head','Abdomen', 'Hand'])

if st.button('Submit'):
    # Display text and image based on selected options
    display_content(organ)