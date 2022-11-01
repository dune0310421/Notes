# bootstrap使用

TODO：需要看文档的

参考API https://v3.bootcss.com/css/

字体图标库 https://www.runoob.com/bootstrap/bootstrap-glyphicons.html

菜鸟教程 https://www.runoob.com/bootstrap/bootstrap-tutorial.html

## 1 安装

bootstrap官网 https://getbootstrap.com/

bootstrap中文网 https://www.bootcss.com/

一套现成的CSS样式集合，最受欢迎的html、css和js框架。

#### 1.1 特点

响应式布局(自适应设备尺寸)，移动设备优先。

12列网格，网页均分为12份自己决定用多少。

自定义jquery插件(使用时需要引入jquery)。

适合没有前端设计的团队。

#### 1.2 下载

1. 下载 https://v3.bootcss.com/getting-started/，其中

   * [用于生产环境的Bootstrap](https://github.com/twbs/bootstrap/releases/download/v3.4.1/bootstrap-3.4.1-dist.zip) -下载的东西少用于生产环境
   * [源码](https://github.com/twbs/bootstrap/archive/v3.4.1.zip) -下载的东西比较全

   下载完成后

   * 复制dist/css中的bootstrap.min.css到项目的css中
   * 复制dist/js中的bootstrap.min.js到项目的js中
   * dist/fonts为字体样式

   或者直接复制整个dist文件夹到项目中改名为bootstrap，因为可能有其他样式，比如类ui

   或者不想下载的话，可使用在线样式链接(在同一个下载页面有)，此时要求网络良好。

2. 下载jquery.js https://jquery.com/ 

#### 1.3 模板

在html中的模板

```html
<!DocTYPE html>
<htm1 lang ="en">
    <head>
        <meta charset ="utf-8">
		<!--使用 X-UA-compatible来设置IE浏览器兼容模式最新的渲染模式
			只有低版本IE不兼容，其他浏览器一般不存在此问题-->
        <meta http-equiv="x-UA-compatib1e" content="IE=edge">
		<!--viewport 表示用户是否可以缩放页面
			width 指定视区的逻辑宽度
			device-width 指示视区宽度应为设备的屏幕宽度
			initial-scale 设置web页面的初始缩放比例，==1时显示末经缩放的Web文档
		-->
		<meta name="viewport" content="width=device-width, initia1-scale=1">
        <title>Bootstrap的НTML标准模板</title>
		<!--载入Bootstrap的css-->
		<link href="css/bootstrap.min.css" rel="sty1esheet">
    </head>
    
	<body>
        <h1>Hello, world!</h1>
    </body >
    
    <!--如果要使用Bootstrap的js插件，必须先调入jQuery-->
    <script src="js/jquery-3.4.1.js"></script>
    <!--包括所有bootstrap的js插件或者可以根据需要使用的js插件调用-->
    <script src="js/bootstrap.min.js"></script>
    
</htm1>
```

说明：

* viewport <meta>标记用于指定用户是否可以缩放 Web 页面
* width 和 height 指令分别指定视区的逻辑宽度和高度。他们的值为以像素为单位的数字或一个特殊的标记符号。
  * width 指令使用 device-width 标记可以指示视区宽度应为设备的屏幕宽度
  * height 指令使用 device-height 标记指示视区高度为设备的屏幕高度
* initial-scale 指令用于设置 Web 页面的初始缩放比例。默认的初始缩放比例值因智能手机浏览器的不同而有所差异。通常情况下设备会在浏览器中呈现出整个 Web 页面，设为1.0则将显示未经缩放的 Web 文档。

## 2 布局容器

共两种。不兼容，不能相互嵌套，可以但不建议两种一起用。

#### 固定宽度

两侧有留白效果。大部分网站都如此，视觉效果好。

```html
<div class="container">
  	.container类用于固定宽度并支持响应式布局的容器
</div>
```

#### 全部宽度

占据全部视口

```html
<div class="container-fluid">
	.contain-fluid类用于100%宽度，占据全部视口(viewport)的容器
</div>
```

## 3 栅格网格系统

Bootstrap 提供了一套响应式、移动设备优先的流式栅格系统，随着屏幕或视口(viewport)尺寸的增加，系统会自动分为最多12列。栅格系统用于通过一系列的行(row)与列(column)的组合来创建页面布局，内容放入这些创建好的布局中。
网格系统实现原理：定义容器大小，平分12份(最常见，也有平分成24份或32份)，再调整内外边距，最后结合媒体查询，就制作出了强大的响应式网格系统。 Bootstrap 框架中的网格系统就是将容器平分成12份。

TODO：css文档列对齐那里有很多实例

### 3.1 概述

#### 3.1.1元素

* container 容器，所有item都是在container内

* row 行，必须在容器内。

* 列，有xs(超小屏，自动)，ms(小屏，750px)，md(中屏，常用，970px)，lg(大屏，1170px)。

  格式为`col-屏幕大小-占几格`。一行中超过12格就不在一行了，自动换行。

```html
<div class="container">
    <div class="row"> <!--行-->
        <div class="col-md-4" style="background-color: #9acfea">占4格</div> <!--列-->
        <div class="col-md-8" style="background-color: #e4b9c0">占8格</div>
    </div>
</div>
```

#### 3.1.2 媒体查询

自动查询屏幕大小。在类中可以同时写多种列样式

```html
<div class="col-md-4 col-ms-6">zgq</div> <!--列-->
```

则先自动查询屏幕，再选择占几列，如果此时为中等屏幕则占4列，如果为小屏幕则占6列。

#### 3.1.3 栅格参数

通过下表可以详细查看 Bootstrap 的栅格系统是如何在多种屏幕设备上工作的。

|                       | 超小屏幕 手机 (<768px) | 小屏幕 平板 (≥768px)                                | 中等屏幕 桌面显示器 (≥992px) | 大屏幕 大桌面显示器 (≥1200px) |
| :-------------------- | :--------------------- | :-------------------------------------------------- | :--------------------------- | :---------------------------- |
| 栅格系统行为          | 总是水平排列           | 开始是堆叠在一起的，当大于这些阈值时将变为水平排列C | 同                           | 同                            |
| `.container` 最大宽度 | None (自动)            | 750px                                               | 970px                        | 1170px                        |
| 类前缀                | `.col-xs-`             | `.col-sm-`                                          | `.col-md-`                   | `.col-lg-`                    |
| 最大列(column)宽      | 自动                   | ~62px                                               | ~81px                        | ~97px                         |

槽(gutter)宽：30px(每列左右均有15px)。均可嵌套、可偏移，均满足列排序 。

### 3.2 列组合

`.col-屏幕大小-占几格`

div本来是块级元素，独占一行，(img等元素可以一行多个)两个div在同一行需要用浮动(float)实现，但栅格网格系统自动处理好了格数。

转评：改变viewport大小的时候在同一行的div也可能重新布局自动换行，全屏看时正常。

### 3.3 列偏移

.`col-屏幕大小-offset-偏移几格`

前一列偏移，后一列跟着偏移。需要保证偏移+格子数量<=12。

```html
<div class="row"> <!--行-->
    <div class="col-md-2" style="background-color: #f8efc0">占2格</div> <!--列-->
    <div class="col-md-2 col-md-offset-3" style="background-color: #f0ad4e">偏移3格，占2格</div>
</div>
```

### 3.4 列排序

`.col-屏幕大小-push-浮动几格`和`.col-屏幕大小-pull-浮动几格`

左右浮动，只浮动一个列，往前(左)pull，往后(右)push。有遮挡关系时，后面的列会覆盖前面的列。

```html
<div class="row"> <!--排序前-->
    <div class="col-md-1" style="background-color: #dff0d8">占1格</div>
    <div class="col-md-2" style="background-color: #f8efc0">占2格</div>
    <div class="col-md-4" style="background-color: #985f0d">占4格</div>
    <div class="col-md-2" style="background-color: #ebccd1">占2格</div>
</div>
<div class="row"> <!--排序后-->
    <div class="col-md-1" style="background-color: #dff0d8">占1格</div>
    <div class="col-md-2 col-md-push-1" style="background-color: #f8efc0">后移1格，占2格</div>
    <div class="col-md-4" style="background-color: #985f0d">占4格</div>
    <div class="col-md-2 col-md-pull-1" style="background-color: #ebccd1">前移1格，占2格</div>
</div>
```

### 3.5 列嵌套

在一个列中添加一个或多个row，在该row中插入列。即，每一列可以再被均分为12列，无限嵌套。

```html
<div class="row"> <!--行-->
    <div class="col-md-6" style="background-color: #dff0d8"> <!--列-->
        <div class="row"> <!--嵌套的行-->
            <div class="col-md-1" style="background-color: #e4b9b9">嵌套1格</div>
            <div class="col-md-2" style="background-color: #f8efc0">嵌套2格</div>
            <!--此时的2格代表嵌套行的2/12，即此时只占实际屏幕的一格-->
        </div>
    </div>
</div>
```

## 4 常用样式

bootstrap将很多style样式统一成class，可以直接在class中加，十分方便。

### 4.1 排版

TODO：对齐后列表前还需要看css文档

#### 4.1.1 标题

bootstrap对`<h1>`到`<h6>`标题效果进行了覆盖。

此外提供了 `.h1` 到 `.h6` 类，给内联(inline)属性的文本赋予标题的样式。副标题`.small`。

```html
<h1>标题1<small>副标题</small></h1>
<div class="h2">标题2<small>副标题2</small></div>
<div class="h3">标题3<span class="small">副标题3</span></div>
```

#### 4.1.2 段落

 `.lead` 类：让段落突出显示，增大字号、调整行高和margin。

`<small>`小字号，`<b>`、`<strong>`加粗，`<i>`、`<em>`斜体，`<del>`、`<s>`删除线，`<u>`、`<ins>`下划线。

#### 4.1.3 强调

用颜色表示强调，当然也可以不用这个。

```html
<div class="text-muted">提示，浅灰色(#999)</div>
<div class="text-primary">主要，蓝色(#428bca)</div>
<div class="text-success">成功，浅绿(#3c763d)</div>
<div class="text-info">通知信息，浅蓝(331708f)</div>
<div class="text-warning">警告，黄色(#8a6d3b)</div>
<div class="text-danger">危险，褐色(#a94443)</div>
```

#### 4.1.4 对齐

CSS中常用text-align实现对齐，但是bootstrap将它们统一成class。

```html
<p style="text-align: right">正常的右对齐效果</p>

<p class="text-left">左对齐</p>
<p class="text-center">居中</p>
<p class="text-right">右对齐</p>
<p class="text-justify">两端对齐</p>
<p class="text-nowrap">无换行文本(?)</p>
```

#### 4.1.5 列表

列表共有3种类型

* 无序列表`<ul><li>...</li></ul>`
* 有序列表`<ol><li>...</li></ol>`
* 自定义列表`<dl><dt>...</dt><dd>...</dd></dl>`

##### 去点列表

`.list-unstyled`

```html
<ul class="list-unstyled">
    <li>去点列表项目1</li>
    <li>去点列表项目2</li>
</ul>
```

##### 内联列表

`.list-inline`

将竖直列表换成水平列表，添加少量的内补(padding)，将所有元素放置于同一行，去掉项目符号。

可用于制作导航栏。

```html
<ol class="list-inline">
    <li>内联列表项目1</li>
    <li>内联列表项目2</li>
</ol>
```

##### 水平排列的自定义列表

`.dl-horizontal`

当标题宽度超过160px时，将会显示三个省略号(自动截断)。

```html
<dl class="dl-horizontal">
    <dt>html</dt>
    <dd>超文本标记语言</dd>
    <dt>当标题宽度超过160px时，将会显示三个省略号</dt>
    <dd>如标题所示</dd>
</dl>
```

#### 4.1.6 代码

##### 单行内联代码
`<code></code>`

```html
<code>
    int i = 0;<br> <!--注意单行代码不识别回车，这里用br换行-->
    i++;
</code>
```

##### 用户键入效果

`<kbd></kbd>`

表示用户需要自己键入的东西。

```html
<p>使用<kbd>ctrl</kbd>+<kbd>s</kbd>保存内容</p>
```

##### 多行代码块

`<pre></pre>`

代码会保留原本格式，包括空格和回车。所以代码前不留空格保持样式好看。

```html
<pre>
int i = 0;
i++;
</pre>
```

显示html代码时，需要将尖括号做转义处理，即使用字符实体。

```html
<pre>&lt;p&gt;内容&lt;/p&gt;</pre>
```

##### 滚动条

 `.pre-scrollable` 

设置 max-height 为 350px ，并在垂直方向展示滚动条。

```html
<pre class="pre-scrollable">
很长的代码
</pre>
```

##### 变量

`<var></var>`

不自成一个段落。

```html
<var>y</var> = <var>m</var><var>x</var> + <var>b</var>
```

##### 程序输出

`<samp></samp>`

不自成一个段落。

```html
<samp>exit with code 0...</samp>
```

#### 4.1.7 表格

1种基本样式+4种附加样式+响应式表格设计。

##### 样式

基础样式：`.table`，必须添加

附加样式：

1. 条纹状表格：`.table-striped`
2. 带边框的表格：`.table-bordered`
3. 鼠标悬停高亮 ：`.table-hover`
4. 紧缩表格 ：` .table-condensed`，表格更加紧凑

状态类：为行或单元格设置颜色。

| Class      | 描述                                 |
| :--------- | :----------------------------------- |
| `.active`  | 鼠标悬停在行或单元格上时所设置的颜色 |
| `.success` | 标识成功或积极的动作                 |
| `.info`    | 标识普通的提示信息或动作             |
| `.warning` | 标识警告或需要用户注意               |
| `.danger`  | 标识危险或潜在的带来负面影响的动作   |

```html
<table class="table table-bordered table-hover">
    <tr class="active">
        <th>标题1</th>
        <th>标题2</th>
        <th>标题3</th>
    </tr>
    <tr class="danger">
        <td>内容11</td>
        <td>内容12</td>
        <td>内容13</td>
    </tr>
    <tr class="success">
        <td>内容21</td>
        <td>内容22</td>
        <td>内容23</td>
    </tr>
</table>
```

##### 响应式表格

将任何 `.table` 元素包裹在 `.table-responsive` 元素内，即可创建响应式表格。

会在小屏幕设备(小于768px)水平滚动。当屏幕大于 768px 宽度时，无水平滚动条。

```html
<div class="table-responsive">
    <table class="table">
        ...
    </table>
</div>
```

### 4.2 表单

TODO：看css网页，按钮之前有很多例子

表单是与用户做交流的网页控件，前台和后台的交互。

#### 4.2.1 表单控件

样式：`.from-control`样式，定义表单元素。可以结合栅格网格系统制作，不然会占一整行。

大小：`.input-lg`(较大)、`.input-sm`(较小)，用于设置高度。宽度用col来设置。

##### 输入框text

包裹在`.form-group`中效果更好(增大与其他控件的间距)

```html
<div class="row">
    <div class="col-md-3">
        <div class="form-group">
            <label for="id1">输入框1</label>
            <input type="text" class="form-control" id="id1" placeholder="请输入"/><br>
        </div>
        <input type="text" class="form-control input-lg"/><br>
        <input type="text" class="form-control input-sm"/><br>
    </div>
</div>
```

##### 下拉选择框select

多行选择设置 multiple="multiple"，按住<kbd>ctrl</kbd>即可多选。

```html
<div class="row">
    <div class="col-md-2">
        <select class="form-control">
            <option>请选择城市</option>
            <option>北京</option>
            <option>上海</option>
        </select> <br>
    </div>
    <div class="col-md-2">
        <select class="form-control" multiple="multiple">
            <option>请选择城市</option>
            <option>北京</option>
            <option>上海</option>
            <option>成都</option>
            <option>松原</option>
        </select> <br>
    </div>
</div>
```

##### 文本域textarea

```html
<div class="row">
    <div class="col-md-4">
        <textarea class="form-control">
        </textarea> <br>
    </div>
</div>
```

##### 单选框和复选框

单选框`<radio>`，复选框`<checkbox>`

分为两种：竖直显示和水平显示

竖直显示：在`<div>`中设置class为`.radio`或`.checkbox`。

例子中将`<input>`标签放在`<label>`中可以绑定文字和复选框。

```html
<div class="row">
    <div class="col-md-2">
        <div class="checkbox">
            <label><input type="checkbox" name="hobby"/>唱歌</label>
        </div>
        <div class="checkbox">
            <label><input type="checkbox" name="hobby"/>跳舞</label>
        </div>
    </div>
</div>
```
水平显示：需要在label中设置class为`.radio-inline`或`.checkbox-inline`。由于水平显示，所以不要div。
```html
<div class="row">
    <div class="col-md-2">
        <label class="radio-inline"><input type="radio" name="sex"/>男</label>
        <label class="radio-inline"><input type="radio" name="sex"/>女</label>
    </div>
</div>
```

注意，不带label文本的checkbox 和 radio目前只适用于非内联的 checkbox 和 radio。

##### 按钮

基础样式：`.btn`

附加样式(bootstrap预定义好的颜色)：7种

```html
<button class="btn">基础按钮</button>
<button class="btn btn-default">(默认样式)Default</button>
<button class="btn btn-primary">(首选项)Primary</button>
<button class="btn btn-success">(成功)Success</button>
<button class="btn btn-info">(一般信息)Info</button>
<button class="btn btn-warning">(警告)Warning</button>
<button class="btn btn-danger">(危险)Danger</button>
<button class="btn btn-link">(链接)Link</button>
```

多标签使用，将其他标签设置为按钮样式：在class中添加`.btn`即可。

```html
<!--通过按钮样式设置其他元素为按钮效果-->
<a href="#" class="btn btn-danger">a标签</a>
<span class="btn btn-primary">span标签</span>
<div class="btn btn-info">div标签</div><br>
```

按钮大小：1默认+3扩展

```html
<!--设置按钮大小-->
<button class="btn btn-default">默认</button>
<button class="btn btn-primary btn-lg">大</button>
<button class="btn btn-success btn-ms">小</button>
<button class="btn btn-info btn-xs">超小</button><br>
```

class中添加 `.btn-block` 类，可将其拉伸至父元素100%的宽度，而且按钮也变为了块级（block）元素。

```html
<button class="btn btn-primary btn-block">(块级元素)按钮</button>
<button class="btn btn-default btn-block">(块级元素)按钮</button>
```

禁用状态：两种禁用方式：禁用和样式禁用。

class中添加`.disabled`只是在hover时呈现禁用样式。这两种禁用可以一起用效果更好。

```html
<button class="btn" onclick="alert('hello');" disabled="disabled">禁用</button>
<button class="btn btn-primary disabled" onclick="alert('hello');">样式禁用</button><br>
```

激活状态：class中添加 `.btn-block` 类，呈现激活状态外观。

```html
<button class="btn active">保持激活状态样式</button>
```

##### 静态控件

为 `<p>`元素添加 `.form-control-static` 类，可以在表单中将一行纯文本和` <label>`元素放置于同一行。

```html
<form class="form-inline"> <!--内联布局form-inline后面会讲到-->
    <div class="form-group">
        <label class="sr-only">Email</label>
        <p class="form-control-static">email@example.com</p>
    </div>
    <div class="form-group">
        <label for="pwd" class="sr-only">Password</label>
        <input type="password" class="form-control" id="pwd" placeholder="Password">
    </div>
    <button type="submit" class="btn btn-default">提交</button>
</form>
```

##### 其他

帮助文本、校验状态、额外图标 https://v3.bootcss.com/css/?#forms-help-text

#### 4.2.2 表单布局

创建表单步骤：

* 向父`<form>`元素添加role="form"
* 将标签和控件放在一个带有`.form-group`类的`<div>`中，表示是表单的一组，以获取元素间的最佳间距。
* 将所有的文本元素`<input>`、`<textarea>`、`<select>`中添加`.form-control`类。

`.form-group`可以设置大小`.form-group-lg`等(同按钮大小设置)。

所有设置了 `.form-control` 类的 `<input>`、`<textarea> `和`<select>`元素都将被默认设置宽度属性为 width: 100%，因此配合`<label>`和栅格网格系统达到最佳视觉效果。注意，在`<input>`中，type是必需的。

##### 水平表单

为表单添加`.form-horizontal`类，配合栅格网格系统，可以将 `label` 标签和控件组水平并排布局。

这样做将改变 `.form-group` 的行为，使其表现为栅格系统中的行(row)，因此就无需再额外添加 `.row` 了。

```html
<form action="#" class="form-horizontal" role="form">
    <!--表单中的表单元素组-->
    <!--表单标题-->
    <h2 class="text-center">用户信息</h2>
    <!--姓名-->
    <div class="form-group">
        <label for="uname" class="control-label col-md-2 col-md-offset-1">姓名</label>
        <div class="col-md-6">
            <input type="text" id="uname" class="form-control" placeholder="输入姓名"/>
            <!--注意，在<input>中，type是必需的。-->
        </div>
    </div>
	<!--性别-->
    <div class="form-group">
        <label class="control-label col-md-2 col-md-offset-1">性别</label>
        <div class="col-md-2">
            <label class="radio-inline"><input type="radio" name="sex"/>男</label>
            <label class="radio-inline"><input type="radio" name="sex"/>女</label>
        </div>
    </div>
	<!--城市-->
    <div class="form-group">
        <label for="city" class="control-label col-md-2 col-md-offset-1">城市</label>
        <div class="col-md-2">
            <select id="city" class="form-control">
                <option>请选择城市</option>
                <option>北京</option>
                <option>上海</option>
            </select>
        </div>
    </div>
    <!--提交按钮-->
    <div class="form-group text-center">
        <button class="btn btn-primary">提交</button>
    </div>
</form>
```



##### 内联表单

为表单添加 `.form-inline` 类，可使内容左对齐并且表现为inline-block级别的控件，因此表单所有控件都在同一行显示。只适用于视口（viewport）至少在 768px 宽度时（视口宽度再小的话就会使表单折叠）。

注意，可能需要手动设置宽度；一定要为每个输入控件设置` <label>`标签，即使通过为 `<label>`设置 `.sr-only` 类进行隐藏。

内联表单中无需设置格子(col)，因为所有元素都在同一行，设置格子没有意义。

```html
<form class="form-inline">
    <div class="form-group">
        <label for="uname1">姓名</label>
        <input type="text" id="uname1" class="form-control" placeholder="请输入姓名"/>
    </div>
    <div class="form-group">
        <label class="control-label">性别</label>
        <label class="radio-inline"><input type="radio" name="sex"/>男</label>
        <label class="radio-inline"><input type="radio" name="sex"/>女</label>
    </div>
    <div class="form-group">
        <button class="btn btn-primary">提交</button>
    </div>
</form>
```

### 4.3 缩略图

最常用的地方：商品列表。

常与栅格网格系统、标题、文本、按钮等搭配使用。

```html
<div class="row">
    <!--每个缩略图用一个栅格col装起来-->
    <div class="col-md-3">
        <div class="thumbnail">
            <img src="img/豆豆眼权1.jpg" alt="...">
            <h3>朱广权</h3>
            <p>中央广播电视总台新闻频道主播。</p>
            <button class="btn btn-danger">
                <span class="glyphicon glyphicon-heart"></span> 喜欢
                <!--上面class里是bootstrap自带的图标，直接放在一个span里即可。-->
            </button>
            <button class="btn btn-warning">
                <span class="glyphicon glyphicon-star-empty"></span> 收藏
            </button>
        </div>
    </div>
</div>
```

### 4.4 面板

头+内容。

默认的`.panel`组件锁之后的知识设置基本的边框(border)和(padding)来包含内容。

`.panel-default`：默认样式

`.panel-heading`：面板头

`.panel-body`：面板主体内容

```html
<div class="panel panel-info"> <!--panel-info是颜色-->
    <div class="panel-heading">
        .....
    </div>
    <div class="panel-body">
        .....
    </div>
</div>
```

## 5 bootstrap插件

### 5.1 导航

使用下拉菜单与按钮组合。

基本样式：`.nav`与"nav-tabs"、"nav-pills"组合制作导航。

#### 分类

* 标签型(nav-tabs)导航

  ```html
  <p>标签式的导航菜单</p>
  <ul class="nav nav-tabs">
      <li class="active"><a href="#">Home</a></li>
      <li><a href="#">SVN</a></li>
      <li><a href="#">iOS</a></li>
      <li><a href="#">VB.Net</a></li>
      <li><a href="#">Java</a></li>
      <li><a href="#">PHP</a></li>
  </ul>
  ```

* 胶囊形(nav-pills)导航

  ```html
  <p>基本的胶囊式导航菜单</p>
  <ul class="nav nav-pills">
      <li class="active"><a href="#">Home</a></li>
      <li><a href="#">SVN</a></li>
      <li><a href="#">iOS</a></li>
      <li><a href="#">VB.Net</a></li>
      <li><a href="#">Java</a></li>
      <li><a href="#">PHP</a></li>
  </ul>
  ```

* 堆栈(nav-stacked)导航，即垂直导航栏。可以与其他样式结合使用。

  ```html
  <ul class="nav nav-pills nav-stacked">
  ```

* 自适应(nav-justified)导航，即两端对齐。

* 面包屑式(breadcrumb)导航，单独使用样式，不与nav一起使用，直接加入到ol、ul中即可，一般用于导航，主要是起的作用是告诉用户现在所处页面的位置(当前位置)

  ```html
  <ul class="breadcrumb">
      <li><a href="#">Home</a></li>
      <li><a href="#">2013</a></li>
      <li class="active">十一月</li>
  </ul>
  ```

#### 状态

* 选中状态：active样式

* 禁用状态：disabled

  ```html
  <li class="disabled"><a href="#">禁用的item</a></li>
  ```

### 5.2 分页导航

分页导航：`.pagination`

```html
<ul class="pagination">
    <li><a href="#">&laquo;</a></li>
    <li><a href="#" class="active">1</a></li>
    <li><a href="#">2</a></li>
    <li><a href="#">3</a></li>
    <li><a href="#">4</a></li>
    <li><a href="#">5</a></li>
    <li><a href="#">&raquo;</a></li>
</ul>
```

翻页导航：`pager`

```html
<ul class="pager">
    <li><a href="#">Previous</a></li>
    <li><a href="#">Next</a></li>
</ul>
```

### 5.3 下拉菜单

实现下拉菜单需要使用js

```html
<!--引入jquery核心js文件，需要在bootstrap的js之前引入-->
<script src="js/jquery-3.6.1.js" type="text/javascript" charset="UTF-8"></script>
<!--引入bootstrap的js文件-->
<script src="bootstrap/js/bootstrap.min.js" type="text/javascript" charset="UTF-8"></script>
```

步骤:

使用一个类名为dropdown或btn-group的div包裹整个下拉框。默认向下dropdown，向上弹起加入为`.dropup`。

```html
<div class="dropdown">
	...
</div>
```

使用button作为父菜单，使用类名`.dropdown-toggle`和自定义`data-toggle`属性

```html
<button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
	按钮
    <span class="caret"></span> 
</button>
```

下拉菜单项使用一个ul列表，并且定义一个类名为`.dropdown-menu`

* 分组分割线：`<li>`加类名`.divider`

* 分组标题：`<li>`加类名`.dropdown-header`

* 对齐方式：`.dropdown-menu-left`左对齐默认样式`.dropdown-menu-right`右对齐

* 激活状态`.active`和禁用状态`.disabled`

```html
<ul class="dropdown-menu">
    <!--分组标题：<li>加类名.dropdown-header-->
    <li class="dropdown-header">--CCTV1--</li>
    <li><a href="#" target="_blank">撒贝宁</a></li>
    <li class="divider"></li><!--分组分割线：<li>加类名.divider-->
    <li class="dropdown-header">--CCTV13--</li>
    <li class="active"><a href="#" target="_blank">朱广权</a></li>
    <li><a href="#" target="_blank">李文静</a></li>
</ul>
```

### 5.4 模态框

模态框（Modal）是覆盖在父窗体上的子窗体。通常，目的是显示来自一个单独的源的内容，可以在不离开父窗体的情况下有一些互动。子窗体可提供信息、交互等。

#### 两种用法

- 通过 data 属性

  在控制器元素（按钮or链接）上设置属性 data-toggle="modal"，同时设置 data-target="#id" 或 href="#id" 来指定要切换的 id="id"的模态框。

  ```html
  <!-- 按钮触发模态框 -->
  <button class="btn" data-toggle="modal" data-target="#myModal">打开模态框</button>
  ```

- 通过 JavaScript

  通过为按钮绑定JavaScript事件来调用带有 id="myModal" 的模态框。
  
  ```html
  <button class="btn btn-default" id="btn">打开模态框</button>
  ...
  <script>
      // 绑定按钮的点击事件
      $('#btn').click(function(){
          $('#myModal').modal('show'); // 打开模态框
      })
      $('#submit_btn').click(function() {
          $('#myModal').modal('hide'); // 关闭模态框
      })
  </script>
  ```

#### 模态框模板

```html
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header"> <!-- 模态框标题 -->
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                <h4 class="modal-title" id="myModalLabel">模态框标题</h4>
            </div>
            <div class="modal-body"> <!-- 模态框主体内容 -->
            	这里可以是文本、表单...
            </div>
            <div class="modal-footer"> <!-- 模态框底部样式 -->
                <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                <button type="button" class="btn btn-primary">提交</button>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal -->
</div>
```

