# python操作mongodb

版本：python3.8，mongodb3.9

参考：

https://blog.csdn.net/qq_42403866/article/details/104336537

https://blog.csdn.net/dinglin1237/article/details/102286004

### 连接数据库

```python
def connect_mongo(query={},host='localhost', port=27017, username=None, password=None, no_id=True):
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

#### 1.语法

```python
#查询所有数据
db.COLLECTION_NAME.find()
#查询指定某键值的数据，多个键时查询交集
db.COLLECTION_NAME.find({ key1: value1, key2: value2 })
#模糊查询，正则匹配
{"name":/^start/} #以 'start' 开头的匹配式
{"name":/tail$/} #以 'tail' 结尾的匹配式
#读取n个数据记录
db.COLLECTION_NAME.find().limit(10)
# 跳过前n个数据记录
db.COLLECTION_NAME.find().skip(3)
# 排序
db.COLLECTION_NAME.find().sort({KEY:1|-1}) # 1-升序，(-1)-降序
db.COLLECTION_NAME.find(sort=[(KEY,pymongo.ASCENDING)]) # ASCENDING-升 DESCENDING-降
db.COLLECTION_NAME.find().sort([(KEY,pymongo.ASCENDING)])
```

#### 2.条件查询

| 运算符      | 描述                                                     | 示例                                                         |
| ----------- | -------------------------------------------------------- | ------------------------------------------------------------ |
| field:value | 字段值=value                                             | { name : "myName" }                                          |
| $gt         | 大于                                                     | { size : { $gt : 5 } }                                       |
| $gte        | 大于等于                                                 | { size : { $gte : 5 } }                                      |
| $lt         | 小于                                                     | { size : { $lt : 5} }                                        |
| $lte        | 小于等于                                                 | { size : { $lte : 5 } }                                      |
| $ne         | 不等于                                                   | { name : {$ne : "badName"} }                                 |
| $in         | 包含于指定数组[]                                         | { like : { $in : [ "C","JAVA" ] } }                          |
| $nin        | 不包含于指定数组[]                                       | { name : { $nin : ["html","css"] } }                         |
| $or         | 逻辑或连接查询                                           | { $or : [ {size : {$lt : 5} }, {size : {$gt : 10} } ] }      |
| $and        | 逻辑与连接查询                                           | { $and : [ { size : { $gt : 5 } },{ size : { $lt : 10 } } ] } |
| $not        | 反转查询（不等于）                                       | { $not : { name : "myName" } }                               |
| $nor        | 逻辑或非连接查询，不等于任一个                           | { $nor : { size : { $gt : 5 } },{ size : { $lt : 0 } } }     |
| $exists     | true-包含指定字段，false-不包含该字段                    | { name : { $exists : true } }                                |
| $regex      | 匹配正则表达式                                           | { myString : { $regex : ' some.*exp ' } }                    |
| $all        | 指定数组包含所有指定元素                                 | { word : { $all : [ 'a','b','c' ] } }                        |
| $elemMatch  | 返回指定的数组字段至少有一个元素与指定的条件都匹配的文档 | { myArr : { $elemMatch : { { value : { $gt : 5 } },{ size : { $lt : 10 } } } } } |
| $size       | 指定数组的长度                                           | { myArr : { $size : 5 } }                                    |

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
