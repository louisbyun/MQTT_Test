# MQTT_Test
MQTT Test

Run Docker Compose<br>

# Build and run the entire system using Docker Compose<br>
docker-compose up<br><br>
The docker-compose.yml file defines services for two MQTT brokers (mqtt-broker-1 and mqtt-broker-2) and two Python applications (mqtt-publisher and mqtt-subscriber).<br>
The services are built and run together using the docker-compose up command.<br>
The dependencies between services ensure that the MQTT Publisher and Subscriber wait for the corresponding MQTT brokers to be ready before starting.
