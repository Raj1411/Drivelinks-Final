from Google import create_service
import streamlit as st

# read the client secret file in streamlit secret folder
st.secrets['client_secret'] = open('client_secret.json', 'r').read()
CLIENT_SECRET_FILE = st.secrets['client_secret']
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# folder_id = '1nCBwCfey7k26ICDKXVGJHwx2lIBpVaR8'

st.title('Extract Google Drive Links')

file_id=st.text_input('Enter Folder ID')

response = service.files().list(q=f"'{file_id}' in parents",
    fields='files(id, name, webViewLink, webContentLink, parents)').execute()

files = response.get('files', [])

if not files:
    print('No files found.')
else:
    for file in files:
        # print(f"{file.get('name')} ({file.get('id')})")
        st.write(f"{file.get('name')}")

