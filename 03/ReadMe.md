# 基本資料型態

Python的基本資料型態如下:

- 數值型態(numeric type): **整數(int)**、**浮點數(float)**、**複數(complex number)**  

  一般**整數(int)**大小為32bit，範圍是-2147483648~2147483647，  
  但**Python 3已經將整數的儲存空間限制拿掉**了，故沒有long型態了，也就是說int可以是任意大小的數值。  
  浮點數也跟整數一樣沒有限制長度，可以是任意大小的數值。  
  Python對於數值間的運算會自動轉換。  
  Python支援**複數(complex number)**，複數由**實數部分**與**虛數部分**組成，複數的實部與虛部均為**浮點數**。

  ```bash
  >>> x = 10 # 整數
  >>> type(x)
  <class 'int'>
  >>> bigNum = 10_000_000_000_000_000_000_000 # 整數可在數值中加上底線(_)讓數值表達更清楚，底線會被直譯器忽略
  >>> print(bigNum)
  10000000000000000000000
  >>> type(bigNum)
  <class 'int'>
  >>> y = 1.234 # 浮點數
  >>> type(y)
  <class 'float'>
  >>> x = 5 
  >>> x = x + 1.0 # 整數與浮點數做計算會被轉為浮點數
  >>> print(x)
  6.0
  >>> type(x)
  <class 'float'>
  >>> type(4 / 2)
  <class 'float'>
  >>> x = 1.23456E+5 # 科學記號表示法
  >>> x
  123456.0
  >>> y = 1234e-4 # 科學記號表示法
  >>> y
  0.1234
  >>> 3 + 5j # 複數: 3表示實數，5j表示虛數
  (3+5j)
  >>> complex(3 + 5j) # 複數: 3表示實數，5j表示虛數
  (3+5j)
  >>> x = 6 + 9j # 複數
  >>> x.real # 複數的實數
  6.0
  >>> x.imag #0 複數的虛數
  9.0
  ```

- 布林(boolean)型態: True/False，但也被視為**數值型態** [True=1,False=0]
- 文字序列(text sequence type)型態: 就是**字串(string)**型態
- 位元組(bytes)型態: 這是二進位的資料型態，每個單位長度是8bit
- bytearray型態: 
- 序列(sequence type)型態: 此類型又稱作容器(container)，例如: list、tuple
- 對映(mapping type)型態: 此類型又稱作容器(container)，例如: dist
- 集合(set type)型態: 此類型又稱作容器(container)，例如: set、frozenset

## 如何檢查變數資料型態

使用 `type()` 函數可列出變數的資料型態，此函數很重要，因為Python不需要宣告變數的資料型態，故變數的資料型態可能會在程序中產生變化。

## 不同進位的整數

- 2進位整數: 凡`0b`開頭的數字均表示為2進位，可使用`bin()`函數或`format(num, 'b')`函數或`f-string`將一般整數數字轉換為2進位，使用`int('xxx', 2)`將字串轉回整數。

  ```bash
  >>> x = 0b111           # 設定變數為2進位
  >>> x
  7
  >>> bin(7)              # 將整數轉為2進位字串
  '0b111'
  >>> format(7, 'b')      # 將整數轉為2進位字串
  '111'
  >>> f'{x:b}'            # 將x變數帶入並將整數轉為2進位字串
  '111'
  >>> f'{7:b}'            # 將整數轉為2進位字串
  '111'
  >>> f'{7:08b}'          # 將整數轉為2進位字串，0表示填充內容(也只能為0)，8為字串長度8，b表示2進位
  '00000111'
  >>> f'{7:08b}'          # 將整數轉為2進位字串，0表示填充內容(也只能為0)，8為字串長度8，b表示2進位
  '00000111'
  >>> '{:b}'.format(7)    # 將整數轉為2進位字串
  '111'
  >>> int('111', 2)       # 將2進位字串轉回整數
  7
  ```

- 8進位整數: 凡`0o`開頭的數字均表示為8進位，可使用`oct()`函數或`format(num, 'o')`函數或`f-string`將一般整數數字轉換為8進位，使用`int('xxx', 8)`將字串轉回整數。

  ```bash
  >>> x = 0o11            # 設定變數為8進位
  >>> x
  9
  >>> oct(9)              # 將整數轉為8進位字串
  '0o11'
  >>> format(9, 'o')      # 將整數轉為8進位字串
  '11'
  >>> f'{9:o}'            # 將整數轉為8進位字串
  '11'
  >>> f'{9:010o}'         # 將整數9轉為8進位字串，0表示填充內容(也只能為0)，10為字串長度10，o表示8進位
  '0000000011'
  >>> '{:o}'.format(9)    # 將整數轉為8進位字串
  '11'
  >>> int('11', 8)        # 將8進位字串轉回整數
  9
  ```

- 16進位整數: 凡`0x`開頭的數字均表示為16進位，可使用`hex()`函數或`format(num, 'x')`函數或`f-string`將一般整數數字轉換為16進位，使用`int('xxx', 16)`將字串轉回整數。

  ```bash
  >>> x = 0xa1            # 設定變數為16進位
  >>> x
  161
  >>> hex(161)            # 將整數轉為16進位字串
  '0xa1'
  >>> format(161, 'x')    # 將整數轉為16進位字串
  'a1'
  >>> f'{161:x}'          # 將整數轉為16進位字串
  'a1'
  >>> f'{161:04x}'        # 將整數161轉為16進位字串，0表示填充內容(也只能為0)，4為字串長度4，x表示16進位
  '00a1'
  >>> '{:x}'.format(161)  # 將整數轉為16進位字串
  'a1'
  >>> int('a1', 16)       # 將16進位字串轉回整數
  161
  ```

> 參考: [https://www.geeksforgeeks.org/integer-to-binary-string-in-python/](https://www.geeksforgeeks.org/integer-to-binary-string-in-python/)

## 資料型態強制轉型

- `int()`: 將資料型態強制轉換為**整數**, 第二個傳參表示進位,沒帶預設為10進位
- `float()`: 將資料型態強制轉換為**浮點數**

  ```bash
  >>> x = 1.23
  >>> y = int(x) + 5
  >>> type(y)
  <class 'int'>
  >>> print(y)
  6
  >>> x = 10
  >>> y = float(x) + 10
  >>> type(y)
  <class 'float'>
  >>> print(y)
  20.0
  ```

## 布林值資料型態

Python布林用`True`(真)與`False`(偽)來表示，資料型態為`bool`，若將布林值用`int()`函數轉換為數字則`True`會得到**1**，`False`會得到**0**。  
若布林與整數相加會被自動轉換為數值，可用`bool()`來將資料轉換成**True**或**False**，若資料為0或空資料會被轉為**False**

```bash
>>> x = True
>>> type(x)
<class 'bool'>
>>> y = x + 1
>>> print(y)
2
>>> z = x - 1
>>> print(z)
0
>>> z = x - 1.1 # 會被自動轉為浮點數做計算,但看起來跟JS一樣走IEEE 754,會遇到逼近進位問題
>>> print(z)
-0.10000000000000009
>>> bool()  # 以下資料會被bool()函數視為False
False
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool(None)
False
>>> bool(())
False
>>> bool([])
False
>>> bool({})
False
>>> bool(1) # 至於其他皆會被視為True
True
>>> bool(-1)
True
>>> bool([1,2,3])
True
```

Ref: [https://docs.python.org/zh-tw/3/tutorial/floatingpoint.html](https://docs.python.org/zh-tw/3/tutorial/floatingpoint.html)

## 字串資料型態

字串(string)資料是指**兩個單引號**(')或**兩個雙引號**(")之間的任意個數字元符號的資料，資料型態為`str`。  
字串的相加可用運算子 `+` 來將字串串聯成一串

```bash
>>> x = 'test123'
>>> type(x)
<class 'str'>
>>> x = 'Hello'
>>> y = 'Python'
>>> z = x + y
>>> print(z)
HelloPython
```

若字串長度須超過一列，可用三個單引號(或三個雙引號)將字串包夾即可，但此法會有換行符號，  
若要避免換行符號，可在列末端增加 `\` 符號，就可避免字串被換行。也可用 `"` 符號但末端也須增加 `\` 符號，或使用小括號來定義字串。  
若字串內有特殊字元，例如:單引號或雙引號...等，必須在此字元前加上`\`(反斜線)當作**逸出字元**(Escape Character)。

```bash
>>> x = '''test line one
... line two
... line three'''
>>> print(x)  # 有換行符號
test line one
line two
line three
>>> y = '''test line one \
... line two \
... line three'''
>>> print(y) # 沒有換行符號
test line one line two line three
>>> x2 = "test line one " \
... "line two " \
... "line three"
>>> print(x2) # 沒有換行符號，因為末端增加 '\' 符號，造成換列功能失效，所以這三列才會被連接成一列
test line one line two line three
>>> x3 = ("test line one "
... "line two "
... "line three")
>>> print(x3) # 沒有換行符號，因為小括號內的敘述會被當作一列，所以這三列才會被連接成一列
test line one line two line three
>>> s = 'i\'m who im'  # 增加逸出字元'\'
>>> print(s)
i'm who im
>>> s2 = "check the \"type()\" function"
>>> print(s2)
check the "type()" function
>>> s3 = "type \\"
>>> print(s3)
type \
>>> s4 = "line one \nline two" # 輸入逸出字元\n表示換行
>>> print(s4)
line one
line two
>>> s4 = r"line one \nline two" # 字串前加r來防止逸出字元被轉逸，等同讓逸出字元無效
>>> print(s4)
line one \nline two
```

[參考更多的逸出字元](https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences)

## str()函數

`str()`可用來將資料轉為字串，用法很多種，列舉如下:

```bash
>>> x = str() # 設定空字串
>>> x
''
>>> x = str('ABC') # 設定字串
>>> x
'ABC'
>>> x = str(123)
>>> x
'123'
>>> type(x)
<class 'str'>
```

## 字串與字元

Python沒有所謂的字元(character)，一個英文字元在電腦中被儲存成 **8bit** 的一連串0與1，儲存的編碼簡稱`ASCII`，ASCII用 0 ~ 127 定義一個字元，包含33個控制字元(無法顯示)。  

可用`chr(x)`函數來取得輸入的x(數字)的ASCII或Unicode字元。  
Unicode使用**16位元**定義文字，等於有2的16次方(65536)個字元，定義方式是以 `\u` 開頭後面有4個16進位的數字，也就是從`\u0000` ~ `\uFFFF`，漢字的Unicode編碼範圍是 `4E00-9FBB`。  
Unicode編碼中，前128個碼值是保留給ASCII使用，在應用中很常使用`ord()`函數來

```bash
>>> chr(97)         # 將數字轉為ASCII的'a'字元
'a'
>>> ord('a')        # 將Unicode的'a'字元轉回數值
97
>>> chr(0x570b)     # 將數字轉為Unicode的'國'字元
'國'
>>> hex(ord('國'))  # 將Unicode的'國'字元轉回數值(16進位表示)
'0x570b'
```

## UTF-8編碼

utf-8是針對Unicode字符集的**可變長度編碼方式**，utf-8使用1~4個byte來表示一個字符。
對於ASCII字符而已，utf-8用一個byte來儲存ASCII字元，byte的第一個位元(最高位)為0，  
對於中文字就須要3個byte的Unicode而言，第一個byte的前3個位元皆設為1，第4位設為0，
後面第二個和第三個byte的前2位是10，其他則是此中文字的Unicode碼。

公式如下:

```bash
1110xxxx 10xxxxxx 10xxxxxx
```

轉換範例如下:

| utf-8中文編碼規則 | 1 | 1 | 1 | 0 | x | x | x | x | 1 | 0 | x | x | x | x | x | x | 1 | 0 | x | x | x | x | x | x |
| :-----| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| 國的Unicode編碼 |  |  |  |  | 0 | 1 | 0 | 1 |  |  | 0 | 1 | 1 | 1 | 0 | 0 |  |  | 0 | 0 | 1 | 0 | 1 | 1 |
| 國的utf-8編碼 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 |

'國'字的編碼如下:
=> (Unicode) \u570b => 5:0101 | 7: 0111 | 0: 0000 | b: 1011  
=> (utf-8) 0xE59C8B => E:1110 | 5:0101 | 9:1001 | C:1100 | 8:1000 | B:1011  
