# python操作mongodb

版本：python3.8，pymongo3.9

pymongo官方文档：https://www.osgeo.cn/mongo-python-driver/api/index.html

参考：

https://blog.csdn.net/DanielJackZ/article/details/123749384

https://blog.csdn.net/qq_42403866/article/details/104336537

https://blog.csdn.net/dinglin1237/article/details/102286004

### mongodb简介

Mongodb 中使用bson 存储数据（可以理解为在 json 的基础上添加一些 json 中没有的数据类型）。

一条数据称为一个文档/记录。

### 连接数据库

```python
import pymongodb
def connect_mongo(query={},host='localhost', port=27017, username=None, password=None, db='test'):
    if username and password:
        mongo_uri = "mongodb://%s:%s@%s:%s/%s" % (username, password, host, port, db)
        client = pymongo.MongoClient(mongo_uri)
    else:
        client = pymongo.MongoClient(host, port)
    return client
client = connect_mongo()

# 查询数据库
db = client.A.B
```

### 查询

使用 find() 方法查询：返回Cursor对象（指向第一个数据之前的指针），而不是一个文档。

> Cursor对象相当于一个指针，可通过迭代它来访问MongdoDB数据库中的一组对象。Cursor对象内部存储了一个指向当前位置的索引，可以保证每次读取一个文档。在MongoDB中，有些操作只影响Cursor中的当前文档，并将索引数加 1，而有些操作影响当前索引之后的所有文档。

使用find_one() 方法查询直接返回文档（dict）。

#### 1.语法

```python
#查询所有数据
db.COLLECTION_NAME.find()
#查询指定某键值的数据，多个键时查询交集
db.COLLECTION_NAME.find({ key1: value1, key2: value2 })
#查询第一个满足条件的数据
db.COLLECTION_NAME.find_one({ key1: value1, key2: value2 })
#模糊查询，正则匹配
{"name":/^start/} #以 'start' 开头的匹配式
{"name":/tail$/} #以 'tail' 结尾的匹配式
#读取n个数据记录
db.COLLECTION_NAME.find().limit(10)
# 跳过前n个数据记录
db.COLLECTION_NAME.find().skip(3)
# 排序
db.COLLECTION_NAME.find().sort([(KEY1,1|-1),(KEY2,1|-1)]) # 1：升序，-1：降序
db.COLLECTION_NAME.find(sort=[(KEY,pymongo.ASCENDING)]) # ASCENDING-升 DESCENDING-降
db.COLLECTION_NAME.find().sort([(KEY,pymongo.ASCENDING)])
# 计数
db.COLLECTION_NAME.find().count() #已弃用
db.COLLECTION_NAME.count_document({ key1: value1, key2: value2 })
```

#### 2.条件查询

| 运算符                                                       | 描述         | 示例                |
| ------------------------------------------------------------ | ------------ | ------------------- |
| field:value                                                  | 字段值=value | { name : "myName" } |
| `$gt`         | 大于                                                     | { size : { `$gt` : 5 } } |              |                     |
| `$gte`        | 大于等于                                                 | { size : { `$gte` : 5 } } |              |                     |
| `$lt`         | 小于                                                     | { size : { `$lt` : 5} } |              |                     |
| `$lte`        | 小于等于                                                 | { size : { `$lte` : 5 } } |              |                     |
| `$ne`         | 不等于                                                   | { name : {`$ne` : "badName"} } |              |                     |
| `$in`         | 包含于指定数组[]                                         | { like : { `$in` : [ "C","JAVA" ] } } |              |                     |
| `$nin`        | 不包含于指定数组[]                                       | { name : { `$nin` : ["html","css"] } } |              |                     |
| `$or`         | 逻辑或连接查询                                           | { `$or` : [ {size : {`$lt` : 5} }, {size : {`$gt` : 10} } ] } |              |                     |
| `$and`        | 逻辑与连接查询                                           | { `$and` : [ { size : { `$gt` : 5 } },{ size : { `$lt` : 10 } } ] } |              |                     |
| `$not`        | 反转查询（不等于）                                       | { `$not` : { name : "myName" } } |              |                     |
| `$nor`        | 逻辑或非连接查询，不等于任一个                           | { `$nor` : { size : { `$gt` : 5 } },{ size : { `$lt` : 0 } } } |              |                     |
| `$exists`     | true-包含指定字段，false-不包含该字段                    | { name : { `$exists` : true } } |              |                     |
| `$regex`      | 匹配正则表达式                                           | { myString : { `$regex` : ' some.*exp ' } } |              |                     |
| `$all`        | 指定数组包含所有指定元素                                 | { word : { `$all` : [ 'a','b','c' ] } } |              |                     |
| `$elemMatch`  | 返回指定的数组字段至少有一个元素与指定的条件都匹配的文档 | { myArr : { `$elemMatch` : { { value : { `$gt` : 5 } },{ size : { `$lt` : 10 } } } } } |              |                     |
| `$size`       | 指定数组的长度                                           | { myArr : { `$size` : 5 } } |              |                     |

在文档中尽量不要将值赋为null，因为进行null查询时（例如name=null），不仅会返回name值为null的文档，也会将不包含name字段的文档返回。所以应尽量避免使用null值，而应不包含这样的字段，这样就可以使用 $exists运算符进行不包含查询了。

#### 3.子文档查询

```python
{     "father" : {
         "name" : "uzi",
         "age" : 24 }
} # 这里father字段又对应了一个子文档
```

#### 4.投影

find()方法时默认显示所有字段。可以通过给字段赋 1/true 表示包含，赋 -1/false 表示排除。

当字段包含时，只会显示包含的字段；当字段排除时，会显示出排除外的所有字段。

同一个表达式中，不能同时指定包含和排除。

```python
db.student.find({},{name:1}) # 示例
```

#### 5.返回某个字段的值

获取一组文档中某个字段的不同值列表：Collection对象的 distinct() 方法。

```python
db.collection_name.distinct(key,[query]) 
# key-指定要获得值的字段
# query-查询条件（可选）
db.collection_name.distinct("father.name") # 查询子文档中的值
```

#### 6.匹配数据类型

$type操作符是基于BSON类型来检索集合中匹配的数据类型，并返回结果。

```python
db.aaa.find({"name":{$type:2}})
db.aaa.find({"name":{$type:'string'}})
```

类型及代号

| 类型                    | 数字      |                  |
| ----------------------- | --------- | ---------------- |
| Double                  | 1         | 双精度           |
| String                  | 2         | 字符串           |
| Object                  | 3         | 对象             |
| Array                   | 4         | 数组             |
| Binary data             | 5         | 二进制数据       |
| Undefined               | 6(已废弃) |                  |
| Object id               | 7         | 对象ID           |
| Boolean                 | 8         | 布尔型           |
| Date                    | 9         | 日期             |
| Null                    | 10        | 空               |
| Regular Expression      | 11        | 正则表达式       |
| JavaScript              | 13        | js代码           |
| Symbol                  | 14        | 符号             |
| JavaScript (with scope) | 15        | 有作用域的js代码 |
| 32-bit integer          | 16        | 32位整型         |
| Timestamp               | 17        | 时间戳           |
| 64-bit integer          | 18        | 64位整型         |
| Min key                 | -1        | 最小值           |
| Max key                 | 127       | 最大值           |

### 插入

insert_one()：插入一条数据

insert_many()：插入多条数据

save()：插入一条数据

>save()可以在文档不存在的时候插入，存在的时候更新，只有一个参数文档。要是文档含有"_id"，会调用upsert。否则，会调用插入。

```python
res = collection.insert_one(student) # student是一个dict
print(res, res.inserted_id) # 获取_id属性

res = collection.insert_many(studends) # students是一个元素为dict的列表，返回_id的列表
```

MongoDB的每条数据都有一个 _id 属性来唯一标识。insert_one返回的object中的inserted_id可以获取该属性。

### 更新

#### 1.语法

update_one(查询条件，更新条件)：更新满足条件的第一条记录

update_many(查询条件，更新条件)：更新满足条件的all记录

```python
# 更新满足条件{'id', 2}的第一条记录，将id更新为3
res = collection.update_one({'id': 2}, {'$set': {'id': 3, 'age': 10}})
print(res.matched_count, res.modified_count) # 匹配的记录数、影响的记录数
```

为了提高性能，如果update_many()操作中没有互相依赖关系，可以设置ordered=False。

```python
user_data = ({'uid': uid, 'user_data': data} for uid, data in user_dict.items())
user_collection.insert_many(user_data, ordered=False)
```

#### 2.常用修改器

##### 1)$set

指定一个键并更新键值，若键不存在并创建。

##### 2)$inc

对文档的某个值为数值型的键进行增减。操作非数值型的记录报错。

```python
# 更新满足条件 id>1 的所有记录，id 字段自加 100
res = collection.update_many({'id': {'$gt': 1}}, {'$inc': {'id': 100}})
```

##### 3)$unset

用来删除键，不论对目标键使用1、0、-1或者具体的字符串等，都可以删除该目标键。

```python
res = collection.update_many({'id': 2}, {'$set': {'id': 1})
```

##### 4)数组修改器

操作非数组型的记录报错。

* $push

  向数组中添加值。

* $ne

  数组类型键值添加一个元素时，避免在数组中产生重复数据。在有些情况不行。

  ```python
  res = collection.update_many({"title":{"$ne":"t2"}},{"$push":{"title":"t2"}})
  #向title数组中不含t2的记录中插入t2
  ```

* $addToSet

  功能同$ne，但是能直接插入。

  ```python
  res = collection.update_many({},{"$addToSet":{"title":"t2"}})
  #向title数组中不含t2的记录中插入t2
  ```

* $pop

  从数组的头/尾删除数组中的元素，只能为1或-1。

  ```python
  collection.update_many({"name" : "zgq"},{"$pop":{"title":1}}) # 1：从数组的尾部删除
  collection.update_many({"name" : "zgq"},{"$pop":{"title":-1}}) # -1：从数组的头部删除
  ```

* $pull

  从数组中删除满足条件的元素。可看作与push相反。

* 定位修改器

  需要对数组中的值进行操作时，可使用定位操作符"$"定位。可直接将数组下标(从0开始)作为键来选择元素。

  ```python
  record = {
      "uid":"001",
      lst:[
          {"name":"t1","size":10},
          {"name":"t2","size":12}
      ]
  }
  collection.update_many({"uid":"001"},{"$inc":{"lst.0.size":1}}) # 定位到数组第一个元素
  collection.update_many({"lst.name":"t1"},{"$set":{"lst.$.size":1}}) # 定位当前元素
  ```

  若有多个文档满足条件，则只更新第一个文档。

##### 5)$upsert

upsert=True表示如果没有满足更新条件的记录，则会将stu插入集合中。有满足条件的就正常更新。

```python
stu = {'name': 'test3'}
res = collection.update_one({'id': 4}, {'$set': stu}, upsert=True)
print(res.matched_count, res.modified_count) # 打印结果：0 0
# 这里插入后的stu = {'id': 4，'name': 'test3'}，把查询条件也一并插入了
```

#### 3.查询并更新全过程

```python
condition = {'name':'zgq'}						# 1. 定义一个查询条件condition
student = collection.find_one(condition) 			# 2. 根据查询条件查询数据 student
student['age'] = 50 								# 3. 修改student中的age
collection.update_one(condition,{'$set':student}) 	# 4. 更新
```

### 删除

delete_one()：删除符合条件的一条记录

delete_many()：删除符合条件的所有记录

```python
res = collection.delete_one({'id': 1})
print(result.deleted_count) # 查询删除的记录数

# 删除满足条件的所有记录，以下为删除 page < 90 的记录
result = collection.delete_many({'id': {'$lt': 2}})
```

### 大批量读写

#### 1.update_many()参数设置

为了提高性能，如果update_many()操作中没有互相依赖关系，可以设置ordered=False。

```python
user_data = ({'uid': uid, 'user_data': data} for uid, data in user_dict.items())
user_collection.insert_many(user_data, ordere=False)
```

性能提高明显。

#### 2.bulk_write()方法

需要批量操作时候，为了节省网络连接交互次数，可以使用collect.bulk_write()方法。
批量操作中没有互相依赖关系，所以设置ordered=False。如果有前后顺序的互相依赖，需要设置为True。

```python
from pymongo import InsertOne, DeleteOne, UpdateOne
update_info = [
    UpdateOne({"name":"test1"},{"$set":{"age":13}}, upsert=True), 
    UpdateOne({"name":"test2"},{"$set":{"age":10}}, upsert=True)
]
collection.bulk_write(update_info)
```

#### 3.批量读取

批量读取可以使用`$in`操作符，但如果`$in`针对的list过大，可能会报错pymongo.errors.DocumentTooLarge。

可以将大的list分割成1000个一段，然后分段查询。

#### 4.motor库


如果使用Python做大型海量数据批量任务，并且backend用mongodb做数据储存时，常常面临大量读写数据库的情况。尤其是大量更新任务，由于不能批量操作，我们知道pymongo是同步任务机制，相当耗时。

如果采用多线程、多进程的方案确实有效，但编写麻烦、消耗系统资源大（pymongo还不允许fork线程中共用连接）。这里主要瓶颈在于IO，使用单线程异步操作就会效果很好。

Motor是一个异步mongodb driver，支持异步读写mongodb。它通常用在基于Tornado的异步web服务器中。

Motor同时支持使用asyncio（Python3.4以上标准库）作为异步模型，使用起来十分方便。

```python
host = '127.0.0.1'
port = 27017
database = 'local'
import time
# 普通形式
start = time.clock()
from pymongo import MongoClient
connection = MongoClient(host,port)
db = connection[database]
for doc in db.test.find({}, ['_id', 'JobTitle', 'is_end']):
    db.test.update_one({'_id': doc.get('_id')}, {'$set': {'is_end': 1}})
elapsed = (time.clock() - start)
print("Time used:",elapsed) # 运行一下，发现用了4秒左右

# 使用motor以异步的形式
start = time.clock()
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
connection = AsyncIOMotorClient(host,port)
db = connection[database]
async def run():
    async for doc in db.test.find({}, ['_id', 'JobTitle', 'is_end']):
        db.test.update_one({'_id': doc.get('_id')}, {'$set'{'is_end':0}})
asyncio.get_event_loop().run_until_complete(run())
elapsed = (time.clock() - start)
print("Time used:",elapsed) # 仅仅1秒左右就完成了任务
```

### colab连接本地数据库

>非常感谢chatGPT的方案！！！虽然有瑕疵但是结合csdn教程足够了！！

在colab的ipynb文件中输入

```python
!apt install mongodb # 或 pip install？
!service mongodb start #这个好像可以没有
```

安装ngrok https://ngrok.com/download

进行内网穿透

(全教程参考 https://blog.csdn.net/sinat_34842630/article/details/124992878 )

在命令行上运行ngrok，命令如下：

```bash
./ngrok authtoken YOUR_AUTH_TOKEN
#windows应该用 ngrok config add-authtoken YOUR_AUTH_TOKEN
./ngrok tcp 27017
```

其中`YOUR_AUTH_TOKEN`应替换为您的ngrok身份验证令牌。它将显示如下信息：

```css
ngrok by @inconshreveable                                                 (Ctrl+C to quit)                                   
Session Status                online                                     
Session Expires               7 hours, 59 minutes                                     
Version                       2.3.35                                                   
Region                        United States (us)                                       
Web Interface                 http://127.0.0.1:4040                                   
Forwarding                    tcp://x.tcp.ngrok.io:XXXXX -> localhost:27017           
   
Connections                   ttl     opn     rt1     rt5     p50     p90             
                              0       0       0.00    0.00    0.00    0.00 
```

其中，`x.tcp.ngrok.io`是host，`XXXXX`就是 ngrok 的公网port。

连接到MongoDB

在代码单元格中输入以下代码以连接到MongoDB：

```python
from pymongo import MongoClient

# 您需要将`localhost:XXXXX`替换为您在上一步中看到的 ngrok 公网端口号
client = MongoClient('mongodb://x.tcp.ngrok.io:XXXXX/')

# 将`test`替换为您要连接的MongoDB数据库的名称
db = client.test

# 进行其他操作...
```

请注意，当您断开与Colab的连接时，ngrok端口也会关闭，因此您需要重新启动ngrok并将其连接到MongoDB。



