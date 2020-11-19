# python-azure-service-bus-client-sync

Azure Service Bus Client example written in Python

To run this code just export a connection string like an environment variable:

    export SB_CONNECTION_STRING="Endpoint=sb://yourservicebusname.servicebus.windows.net/;SharedAccessKeyName=python-client-sas;SharedAccessKey=xxxxxxxxx=;EntityPath=topic-name"
 
 Then create your virtual env, activate and run the example: 

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    python main.py
    
    
