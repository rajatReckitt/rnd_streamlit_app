import pandas as pd
import numpy as np
import streamlit as st

def cred_entered():
    if st.session_state['user'].strip() == 'admin' and st.session_state['passwd'].strip() == 'admin':
        st.session_state['authenticated'] = True
    else:
        st.session_state['authenticated'] = False
        if st.session_state['passwd']:
            st.warning('Please enter password')
        elif not st.session_state['user']:
            st.warning('Please enter username')
        else:
            st.error('Invalid username/password')

def authenticate_user():
    if 'authenticated' not in st.session_state:
        st.text_input(label = 'Username :', value = '', key = 'user', on_change = cred_entered)
        st.text_input(label = 'Password :', value = '', key = 'passwd', type = 'password', on_change = cred_entered)
        if st.button("Login"):
            cred_entered()
        return False
    else: 
        if st.session_state['authenticated']:
            return True
        else:
            st.text_input(label = 'Username :', value = '', key = 'user', on_change = cred_entered)
            st.text_input(label = 'Password :', value = '', key = 'passwd', type = 'password', on_change = cred_entered)
            if st.button("Login"):
                cred_entered()
            return False
        

if authenticate_user():
    st.title('Uber pickups in NYC')

    DATE_COLUMN = 'date/time'
    DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
                'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

    def load_data(nrows):
        data = pd.read_csv(DATA_URL, nrows=nrows)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data

    data_load_state = st.text('Loading data...')
    data = load_data(10000)
    data_load_state.text("Done! (using st.cache_data)")

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)

    st.subheader('Number of pickups by hour')
    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)

    hour_to_filter = st.slider('hour', 0, 23, 17)
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

    st.subheader('Map of all pickups at %s:00' % hour_to_filter)
    st.map(filtered_data)
    #authenticator.logout("Logout", 'sidebar')