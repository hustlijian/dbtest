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
3. [leveldb](https://code.google.com/p/leveldb/)

### DOC-DB
1. [MongoDB](http://www.mongodb.org/)

### graph-DB
1. [Neo4j](http://www.neo4j.org/)
2. [OrientDB](http://www.orientechnologies.com/orientdb/)

### triple-DB
1. [TDB](https://jena.apache.org/)
2. [Sesame](http://www.openrdf.org/)

## Test Cases

### Case 1: KV Query

Query on a given key, for showing baseline performance.
For DBMS, use SELECT on specified key, for Graph DB, use their own methods to access a specified node.

* Sequential Reads
* Random Reads
* Sequential Writes
* Random Writes

Dataset: kv-dataset-generator.py

### Case 2: Linked Data Query

Query linked data, to find out the database support for relationships.

Dataset: linked-dataset-generator.py

### Case 3: Path finding

Query graph connectivity.

Dataset: graph-dataset-generator.py

### Case 4: Pattern Matching

Query sub-graph.

Dataset: graph-dataset-generator.py

## Results

kv-query-yyyy-mm-dd-.csv
...

## References

1. Benchmarking Top NoSQL Databases, [link](http://www.datastax.com/resources/whitepapers/benchmarking-top-nosql-databases)
2. Scalable SQL and NoSQL data stores, [link](http://dl.acm.org/citation.cfm?id=1978919)
3. Performance of graph query languages: comparison of cypher, gremlin and native access in Neo4j, [link](http://dl.acm.org/citation.cfm?id=2457351)
4. Survey of graph database performance on the HPC scalable graph analysis benchmark, [link](http://dl.acm.org/citation.cfm?id=1927590)
5. Survey of graph database models, [link](http://dl.acm.org/citation.cfm?id=1322433)
6. Graph Database Indexing Using Structured Graph Decomposition, [link](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=4221746&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D4221746)
7. A comparison of a graph database and a relational database: a data provenance perspective, [link](http://dl.acm.org/citation.cfm?id=1900067)
8. Freebase: a collaboratively created graph database for structuring human knowledge, [link](http://dl.acm.org/citation.cfm?id=1376746)
9. Fast and practical indexing and querying of very large graphs, [link](http://dl.acm.org/citation.cfm?id=1247573)
...

