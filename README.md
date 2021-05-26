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
- Added the script for validation and storing only valid data to another file
- Load data to the final table

### What is missing:
- circleci is not complete
- the second part of loading data to postgres sql having some weird connection issue with the hook
- the third one the k8s deployemnt didn't find the chance to at least define it 😒

### How you can run it
- You can spin up the docker image with
<pre>
make events-pipeline-up
</pre>
- I tried to document the validation part, you can run it locally with
<pre>
python shared_utils/schema_verification.py
</pre>
👾 Of course you need to export the PYTHONPATH and have the shared_utils folder part of your PYTHONPATH

🤖This is like a blue print of the application, and it can be improved more!
