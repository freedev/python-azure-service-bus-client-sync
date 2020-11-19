# from azure.servicebus.control_client import ServiceBusService, Topic, Rule, DEFAULT_RULE_NAME
from azure.servicebus.servicebus_client import ServiceBusClient
from azure.servicebus.common.message import Message
import os

connection_string = os.getenv('SB_CONNECTION_STRING')
topic_name = os.getenv('SB_TOPIC_NAME')
serviceBusClient = ServiceBusClient.from_connection_string(connection_string)
sender = serviceBusClient.get_topic(topic_name)

message = Message("Single Message")
message.content_type = "application/json"
sender.send([message])

