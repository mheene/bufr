# Upload Client for DWDs BUFR Viewer
The upload client sends the BUFR file to the WebService and returns the
response as text.

The directory contains 2 versions of the upload client. The version
bufr2txt.py is the Python 3 version while bufr2txt_v2.py is the Python 2
version of the upload client.

# Requirements 
The file requirements.txt lists the required modules - currently only the
module requests is need. You can install the required module with

pip install requests

or with the requirements file

pip install -r requirements.txt



# Usage:
python bufr2txt.py `<Input BUFR>`





