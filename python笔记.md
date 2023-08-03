## csv读写

#### 读取 CSV 文件

直接读取

打开名为 `file.csv` 的文件，并按行读取其中的数据。每行数据会被转换为一个列表，列表中的元素即为该行中的每个字段。

```python
import csv

with open('file.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)
```

 `csv.DictReader` 方法读取

将每行数据转换为一个字典。在这种情况下，第一行数据会被作为字典的键值：

```python
import csv

with open('file.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        print(row)
```

Pandas

读取名为 `file.csv` 的 CSV 文件，并将其转换为一个 DataFrame 对象

```python
import pandas as pd

df = pd.read_csv('file.csv')
print(df)
```

Numpy

读取名为 `file.csv` 的 CSV 文件，并将其转换为一个 Numpy 数组。我们指定了分隔符为逗号，并指定了该文件的第一行为数据的列名。

```python
import numpy as np

data = np.genfromtxt('file.csv', delimiter=',', names=True, dtype=None)
print(data)
```

#### 写入 CSV 文件

直接写入

创建名为 `file.csv` 的文件，并写入三行数据。在这个例子中，我们使用了 `csv.writer` 方法来写入 CSV 数据。首先，我们调用 `writerow` 方法写入了 CSV 文件的第一行数据，然后分别写入了两行数据。

```python
import csv

with open('file.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Name', 'Age', 'Gender'])
    csvwriter.writerow(['Alice', 25, 'F'])
    csvwriter.writerow(['Bob', 30, 'M'])
```

 `csv.DictWriter` 方法

在这种情况下，需要在调用 `writerow` 方法前先调用 `writeheader` 方法，以写入 CSV 文件的第一行数据：

```python
import csv

with open('file.csv', 'w') as csvfile:
    fieldnames = ['Name', 'Age', 'Gender']
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writeheader()
    csvwriter.writerow({'Name': 'Alice', 'Age': 25, 'Gender': 'F'})
    csvwriter.writerow({'Name': 'Bob', 'Age': 30, 'Gender': 'M'})
```

以上代码会创建名为 `file.csv` 的文件，并写入三行数据。在这个例子中，我们使用了 `csv.DictWriter` 方法来写入 CSV 数据。首先，我们调用 `writeheader` 方法写入了 CSV 文件的第一行数据，然后分别写入了两行数据。

Pandas

创建名为 `file.csv` 的文件，并将一个 DataFrame 对象的内容写入该文件。我们指定了 `index=False`，以避免写入索引列。使用 Pandas 也可以方便地将数据写入 CSV 文件。

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30],
    'Gender': ['F', 'M']
}
df = pd.DataFrame(data)
df.to_csv('file.csv', index=False)
```

Numpy

创建名为 `file.csv` 的文件，并将一个 Numpy 数组的内容写入该文件。我们指定了分隔符为逗号，并指定了每列数据的格式。

```python
import numpy as np

data = np.array([('Alice', 25, 'F'), ('Bob', 30, 'M')],
                dtype=[('Name', 'U10'), ('Age', 'i4'), ('Gender', 'U1')])
np.savetxt('file.csv', data, delimiter=',', fmt='%s')
```

## argparse

https://zhuanlan.zhihu.com/p/406211743 用法详解

```python
import argparse
parser = argparse.ArgumentParser(
    usage="how to use", prog='Name',
    description='Front description', epilog='Back description')
parser.add_argument('first')
parser.add_argument('second')
args = parser.parse_args()

print(args)
```

## pygithub

```python
from github import Github

g = Github(token) # using an access token

for repo in g.get_user().get_repos():
    print(repo.name)
    # to see all the available attributes and methods
    # print(dir(repo))
    print(repo.description)
    # repo.edit(description="rq")
```

## turtle库

引入

```python
>>>import turtle
>>>from turtle import 
```

控制画笔绘制状态

```python
pendown() | pd() | down()
penup() | pu() | up()
pensize(wid) | width(wid)
```

控制画笔颜色和字体

```python
color() 
reset()
begin_fill()
end_fill() 
filling()
clear() 
screensize()
showturtle() | st()
hideturtle() | ht()
isvisible() 
write(arg,move=False,align="left",font =("Arial",8,"normal") )
```

控制画笔运动

```python
forward(distance) | fd(distance)
backward(distance)| bk(distance)
|back(distance)
right(angle) | rt(angle)
left(angle) | lt(angle)
setheading(to_angle)
position() | pos()
goto(x,y)
setposition(x,y ) | setpos(x,y )
circle(radius,extent ,steps )
dot(size ,*color)
radians()
stamp()
speed(speed)
clearstamp(stamp_id)
clearstamps(n )
undo()
speed(speed)
heading()
towards(x,y)
distance(x,y)
xcor() ycor() 
setx(x) sety(y)
home()
undo()
degrees(fullcircle = 360.0)
```

TurtleScreen/Screen类的函数

```python
bgcolor(*args)
bgpic(picname )
clearscreen() 
resetscreen()
screensize(cwid ,canvh,bg )
tracer(n ,delay )
listen(xdummy ,ydummy )
onkey((fun,key) 
onkeyrelease((fun,key)
onkeypress(fun,key )
onscreenclick(fun,btn=1,add )
getcanvas() 
getshapes()
turtles()
window_height() 
window_width()
bye() 
exitonclick()
title(titlestring)
setup(wid=_CFG["wid"],h=_CFG["h"],startx=_CFG["leftright"],starty=_CFG["topbottom"])
```

