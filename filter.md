
# 大题
## 1. SQL Console
- 难度: 低
- 分值: 20
- 要求: 设计实现一个数据库控制的console, 能够进行增查删改,并进行自定义的功能扩展。
- 例子:
```
python sql_console.py
Welcome to sql console. Type `help` to get help.
>> list_tables()
name  | columns
t1    | id, username, password
qe    | attr1, attr2, attr3
...
>> t1 = get_table('t1')
Ok
>> t1.insert(username='abc', password='234')
Ok
>> t1.select(username='abc', password='234')
{"username":"abc", "password": "234"}
...
```
- 说明:
    * 鼓励设计出非Python式的console操作语法,但要有合理的语法规则,例如:
    ```
    get_table t1 as this, then this.insert{    // 捕获名为t1的表,在当前作用域名为this
        username != 'abc', 
        age>20
    }
    ```
    * 能够从解析至少一种格式的配置文件,例如:
    
    ```
    >> t1.insert_from_config("config.json")
    Ok
    ```  
    config.json 示例
    ```
    [{"username": "abc", "password":"233"},
     {"username": "bcd"}]

    ```
    * 允许使用任意第三方库。
    * 可能用到的标准库: `sys`, `argparse`.


## 2. LinkedList
- 难度: 低
- 分值: 10
- 要求: 设计实现一个具有链表性质的数据结构, 
    - 具有head和tail两种property, 其中,head获取链表的头部, tail获取链表第二个位置开始的引用。  
    注意: **head和tail应从原链表里获得部分元素的引用,这个过程没有新对象的建立**(在列表中,`a, *b = [1,2,3]`这个式子,其中的`b == [2, 3] => True`, 但`b`作为一个容纳数据的容器,其本身是新建的对象)。
    ```
    a = LinkedList(1, 2, 3, 4)
    a.head
    => 1
    a.tail
    => [2, 3, 4]
    ```
    - 具有一个合适的__iter__元方法,可以进行`for`操作。
    ```python
    for elem in LinkedList(1, 2, 3, 4):
        print (elem)
    => 
    1
    2
    3
    4
    ```
    - 具有一个合适的__eq__元方法,能够根据链表的元素,比较两个链表是否相同。
    - 具有append和appendLeft方法,可以在链表的头部和尾部添加元素。
    - 具有一个reverse方法进行转置。
- 提示: LinkedList可以基于一个`Node class`进行设计。
    ```python
    class Node:
        def __init__(self, v):
            self.value = v
            self.next: Node = None
        def __str__(self):
            return self.v.__str__()
        def __repr__(self):
            return self.__str__()

    ```

## 3. Debug
- 难度: 低
- 分值: 25
- 要求:   
实现一个debug logging程序。它可以对一个项目的文件进行一次预处理,之后,在运行这个项目时,函数对象和类方法对象的显式调用(`obj(*args, **kwargs)`的形式), **其名字,输入参数和返回值的类型和值**都会被记录到一个**确定位置的日志**里。  
**预处理不应该影响程序的结果**。  
假定项目有且只有一个执行入口(main)。

- 例:  
    项目文件(这里只举单个文件模块的例子,你需要处理以文件夹形式存在的项目):
    ```python
    # hw.py
    def another(x):
        return 2*x
    def hw(*input):
        return another(sum(input))  # 内置函数例如sum, 可以不记录。
    # main如下:
    if __name__ == '__main__':
        hw([1,2,3,4])
    ```
    使用命令`python debug_logging.py myproject/ logging.txt`后, 执行`myproject`的入口`hw.py`, 在`logging.txt`里有类似如下的结果:
    ```json
    {"name": "hw",
     "args":{"*input":"list =>  [1,2,3,4]",
             "then": "function => <function <lambda> at 0x7f259fd12e18>"
             },
     "return":"20"},

    {"name":"another",
     "args": {"x": "int => 10"},
     "return": "int => 20"}
    ```

## 4. Storage Server
- 难度: 中
- 分值: 35
- 要求: 设计实现一个服务器,可以通过命令行或者网站后台,远程上传、下载文件。
- 例子:
    ```
    python server_manager_cmd.py
    Welcome to server manager! Type `help` to get help.
    >> upload -f "myfile.py"  # upload a file to your server 
    Wait a minute...
    Ok
    >> upload -d "my_package/"  # zip a directiory and upload it.
    >> download "my_package" "my_local_directory/" # create a local directory and download some package into it.
    ```
- 知识补充: 
    * 数据传输的POST, GET等method.
    * 著名的python网络库 `requests` 可以很好的操作文件上传下载.
    * `zip, gzip`等库可以进行文件的压缩相关操作。
    * 如果想使用网站后台, 推荐使用`django`的admin后台。但不建议使用网站后台操作,会酌情扣分。


## 5. Web Design
- 难度: 中
- 分值: 45
- 要求: 不允许抄袭原版,仿造[这个网站](https://www.bilibili.com/)的首页。可以只实现滚动页面的最顶层部分, 不必支持滚屏。
- 注: 可以下载原网页的图片文件,但JS和CSS只能参考不能抄袭。



## 6. 刷题
- 难度: 中
- 分值: 
    - 注册自己的github账号: 5分 
    - 6kyu: 1分
    - 5kyu: 2分
    - 4kyu: 4分
    - 3kyu: 16分
    - 2kyu: 64分
    - 1kyu: 100分
- 说明:   
网址地址: [CodeWars](http://www.codewars.com/)。  
以上分值按题目计算，可以叠加。



## 7. 按键精灵
- 难度: 高
- 分值: 90
- 要求: 设计实现一个控制windows系统下鼠标键盘操作事件的系统。并使用它, 设计一个脚本, 在PC端对一个手游(使用模拟器)进行日常奖励的领取和简单关卡的通关。
- 参考资料: 
    - python win32com
    - pyhook



# 简单题

## 1. 正则表达式(**共19分**)
- 写出以`http`开头, 以`.com`结尾的正则pattern(**2分**)。
- 写出以`http`开头，以`.net`结束或以`https`开头的pattern(**2分**)。
- 写出以能从html文本中提取`<img>`标签的正则pattern(**3分**), 并写出得到其中的`src`属性的pattern(**2分**)。
- 写出匹配文本中所有数值的pattern。(正整数, 负整数, 任意小数, 任意浮点数, 前两者匹配各**1分**, 后两者各**2分**。)
- 写出验证是否为邮箱的pattern(**2分**)。
- 写出能找出所有在`QAQ`和`233`之间的字符串(贪婪模式)的pattern(**3分**)。
- 写出匹配结尾不是`666`的pattern(**2分**)。

## 2. 一个生成所有质数的stream(**共5分**)。
```python
def primes():
    while True:
        ...
        yield

for i, e in enumerate(primes()): // 打印 100 个质数
    print(e)
    if i > 100: break
```
请你实现primes(**3分**), 如果实现比最简单实现更高效的，加**2分**。


## 3. 组合和商集(**6分**)
在下面注释的的位置，用一句话进行补全，完善group_by函数。
```python
def forEach(seq):
    def traverse(f):
        for e in seq:
            f(e)
    return traverse

def setItem(con):
    def apply(e):
        con.append(e)
    return apply

from collections import defaultdict
def group_by(f, con):
    dic = defaultdict(list)
    # 补全这句话
    return dic
```
要求:   
使得group_by函数效果如下：
```python
group_by(lambda x:x%2, [1, 2, 3, 4])
=> 
defaultdict(list, {0: [2, 4], 1: [1, 3]})

group_by(type, [1, "2", 3.3, 4e-19, lambda x:x, ''])
=> 
defaultdict(list,
            {int: [1],
             str: ['2', ''],
             float: [3.3, 4e-19],
             function: [<function __main__.<lambda>>]})
```



