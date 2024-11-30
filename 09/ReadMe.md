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
