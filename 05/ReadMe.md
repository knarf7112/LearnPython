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
