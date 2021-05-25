## Events pipeline

- this is a very simple example of a data pipeline.

### What it does
1. read data from json file locally
2. validate the schema changing of the data
3. write the data to sql table


### Start with schema validation
- What do we know?
  - Data is in json format
  - We need to make sure each key has the right value type
> So here decided to go very simple and use `jsonschema` validator

### Step
- Added the validator in shared_utils
- spin up my docker image
- connected to Postgres instance and created the db 
<pre>
docker exec -it events_pipeline_postgres_1 bash
psql -U flink
CREATE DATABASE flink_db;
</pre>

- Added the connection as Airflow variable
- Added the script for loading data from json to staging table
- Make transformation (I saw we have data as json object so need to flatten it)
- Load data to the final table

