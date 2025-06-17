# Readme

Solution contains 1 Python file and 3 jupyter lab notebooks. To run them, add them to your jupyter-lab running inside your Python/Kafka-VM: http://127.0.0.1:28888

To run the example first: create the topics and install the required Python libraries:

if ModuleNotFoundError: No module named 'confluent_kafka' -> install it in one of your notebooks with: `!pip install confluent-kafka`
if ModuleNotFoundError: No module named 'sensemapi' -> install it in one of your notebooks with: `!pip install sensemapi`

before you start create topics: sensor_raw, sensor_filtered:

1. use `vagrant ssh` to connect to your vm
2. connect to a kafka broker: `docker exec -ti kafka-1 bash`
3. create topic 'sensor_raw': `kafka-topics --create --if-not-exists --zookeeper zookeeper-1:2181 --topic sensor_raw --partitions 6 --replication-factor 2`
4. create topic 'sensor_filtered': `kafka-topics --create --if-not-exists --zookeeper zookeeper-1:2181 --topic sensor_filtered --partitions 6 --replication-factor 2`
