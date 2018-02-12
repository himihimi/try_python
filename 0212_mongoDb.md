```
himiMacBookPro:local himi$ ls /Users/himi/Downloads/mongodb-osx-ssl-x86_64-3.6.2.tgz
/Users/himi/Downloads/mongodb-osx-ssl-x86_64-3.6.2.tgz
太傻了 源码直接下来
```

其实可以用  http://www.runoob.com/mongodb/mongodb-osx-install.html  上面写的来

```
# 进入 /usr/local
cd /usr/local

# 下载
sudo curl -O https://fastdl.mongodb.org/osx/mongodb-osx-x86_64-3.4.2.tgz

我要把自己下来的那个移动到
mv /Users/himi/Downloads/mongodb-osx-ssl-x86_64-3.6.2.tgz /usr/local

himiMacBookPro:local himi$ sudo mv /Users/himi/Downloads/mongodb-osx-ssl-x86_64-3.6.2.tgz /usr/local
Password:
ok

# 解压
sudo tar -zxvf mongodb-osx-x86_64-3.4.2.tgz

himiMacBookPro:local himi$ sudo tar -zxvf mongodb-osx-ssl-x86_64-3.6.2.tgz
x mongodb-osx-x86_64-3.6.2/README
x mongodb-osx-x86_64-3.6.2/THIRD-PARTY-NOTICES
x mongodb-osx-x86_64-3.6.2/MPL-2
x mongodb-osx-x86_64-3.6.2/GNU-AGPL-3.0
x mongodb-osx-x86_64-3.6.2/bin/mongodump
x mongodb-osx-x86_64-3.6.2/bin/mongorestore
x mongodb-osx-x86_64-3.6.2/bin/mongoexport
x mongodb-osx-x86_64-3.6.2/bin/mongoimport
x mongodb-osx-x86_64-3.6.2/bin/mongostat
x mongodb-osx-x86_64-3.6.2/bin/mongotop
x mongodb-osx-x86_64-3.6.2/bin/bsondump
x mongodb-osx-x86_64-3.6.2/bin/mongofiles
x mongodb-osx-x86_64-3.6.2/bin/mongoreplay
x mongodb-osx-x86_64-3.6.2/bin/mongoperf
x mongodb-osx-x86_64-3.6.2/bin/mongod
x mongodb-osx-x86_64-3.6.2/bin/mongos
x mongodb-osx-x86_64-3.6.2/bin/mongo
x mongodb-osx-x86_64-3.6.2/bin/install_compass
himiMacBookPro:local himi$ ls
???为什么有这么多x???

# 重命名为 mongodb 目录

sudo mv mongodb-osx-x86_64-3.4.2 mongodb

```
```
安装完成后，我们可以把 MongoDB 的二进制命令文件目录（安装目录/bin）添加到 PATH 路径中：
虽然我加了但是我其实不是很懂
himiMacBookPro:local himi$ echo $PATH
/Library/Frameworks/Python.framework/Versions/3.5/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

himiMacBookPro:local himi$ export PATH=/usr/local/mongodb/bin:$PATH

himiMacBookPro:local himi$ echo $PATH
/usr/local/mongodb/bin:/Library/Frameworks/Python.framework/Versions/3.5/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```
```
其实用绝对路径就可以启动的
也许是加了path之后启动就方便了?
sorry
i dont know

himiMacBookPro:~ himi$ /usr/local/mongodb/bin/mongo
MongoDB shell version v3.6.2
connecting to: mongodb://127.0.0.1:27017
2018-02-12T20:04:22.001+0900 W NETWORK  [thread1] Failed to connect to 127.0.0.1:27017, in(checking socket for error after poll), reason: Connection refused
2018-02-12T20:04:22.003+0900 E QUERY    [thread1] Error: couldn't connect to server 127.0.0.1:27017, connection attempt failed :
connect@src/mongo/shell/mongo.js:251:13
@(connect):1:6
exception: connect failed


himiMacBookPro:~ himi$ /usr/local/mongodb/bin/mongod
2018-02-12T20:04:33.830+0900 I CONTROL  [initandlisten] MongoDB starting : pid=24590 port=27017 dbpath=/data/db 64-bit host=himiMacBookPro.local
2018-02-12T20:04:33.830+0900 I CONTROL  [initandlisten] db version v3.6.2
2018-02-12T20:04:33.830+0900 I CONTROL  [initandlisten] git version: 489d177dbd0f0420a8ca04d39fd78d0a2c539420
2018-02-12T20:04:33.830+0900 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 0.9.8zc 15 Oct 2014
2018-02-12T20:04:33.830+0900 I CONTROL  [initandlisten] allocator: system
2018-02-12T20:04:33.830+0900 I CONTROL  [initandlisten] modules: none
2018-02-12T20:04:33.830+0900 I CONTROL  [initandlisten] build environment:
2018-02-12T20:04:33.830+0900 I CONTROL  [initandlisten]     distarch: x86_64
2018-02-12T20:04:33.830+0900 I CONTROL  [initandlisten]     target_arch: x86_64
2018-02-12T20:04:33.831+0900 I CONTROL  [initandlisten] options: {}
2018-02-12T20:04:33.832+0900 I STORAGE  [initandlisten] exception in initAndListen: NonExistentPath: Data directory /data/db not found., terminating
2018-02-12T20:04:33.832+0900 I CONTROL  [initandlisten] now exiting
2018-02-12T20:04:33.832+0900 I CONTROL  [initandlisten] shutting down with code:100
大概说的是没有db
所以建立一个

```


```
sudo mkdir -p /data/db

???
himiMacBookPro:local himi$ ls -al /
total 46
略
drwxr-xr-x    3 root  wheel    102  2 12 20:25 data
竟然在根的..我也没仔细看
算了 在根就在根

```

```
sudo mkdir -p /data/db

启动 mongodb，默认数据库目录即为 /data/db：

sudo mongod

# 如果没有创建全局路径 PATH，需要进入以下目录
cd /usr/local/mongodb/bin
sudo ./mongod


https://www.mongodb.com/blog/post/mongodb-security-part-ii-10-mistakes-that-can


himiMacBookPro:local himi$ sudo mongod
Password:
2018-02-12T20:38:29.376+0900 I CONTROL  [initandlisten] MongoDB starting : pid=24752 port=27017 dbpath=/data/db 64-bit host=himiMacBookPro.local
2018-02-12T20:38:29.376+0900 I CONTROL  [initandlisten] db version v3.6.2
2018-02-12T20:38:29.376+0900 I CONTROL  [initandlisten] git version: 489d177dbd0f0420a8ca04d39fd78d0a2c539420
2018-02-12T20:38:29.376+0900 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 0.9.8zc 15 Oct 2014
2018-02-12T20:38:29.376+0900 I CONTROL  [initandlisten] allocator: system
2018-02-12T20:38:29.376+0900 I CONTROL  [initandlisten] modules: none
2018-02-12T20:38:29.376+0900 I CONTROL  [initandlisten] build environment:
2018-02-12T20:38:29.377+0900 I CONTROL  [initandlisten]     distarch: x86_64
2018-02-12T20:38:29.377+0900 I CONTROL  [initandlisten]     target_arch: x86_64
2018-02-12T20:38:29.377+0900 I CONTROL  [initandlisten] options: {}
2018-02-12T20:38:29.378+0900 I -        [initandlisten] Detected data files in /data/db created by the 'wiredTiger' storage engine, so setting the active storage engine to 'wiredTiger'.
2018-02-12T20:38:29.378+0900 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=7680M,session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),
2018-02-12T20:38:29.984+0900 I STORAGE  [initandlisten] WiredTiger message [1518435509:984306][24752:0x7fff75831300], txn-recover: Main recovery loop: starting at 2/6400
2018-02-12T20:38:30.104+0900 I STORAGE  [initandlisten] WiredTiger message [1518435510:104103][24752:0x7fff75831300], txn-recover: Recovering log 2 through 3
2018-02-12T20:38:30.193+0900 I STORAGE  [initandlisten] WiredTiger message [1518435510:193325][24752:0x7fff75831300], txn-recover: Recovering log 3 through 3
2018-02-12T20:38:30.457+0900 I CONTROL  [initandlisten]
2018-02-12T20:38:30.457+0900 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2018-02-12T20:38:30.457+0900 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2018-02-12T20:38:30.457+0900 I CONTROL  [initandlisten] ** WARNING: You are running this process as the root user, which is not recommended.
2018-02-12T20:38:30.458+0900 I CONTROL  [initandlisten]
2018-02-12T20:38:30.458+0900 I CONTROL  [initandlisten] ** WARNING: This server is bound to localhost.
2018-02-12T20:38:30.458+0900 I CONTROL  [initandlisten] **          Remote systems will be unable to connect to this server.
2018-02-12T20:38:30.458+0900 I CONTROL  [initandlisten] **          Start the server with --bind_ip <address> to specify which IP
2018-02-12T20:38:30.458+0900 I CONTROL  [initandlisten] **          addresses it should serve responses from, or with --bind_ip_all to
2018-02-12T20:38:30.458+0900 I CONTROL  [initandlisten] **          bind to all interfaces. If this behavior is desired, start the
2018-02-12T20:38:30.458+0900 I CONTROL  [initandlisten] **          server with --bind_ip 127.0.0.1 to disable this warning.
2018-02-12T20:38:30.458+0900 I CONTROL  [initandlisten]
2018-02-12T20:38:30.529+0900 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/data/db/diagnostic.data'
2018-02-12T20:38:30.530+0900 I NETWORK  [initandlisten] waiting for connections on port 27017
^C
2018-02-12T20:39:37.295+0900 I CONTROL  [signalProcessingThread] got signal 2 (Interrupt: 2), will terminate after current cmd ends
2018-02-12T20:39:37.295+0900 I NETWORK  [signalProcessingThread] shutdown: going to close listening sockets...
2018-02-12T20:39:37.295+0900 I NETWORK  [signalProcessingThread] removing socket file: /tmp/mongodb-27017.sock
2018-02-12T20:39:37.296+0900 I FTDC     [signalProcessingThread] Shutting down full-time diagnostic data capture
2018-02-12T20:39:37.297+0900 I STORAGE  [signalProcessingThread] WiredTigerKVEngine shutting down
2018-02-12T20:39:37.523+0900 I STORAGE  [signalProcessingThread] shutdown: removing fs lock...
2018-02-12T20:39:37.524+0900 I CONTROL  [signalProcessingThread] now exiting
2018-02-12T20:39:37.524+0900 I CONTROL  [signalProcessingThread] shutting down with code:0


himiMacBookPro:bin himi$ sudo mongod --port 27017 --dbpath /data/db
一样


himiMacBookPro:~ himi$ sudo /usr/local/mongodb/bin/mongod --version
db version v3.6.2
git version: 489d177dbd0f0420a8ca04d39fd78d0a2c539420
OpenSSL version: OpenSSL 0.9.8zc 15 Oct 2014
allocator: system
modules: none
build environment:
    distarch: x86_64
    target_arch: x86_64
    
3.6.2 是不是太.....高了所以才....


```

```
再打开一个终端进入执行以下命令：

$ cd /usr/local/mongodb/bin 
$ ./mongo
MongoDB shell version v3.4.2
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.4.2
Welcome to the MongoDB shell.
……
> 1 + 1
2
> 
注意：如果你的数据库目录不是/data/db，可以通过 --dbpath 来指定。
```



```
himiMacBookPro:venv himi$ /Users/himi/12_py/pc_ce/venv/bin/pip install pymongo
Collecting pymongo
  Downloading pymongo-3.6.0-cp35-cp35m-macosx_10_6_intel.whl (315kB)
    100% |████████████████████████████████| 317kB 226kB/s
Installing collected packages: pymongo
Successfully installed pymongo-3.6.0
himiMacBookPro:venv himi$

第三方库倒是这样弄好了
```


感谢大佬
我总算知道为什么
因为加d的是服务器
好比 mysqld 和 httpd
mysql在启动的时候也是要 ini什么mysqld 还有apache也是
要先启动服务器才能使用服务

而mongo也是

他的目录下
```
himiMacBookPro:~ himi$ ls -l /usr/local/mongodb/
total 232
-rw-r--r--@  1 500   staff  34520  1 11 01:06 GNU-AGPL-3.0
-rw-r--r--@  1 500   staff  16726  1 11 01:06 MPL-2
-rw-r--r--@  1 500   staff   2195  1 11 01:06 README
-rw-r--r--@  1 500   staff  57190  1 11 01:06 THIRD-PARTY-NOTICES
drwxr-xr-x  16 root  wheel    544  2 12 19:41 bin
```

bin的里面
```
himiMacBookPro:~ himi$ ls -l /usr/local/mongodb/bin/
total 560968
-rwxr-xr-x@ 1 500  staff  10812344  1 11 01:06 bsondump
-rwxr-xr-x@ 1 500  staff      5791  1 11 01:32 install_compass
-rwxr-xr-x@ 1 500  staff  32089820  1 11 01:30 mongo
-rwxr-xr-x@ 1 500  staff  57344772  1 11 01:30 mongod
-rwxr-xr-x@ 1 500  staff  13227464  1 11 01:07 mongodump
-rwxr-xr-x@ 1 500  staff  11195216  1 11 01:07 mongoexport
-rwxr-xr-x@ 1 500  staff  11064936  1 11 01:07 mongofiles
-rwxr-xr-x@ 1 500  staff  11363304  1 11 01:07 mongoimport
-rwxr-xr-x@ 1 500  staff  56920936  1 11 01:30 mongoperf
-rwxr-xr-x@ 1 500  staff  14863080  1 11 01:08 mongoreplay
-rwxr-xr-x@ 1 500  staff  14586312  1 11 01:07 mongorestore
-rwxr-xr-x@ 1 500  staff  31266080  1 11 01:19 mongos
-rwxr-xr-x@ 1 500  staff  11421944  1 11 01:06 mongostat
-rwxr-xr-x@ 1 500  staff  11019616  1 11 01:08 mongotop
```

而这个里面执行 
> mongod 就是启动服务器!!!!!!!!!!!!!!!

> mongo 就是启动服务!!!!!!!!!! 

所以1.启动服务器
选择启动的方式: 直接路径启动的,选择数据库的
我现在有两个数据库

>一个 /data/db

>一个是我以为那个db权限不够 /Users/himi/12_code/m_db/

比如:
```
himiMacBookPro:bin himi$ mongod --dbpath /Users/himi/12_code/m_db/

himiMacBookPro:bin himi$ sudo mongod
因为default的/data/db 权限比较高 不sudo开不了
```
然后下面显示的就仿佛是 tail 了 整个启动log
在服务的内容可以在这里看到
```
2018-02-12T22:41:18.598+0900 I CONTROL  [initandlisten] MongoDB starting : pid=25318 port=27017 dbpath=/Users/himi/12_code/m_db/ 64-bit host=himiMacBookPro.local
2018-02-12T22:41:18.598+0900 I CONTROL  [initandlisten] db version v3.6.2
2018-02-12T22:41:18.598+0900 I CONTROL  [initandlisten] git version: 489d177dbd0f0420a8ca04d39fd78d0a2c539420
2018-02-12T22:41:18.598+0900 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 0.9.8zc 15 Oct 2014
2018-02-12T22:41:18.598+0900 I CONTROL  [initandlisten] allocator: system
2018-02-12T22:41:18.598+0900 I CONTROL  [initandlisten] modules: none
2018-02-12T22:41:18.598+0900 I CONTROL  [initandlisten] build environment:
2018-02-12T22:41:18.598+0900 I CONTROL  [initandlisten]     distarch: x86_64
2018-02-12T22:41:18.598+0900 I CONTROL  [initandlisten]     target_arch: x86_64
2018-02-12T22:41:18.598+0900 I CONTROL  [initandlisten] options: { storage: { dbPath: "/Users/himi/12_code/m_db/" } }
2018-02-12T22:41:18.599+0900 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=7680M,session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten]
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten]
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] ** WARNING: This server is bound to localhost.
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] **          Remote systems will be unable to connect to this server.
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] **          Start the server with --bind_ip <address> to specify which IP
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] **          addresses it should serve responses from, or with --bind_ip_all to
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] **          bind to all interfaces. If this behavior is desired, start the
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] **          server with --bind_ip 127.0.0.1 to disable this warning.
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten]
2018-02-12T22:41:19.163+0900 I STORAGE  [initandlisten] createCollection: admin.system.version with provided UUID: cff52967-7888-4eef-a2f6-eea56d9113d6
2018-02-12T22:41:19.348+0900 I COMMAND  [initandlisten] setting featureCompatibilityVersion to 3.6
2018-02-12T22:41:19.378+0900 I STORAGE  [initandlisten] createCollection: local.startup_log with generated UUID: 45667386-43b9-4173-9604-0099a30bc679
2018-02-12T22:41:19.433+0900 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/Users/himi/12_code/m_db/diagnostic.data'
2018-02-12T22:41:19.434+0900 I NETWORK  [initandlisten] waiting for connections on port 27017
2018-02-12T22:46:19.452+0900 I STORAGE  [thread1] createCollection: config.system.sessions with generated UUID: d9b138e3-3cf2-41f2-bfa4-a9339e876b05
2018-02-12T22:46:19.531+0900 I INDEX    [thread1] build index on: config.system.sessions properties: { v: 2, key: { lastUse: 1 }, name: "lsidTTLIndex", ns: "config.system.sessions", expireAfterSeconds: 1800 }
2018-02-12T22:46:19.531+0900 I INDEX    [thread1] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2018-02-12T22:46:19.543+0900 I INDEX    [thread1] build index done.  scanned 0 total records. 0 secs



2018-02-12T23:28:19.841+0900 I NETWORK  [listener] connection accepted from 127.0.0.1:52697 #1 (1 connection now open)
2018-02-12T23:28:19.842+0900 I NETWORK  [conn1] received client metadata from 127.0.0.1:52697 conn: { application: { name: "MongoDB Shell" }, driver: { name: "MongoDB Internal Client", version: "3.6.2" }, os: { type: "Darwin", name: "Mac OS X", architecture: "x86_64", version: "14.1.1" } }
2018-02-12T23:40:45.059+0900 I NETWORK  [conn1] end connection 127.0.0.1:52697 (0 connections now open)
2018-02-12T23:41:00.986+0900 I NETWORK  [listener] connection accepted from 127.0.0.1:53456 #2 (1 connection now open)
2018-02-12T23:41:00.986+0900 I NETWORK  [conn2] received client metadata from 127.0.0.1:53456 conn: { application: { name: "MongoDB Shell" }, driver: { name: "MongoDB Internal Client", version: "3.6.2" }, os: { type: "Darwin", name: "Mac OS X", architecture: "x86_64", version: "14.1.1" } }
```

2. 换一个窗口使用服务
我虽然是在path里定义了
但是我不会用
所以还是绝对路径把

```
himiMacBookPro:~ himi$ /usr/local/mongodb/bin/mongo
MongoDB shell version v3.6.2
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.2
Server has startup warnings:
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten]
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten]
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] ** WARNING: This server is bound to localhost.
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] **          Remote systems will be unable to connect to this server.
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] **          Start the server with --bind_ip <address> to specify which IP
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] **          addresses it should serve responses from, or with --bind_ip_all to
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] **          bind to all interfaces. If this behavior is desired, start the
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten] **          server with --bind_ip 127.0.0.1 to disable this warning.
2018-02-12T22:41:19.149+0900 I CONTROL  [initandlisten]
>

>
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
>

```

> 新开一个 terminal 然后用 mongodb shell 呀

> mongod 是 mongodb 的服务端

> mongo 是 mongodb 的客户端……

> 配置和启动的话一般官网都有步骤吧

> 比如这个 https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/#install-mongodb-community-edition-with-homebrew

- https://docs.mongodb.com/getting-started/shell/client/ 

- https://stackoverflow.com/questions/5596521/what-is-the-correct-way-to-start-a-mongod-service-on-linux-os-x


然后我发现这个里面说得不错......

- http://www.runoob.com/mongodb/mongodb-connections.html


> http://api.mongodb.com/python/current/

这个第三方库的说明就倒是再看吧