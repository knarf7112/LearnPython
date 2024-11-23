# 流程控制

程式設計過程遇到的轉折點而產生的條件分支就是**流程控制**。  
Python官方建議程式碼不要超過80列。

## 關係運算子

以下是關係運算子列表:

| 關係運算子 | 運算子說明 | 範例 | 範例說明 |
| :----: | :---- | :---- | :---- |
| > | 大於 | a > b | 是否a大於b |
| >= | 大於或等於 | a >= b | 是否a大於或等於b |
| < | 小於 | a < b | 是否a小於b |
| <= | 小於或等於 | a <= b | 是否a小於或等於b |
| == | 等於 | a == b | 是否a等於b |
| <= | 不等於 | a != b | 是否a不等於b |

## 邏輯運算子

邏輯運算子有 `and` 、 `or` 、 `not`，Python的邏輯運算中，`0`被視為`False`，其他值當作`True`。  

`and` 的真值表如下:

  | and | `True` | `False` |
  | :-: | :-: | :-: |
  | `True` | True | False |
  | `False` | False | False |

`or` 的真值表如下:

  | or | `True` | `False` |
  | :-: | :-: | :-: |
  | `True` | True | True |
  | `False` | True | False |

`not` 的真值表如下:

  | not | `True` | `False` |
  | :-: | :-: | :-: |
  |  | False | True |

範例:

```python
>>> x = (10 > 8) and ( 5 > 1) # True and True => x = True
>>> x = (10 < 8) and ( 5 > 1) # False and True => x = False (當前面邏輯運算為False時，後面邏輯運算不會執行，因為已經不可能為True)
>>> x = (10 > 8) or ( 5 > 1) # True or True => x = True(當前面邏輯運算為True時，後面邏輯運算不會執行，因為已經不可能為False)
>>> x = (10 < 8) or ( 5 > 1) # True or False => x = True
>>> 0 and True # 0被視為False
0
>>> 0 or -1 or 10 # 非0均被視為True
-1
>>> 0 or False or 10
10
>>> not False
True
>>> not -1
False
>>> not 0
True
>>> False or '' or 'test' # 空字串也視為False，因為會被轉為0
'test'
>>> 'test' or 'abc'
'test'
```

## 條件判斷 `if` | `elseif` | `else`

Python使用 `內縮` 來區隔 `if` 敘述的程式碼區塊，**內縮必須是4個空白字元**(Python PEP-8風格)。  
Python的內縮式有意義的，相同的程式碼區塊必須在相同的內縮，否則會產生錯誤。

```text
if (條件判斷):  # 條件判斷外的小括號可有可無
    程式碼區塊1
    程式碼區塊1
elseif (條件判斷):
    程式碼區塊2
    程式碼區塊2
else:
    程式碼區塊3
    程式碼區塊3

# 若只有一行
if (條件判斷):  程式碼區塊
```

```python
>>> if 10 > 8:                    # 條件為True，故執行'if'內的程式碼區塊
...     print('區塊一')
...     print('區塊一的下一列')
... else:
...     print('區塊二')
...     print('區塊二的下一列')
...     
區塊一
區塊一的下一列
>>> if 10 > 8:
...     print('區塊一')
...       print('區塊一的下一列')  # 若內縮不對就會產生錯誤
... else:
...     print('區塊二')
...     print('區塊二的下一列')
...     
  File "<python-input-24>", line 3
    print('區塊一的下一列')
IndentationError: unexpected indent
>>> x = 10
>>> print(f"{x}是奇數" if x % 2 else f"{x}是偶數") # 條件判斷也可這樣寫
10是偶數
```

Python可簡化 `if` 敘述的語法:

```python
max_ = x if x > y else y # 預設返回x，若 x > y就結束，否則返回y(取最大值)
min_ = x if x < y else y # 預設返回x，若 x < y就結束，否則返回y(取最小值)

max_ = max(x, y)         # 使用內建函數來返回最大值
min_ = min(x, y)         # 使用內建函數來返回最小值
```

## 尚未設定的變數 `None`

程式設計上可以將變數先設定為 `None` 表示尚未設定的意思，但要注意 `None` 在布林運算時，會被當作 `False`。

```python
>>> x = None
>>> type(x)
<class 'NoneType'>
```

## Python 物件導向觀念

在物件導向(Object Oriented Programming)觀念裡，所有資料均為一個**物件**(Object)，例如，*整數*、*浮點數*、*字串*或*串列*。  
為物件建立一些方法(method)以供這些物件使用，這些方法所指的是物件本身提供的方法，而這些方法是放在類別內的。  
Python有為一些基本物件提供**預設**的方法，基本語法如下:

> 物件.方法()

取得物件的方法列表可用 `dir()` 函數，若要了解特定方法可用 `help(物件.方法)` 函數來取得方法的資訊。

```python
>>> x = [1, 2, 3]
>>> dir(x)             # 查找串列的所有方法
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(x.pop)        # 查找串列的'pop()'方法資訊
Help on built-in function pop:

pop(index=-1, /) method of builtins.list instance
    Remove and return item at index (default last).

    Raises IndexError if list is empty or index is out of range.

>>> x = "ABC"
>>> dir(x)            # 查找字串的所有方法
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 
'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(x.translate) # 查找字串的'translate()'方法資訊
Help on built-in function translate:

translate(table, /) method of builtins.str instance
    Replace each character in the string using the given translation table.

      table
        Translation table, which must be a mapping of Unicode ordinals to
        Unicode ordinals, strings, or None.

    The table must implement lookup/indexing via __getitem__, for instance a
    dictionary or list.  If this operation raises LookupError, the character is
    left untouched.  Characters mapped to None are deleted.

>>> x = 123
>>> dir(x)             # 查找整數的所有方法
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
```

##

以下是`字串`常用的方法:

* `lower()`: 將字串轉小寫
* `upper()`: 將字串轉大寫
* `title()`: 將字串第一個字轉大寫，其餘轉小寫
* `swapcase()`: 將所有字串內的大寫轉小寫，小寫轉大寫
* `rstrip()`: 刪除字串末端多餘的空白
* `lstrip()`: 刪除字串開頭多餘的空白
* `strip()`: 刪除字串頭尾兩端多餘的空白
* `center()`: 字串在指定寬度置中對齊
* `rjust()`: 字串在指定寬度靠右對齊
* `ljust()`: 字串在指定寬度靠左對齊
* `zfill()`: 設定字串長度，原字串長度靠右對齊，左邊多餘空間補0

```python
>>> 'abc'.upper()  # 轉大寫
'ABC'
>>> 'AbC'.lower()  # 轉小寫
'abc'
>>> 'THiS iS TEst'.title()       # 將開頭轉大寫，其餘轉小寫
'This Is Test'
>>> 'THiS iS TEst'.swapcase()    # 將字串全部大小寫顛倒
'thIs Is teST'
>>> '  This is Test  '.strip()   # 將頭尾空白刪除
'This is Test'
>>> '  This is Test  '.rstrip()  # 僅刪除尾部的空白
'  This is Test'
>>> '  This is Test  '.lstrip()  # 僅刪除開始的空白
'This is Test  '
>>> 'Hello'.center(7)            # 將字串置中於長度7的空間中
' Hello '
>>> 'Hello'.rjust(7)             # 字串在指定寬度為7(不足的補空白)並靠右對齊
'  Hello'
>>> 'Hello'.ljust(7)             # 字串在指定寬度為7(不足的補空白)並靠左對齊
'Hello  '
>>> 'Hello'.zfill(7)             # 設定字串長度為7，原字串長度靠右對齊，左邊多餘空間補0
'00Hello'
```

以下是`串列`常用的方法:

* `append()`: 在串列末端新增一個元素
* `insert(index, value)`: 在串列任意位置插入一個元素
* `pop()`: 刪除串列末端或指定索引的元素
* `remove()`: 刪除串列指定索引的元素
* `reverse()`: 將串列內容前後全部顛倒
* `sort(key=None, reverse=False)`: 將串列元素排序, key是一個選項(預設為None)，可傳入一個函數用來從每個元素提取一個比較的key，reverse表示是否顛倒內容(預設為False，表示串列元素**由小到大**排序)
* `sorted(iterable, key=None, reverse=False)`: 將串列元素儲存於**新串列**後排序，iterable為必要參數，是一個可送代的物件(串列或字典或字串...等等)，其餘參數意義同`sort()`
* `index(value, start=0, end=len(list))`: 依序查找串列內匹配條件的元素並返回該索引，第一次匹配就返回，value表示查找的內容值，start表示查找索引起始位置(預設為0)，end表示查找索引結束位置(預設為送代物件的長度)，若找不到內容值會出現**錯誤**
* `count()`: 傳回特定元素內容出現於串列的次數(即查找指定元素在串列內出現的次數)

```python
# ============================= 串列操作 ====================================================================================
>>> mobiles = ['Apple', 'Oppo', 'Samsung', 'Vivo', 'Mi', ]
>>> mobiles.append('Google')                                  # 在末端新增一個元素
>>> mobiles
['Apple', 'Oppo', 'Samsung', 'Vivo', 'Mi', 'Google']
>>> mobiles.insert(2, 'Sony')                                 # 指定索引2的位置插入一個元素
>>> mobiles
['Apple', 'Oppo', 'Sony', 'Samsung', 'Vivo', 'Mi', 'Google']
>>> mobiles.pop(2)                                            # 指定刪除索引2的元素
'Sony'
>>> mobiles
['Apple', 'Oppo', 'Samsung', 'Vivo', 'Mi', 'Google']
>>> mobiles.pop()                                             # 刪除末端的元素
'Google'
>>> mobiles
['Apple', 'Oppo', 'Samsung', 'Vivo', 'Mi']
>>> mobiles.remove('Samsung')                                 # 刪除匹配內容的元素
>>> mobiles
['Apple', 'Oppo', 'Vivo', 'Mi']
>>> mobiles.reverse()                                         # 將串列的元素顛倒(串列還是原本的參考)
>>> mobiles
['Mi', 'Vivo', 'Oppo', 'Apple']
>>> mobiles.sort(key=len, reverse=True)                       # 依據len函數來排序(每個字串的長度)並將結果由大到小排序
>>> mobiles
['Apple', 'Vivo', 'Oppo', 'Mi']
>>> 
>>> a1 = [3, 1, 4, 2, 5, 9, 6]
>>> a1.sort()                                                 # 排序串列後會直接更改原素的順序
>>> a1
[1, 2, 3, 4, 5, 6, 9]
>>> a2 = sorted(a1,reverse=True)                              # 產生一個新串列並排序，不會更改原本的串列
>>> a2
[9, 6, 5, 4, 3, 2, 1]
>>> a2 == a1
False
>>> sorted('bca')
['a', 'b', 'c']
>>> mobiles.index('Mi')                                      # 查找'Mi'並找到其索引位置為3
3
>>> mobiles.index('Mi', 10)                                  # 查找'Mi'並從索引10開始，找不到拋出錯誤
Traceback (most recent call last):
  File "<python-input-91>", line 1, in <module>
    mobiles.index('Mi', 10)
    ~~~~~~~~~~~~~^^^^^^^^^^
ValueError: 'Mi' is not in list
>>> [1, 2, 1, 3, 1, 4].count(1)                              # 搜尋值1在串列出現的次數
3
# ============================= 字串操作 ====================================================================================
>>> 'abcabcabc'.count('abc')                                 # 搜尋值'abc'在串列出現的次數
3
>>> 'abcabcabc'.count('abc', 2, 6)                           # 搜尋值'abc'在串列出現的次數，從索引2開始到索引6(不包含索引6)
1
>>> 'abcabcabc'.count('abc', 2, 5)                           # 搜尋值'abc'在串列出現的次數，從索引2開始到索引6(不包含索引6)
0
>>> 'abcabcabc'.index('d')                                   # 從左至右查找字串，找不到會拋出錯誤
Traceback (most recent call last):
  File "<python-input-16>", line 1, in <module>
    'abcabcabc'.index('d')
    ~~~~~~~~~~~~~~~~~^^^^^
ValueError: substring not found
>>> 'abcabcabc'.find('d')                                    # 從左至右查找字串，找不到返回-1
-1
>>> 'abcabcabc'.rfind('d')                                    # 從右至左查找字串，找不到返回-1
-1
# ============================= 串列操作 ====================================================================================
>>> a1 = [1, 2, 3]
>>> a1.append([4, 5, 6])                                     # 尾部插入一個串列
>>> a1
[1, 2, 3, [4, 5, 6]]
>>> a2 = [1, 2, 3]
>>> a2.extend([4, 5, 6])                                     # 尾部插入一個串列，extend會先分解成元素(只會打散第一層)，再一個一個插入
>>> a2
[1, 2, 3, 4, 5, 6]
>>> a2.extend([[7, 8, 9], 10, 11])
>>> a2
[1, 2, 3, 4, 5, 6, [7, 8, 9], 10, 11]
```

## 串列的切片拷貝

切片拷貝的觀念是執行拷貝後會產生一個**新的串列物件**(僅串列物件為拷貝的，裡面的元素還是原本的參考)。

拷貝方式如下:

```python
import copy
x = [1, 2, 3]
y = x[:]               # 淺拷貝
x.copy()               # 淺拷貝

z = copy.deepcopy(x)   # 深拷貝
```

## 將字串轉成串列

```python
>>> x = list('abcdef')
>>> x
['a', 'b', 'c', 'd', 'e', 'f']
```

## 將字串分割與結合

用`split(ch)`將字串以空格(沒有傳入參數)或指定符號來當作分隔符號，將字串拆開變成一個串列。
用`join(list)`將串列連結再一起。

```python
>>> str1 = 'This is test string'
>>> str2 = r'D:\a\b\c\d.txt'
>>> str1.split()
['This', 'is', 'test', 'string']
>>> str2.split('\\')
['D:', 'a', 'b', 'c', 'd.txt']
>>> '\\'.join(['D:', 'a', 'b', 'c', 'd.txt'])
'D:\\a\\b\\c\\d.txt'
>>> '**'.join(['D:', 'a', 'b', 'c', 'd.txt'])
'D:**a**b**c**d.txt'
```

## 賦值與參考

Python 賦值給另一個變數時，只是將變數位址拷貝給另一個變數，故當原變數內的屬性有變動時，需要注意有參考該變數的其他變數是會跟者被影響的(和javascript概念一樣)。

```python
>>> x = [1, 2, 3]
>>> y = [0, x]
>>> y
[0, [1, 2, 3]]
>>> x[1] = 9              # 變動x[1]內容值
>>> y
[0, [1, 9, 3]]            # 變數y也跟者被變動了
```

## in 和 not in 運算式

當需要判斷一個物件是否屬於另一個物件，可用 `in` 運算式檢查，反之則使用 `not in`，物件可以是字串(string)、串列(list)、元祖(tuple)、字典(dist)。
> 格式:  
> boolean = obj in A  
> boolean = obj not in A

```python
>>> 5 not in [2, 3, 5, 9, 7]        # 5是否不存在於串列中
False
>>> 5 in [2, 3, 5, 9, 7]            # 5是否存在於串列中
True
>>> 'b' in 'abc'
True
>>> 'bc' in 'abc'
True
>>> 'b' not in 'abc'
False
```

## is 或 is not 運算式

當需要比較兩個物件是否指向的記憶體相同，可用 `is`(反之用 `is not`)，物件可以是變數、字串、串列、元祖、字典。
> 格式:  
> boolean = obj1 is obj2  
> boolean = obj1 is not obj2

```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a is b
False
>>> id(a)
2408372630400
>>> id(b)
2408373834496
>>> c = a
>>> c is a
True
>>> c is not a
False
>>>
>>> x = 10
>>> y = 10
>>> z = 15
>>> r = 20
>>> print('x = %d, y = %d, z = %d, r = %d' % (x, y, z, r))
x = 10, y = 10, z = 15, r = 20
>>> r = 10
>>> print(f'x_addr={id(x)}, y_addr={id(y)}, z_addr={id(z)}, r_addr={id(r)}')
x_addr=140717704668360, y_addr=140717704668360, z_addr=140717704668520, r_addr=140717704668360
```

## enumerate物件

`enumerate()` 方法可將iterable(迭代)類數值的**元素**用**索引**配對方式傳回，返回的數據稱**enumerate物件**，用這類方式可以為迭代物件的每個元素增加索引值以便依序送出所有元素。  
iterable可以是**串列(list)**、**元祖(tuple)**、**集合(set)** ...等。

> 語法格式如下:  
> obj = enumerate(iterable[, start=0]) # 若省略 start = 設定，預設索引為 0

```python
>>> mobiles = ['Apple', 'Oppo', 'Samsung', 'Vivo', 'Mi', ]
>>> enumerate_mobiles = enumerate(mobiles)                                  # 將串列轉成enumerate物件(預設索引為0)
>>> enumerate_mobiles
<enumerate object at 0x00000230BE430540>
>>> print('轉成串列輸出，初始索引值是0 = ', list(enumerate_mobiles))          # 將enumerate物件轉回串列(僅能轉一次，類似stream，迭代完就沒了)
轉成串列輸出，初始索引值是0 =  [(0, 'Apple'), (1, 'Oppo'), (2, 'Samsung'), (3, 'Vivo'), (4, 'Mi')]
>>> list(enumerate_mobiles)                                    
[]
>>> enumerate_mobiles = enumerate(mobiles)
>>> list(enumerate_mobiles)
[(0, 'Apple'), (1, 'Oppo'), (2, 'Samsung'), (3, 'Vivo'), (4, 'Mi')]
>>> list(enumerate_mobiles)
[]
>>> enumerate_mobiles = enumerate(mobiles, 10)                              # 將串列轉成enumerate物件並設定初始索引為10
>>> print('轉成串列輸出，初始索引值是10 = ', list(enumerate_mobiles))
轉成串列輸出，初始索引值是10 =  [(10, 'Apple'), (11, 'Oppo'), (12, 'Samsung'), (13, 'Vivo'), (14, 'Mi')]
```
