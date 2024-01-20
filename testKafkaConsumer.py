# using confluent-kafka

#pip install confluent-kafka

from confluent_kafka import Consumer
################
c=Consumer({'bootstrap.servers':'localhost:9092','group.id':'python-consumer','auto.offset.reset':'earliest'})
print('Kafka Consumer has been initiated...')

#Determine the name of the topic that should be consumed and subscribe to it. 
# If there is more then one topic available, you can list their names with the list_topics().topics command:
print('Available topics to consume: ', c.list_topics().topics)
c.subscribe(['user-tracker'])

# In order to start receiving events you create an infinite loop that polls the topic, looking for any available messages. The consumer can always be adjusted to start and stop from a specific offset:
def main():
    while True:
        msg=c.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data=msg.value().decode('utf-8')
        print(data)
    c.close()
main()