# Dockerfile and docker-compose  for standing up one or more Confluent self-managed syslog connectors

## Create python.config and .env file in the root director

### python config

```bash
# Required connection configs for Kafka producer, consumer, and admin
bootstrap.servers=<bootstrap_servers>:9092
security.protocol=SASL_SSL
sasl.mechanisms=PLAIN
sasl.username=<sasl.username>
sasl.password=<sasl.password>

# Best practice for higher availability in librdkafka clients prior to 1.7
session.timeout.ms=45000
```

### .env

```bash
BOOTSTRAP_SERVERS="<bootstrap_servers>:9092"
SCHEMA_REGISTRY_URL="https://<schema_url>.confluent.cloud"
BASIC_AUTH_CREDENTIALS_SOURCE="USER_INFO"
SCHEMA_REGISTRY_BASIC_AUTH_USER_INFO="<sasl.username>:<sasl.password>"
SASL_JAAS_CONFIG="org.apache.kafka.common.security.plain.PlainLoginModule required username='<sasl.username>' password='<sasl.password>';"

```
