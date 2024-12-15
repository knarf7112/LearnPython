# 字典(Dict)

**串列(list)**與**元組(tuple)**是一種有順序的資料結構，而字典(dict)是一種沒有順序的資料結構，其元素是用 `"鍵:值"` 方式`配對儲存`。

## 定義

字典是將 `"鍵:值"` 放在大括號 **"{}"** 內，字典的**鍵(key)**一般常用 *字串* 或 *數字* 當作是鍵，一個字典中不可有重複的鍵出現，**值**可以是任何Python的資料物件。  

字典語法如下:

```python
x = { 鍵1:值1, 鍵2:值2, ..., 鍵n:值n }  # x是字典變數名稱
```

## 字典取值與賦值

```python
# 宣告字典
>>> x = { 'name': 'test', 'age': 123, 'likes': ['read', 'play', 'sleep'], 0: 'data1', 1: 'data2', True: False, None: None }
>>> type(x)               # 字典資料類型
<class 'dict'>
>>> x['name']             # 取得字典鍵為name的值
'test'
>>> x[0]
'data1'
>>> x[False]              # False會被轉為0, 0的值為'data1'
'data1'
>>> x[1]                  # 宣告變數時，True被轉型為1, 所以後宣告的key:value pair蓋掉前一個相同的key:value pair               
False
>>> type(x[None])
<class 'NoneType'>
>>> x['name'] = 'hello'   # 變更 'name' 的值
>>> x['name']
'hello'
```

## 檢查鍵是否存在

```python
>>> x = { 'name': 'test', 'age': 123, 'likes': ['read', 'play', 'sleep'], 0: 'data1', 1: 'data2', True: False, None: None }
>>> 'name' in x # 鍵'name'存在於x變數
True
>>> 0 in x
True
>>> False in x  # 字典內並沒有鍵為False, False會被轉為0, 而鍵 0 存在於x變數中, 故返回True
True
>>> 99 in x     # 鍵 99 不存在於x變數
False
```

## 刪除字典內的特定元素

通常會先檢查鍵是否存在才刪除，若**刪除一個不存在的鍵會產生錯誤**，  
若**刪除一個變數後再執行該變數也會產生錯誤**，可用 `locals()` 函數檢查當下是否存在該變數。
Python有提供一個 `isinstance(var, type)` 函數來檢查變數的資料類型， `eval('xxx')` 轉換成可執行的程式碼後並執行，eval() 不能進行復雜的邏輯運算，例如賦值操作、迴圈...等。

 刪除語法如下:

```python
del x[鍵]  # 刪除特定'鍵'元素
del x      # 刪除x變數，若變數已被刪除後才執行，會產生錯誤
```

範例:

```python
>>> x = { 'name': 'test', 'age': 123, 'likes': ['read', 'play', 'sleep'], 0: 'data1', 1: 'data2', True: False, None: None }
>>> 'x' in locals()  # 檢查變數x是否存在
True
>>> del x            # 刪除變數x
>>> 'x' in locals()  # 檢查變數x是否存在
False
>>> ####################### 判斷變數的資料類型 ############################
>>> x1,x2,x3,x4,x5,x6 = 123,'abc',True,[],(),{}
>>> isinstance(x1, int)        # int => class int
True
>>> isinstance(x2, str)        # str => class str
True
>>> isinstance(x3, bool)       # bool => class bool
True
>>> isinstance(x4, list)       # list => class list
True
>>> isinstance(x5, tuple)      # tuple => class tuple
True
>>> isinstance(x6, dict)       # dict => class dict
True
```

## 刪除字典特定元素並返回該元素

Python可用 `pop(key[, default])` 方法將字典特定元素刪除並返回刪除的元素，第一個參數是要刪除的`鍵(key)`，第二個參數為選項，當找不到要刪除的鍵則返回default內容，若default內容沒有設定則產生錯誤。  

範例如下:

```python
>>> x = { 'name': 'test', 'age': 123 }
>>> x.pop('name')                    # 刪除鍵'name'並返回該刪除鍵的值
'test'
>>> x
{'age': 123}
>>> x.pop('abc', '找不到(key)abc')   # 刪除鍵'abc'但找不到，返回default內容
'找不到(key)abc'
>>> x.pop('abc')                    # 刪除鍵'abc'但找不到，產生錯誤
Traceback (most recent call last):
  File "<python-input-20>", line 1, in <module>
    x.pop('abc')
    ~~~~~^^^^^^^
KeyError: 'abc'
```

Python可用 `popitem()` 方法將字典用 **後進先出(Last In First out, LIFO)** 的方式將元素刪除並返回刪除元素的 `key:value pair`元組物件。

範例如下:

```python
>>> x = { 'name': 'test', 'age': 123, 1: 111, 0: 0 }
>>> x.popitem()           # 依據宣告的時間點pop出該元素
(0, 0)
>>> x.popitem()
(1, 111)
>>> x.popitem()
('age', 123)
>>> x.popitem()
('name', 'test')
>>> x.popitem()
Traceback (most recent call last):
  File "<python-input-29>", line 1, in <module>
    x.popitem()
    ~~~~~~~~~^^
KeyError: 'popitem(): dictionary is empty'
>>> x = { 'name': 'test', 'age': 123, 1: 111, 0: 0 }
>>> del x['name']        # 刪除掉該元素
>>> x
{'age': 123, 1: 111, 0: 0}
>>> x['name'] = 'test'   # 再新增回去該元素
>>> x
{'age': 123, 1: 111, 0: 0, 'name': 'test'}
>>> x.popitem()          # pop最後新增的元素
('name', 'test')
>>> x.popitem()          # 所以dict看是無序,但其實內部狀態有紀錄新增元素時的先後順序
(0, 0)
```

## 刪除字典內所有元素或新增空字典

```python
>>> x = { 'name': 'test', 'age': 123, 1: 111, 0: 0 }
>>> x.clear() # 清除字典內所有元素
>>> x
{}
>>> y = {}    # 新增一個空字典
```

## 字典的淺拷貝/深拷貝

```python
>>> ################################## 淺拷貝 ###################################################
>>> x = { 'name': 'test', 'age': 123, 'a': [1, 2, 3], 'b': { 'b1': 'bbb', 'b2': '222' } }
>>> x2 = x.copy()              # '淺拷貝'該字典到變數x2
>>> id(x)
1578444773312
>>> id(x2)
1578444773056
>>> x
{'name': 'test', 'age': 123, 'a': [1, 2, 3], 'b': {'b1': 'bbb', 'b2': '222'}}
>>> x2['a'][1] = '是否影響到x'  # 變更x2內'a'的第2個元素值,連帶影響x內'a'的第2個元素值
>>> x
{'name': 'test', 'age': 123, 'a': [1, '是否影響到x', 3], 'b': {'b1': 'bbb', 'b2': '222'}}
>>> ################################## 深拷貝 ###################################################
>>> import copy
>>> x = { 'name': 'test', 'age': 123, 'a': [1, 2, 3], 'b': { 'b1': 'bbb', 'b2': '222' } }
>>> x2 = copy.deepcopy(x)              # '深拷貝'該字典到變數x2
>>> id(x)
1578444772416
>>> id(x2)
1578444936128
>>> x
{'name': 'test', 'age': 123, 'a': [1, 2, 3], 'b': {'b1': 'bbb', 'b2': '222'}}
>>> x2['a'][1] = '是否影響到x'  # 變更x2內'a'的第2個元素值,不會影響x內'a'的第2個元素值(全部資料已是兩個獨立的記憶體位置)
>>> x
{'name': 'test', 'age': 123, 'a': [1, 2, 3], 'b': {'b1': 'bbb', 'b2': '222'}}
>>> x2
{'name': 'test', 'age': 123, 'a': [1, '是否影響到x', 3], 'b': {'b1': 'bbb', 'b2': '222'}}
```

## 取得字典的元素數量

```python
>> x = { 'name': 'test', 'age': 123, 'a': [1, 2, 3], 'b': { 'b1': 'bbb', 'b2': '222' } }
>>> len(x)
4
```

## 字典的風格

字典設定建議用 `PEP 8` 的Python風格設計，範例如下:

```python
players = {
    'A':'AAA',
    'B':'BBB',
    'C':'CCC',
    'D':'DDD',
}

players2 = {'A':'AAA',
            'B':'BBB',
            'C':'CCC',
            'D':'DDD'}
```

## 多個字典的合併

若想將2個字典合併成1個，可使用 `update()` 方法。  
Python 3.5版以後，合併字典新方法可用 `{ **dict1, **dict2 }`，有點類似JavaScript的解構賦值(Destructing assignment)

```python
>>> ###################### 一般合併 ##########################
>>> d1 = { 1:11, 2:22, 3:33 }
>>> d2 = { 21:221, 22:222, 23:233 }
>>> d1.update(d2)                      # 將d2字典合併到d1
>>> d1
{1: 11, 2: 22, 3: 33, 21: 221, 22: 222, 23: 233}
>>> ###################### 字典有交疊元素 ####################
>>> d3 = { 1:11, 2:22 }
>>> d4 = { 2:00, 3:33 }
>>> d4.update(d3)                      # d3與d4有相同的key，該key的值會被d3給蓋掉
>>> d4
{2: 22, 3: 33, 1: 11}
>>> ###################### Python3.5的新合併方式 #############
>>> d5 = { 1:'a', 2:'b' }
>>> d6 = { 1:'aaa', 3:'c' }
>>> { **d5, **d6 }
{1: 'aaa', 2: 'b', 3: 'c'}
>>> { **d6, **d5 }             # 須注意相同key之間的值是後者蓋前者
{1: 'a', 3: 'c', 2: 'b'}
```

## 將雙值序列的資料轉成字典

```python
>>> dict([['日本', '東京'],['泰國','曼谷'],['英國','倫敦']])  # 將雙值串列轉換成字典
{'日本': '東京', '泰國': '曼谷', '英國': '倫敦'}
>>> dict([('日本', '東京'),['泰國','曼谷'],['英國','倫敦']])  # 雙值串列(list)也可以是元組(tuple)
{'日本': '東京', '泰國': '曼谷', '英國': '倫敦'}
>>> dict(('ab', 'cd', 'ed'))
{'a': 'b', 'c': 'd', 'e': 'd'}
>>> dict(['ab', 'cd', 'ed'])
{'a': 'b', 'c': 'd', 'e': 'd'}
```

## `zip()`

```python
>>> dict(zip('abcde', range(5)))
{'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
>>> dict(zip(['k1', 'k2', 'k3'], range(3)))
{'k1': 0, 'k2': 1, 'k3': 2}
```

## 遍歷字典

遍歷字典的方式類似JavaScript，以下幾種:

1. `items()`: 遍歷字典的鍵:值
2. `keys()`: 遍歷字典的鍵
3. `values()`: 遍歷字典的值
4. `sorted()`: 排序內容

> 早期字典是一個`無序`的資料結構，不會關注元素的排列順序，**Python3.7**之後，**字典會保留元素插入順序**

範例:

```python
>>> ################## 遍歷字典的 key:value pair ############################
>>> x = {'k1': 'v1', 'k2':'v2', 'k3':'v3' }
>>> for key, value in x.items():
...     print(f'key={key}, value={value}')
... 
key=k1, value=v1
key=k2, value=v2
key=k3, value=v3
>>> ################## 遍歷字典的 key 列表 ##################################
>>> for key in x.keys():
...     print(f'key={key}, value={x[key]}')
... 
key=k1, value=v1
key=k2, value=v2
key=k3, value=v3
>>> for key in x:                             # 省略.keys()也可獲得key列表
...     print(f'key={key}, value={x[key]}')
... 
key=k1, value=v1
key=k2, value=v2
key=k3, value=v3
>>> ################## 遍歷字典的 value 列表 ################################
>>> for val in x.values():
...     print(f'value={val}')
... 
value=v1
value=v2
value=v3
```

## 依鍵排序與遍歷字典

Python的字典不會處理排序，若想要遍歷字典並同時列出排序結果，可使用 `sorted()` 方法。

`sorted()` 函數可對任何**可迭代的對象**進行排序，並返回一個排序後的新串列，`sorted()` 語法如下:

```python
sorted_dict = sorted(my_dict.items(), key=lambda x:x[1], reserve=True)
# my_dict.items表示要排序的迭代物件(每個元素為tuple物件)
# key表示排序的鍵，lambda x:x[1]的x[1]表示tuple元素的第1個元素值
```

範例:

```python
>>> ###################### 依據鍵排序 ########################################
>>> for key in sorted(d):                     # 排序，預設為小 -> 大
...     print(f'key={key}, val={d[key]}')
... 
key=1, val=1
key=2, val=2
key=3, val=3
key=4, val=4
key=5, val=5
>>> d                                         # 原來數據沒有變動
{3: 3, 1: 1, 4: 4, 5: 5, 2: 2}
>>> for key in sorted(d, reverse=True):       # 反向排序(大 -> 小)
...     print(f'key={key}, val={d[key]}')
... 
key=5, val=5
key=4, val=4
key=3, val=3
key=2, val=2
key=1, val=1
>>> ###################### 指定字典的值來當作排序的依據 #########################
>>> for key,val in sorted({ 1:3, 2:4, 3:1, 4:5, 5:2 }.items(), key=lambda k:k[1]):  # k就是items()後的每個tuple元素，裡面有兩個元素，索引0就是key，索引1就是value
...     print(f'key={key}, val={val}')
...     
key=3, val=1
key=5, val=2
key=1, val=3
key=2, val=4
key=4, val=5
>>> ###################### 依據鍵排序(鍵的型態不同) ############################
>>> x = { 'b':'b', 'c':'c', 3:3,  'a':'a', 2:2 }
>>> for key in sorted(x, key=lambda x: str(x)):  # 需要將鍵轉型成相同型別才能比較與排序，否則會產生錯誤
...     print(f'key={key}, val={x[key]}')
... 
key=2, val=2
key=3, val=3
key=a, val=a
key=b, val=b
key=c, val=c
>>> ###################### 雙層for並排序 ######################################
>>> for key1,val1 in sorted({ 1:3, 2:4, 3:1, 4:5, 5:2 }.items(), key=lambda k:k[1]):
...     for key2,val2 in sorted({ 'b':'b', 'a':'a', 'c':'c' }.items()):
...         print(f'key1={key1},val1={val1}|key2={key2},val2={val2}')
... 
key1=3,val1=1|key2=a,val2=a
key1=3,val1=1|key2=b,val2=b
key1=3,val1=1|key2=c,val2=c
key1=5,val1=2|key2=a,val2=a
key1=5,val1=2|key2=b,val2=b
key1=5,val1=2|key2=c,val2=c
key1=1,val1=3|key2=a,val2=a
key1=1,val1=3|key2=b,val2=b
key1=1,val1=3|key2=c,val2=c
key1=2,val1=4|key2=a,val2=a
key1=2,val1=4|key2=b,val2=b
key1=2,val1=4|key2=c,val2=c
key1=4,val1=5|key2=a,val2=a
key1=4,val1=5|key2=b,val2=b
key1=4,val1=5|key2=c,val2=c
```

## 字典常用函數 `fromkeys()`

建立字典的靜態方法，語法如下:

```python
my_dict = dict.fromkeys(seq[, value]) # 使用 seq 來建立字典，序列內容會是字典的鍵，value預設為None，表示字典鍵的值
```

範例:

```python
>>> dict.fromkeys(['a','b','c'])                  # 將串列轉成字典
{'a': None, 'b': None, 'c': None}
>>> dict.fromkeys(('a','b','c'))                  # 將元組轉成字典
{'a': None, 'b': None, 'c': None}
>>> dict.fromkeys(('a','b','c'), (1,2,3))         # 將元組轉成字典並設定值
{'a': (1, 2, 3), 'b': (1, 2, 3), 'c': (1, 2, 3)}
```

## 字典常用函數 `get()`

搜尋字典的鍵，若鍵存在則返回該鍵的值，否則返回預設值。

範例:

```python
>>> { 'a':'a1', 'b':'b2', 'c':'c3' }.get('a')                  # 查找鍵 'a' 是否存在，存在返回該鍵的值
'a1'
>>> type({ 'a':'a1', 'b':'b2', 'c':'c3' }.get('a1'))           # 查找鍵 'a1' 是否存在，不存在返回None
<class 'NoneType'>
>>> { 'a':'a1', 'b':'b2', 'c':'c3' }.get('a1', 'a1 is empty')  # 查找鍵 'a1' 是否存在，不存在返回設定的default
'a1 is empty'
```

## 字典常用函數 `setdefault()`

與 `get()` 類似，但 `get()` 不會變更字典內容，此方法會變更內容。  
使用 `setdefault()`，若搜尋的`鍵`不存在，會將 `鍵:值` 加入字典，如果有設定預設值，則會將 `鍵:值` 加入字典，如果沒有設定預設值，則會將 `鍵:None` 加入字典。

```python
>>> d1 = { 'a':'a1', 'b':'b2', 'c':'c3' }
>>> d1.setdefault('a', 'a2')                # 'a' 存在，故返回鍵 'a' 的值
'a1'
>>> d1                                      #  因為 'a' 已存在，就不會變更字典
{'a': 'a1', 'b': 'b2', 'c': 'c3'}
>>> d1.setdefault('a2', 'a2')               # 'a2' 不存在，故同時間將'a2:a2'加入字典並返回鍵 'a2' 的值
'a2'
>>> d1
{'a': 'a1', 'b': 'b2', 'c': 'c3', 'a2': 'a2'}  # 字典被加入 '鍵:值' 元素了
```

## 凱薩密碼練習

```python
>>> ################### 加密 ######################
>>> abc = 'abcdefghijklmnopqrstuvwxyz'    # 字母表
>>> front = abc[:5]                       # 前5個字母 (位移5位)
end = abc[5:]                             # 剩餘字母
>>> subText = end + front                 # 對照表
>>> encry_dict = dict(zip(abc, subText))  # 將字母表與對照表合併 (key為字母表, value為對照表)
>>> encry_dict
{'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j', 'f': 'k', 'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o', 'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't', 'p': 'u', 'q': 'v', 'r': 'w', 's': 'x', 't': 'y', 'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c', 'y': 'd', 'z': 'e'}
>>> cipher = []                           # 用來放密文的串列
>>> msg = 'hello'                         # 原文(未加密)
>>> for i in msg:
...     v = encry_dict[i]                 # 用對照表產生密文字母(此變數仍存在於此scope)
...     cipher.append(v)                  # 將該字母加入串列
... 
>>> cipher_text = ''.join(cipher)         # 將串列內字母合併成字串
>>> cipher_text                           # 密文
'mjqqt'
>>> ################### 解密 ######################
>>> decry_dict = dict([(value, key) for key, value in encry_dict.items()])  # 將上面字母表與對照表相反(key為對照表, value為字母表)
>>> decry_dict
{'f': 'a', 'g': 'b', 'h': 'c', 'i': 'd', 'j': 'e', 'k': 'f', 'l': 'g', 'm': 'h', 'n': 'i', 'o': 'j', 'p': 'k', 'q': 'l', 'r': 'm', 's': 'n', 't': 'o', 'u': 'p', 'v': 'q', 'w': 'r', 'x': 's', 'y': 't', 'z': 'u', 'a': 'v', 'b': 'w', 'c': 'x', 'd': 'y', 'e': 'z'}
>>> for s in cipher_text:
...     c = decry_dict[s]                # 用對照表還原密文字母
...     decry_list.append(c)             # 將該字母加入串列
... 
>>> decry_text = ''.join(decry_list)     # 將串列內字母合併成字串
>>> decry_text                           # 原文
'hello'
```
