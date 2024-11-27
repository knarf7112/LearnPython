# 元組(Tuple)

**元組**與**串列**最大差異是`元素值`與`元素個數`是**不可變**，又稱**不可變的串列**。

## 基本

串列的定義是將元素放在中括號內，**元組(tuple)**則是將**元素**放在 **小括號"()"** 內。

```python
myTuple = (元素1, 元素2, ..., 元素n,)  # myTuple是元組變數名稱
# 元素可以是 整數、字串、串列...等等
```

範例:

```python
>>> t0 = 1, 2, 3                         # 簡便建立元組的方式
>>> t1 = (1, 2, 3)
>>> t2 = ('a', 'b', 'c')
>>> t3 = (1,)
>>> t3[0] = 9                            # 變更元素值會產生錯誤
Traceback (most recent call last):
  File "<python-input-48>", line 1, in <module>
    t3[0] = 9
    ~~^^^
TypeError: 'tuple' object does not support item assignment

>>> t0 = (1,2,[1,2])
>>> t0
(1, 2, [1, 2])
>>> t0[2][0] = 3                         # 但變更元組內的串列內的元素值就不會產生錯誤，元組僅第一層不可變
>>> t0
(1, 2, [3, 2])
```

## 遍歷元組

可用for迴圈，方式與串列相同。

```python
>>> t0 = ('a', 'b', 'c')
>>> for n in t0:
...     print(n)
... 
a
b
c
```

## 元組切片

元組切片與串列相同。

```python
>>> t1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
>>> t1[2:]
('c', 'd', 'e', 'f', 'g')
>>> t1[:2]
('a', 'b')
>>> t1[::-1]
('g', 'f', 'e', 'd', 'c', 'b', 'a')
```

## 方法與函數

原本在**串列**上使用的**方法**或**函數**如果不會更改元組內容的就可以使用，例: `len()`、`index()`、`count()`。  
如果會更改內容的則無法使用，例: `append()`、`insert()`、`pop()`。

```python
>>> t1 = (1, 2, 3, 4, 5, 6)
>>> dir(t1)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> t1.index(5)  # 值為5的索引位置是4
4
>>> t1.count(5)  # 值為5的個數有1個
1
>>> len(t1)      # t1的元素有6個
6
```

## 串列與元組的資料格式交換

當需要將**元組**或**其他資料型態**轉成**串列**，使用 `list(data)` 函數，將 `data`傳入後，返回轉換後的**串列**資料。  

```python
>>> list()                                                       # 不帶任何參數，則轉換空串列
[]
>>> list('hello')                                                # 字串轉串列
['h', 'e', 'l', 'l', 'o']
>>> list(['a', 'b', 'c'])                                        # 串列轉串列
['a', 'b', 'c']
>>> list(('a', 'b', 'c'))                                        # 元組轉串列
['a', 'b', 'c']
>>> list({ 'data1', 'data2', 'data3' })                          # 集合轉串列，順序不固定
['data2', 'data3', 'data1']
>>> list({ 'key1': 'val1', 'key2': 'val2', 'key3': 'val3' })     # 字典轉串列，會返回字典的鍵（keys）作為串列
['key1', 'key2', 'key3']
>>> def gen1():                                                  # Python中的任何可迭代物件（如生成器、其他串列等）都可以使用list()函數來轉換
...     yield from range(3)
>>> list(gen1())
[0, 1, 2]
>>> t1 = ['aa', 'bb', 'cc']
>>> enum_t1 = enumerate(t1)
>>> t2 = list(enum_t1)                                           # enumerate物件轉成串列，但經過enumerate後的元素會被轉成元組(tuple)
>>> t2
[(0, 'aa'), (1, 'bb'), (2, 'cc')]
>>> type(t2[0])
<class 'tuple'>
```

當需要將**串列**或**其他資料型態**轉成**元組**，使用 `tuple(data)` 函數，將 `data`傳入後，返回轉換後的**元組**資料。

```python
>>> tuple()                                                       # 不帶任何參數，則轉換空元組
()
>>> tuple('hello')                                                # 字串轉元組
('h', 'e', 'l', 'l', 'o')
>>> tuple(['a', 'b', 'c'])                                        # 串列轉元組
('a', 'b', 'c')
>>> tuple(('a', 'b', 'c'))                                        # 元組轉元組
('a', 'b', 'c')
>>> tuple({ 'data1', 'data2', 'data3' })                          # 集合轉元組，順序不固定
('data2', 'data3', 'data1')
>>> tuple({ 'key1': 'val1', 'key2': 'val2', 'key3': 'val3' })     # 字典轉元組，會返回字典的鍵（keys）作為元組
('key1', 'key2', 'key3')
>>> def gen2():                                                  # Python中的任何可迭代物件（如生成器、其他串列等）都可以使用tuple()函數來轉換
...     yield from range(4)
>>> tuple(gen2())
(0, 1, 2, 3)
```

## 取得元組內最大值與最小值

當需要從元組內取得**最大值**，可使用 `max(tup)` 函數來獲取元組內的**最大值**，使用 `min(tup)` 函數來獲取元組內的**最小值**。

```python
>>> max((3, 1, 2, 5, 4))
5
>>> min((3, 1, 2, 5, 4))
1
```

## `zip()`打包多個物件

可用 `zip()` 函數將多個物件打包成**zip物件**，傳入的參數主要是2個或以上的可迭代物件，若可迭代物件的長度不同，會以最少的為基準。  

如果在 `zip()` 內的參數前面加上 `*` 表示要做解壓縮 `unzip()` 的行為。

```python
>>> fields = ['Name', 'Age', '測試', '這筆不會進zip']
>>> info = ('PPP', 'AAA', '哈哈')
>>> zipData = zip(fields, info)                        # 將可迭代的物件zip成一個物件
>>> zipData
<zip object at 0x0000023051618040>
>>> type(zipData)
<class 'zip'>
>>> mergeData = list(zipData)                          # 將zip物件轉換成串列，裡面元素為tuple    
[('Name', 'PPP'), ('Age', 'AAA'), ('測試', '哈哈')]
>>> f, i = zip(*mergeData)                             # 將合併的數據拆回去
>>> f
('Name', 'Age', '測試')
>>> i
('PPP', 'AAA', '哈哈')
>>> ###################################################
>>> x1 = (1,2,3)
>>> x2 = (4,5,6,7)
>>> x3 = (7,8,9,10,11)
>>> zipX = zip(x3, x2, x1)
>>> list(zipX)
[(7, 4, 1), (8, 5, 2), (9, 6, 3)]
>>> y3,y2,y1 = zip(*list(zipX))                       # 解壓縮只有一次，做完後zipX裡面的資料就清空了   
>>> y3
(7, 8, 9)
>>> y2
(4, 5, 6)
>>> y1
(1, 2, 3)
>>> y3,y2,y1 = zip(*list(zipX))
Traceback (most recent call last):
  File "<python-input-165>", line 1, in <module>
    y3,y2,y1 = zip(*list(zipX))
    ^^^^^^^^
ValueError: not enough values to unpack (expected 3, got 0)
```

## 生成式(generator)

生成式與串列生成式類似，差異只是*中括號* `[]` 換成*小括號* `()`，生成式可用`list()`將此生成式轉成串列或用`tuple()`將此生成式轉成元組，  
但`只能使用一次`，因為生成式不會記住所擁有的內容，如果要使用第二次將會得到空串列。

生成式語法如下:

```python
num = (n for n in iterable_object)
```

範例如下:

```python
>>> ###################範例1#######################################
>>> x = (n for n in range(3))
>>> x
<generator object <genexpr> at 0x00000230511F1F00>
>>> type(x)
<class 'generator'>
>>> for n in x: print(f'n={n}')     # 用迭代輸出，執行第一次列舉裡面的元素
... 
n=0
n=1
n=2
>>> for n in x: print(f'n={n}')     # 再執行一次，返回空的
... 
>>> ###################範例2#######################################
>>> x2 = (n for n in range(3))
>>> xlst = list(x2)                 # 將生成式轉成串列
>>> xlst
[0, 1, 2]
>>> xtup = tuple(x2)                # 再將生成式轉成元組，但結果元組為空的
>>> xtup
()
>>> ###################範例3#######################################
>>> x3 = (n for n in range(3))
>>> xtup = tuple(x3)                # 將生成式轉成元組
>>> xtup
(0, 1, 2)
>>> xlst = list(x3)                 # 再將生成式轉成串列，但結果串列為空的
>>> xlst
[]
```

## 元組的功能

元組資料結構上比串列簡單，故占用較少的系統資源，且能保護資料不被更動。

## bytes 與 bytearray 資料格式

這兩種均是二進位的資料格式，使用8位元儲存整數序列。
bytes資料格式是內容`不可變`的，類似元組，可用 `bytes()` 函數將串列內容轉換為bytes格式。  
bytearray則是`可變`的，類似串列，可用 `bytearray()` 函數將串列內容轉換為bytes格式。

```python
>>> ################# bytes 範例 ##############################################
>>> x = [1, 3, 5, 256, 4]
>>> b1 = bytes(x)                   # 因為整數範圍超過2^8=> 0 ~ 255, 所以產生錯誤了
Traceback (most recent call last):
  File "<python-input-195>", line 1, in <module>
    b1 = bytes(x)
ValueError: bytes must be in range(0, 256)
>>> x = [1, 3, 5, 255, 4]
>>> b1 = bytes(x)
>>> b1
b'\x01\x03\x05\xff\x04'
>>> type(b1)
<class 'bytes'>
>>> b1[0]
1
>>> b1[0] = 2                                   # 若變更值會產生錯誤
Traceback (most recent call last):
  File "<python-input-201>", line 1, in <module>
    b1[0] = 2
    ~~^^^
TypeError: 'bytes' object does not support item assignment
>>> ################# bytearray 範例 ##############################################
>>> x1 = [1, 3, 5, 255, 4]
>>> b2 = bytearray(x1)
>>> b2
bytearray(b'\x01\x03\x05\xff\x04')
>>> type(b2)
<class 'bytearray'>
>>> b2[0]
1
>>> b2[0] = 3                                  # 若變更值會成功
>>> b2[0]
3
```
