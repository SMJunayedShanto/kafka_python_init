# >>> To install the kafka library, use the following pip command:

# pip3 install confluent-kafka


# Run A Local Kafka Cluster With Docker
# In order to run a Kafka cluster in local, you need two things: a Kafka broker and Zookeeper.

# The most convenient way to set them up, is to use a Docker compose file to run multiple containers and launch everything with a single configuration script.

# Use this coomand to run docker-compose file

# docker-compose up -d

# Build A Kafka Producer
# Now that your Kafka cluster is running in the background, it comes the fun part: building a producer with Python.

# In the example that follow, you will simulate the generation of fake data about user with Faker and write them to the user-tracker topic.

# pip install Faker

# Configure the format of your logs. Every time a new event becomes available, logs will be appended in a producer.log file in your main directory:

# Build A Kafka Consumer
# In Kafka, consumers are built to read and often clean, transform or enrich messages from topics. At their core, consumers run as an unbounded loop that awaits for messages to be delivered to the topics they are listening to.

# Messages can be read from the beginning (very first message in the topic) or start from a specific position in the topic, known as offset, which is tracked by Zookeeper.