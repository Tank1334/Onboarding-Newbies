# Practical Exercise - Meet the Hadoop Ecosystem in Action

## Goals:
- Gain a foundational understanding of the Hadoop ecosystem with hands-on experience.
- Explore key components and their roles in big data processing.
- Make connections between the Hadoop ecosystem and real-world use cases.
- Explore the Cloudera Manager and the Hadoop ecosystem in action.
- Explore our Dashboard for monitoring and managing the Hadoop ecosystem.

:warning: **Note:**
- Pay attention to run your commands in the DEV environment, so you don't affect the TEST and PROD environments.

## Tasks:

Make sure to include photos for each step!

#### Getting to know the Cloudera Manager
1. Enter the Cluoudera Manager of the dev environmet.
2. Navigate to the HDFS service.
3. Navigate to the active NameNode.
4. What is the namenodes transaction count?
5. Using the CM, find out how much memory does the Namenode server has & and how much is utilized out of it.
6. Enter the charts library of the active namenode, explain about 3 different charts and how they me be of use to us.
7. Now, we would like to look at some logs.
8. Use the CM to read the logs of the namenode in the lates 30 mins.
9. Enter the configuration tab of the namenode.
10. Find the configuration that specifies where the namenode's logs are stored.
11. Now SSH to the namenode's server, and look at the directory you have found in step 10, and check the out.
12. Now repeat steps 5-11 just for the hive meatstore server role (match the steps for the role yourself).
13. on the hive metastore server check the status of the cloudera-scm-agent service. What is the cloudera-scm-agent?

#### Interacting with the services
1. Create a csv file of your choice using excel, make sure it resmebles a table by having headers for each column, and a few data rows.
2. SSH to a server where the HDFS CLI can be used on it.
3. Upload the csv file to your home directory (create a specialized directory for this excercise called 'my_table_exercise') in HDFS using the HDFS CLI.
4. Now try to see if the file is there, if it is read it using the HDFS CLI.
5. Navigate to the HUE interface.
6. Create a hive table on your uploaded CSV file.
7. Query the table.
8. Query the same table using Impala, What did you have to do in order to make it queriable in Impala?

### 883 Group Dashboards - For each service, answer the following questions:
- What is the go address for each dashboard?
- What are the main features of each dashboard?


## Additional Resources:
- [Cloudera Manager](https://www.cloudera.com/products/cloudera-manager.html)
- [Cloudera Manager Documentation](https://docs.cloudera.com/documentation/enterprise/6/6.3/topics/cm_ig_intro.html)
- [Cloudera Manager API](https://cloudera.github.io/cm_api/apidocs/v19/path__clusters_-clusterName-.html)
- [Cloudera Manager API Documentation](https://cloudera.github.io/cm_api/apidocs/v19/index.html)

## Questions:
- YOU HAVE TO ASK YOUR MENTOR EACH TIME YOU HAVE A QUESTION! :stop_sign:
- **THIS IS THE IMPORTANT CHEPTER OF THE HADOOP ECOSYSTEM**, SO TAKE YOUR TIME TO UNDERSTAND IT WELL! :key:
