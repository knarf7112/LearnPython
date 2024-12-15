# 集合(Set)

集合是無順序且每個元素均`唯一`。  
集合元素的`值`是不可變的(immutable)，常見元素有`整數(intger)`、`浮點數(float)`、`字串(string)`、`元組(tuple)`...等。  
而`串列(list)`、`字典(dict)`、`集合(set)`...等是可變(mutable)的內容，所以不可以是集合元素，但集合本身是可變的，可以為集合`新增`或`刪除`集合的元素。  
集合主要用途為`消除重複`。

## 建立集合

```python
>>> lang = { 'Python', 'C', 'Java' }
>>> type(lang)
<class 'set'>
>>> a = { 2, 3, 4, 5, 2, 2, 2 }  # 重複的元素只會保留一份
>>> a
{2, 3, 4, 5}
```

## 使用`set()`建立集合

Python內建的`set()`函數也可建立集合，傳入參數只有一個，此元素可以是`字串(string)`、`串列(list)`、`元組(tuple)`、`字典(dict)`等類型數據。

```python
>>> s1 = set('hello')
>>> s1                       
{'h', 'l', 'e', 'o'}
>>> set('Deepmind')          # 字母順序被打亂了，因為set是無序的
{'m', 'D', 'p', 'n', 'e', 'd', 'i'}
>>> s2 = set(['test', 'Test', 'abc'])
>>> s2
{'test', 'Test', 'abc'}
>>> s3 = set((1, 2, 3))
>>> s3
{1, 2, 3}
>>> len(s3)                  # 查看集合內的元素數量
3
```

## 空集合

只有使用`set()`能建立空集合。

```python
>>> type({})
<class 'dict'>
>>> type(set())
<class 'set'>
```

## 集合操作

| Python符號 | 說明 | 函數 |
| --- | --- | --- |
| & | 交集 | intersection() |
| \| | 聯集 | union() |
| - | 差集 | difference() |
| ^ | 對稱差集 | symmetric_difference() |
| == | 等於 | 無 |
| != | 不等於 | 無 |
| in | 是成員 | 無 |
| not in | 不是成員 | 無 |

範例:

```python
>>> A = { 'A1', 'B2', 'C3' }
>>> B = { 'B1', 'B2', 'B3' }
>>> C = { 'A1', 'B2', 'C3' }
>>> D = { 'B2', 'C3' }
>>> A & B                        # A與B的交集(取得A與B共有的元素)
{'B2'}
>>> A.intersection(B)
{'B2'}
>>> A | B                        # A與B的聯集(取得存在於A或存在於B的元素)
{'B1', 'A1', 'C3', 'B2', 'B3'}
>>> A.union(B)
{'B1', 'A1', 'C3', 'B2', 'B3'}
>>> A - B                        # A與B的差集(取得A裡面的元素但排除與B共有的元素)
{'A1', 'C3'}
>>> A.difference(B)
{'A1', 'C3'}
>>> B - A                        # B與A的差集(取得B裡面的元素但排除與A共有的元素)
{'B1', 'B3'}
>>> B.difference(A)
{'B1', 'B3'}
>>> A ^ B                        # A與B的全部差集(取得A與B不共有的所有元素)
{'B1', 'A1', 'C3', 'B3'}
>>> A.symmetric_difference(B)
{'B1', 'A1', 'C3', 'B3'}
>>> A == C                       # 檢查A與C元素是否相同
True
>>> A != B                       # 檢查A與B元素是否不同
True
>>> 'A1' in A                    # 檢查 'B1' 是否為A的元素
True
>>> 'B1' not in A                # 檢查 'B1' 是否不是A的元素
True
```

## 集合的新增/修改/刪除操作

| 函數 | 說明 |
| --- | --- |
| add() | 加一個元素到集合 |
| clear() | 刪除集合所有元素 |
| copy() | 複製集合 |
| discard() | 若為集合成員就刪除 |
| isdisjoint() | 若兩個集合沒有交集返回True |
| issubset() | 若另一個集合包含這個集合返回True |
| isupperset() | 若這個集合包含另一個集合返回True |
| pop() | 傳回所刪除的元素，若元素不存在，程式返回KeyError |
| remove() | 刪除指定元素，若此元素不存在，程式返回KeyError |
| update() | 使用聯集更新集合內容 |

範例:

```python
>>> s1 = set()
>>> s1.add('A1')                         # 新增元素
>>> s1
{'A1'}
>>> c = [1,2,3]
>>> s1.add(c)                            # 集合無法新增mutable的集合，只能新增immutable的集合，例如tuple
Traceback (most recent call last):
  File "<python-input-38>", line 1, in <module>
    s1.add(c)
    ~~~~~~^^^
TypeError: unhashable type: 'list'
>>> c = (1,2)
>>> s1.add(c)
>>> s1
{(1, 2), 'A1'}
>>> s2 = s1.copy()                       # 複製集合
>>> s2
{(1, 2), 'A1'}
>>> s1.remove('A2')                      # 刪除集合內的指定元素，若不存在該元素會產生KeyError錯誤
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    s1.remove('A2')
    ~~~~~~~~~^^^^^^
KeyError: 'A2'
>>> s1.remove('A1')                      # 刪除集合內的指定元素成功則返回None
>>> s1.discard('A2')                     # 刪除集合內的指定元素，成功或失敗均返回None，若不存在該元素也不會產生錯誤
>>> s2 = { 'A1', 'A2', 'A3', 'A4' }
>>> s2.pop()                             # 隨機的方式刪除元素，被刪除的元素會返回，若集合已是空集合則產生錯誤
'A1'
>>> s2.pop()
'A3'
>>> s2.pop()
'A2'
>>> s2.pop()
'A4'
>>> s2.pop()
Traceback (most recent call last):
  File "<python-input-25>", line 1, in <module>
    s2.pop()
    ~~~~~~^^
KeyError: 'pop from an empty set'
>>> s3 = { 'A1', 'A2', 'A3', 'A4' }
>>> s3.clear()                          # 刪除集合內的所有元素並返回None
>>> s3
set()
>>> s3 == set()                         # 檢查是否為空集合
True
>>> s4 = { 'A1', 'A2', 'A3', 'A4' }
>>> s5 = { 'B1', 'B2', 'B3', 'B4' }
>>> s6 = { 'A1', 'B2', 'B3' }
>>> s4.isdisjoint(s5)                   # 檢查 s4 與 s5 是否有共同的元素，存在共同元素返回False,否則返回True
True
>>> s4.isdisjoint(s6)
False
>>> s5.isdisjoint(s4)
True
>>> s5.isdisjoint(s6)
False
>>> s7 = { 'A1', 'A2', 'A3', 'A4', 'A5' }
>>> s8 = { 'A2', 'A3', 'B4' }
>>> s9 = { 'A2', 'A3' }
>>> s8.issubset(s7)                    # 檢查 s8 內的所有元素是否全部均存在於s7
False
>>> s9.issubset(s7)                    # 檢查 s9 內的所有元素是否全部均存在於s7
True
>>> s7 = { ('A1', ('A2-1', 'A2-2', ('A3-1-1', 'A3-1-2'))), 'A3', 'A4', 'A5' }
>>> s9 = { ('A1', ('A2-1', 'A2-2', ('A3-1-1', 'A3-1-2'))) }
>>> s9.issubset(s7)                    # 檢查 s9 內的所有元素是否全部均存在於s7(內崁3層tuple)
True
>>> s9.isdisjoint(s7)                  # 檢查 s9 與 s7 是否有共同的元素，內崁3層tuple仍可檢查出共同元素
False
>>> s7.issuperset(s9)                  # 檢查 s7 是否為 s9 的父集合，內崁3層tuple仍可檢查出來
True
>>> s7.issuperset({ 'A1' })            # 檢查 s7 是否為 { 'A1' } 的父集合，無法檢測內崁的部分元素
False
>>> s10 = { 'A1', 'A2', 'A3' }
>>> s10.update({ 'B1', 'B2' })         # 將集合的所有元素加到 s10 集合內
>>> s10
{'B1', 'A1', 'A3', 'B2', 'A2'}
```

## 適用集合的內建方法

| 函數 | 說明 |
| --- | --- |
| len() | 集合內的元素數量 |
| max() | 集合內的最大值 |
| min() | 集合內的最小值 |
| sorted() | 返回一個已排序的新串列，原本的集合並沒有改變 |
| sum() | 集合內的值加總 |

```python
>>> s1 = { 5, 3, 1, 8, 2 }
>>> len(s1)                  # 集合內的元素數量
5
>>> max(s1)                  # 集合內的最大值
8
>>> min(s1)                  # 集合內的最小值
1
>>> sorted(s1)               # 返回一個已排序的新串列，原本的集合並沒有改變
[1, 2, 3, 5, 8]
>>> sorted(s1, reverse=True)
[8, 5, 3, 2, 1]
>>> sorted(s1,key=lambda x:x%2)  # 也可用key(餘數為0在前面)
[2, 8, 1, 3, 5]
>>> sum(s1)
19
```

## 凍結集合(frozenset)

`set` 是可變(mutable)的集合，`frozenset` 是不可變(immutable)的集合，直譯為**凍結集合**。  
只要設定元素後，就不可異動集合，若將元組(tuple)想成`不可變串列`(immutable list)，凍結集合就是`不可變集合`(immutable set)。

凍結集合特點是可用作字典的鍵(key)，也可做為其他集合的元素，建立方式只能使用 `frozenset()` 函數來建立，建立後不可用`add()`或`remove()`更動該集合，但可以用 `intersection()`、`union()`、`difference()`、`symmetric_difference()`、`copy()`、`issubset()`、`issuperset()`、`isdisjoint()`等等方法(不會異動集合)。

範例:

```python
>>> x = frozenset(['A', 'B', 'C'])
>>> type(x)
<class 'frozenset'>
<class 'frozenset'>
>>> y = frosenset([1, 2, 3])
>>> x.union(y)
frozenset({'A', 1, 2, 3, 'B', 'C'})
>>> x | y
frozenset({'A', 1, 2, 3, 'B', 'C'})
>>> x.difference(y)
frozenset({'A', 'C', 'B'})
>>> x.intersection(y)
frozenset()x
>>> x & y
frozenset()
```

## 集合的生成式

語法如下:
> 新集合 = { 運算式 for 運算式 in 可迭代項目 }

範例:

```python
>>> s = { n for n in range(2, 30, 2) }
>>> s
{2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28}
>>> { n for n in range(2, 30, 2) if n % 10 != 0 }      # 從2~29範圍開始生成，每次遞增2，但n除10的餘數不能為0(排除10,20)
{2, 4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28}
>>> { alphabet: 'helloWorld!'.count(alphabet) for alphabet in set('helloWorld!') }  # 很簡易的就可以寫出檢查字母的出現次數
{'!': 1, 'r': 1, 'e': 1, 'W': 1, 'd': 1, 'o': 2, 'l': 3, 'h': 1}
```
