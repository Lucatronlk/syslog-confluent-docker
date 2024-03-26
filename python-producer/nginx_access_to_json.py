import re
import json

# Initialize an empty list to store log entries
log_entries = []

# Open the log file for reading
with open('logs/access.log', 'r') as f:
    for line in f:
        # Define the regular expression pattern to match the log format
        pattern = re.compile(r'\[(.*?)\] - (\S+) (\S+) - (\S+) "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"')
        m = pattern.match(line)
        if m:
            # Extract matched groups and create a dictionary
            dic = {
                'timestamp': m.group(1),
                'logger': m.group(2),
                'remote_addr': m.group(3),
                'remote_user': m.group(4),
                'request': m.group(5),
                'status': m.group(6),
                'body_bytes_sent': m.group(7),
                'http_referer': m.group(8),
                'http_user_agent': m.group(9)
            }
            # Append the dictionary to the list of log entries
            log_entries.append(dic)
        else:
            print('Failed to parse line:', line)

# Write the list of log entries to a JSON file
with open('logs/access.json', 'w') as new_f:
    json.dump(log_entries, new_f, indent=4)
