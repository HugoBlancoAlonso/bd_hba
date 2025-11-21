```python
%cd pruebas/indice_invertido/
```

    /media/notebooks/pruebas/indice_invertido


    /usr/local/lib/python3.10/dist-packages/IPython/core/magics/osm.py:417: UserWarning: This is now an optional IPython functionality, setting dhist requires you to install the `pickleshare` library.
      self.shell.db['dhist'] = compress_dhist(dhist)[-100:]



```python
%%writefile mapper.py
#!/usr/bin/env python3

import sys
import os

filename = os.environ.get("map_input_file", "desconocido")

for line in sys.stdin:
    line = line.strip().split()
    for word in line:
        print(f"{word}\t{filename}")
```

    Overwriting mapper.py



```python
%%writefile reducer.py
#!/usr/bin/env python3

import sys

current_word = None
docs = set()

for line in sys.stdin:
    word, doc = line.strip().split("\t", 1)
    if current_word == word:
        docs.add(doc)
    else:
        if current_word:
            print(f"{current_word}\t{','.join(sorted(docs))}")
        current_word = word
        docs = {doc}

if current_word:
    print(f"{current_word}\t{','.join(sorted(docs))}")
```

    Overwriting reducer.py



```python
%%writefile doc1.txt
el cielo es azul
```

    Overwriting doc1.txt



```python
%%writefile doc2.txt
el sol es amarillo
```

    Overwriting doc2.txt



```python
%%writefile doc3.txt
el cielo es grande
```

    Overwriting doc3.txt



```python
!hdfs dfs -ls /
```

    Found 4 items
    drwxr-xr-x   - root supergroup          0 2025-11-13 10:08 /contar_palabras
    drwxr-xr-x   - root supergroup          0 2025-11-18 09:23 /indice_invertido
    drwxrwx---   - root supergroup          0 2025-11-12 11:31 /tmp
    drwxrwxrwt   - root root                0 2025-11-18 09:10 /yarn



```python
!hdfs dfs -mkdir /indice_invertido
!hdfs dfs -put doc*.txt /indice_invertido
```


```python
!hadoop jar \
/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \
-file mapper.py \
-file reducer.py \
-mapper mapper.py \
-reducer reducer.py \
-input /indice_invertido/ \
-output /indice_invertido/salida

```

    2025-11-21 13:34:20,758 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
    packageJobJar: [mapper.py, reducer.py, /tmp/hadoop-unjar7358244272729334237/] [] /tmp/streamjob4986789664173839746.jar tmpDir=null
    2025-11-21 13:34:21,298 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at yarnmanager/172.20.0.6:8032
    2025-11-21 13:34:21,420 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at yarnmanager/172.20.0.6:8032
    2025-11-21 13:34:21,600 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/root/.staging/job_1763731605970_0004
    2025-11-21 13:34:21,967 INFO mapred.FileInputFormat: Total input files to process : 3
    2025-11-21 13:34:22,039 INFO mapreduce.JobSubmitter: number of splits:3
    2025-11-21 13:34:22,126 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1763731605970_0004
    2025-11-21 13:34:22,126 INFO mapreduce.JobSubmitter: Executing with tokens: []
    2025-11-21 13:34:22,277 INFO conf.Configuration: resource-types.xml not found
    2025-11-21 13:34:22,277 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
    2025-11-21 13:34:22,327 INFO impl.YarnClientImpl: Submitted application application_1763731605970_0004
    2025-11-21 13:34:22,351 INFO mapreduce.Job: The url to track the job: http://yarnmanager:8088/proxy/application_1763731605970_0004/
    2025-11-21 13:34:22,352 INFO mapreduce.Job: Running job: job_1763731605970_0004
    2025-11-21 13:34:26,424 INFO mapreduce.Job: Job job_1763731605970_0004 running in uber mode : false
    2025-11-21 13:34:26,424 INFO mapreduce.Job:  map 0% reduce 0%
    2025-11-21 13:34:31,473 INFO mapreduce.Job:  map 100% reduce 0%
    2025-11-21 13:34:35,491 INFO mapreduce.Job:  map 100% reduce 100%
    2025-11-21 13:34:35,497 INFO mapreduce.Job: Job job_1763731605970_0004 completed successfully
    2025-11-21 13:34:35,551 INFO mapreduce.Job: Counters: 54
    	File System Counters
    		FILE: Number of bytes read=649
    		FILE: Number of bytes written=1257951
    		FILE: Number of read operations=0
    		FILE: Number of large read operations=0
    		FILE: Number of write operations=0
    		HDFS: Number of bytes read=349
    		HDFS: Number of bytes written=601
    		HDFS: Number of read operations=14
    		HDFS: Number of large read operations=0
    		HDFS: Number of write operations=2
    		HDFS: Number of bytes read erasure-coded=0
    	Job Counters 
    		Launched map tasks=3
    		Launched reduce tasks=1
    		Data-local map tasks=3
    		Total time spent by all maps in occupied slots (ms)=7108
    		Total time spent by all reduces in occupied slots (ms)=1683
    		Total time spent by all map tasks (ms)=7108
    		Total time spent by all reduce tasks (ms)=1683
    		Total vcore-milliseconds taken by all map tasks=7108
    		Total vcore-milliseconds taken by all reduce tasks=1683
    		Total megabyte-milliseconds taken by all map tasks=7278592
    		Total megabyte-milliseconds taken by all reduce tasks=1723392
    	Map-Reduce Framework
    		Map input records=3
    		Map output records=12
    		Map output bytes=619
    		Map output materialized bytes=661
    		Input split bytes=294
    		Combine input records=0
    		Combine output records=0
    		Reduce input groups=7
    		Reduce shuffle bytes=661
    		Reduce input records=12
    		Reduce output records=7
    		Spilled Records=24
    		Shuffled Maps =3
    		Failed Shuffles=0
    		Merged Map outputs=3
    		GC time elapsed (ms)=236
    		CPU time spent (ms)=3090
    		Physical memory (bytes) snapshot=1236508672
    		Virtual memory (bytes) snapshot=10409000960
    		Total committed heap usage (bytes)=994050048
    		Peak Map Physical memory (bytes)=344846336
    		Peak Map Virtual memory (bytes)=2600787968
    		Peak Reduce Physical memory (bytes)=245776384
    		Peak Reduce Virtual memory (bytes)=2609070080
    	Shuffle Errors
    		BAD_ID=0
    		CONNECTION=0
    		IO_ERROR=0
    		WRONG_LENGTH=0
    		WRONG_MAP=0
    		WRONG_REDUCE=0
    	File Input Format Counters 
    		Bytes Read=55
    	File Output Format Counters 
    		Bytes Written=601
    2025-11-21 13:34:35,551 INFO streaming.StreamJob: Output directory: /indice_invertido/salida



```python
#!hdfs dfs -rm -r /indice_invertido/salida
```


```python
!hdfs dfs -cat /indice_invertido/salida/part-00000
```

    amarillo	hdfs://namenode:9000/indice_invertido/doc2.txt
    azul	hdfs://namenode:9000/indice_invertido/doc1.txt
    cielo	hdfs://namenode:9000/indice_invertido/doc1.txt,hdfs://namenode:9000/indice_invertido/doc3.txt
    el	hdfs://namenode:9000/indice_invertido/doc1.txt,hdfs://namenode:9000/indice_invertido/doc2.txt,hdfs://namenode:9000/indice_invertido/doc3.txt
    es	hdfs://namenode:9000/indice_invertido/doc1.txt,hdfs://namenode:9000/indice_invertido/doc2.txt,hdfs://namenode:9000/indice_invertido/doc3.txt
    grande	hdfs://namenode:9000/indice_invertido/doc3.txt
    sol	hdfs://namenode:9000/indice_invertido/doc2.txt



```python
cat doc1.txt | python3 mapper.py | sort | python3 reducer.py
```

    azul	desconocido
    cielo	desconocido
    el	desconocido
    es	desconocido

