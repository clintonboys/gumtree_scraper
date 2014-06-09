__author__ = 'cboys'
import mandrill
import json
mandrill_client=mandrill.Mandrill('dZkyaV369DEIq05GtvpCJw')

def new_result_email(result,artist,city):
    subj=artist+' '+city
    body=json.dumps(result)
    message = {
     'from_email': 'cboys@maths.usyd.edu.au',
     'from_name': 'Clinton Boys',
     'headers': {'Reply-To': 'cdsboys@gmail.com'},
#     'html': 'Hey',
     'important': True,
     'preserve_recipients': None,
     'return_path_domain': None,
     'signing_domain': None,
     'subject': subj,
     'text': body,
     'to': [{'email': 'cdsboys@gmail.com',
             'name': 'Clinton Boys',
             'type': 'to'}],
    }
    result = mandrill_client.messages.send(message=message)
    print(result)