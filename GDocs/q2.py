from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/documents']

# The ID of a sample document.
DOCUMENT_ID = '195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE'

def main():
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('docs', 'v1', credentials=creds)
    title = '__Dox Garamond from q2.py'
    body = {
    "title":title
    }
    doc = service.documents().create(body=body).execute()
    print('Created document with TITLE: {0}'.format(
        doc.get('title')))
    myid = doc.get('documentId')

    print('Created document with ID: {0}'.format(myid))
    # Retrieve the documents contents from the Docs service.
    #document = service.documents().get(documentId=DOCUMENT_ID).execute()

    print('The title of the document is: {}'.format(doc.get('title')))
    #print('The body of the document is: {}'.format(doc.get('body')))
    req = [
        {
           'insertText': {
               'location': {
                   'index':1,
               },
               'text': " 1Il1-"
           }
        },
        {
            'updateTextStyle': {
                'range': {
                    'startIndex': 5,
                    'endIndex': 7
                },
                'textStyle': {
                    'baselineOffset' : "SUPERSCRIPT",
                },
                'fields': 'baselineOffset'
            }
        },
        { 'updateTextStyle': {
            'range': {
            'startIndex' :1,
            'endIndex':7
            },
            'textStyle': {
            'weightedFontFamily': {
                'fontFamily': 'EB Garamond'
            },
            'fontSize': {
                'magnitude': 28,
                'unit': 'PT'
            },
            },
            'fields': 'weightedFontFamily,fontSize'
            }
         },
         {
            'insertText': {
                'location': {
                    'index':1,
                },
                'text': " C2H4"
            }
        },
        {
            'updateTextStyle': {
                'range': {
                    'startIndex': 5,
                    'endIndex': 6
                },
                'textStyle': {
                    'baselineOffset' : "SUBSCRIPT"
                },
                'fields': 'baselineOffset'
            }
        },
        {
            'updateTextStyle': {
                'range': {
                    'startIndex': 3,
                    'endIndex': 4
                },
                'textStyle': {
                    'baselineOffset' : "SUBSCRIPT"
                },
                'fields': 'baselineOffset'
            }
        },
         {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': " text2"
            }
        },
        {
            'updateTextStyle': {
                'range': {
                    'startIndex': 1,
                    'endIndex': 5
                },
                'textStyle': {
                    'bold': "false",
                    'italic': "false"
                },
                'fields': 'bold,italic'
            }
        },
                 {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': "third text "
            }
        },
        
    ]


    doc2 = service.documents().batchUpdate(body={'requests': req},
            documentId=myid, fields='').execute()

#

if __name__ == '__main__':
    main()
