# python-azure-service-bus-client-sync

Azure Service Bus Client example written in Python

To run this code just export the connection string and topic name like an environment variables:

    export SB_CONNECTION_STRING="Endpoint=sb://yourservicebusname.servicebus.windows.net/;SharedAccessKeyName=python-client-sas;SharedAccessKey=xxxxxxxxx="
    export SB_TOPIC_NAME="test-topic"

 Then create your virtual env, activate and run the example:

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    python main.py
