# 函數(function)

函數就是一系列指令敘述所組成，目的有兩個，一是將功能拆分成小部分來執行，簡化維護，偵錯容易，一是將重複的部分再利用。

## 定義

```python
def 函數名稱(參數值1[, 參數值2, ...]):
    """
    函數註解(docstring)
    """
    程式碼區塊
    return [回傳值1, 回傳值2, ...]
```

* 函數名稱必須唯一，命名規則`PEP8`風格建議第一個英文字母`小寫`
* 參數值是可有可無，各參數用`,`逗號隔開
* 函數註解也是可有可無，但大型程式建議加上註解方便維護，此處註解也稱docstring(document string)
* 返回值也是可有可無，若有回傳多個資料必須用`,`逗號隔開

```python
>>> def sub(a, b):
...     ''' 減法 '''
...     s = a - b
...     print(f'sub={s}')
...     return [s, a, b]
... 
>>> sub(3, 1)
sub=2    
[2, 3, 1]
```

## 關鍵字參數

關鍵字參數(keyword arguments)是指呼叫函數時，參數用 `參數名稱=值` 的方式來傳入參數，這時位置就不重要了。

```python
>>> def sub(a, b):
...     ''' 減法 '''
...     s = a - b
...     print(f'sub={s}')
...     return [s, a, b]
... 
>>> sub(b=1, a=3)  # 指定參數名稱後，參數位置就不重要了
sub=2
[2, 3, 1]
```

## 參數預設值

當呼叫函數，但可能不傳參數就可設定參數的預設值，須注意有預設值的參數位置必須在參數列的最右邊。

```python
>>> def sub(a, b = 1):
...     ''' 減法 '''
...     s = a - b
...     print(f'sub={s}')
...     return [s, a, b]
... 
>>> sub(3)  # 沒有傳入第2個參數，b會用1(預設值)來執行
sub=2
[2, 3, 1]
```

## 函數回傳值

若呼叫函數沒有回傳值，Python會自動回傳`None`(Python在直譯時會自動將回傳處理成"return None")。

```python
>>> ######### 若無回傳值，則預設返回None ########################
>>> def return_none():
...     return
... 
>>> type(return_none())
<class 'NoneType'>
>>> ######### 返回值 ########################
>>> def return_value(a, b):
...     return a - b;
... 
>>> return_value(3, 1)
2
>>> ######### 返回多筆資料(返回類型:tuple) ########################
>>> def return_muti(a, b):
...     ''' 加,減,乘,除 '''
...     addResult = a + b
...     subResult = a - b
...     mulResult = a * b
...     divResult = a / b
...     return addResult, subResult, mulResult, divResult  # Python會將結果打包成tuple
... 
>>> return_muti(9, 3)
(12, 6, 27, 3.0)
>>> ######### 返回串列(list) ########################
>>> def return_list(a, b):
...     return [a + b, a - b]
... 
>>> return_list(5, 3)
[8, 2]
>>> [r1, r2] = return_list(5, 3)
>>> ######### 返回字典(dict) ########################
>>> def return_dict(a, b):
...     return {  'add': a + b, 'sub': a - b }
... 
>>> return_dict(5, 3)
{'add': 8, 'sub': 2}
```

## 傳遞任意數量的參數

若傳遞的參數數量不明確，可於參數前加上 `*` 表示該參數可從0到多個參數會傳遞，此方式會將所傳遞的參數轉成**元組(tuple)**。  
若有一般參數，則有 `*` 的參數必須於最右邊。  
若參數是**關鍵字參數(參數名稱 = 值)**，可於參數前加上 `**` 表示該參數可從0到多個參數且參數為**字典**元素，Python會將傳遞的參數轉為**字典(dict)**，引數為字典的*鍵*，對應的值為字典的*值*。

```python
>>> def any_arguments(*args):
...     print(args)
...     idx = 0
...     for item in args:
...         print(f'第{idx}個參數值{item}')
...         idx += 1
...         
>>> any_arguments('a', 'b', 'c', 'd', 'e')
('a', 'b', 'c', 'd', 'e')
第0個參數值a
第1個參數值b
第2個參數值c
第3個參數值d
第4個參數值e
>>> ################### 有*號的參數只能放最右邊 #########################
>>> def any_arguments(first, *args):
...     print(first, args)
...     idx = 0
...     for item in args:
...         print(f'第{idx}個參數值{item}')
...         idx += 1
... 
>>> any_arguments('這是第一個參數', 'a', 'b', 'c', 'd', 'e')
這是第一個參數 ('a', 'b', 'c', 'd', 'e')
第0個參數值a
第1個參數值b
第2個參數值c
第3個參數值d
第4個參數值e
>>> ################### 有**號的參數只能放最右邊 #########################
>>> def any_arguments(first, **args):
...     print(first, args)
...     for key,val in args.items():
...         print(f'key={key}, value={val}')
...         
>>> any_arguments('這是第一個參數', Name = 'Test', Age = 18, likes = ['game', 'swim', 'sleep'], NickName = 'hello')
這是第一個參數 {'Name': 'Test', 'Age': 18, 'likes': ['game', 'swim', 'sleep'], 'NickName': 'hello'}
key=Name, value=Test
key=Age, value=18
key=likes, value=['game', 'swim', 'sleep']
key=NickName, value=hello
```

## 進階函數

在Python中，所有東西皆為物件，例如:字串、串列、字典、...、函數等。  
所以也可以將函數賦值給一個變數，也可將函數當參數傳遞，也可動態建立與銷毀，故函數與其他物件(數字，字串，串列...等等)有相同的地位。
所以函數又稱`第一類物件(First-Class Objects)`。

```python
>>> ########################## 函數註解(文件字串) ####################################
>>> def test_function(name):
...     """這是test_function函數的說明,需要傳遞name字串參數"""
...     print(f'Hi, {name} , this is test_function call')
...
>>> help(test_function)
Help on function test_function in module __main__:

test_function(name)
    這是test_function函數的說明,需要傳遞name字串參數
>>> test_function.__doc__
'這是test_function函數的說明,需要傳遞name字串參數'
>>> ########################## 函數可當參數傳遞或賦值給其他變數 ####################################
>>> def call(fn, *args):
...     """ *args可當作不定量函數的參數傳遞ㄋㄩ """
...     fn(*args)
... 
>>> call(test_function, 'Qoo')
Hi, Qoo , this is test_function call
>>> fn1 = test_function
>>> type(fn1)
<class 'function'>
>>> type(test_function)
<class 'function'>
```

## 崁套函數

函數內部也可以有函數，崁套函數用來封裝、隱藏或重複使用的效果。
類似javascript的閉包(closure)

```python
>>> def outer():
...     x = 10      # x變數僅存在於此函數內
...     def inner(y):
...         return x * y
...     return inner
... 
>>> call_inner = outer()
>>> call_inner2 = outer()
>>> call_inner(5)
50
>>> print(call_inner)     # 返回的函數為內層inner函數的記憶體位址
<function outer.<locals>.inner at 0x000001D78D1007C0>
>>> print(call_inner2)    # 返回的函數為內層inner函數的記憶體位址
<function outer.<locals>.inner at 0x000001D78D100860>
```
