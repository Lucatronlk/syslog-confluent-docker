#
# Copyright 2020 Confluent Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
FROM confluentinc/cp-kafka-connect-base:7.5.3

ENV CONNECT_PLUGIN_PATH: "/usr/share/java,/usr/share/confluent-hub-components"

RUN confluent-hub install --no-prompt confluentinc/kafka-connect-syslog:latest



COPY generate_syslog.sh /tmp/generate_syslog.sh

# RUN chmod +x /tmp/generate_syslog.sh

# Download wait-for-it.sh from GitHub
COPY wait-for-it.sh /tmp/wait-for-it.sh

# RUN chmod +x /tmp/wait-for-it.sh
