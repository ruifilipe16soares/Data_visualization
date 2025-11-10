# Kafka & Debezium Docker Setup

This **Docker Compose** file deploys a lightweight **Kafka + Zookeeper + Debezium Connect** stack used for real-time data streaming and integration with the ELK environment.

---

## Services Overview

- **Zookeeper:** Coordinates and manages Kafka brokers (port `2181`)  
- **Kafka:** Message broker for streaming events (port `9092`)  
- **Connect (Debezium):** Handles connectors such as **MySQL → Elasticsearch** (port `8083`)

---

## Network Configuration

All containers run inside the same Docker network used by the **ELK stack**:

```yaml
networks:
  elasticnet:
    external: true
    name: elk_elasticnet
```

## Plugin Installation (Before Starting the Container)

Before running the stack with `docker-compose up -d`, make sure the **Elasticsearch Kafka Connector** plugin is installed inside the `kafka-connect-plugins` folder.

---

### How to Install the Plugin via Command Line

Run the following command in the same directory as your `docker-compose.yml`:

```bash
mkdir -p kafka-connect-plugins
cd kafka-connect-plugins
wget https://packages.confluent.io/maven/io/confluent/kafka-connect-elasticsearch/14.1.2/kafka-connect-elasticsearch-14.1.2.zip
unzip kafka-connect-elasticsearch-14.1.2.zip -d confluentinc-kafka-connect-elasticsearch-14.1.2
rm kafka-connect-elasticsearch-14.1.2.zip
```
The connector’s JAR files are too large to store directly in the repository, so only the plugin folder structure is included.
Before starting the containers, you need to download the plugin manually as shown above.

After installation, you can safely start the Kafka stack:

`docker-compose up -d`

IMP: Don't forget to write your credentials in `secrets` folder, on both files.
