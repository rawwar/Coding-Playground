cd into the extracted zookeeper folder

create a configuration file in conf/zoo.cfg with following configuration

```
tickTime=2000
dataDir=/tmp/zookeeper/datadir
clientPort=2181
```

**bin/zkServer.sh start** : Starts a zookeeper server

**bin/zkServer.sh stop** : To stop the zookeeper server


**bin/zkCli.sh --server localhost:2181**: To connect to the zookeeper server

### Once connected:

**ls /** : list znodes at /

**create /node1 hello** : create a znode named node1 under / with data "hello"

**get /node1**: get data in /node1

**get -s /node1** : Gets data along with detailed info like version, time stamps