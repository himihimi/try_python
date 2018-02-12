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