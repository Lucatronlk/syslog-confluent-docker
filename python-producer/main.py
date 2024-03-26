import confluent_kafka
from confluent_kafka import Producer, KafkaError
import json
import ccloud_lib
import requests




# Read arguments and configurations and initialize

config_file = 'python.config'
conf = ccloud_lib.read_ccloud_config(config_file)

# Function to produce logs to Kafka based on log type and topic
def produce_logs(log_file_path, log_type, topic_name):
    producer = confluent_kafka.Producer(conf)

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            try:
                producer.produce(topic_name, line.rstrip())
                producer.flush()  # Ensure messages are sent promptly
            except Exception as e:
                print(f'Error producing log: {e}')

    producer.flush()  # Ensure all remaining messages are sent

# Example usage for different log types and topics
produce_logs('logs/access.log', 'access', 'syslogs')
produce_logs('logs/endpoint.log', 'windows', 'endpoint')
produce_logs('logs/ids.log', 'ids', 'ids')
# produce_logs('/path/to/firewall/log/file', 'firewall', 'cloud-watch-log')
# produce_logs('/path/to/firewall/log/file', 'firewall', 'firewall-topic')
