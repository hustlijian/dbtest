# Database Query Test

Comprehensive database query test, with a focus on linked data and complex query.

## Subjectives

### RDB
1. [MySQL](http://www.mysql.com/)
2. [PostgreSQL](http://www.postgresql.org/)
3. [Sqlite](http://www.sqlite.org/)

### KV-DB
1. [Redis](http://redis.io/)
2. [Memcached](http://memcached.org/)

### DOC-DB
1. [MongoDB](http://www.mongodb.org/)

### graph-DB
1. [Neo4j](http://www.neo4j.org/)
2. [OrientDB](http://www.orientechnologies.com/orientdb/)

### triple-DB
1. [TDB](https://jena.apache.org/)
2. [Sesame](http://www.openrdf.org/)

## Test Cases

1. KV Query

Query on a given key, for showing baseline performance.
For DBMS, use SELECT on specified key, for Graph DB, use their own methods to access a specified node.

* Sequential Reads
* Random Reads
* Sequential Writes
* Random Writes

Dataset: kv-dataset-generator.py

2. Linked Data Query

Query linked data, to find out the database support for relationships.

Dataset: linked-dataset-generator.py

3. Path finding

Query graph connectivity.

Dataset: graph-dataset-generator.py

4. Pattern Matching

Query sub-graph.

Dataset: graph-dataset-generator.py

## Results

kv-query-yyyy-mm-dd-.csv
...


