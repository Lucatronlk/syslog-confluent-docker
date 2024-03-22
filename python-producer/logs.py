import boto3
import random
import datetime
from time import sleep

# Initialize the boto3 client for CloudWatch Logs
cloudwatch_logs = boto3.client('logs')

# Function to generate dummy CloudWatch log events
def generate_cloudwatch_logs(log_group, stream_name, event_count):
    current_time = datetime.datetime.now()
    timestamp = int(current_time.timestamp() * 1000) # Convert timestamp to string
    events = []
    for _ in range(event_count):
        message = f"Dummy log data {random.randint(1, 100)}"
        event = {
            'timestamp': timestamp,  # Use timestamp string
            'message': message
        }
        events.append(event)
        current_time += datetime.timedelta(milliseconds=1000)  # Increment timestamp for each event
        timestamp = int(current_time.timestamp() * 1000)  # Convert updated timestamp to string
    #cloudwatch_logs = boto3.client('logs')
    #cloudwatch_logs.put_log_events(logGroupName=log_group, logStreamName=stream_name, logEvents=events)


# Function to generate dummy S3 access logs
def generate_s3_logs(bucket_name, key_prefix, log_count):
    s3 = boto3.client('s3')
    for i in range(log_count):
        log_data = f"Dummy S3 access log data {random.randint(1, 100)}"
        #s3.put_object(Bucket=bucket_name, Key=f"{key_prefix}/dummy_log_{i}.txt", Body=log_data)

# Function to generate dummy syslogs
def generate_syslogs(log_file_path, log_count):
    with open(log_file_path, 'a') as log_file:
        for i in range(log_count):
            log_entry = f"Dummy syslog data {random.randint(1, 100)}\n"
            log_file.write(log_entry)

# Function to generate dummy firewall logs
def generate_firewall_logs(log_file_path, log_count):
    with open(log_file_path, 'a') as log_file:
        for i in range(log_count):
            log_entry = f"Dummy firewall log data {random.randint(1, 100)}\n"
            log_file.write(log_entry)

# Run the log generation process 5 times with a 5-minute interval and 2-minute break
for round in range(5):
    print(f"Starting round {round+1} of log generation.")
    generate_cloudwatch_logs('cloudwatch-kafka-logs', 'stream-1', 10)
    #enerate_s3_logs('s3-kafka-logs-bucket', 's3_kafka', 10)
    generate_syslogs('logs/syslog.log', 10)
    generate_firewall_logs('/logs/firewall.log', 10)
    print(f"Finished round {round+1} of log generation.")
    
    if round < 4:  # Wait for 5 minutes only if it's not the last round
        print("Waiting for 5 minutes before the next round...")
        sleep(300)  # 5 minutes
        print("Taking a 2-minute break...")
        sleep(120)  # 2 minutes

print("Log generation completed.")