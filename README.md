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