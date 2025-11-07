#  Data Visualization

Creating a real-time **data pipeline** to generate **dynamic dashboards** from a **MySQL database**.

---

##  Overview

This project implements an end-to-end data architecture designed to support **healthcare management professionals** with a **free, data-driven decision-support solution**.

---

##  Key Features

- **Real-Time Data Architecture**  
  Designed and implemented a pipeline enabling continuous data flow and decision-making in real time.

- **Event-Driven Processing**  
  Captures data from the main **MySQL** database, streams it via **Kafka**, and indexes it into **Elasticsearch**.

- **Automated Transformation & Visualization**  
  Uses **Python** scripts for data transformation and **Kibana** dashboards for insightful visualization — all deployed using **Docker**.

---

##  Pipeline Diagram

Below is the high-level representation of the data flow and components involved:

<p align="center">
  <img src="bpmn_diagram.PNG" alt="Data Pipeline Diagram" width="700">
</p>

---

##  Technologies Used

| Component        | Technology        |
|------------------|------------------|
| Database         | MySQL            |
| Message Broker   | Apache Kafka     |
| Transformation   | Python           |
| Indexing Engine  | Elasticsearch    |
| Visualization    | Kibana           |
| Containerization | Docker           |

---



<!-- 
1º passo: instalar o elastic e o kibana. falar logo dos backups e do user anonimo. subir os containers
2º passo: fazer download do plugin. instalar o kafka. 
3º passo: conectores. 
4º passo: transformação dos dados. (documento conf)
5º passo: dashboard exemplo 
-->
