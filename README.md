# Data-Challenge
This is the code for the Data Challenge

Here you will find the python code which is in charge of the api, as well as the Dockerfile and cloudbuild.yaml for deployment in the cloud.

The architecture consists of an API developed with flask that receives requests in the form of CSV files and writes the data to a postgresql Database.
The API is deployed in GCP Cloudrun. It has a continuous integration with a GCP Cloudbuild and Github integration.
The database is deployed in GCP CloudSQL.

You will also find 2 SQL files that are the queries that were needed for the challenge.

There are also some visualizations using Looker Studio.

For cost purposes all the cloud services will be turned off but if you wish to see them in action, let me know and I will turn them on.