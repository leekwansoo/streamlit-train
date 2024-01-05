import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4, 10), columns=("col %d" % i for i in range(10)))

st.table(df)

st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})

# Initial scorecard dataframe


df = pd.DataFrame({
    'Title': ['A', 'B', 'Total'],
    'Row1': [0, 0, 0],
    'Row2': [0, 0, 0]
})


# Getting user input
input_A = st.number_input('Input for A', value=0)
input_B = st.number_input('Input for B', value=0)

# Update dataframe with user input
df.at[0, 'Row1'] = input_A
df.at[1, 'Row1'] = input_B
df.at[0, 'Row2'] = input_A
df.at[1, 'Row2'] = input_B

# Recalculate the Total column
df.at[2, 'Row1'] = df['Row1'].sum()
df.at[2, 'Row2'] = df['Row2'].sum()

# Display the updated dataframe
st.table(df.set_index('Title'))