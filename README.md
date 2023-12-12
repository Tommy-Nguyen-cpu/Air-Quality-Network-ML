# Air-Quality-Network-ML
## Introduction
The escalating release of carbon dioxide (CO2), a direct consequence of increased vehicle usage, factory production, and other human activities, has exacerbated air pollution, adversely affecting the lives of many around the globe. This issue disproportionately impacts low-to-middle income countries, including Africa. To address this growing concern, the need for effective air pollution detection technologies has become increasingly evident. This has led to the establishment of "sensors.AFRICA," a pan-African citizen science initiative operating one of the largest air quality sensor networks in East, West, and South Africa. This extensive network empowers individuals and local authorities to monitor air pollution trends, enabling timely interventions and informed policy decisions. However, despite its significance, the sensor network faces challenges, including downtime leading to data gaps and increased vulnerability to cyber threats. This paper aims to explore potential solutions to these challenges by applying machine learning concepts to enhance security and protect against cyber threats. \par
The project will explore the potential usage of neural network in predicting missing values within the air quality data.

## Selection of Data
The data used in our project was given to us by the individuals at sensor.AFRICA for the hackathon. The data contains roughly 24 million rows, each row containing the following columns: timestamp, value, 	parameter,	device_id,	chip_id,	sensor_type,	sensor_id,	location_id,	location,	street_name,	city,	country,	latitude,	longitude,	deployment_date. Most of the information provided were not useful in our model (such as chip_id, sensor_type, sensor_id, etc). As such, the columns that were not useful were removed. <br />
It is worth noting that our training process cuts down the number of rows from 24 million to 6 million in order to allow our code to run on Google Colab. <br />
The process of cleaning the data was arduous and required the most amount of time to do. Firstly, the data contained significant amount of missing data between records, rendering large amounts of the dataset unusable. Secondly, the data contained inconsistent gaps between related records

## Method



<br />Repository containing the code for the "Hack to the Rescue" hackathon. <br />
Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

## How to run
#### Install Prerequisites
* Docker-compose (https://docs.docker.com/compose/install/)
#### Build docker containers
* `$ docker-compose up -d --build`

#### Go to [localhost:4201](http://localhost:4201/)
* Files to test uploading provided under `example_uploads/`
* Uploaded CSVs should be under 500k rows, anything greater cannot be processed by the server.
