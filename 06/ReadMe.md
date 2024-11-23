# 串列(list)

**串列(list)** 是Python的一種可更改內容的資料型態，由一系列元素所組成的有序容器。

## 基本知識

與其他語言的 **陣列(Array)** 相似，裡面可以儲存相同型態的資料或不相同型態的資料。

定義串列語法格式如下:

```python
  x = [元素1, ..., 元素n,]  # x表示宣告的變數名稱, 元素n右邊的逗號可有可無
```

範例如下:

```python
>>> a = ['apple', 'banana', 'orange']  # 定義串列
>>> a[0]                               # 讀取串列變數a的第一個元素
'apple'
>>> a[-1]
'orange'
>>> a1, a2, a3 = a                     # 將串列內容依序解構到變數a1,a2,a3
>>> a1,a2,a3
('apple', 'banana', 'orange')
>>> a[9]                               # 讀取的索引不存在於串列時，會產生錯誤
Traceback (most recent call last):
  File "<python-input-13>", line 1, in <module>
    a[9]
    ~^^^
IndexError: list index out of range
```

## 串列切片(slice)

設計程序時常需要將串列的內容拆分，**取得前幾個元素**、**後幾個元素**、**某個區間的元素**或**依據一定規則排序的元素**，取得的一系列元素稱 **子串列**，此概念稱**串列切片(list slices)**。  

切片說明如下:

```python
  [start : end : step]

  # start: 表示起始索引，若省略表示從0開始
  # end:   表示結束索引(不包含此索引元素)，若省略表示到末端的所有元素
  # step:  表示每隔多少區間再讀取元素
  # 索引可為正數或負數，正數表示從頭開始(左邊第一個為0,往右遞增)，負數表示從末端開始(右邊第一個為-1，往左遞減)


  x[start:end]          # 取得從索引start到end - 1索引的串列元素
  x[start:]             # 取得從索引start到末端的串列元素
  x[:end]               # 取得從索引0到end - 1索引的串列元素
  x[-n:]                # 取得串列倒數n個的元素
  x[:-n]                # 取得串列前面的部分但不包含倒數n個的串列元素
  x[:]                  # 取得所有的串列元素
  x[::-1]               # 將串列反向排序
```

範例如下:

```python
>>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a[4:6]                                 # 取從索引4~5的串列元素(不包含6)
[5, 6]
>>> a[1:]                                  # 取第一個之後的所有串列元素
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a[-2:]                                 # 取倒數兩個串列元素
[9, 10]
>>> a[:]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]            # 取所有元素(等同原始串列)
>>> a[:] == a
True
>>> a[::-1]                                # 將串列反向(不會做sort)
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> a[::2]                                 # 每隔2就取一次串列元素
[1, 3, 5, 7, 9]
```

## 串列統計的函數

Python內建一些統計的函數，若串列內容全部為**字串**可用`max()`或`min()`來取得字串內unicode碼值的最大或最小值。

若串列內容均為**數值**就可以使用下列這些函數:

- `max()` : 獲得串列中的最大值
- `min()` : 獲得串列中的最小值
- `sum()` : 獲得串列的總和
- `len()` : 獲得串列的元素個數

範例如下:

```python
>>> x = [45, 3, 28, 72, 99, 44, 36, 88]
>>> max(x)
99
>>> min(x)
3
>>> sum(x)
415
>>> len(x)
8
```

## 串列的元素修改

範例如下:

```python
>>> x = ['test', 'qoo', 'abc']
>>> x
['test', 'qoo', 'abc']
>>> x[1] = 'hahaha'            # 修改第1個索引內的值
>>> x
['test', 'hahaha', 'abc']
```

## 串列之間的相加

Python允許使用 `+` 和 `+=` 將兩個串列相加，相當於將兩個串列做合併，若有相同的元素，則會重複出現。

```python
>>> y = [1, 2, 3, 'test']
>>> x = ['test', 'qoo', 'abc']
>>> x + y
['test', 'qoo', 'abc', 1, 2, 3, 'test']
>>> x += y
>>> x
['test', 'qoo', 'abc', 1, 2, 3, 'test']
```

## 串列的乘數

若將串列乘以一個數字，則該數字就是這個串列要重複幾次後產生的新串列。

```python
>>> x = [1, 2, 3]
>>> x * 3                        # 乘以3之後原本的串列變成自己的3倍
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> x + 3                        # 串列不能加一個數字，會產生錯誤
Traceback (most recent call last):
  File "<python-input-72>", line 1, in <module>
    x + 3
    ~~^~~
TypeError: can only concatenate list (not "int") to list
```

## 刪除串列元素

刪除串列可用 `del x[i]` 來刪除串列指定的元素，但此方式**缺點為無法取得被刪除的內容**。  
也可刪除該變數，刪除後就無法操作了。

```python
>>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> del a[1]                            # 刪除第一個索引元素
>>> a
[1, 3, 4, 5, 6, 7, 8, 9, 10]
>>> del a[:-2]                          # 刪除倒數2個以前的串列元素
>>> a
[9, 10]
>>> del a[-2:]                          # 刪除倒數2個的串列元素
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
>>> del a[:3]                           # 刪除從索引0~2的串列元素
>>> a
[4, 5, 6, 7, 8, 9, 10]
>>> del a[::2]                          # 每隔2就刪除索引start到end-1的元素
>>> a
[2, 4, 6, 8, 10]
>>> x = 123
>>> del x                               # 刪除x變數後就無法操作該變數了
>>> x
Traceback (most recent call last):
  File "<python-input-98>", line 1, in <module>
    x
NameError: name 'x' is not defined
```

## 多重指定與串列

在多重指定中，若等號左邊的變數比較少，可用 `*變數` 方式，將多餘的右邊內容用**串列**方式打包給含 `*` 的變數。

```python
>>> a, *b, c = 1, 2, 3, 4, 5    # a分配到1，c分配到5，其餘的以串列的方式分配給b
>>> b
[2, 3, 4]
>>> a, b, *c = 1, 2, 3, 4, 5    # a分配到1，b分配到2，其餘的以串列的方式分配給c
>>> c
[3, 4, 5]
```