# Input / Output

## 格式化輸出資料

使用`print()`函數可輸出資料，依據傳入參數讓輸出的資料作格式化。  

字串格式化有以下3種:

1. 使用 `%` : 可用於Python 2.x ~ 3.x
2. 使用 `{}` 和 `format()` : 可用於Python 2.6 ~ 3.x
3. 使用 `f-strings` : 可用於Python 3.6以上

## `print()` 基本語法

基本語法如下:

```text
  print(value, ..., sep=" ", end="\n", file=sys.stdout, flush=False)
  
  參數:
  value 表示要輸出的資料可一次出多筆資料，各資料用逗號隔開。
  sep 表示當輸出多筆資料時的分隔字元，預設是**空白字元**
  end 表示當輸出資料結束時最後所插入的字元，預設是 **換列字元**
  file 表示資料要輸出的位置，預設是 **stdout**，也就是螢幕，可以將輸出更換為其他檔案或設備或db
  flush 表示是否清除資料流的緩衝區，預設是 **不清除**
```

範例如下:

```python
>>> print('test', '123', 'qoo')
test 123 qoo
>>> print('test', '123', 'qoo', sep = "+")
test+123+qoo
>>> print('test', '123', 'qoo', sep = "+", end = "\n")
test+123+qoo
```

## `print()`輸出並使用 `%` 格式化字串

```text
  "...輸出格式化區..." % (變數系列區, ...)
```

**輸出格式化區** 中，可放置 **變數系列區** 相對應的格式化字元，列表如下:

* `%d` : 格式化整數輸出
* `%f` : 格式化浮點數輸出
* `%x` : 格式化16進位整數輸出
* `%X` : 格式化大寫16進位整數輸出
* `%o` : 格式化8進位整數輸出
* `%s` : 格式化字串輸出
* `%e` : 格式化科學記號e的輸出
* `%E` : 格式化科學記號大寫E的輸出

ex:

```python
>>> print('%s' % '測試字串')
測試字串
>>> print('%d' % 123.456)
123
>>> print('%f' % 123.456)
123.456000
>>> x = 123.456
>>> '%f' % x
'123.456000'
>>> print('%o' % 15)
17
>>> print('%e' % 123456)
1.234560e+05
>>> print('%E' % 123456)
1.234560E+05
>>> print('%x' % 255)
ff
>>> print('%X' % 255)
FF
>>> x,y,z=123,'測試',True
>>> print('%s的數字是%d, bool是%s' %(y, x, z))
測試的數字是123, bool是True
```

## 更精準控制格式化的輸出

```python
>>> '%5d' % 123           # %5d的5表示針對整數的保留格數，若整數長度不足5就會補空格至滿5個長度
'  123'
>>> '%+5d' % 123          # (+)正號表示當整數為正數時顯示+號
' +123'
>>> '%-5d' % 123          # (-)負號表示若字串長度不足靠左對齊並補上空格
'123  '
>>> '%5d' % 123456        # 當整數長度超過5，就不會再補空格
'123456'
>>> '%10.2f' % 12.3456    # %10.2f的10表示針對整個浮點數長度要保留10個(包含小數位)，若長度不足10就會補空格至整個長度為10為止，2表示小數部分要保留的位數，會自動四捨五入
'     12.35'
>>> '%3x' % 255            # %3x的3表示針對16進位的資料長度的保留格數，若16進位長度不足3就會補空格至長度為3
' ff'
>>> '%3.1s' % '測試'       # %3.1s的3表示顯示到輸出的長度為3(不足會補空格)，1表示字串的長度僅能1(超過的字串會被捨棄)
'  測'
>>> '%-3.1s' % '測試'      # (-)負號表示若字串長度不足靠左對齊並補上空格
'測  '
>>> '%3s' % '測試'
' 測試'
```

## `{}` 與 `format()` 函數

這是Python增強格式化輸出的功能，目的是讓字串使用format方法來格式化。

```text
  "...輸出格式化區...".format(變數系列區, ...)
```

**輸出格式化區** 內的變數使用 `{}` 來表示，範例如下:

```python
>>> x,y,z = "測試字串格式化",123,True
>>>
>>> "x={} y={} z={}".format(x, y, z)                 # 依序帶入參數 
'x=測試字串格式化 y=123 z=True'
>>> "x={1} y={2} z={0}".format(x, y, z)              # 也可指定參數依據的順序
'x=123 y=True z=測試字串格式化'
>>> "x={a} y={b} z={c}".format(a = x, b = y, c = z)  # 使用具名參數來帶入參數
'x=測試字串格式化 y=123 z=True'
>>> "x={1:>5d} y={2} z={0:>3.2s}".format(x, y, z)    # {n:xx(f|d|s)}內也可做格式化，(>)表示靠右對齊，n表示變數順序，(f|d|s)分別表示格式化浮點數|整數|字串
'x=  123 y=True z= 測試'
>>> "x={1:<5d} y={2} z={0:<3.2s}".format(x, y, z)    # {n:xx(f|d|s)}內也可做格式化，(<)表示靠左對齊
'x=123   y=True z=測試 '
```

## `f-strings`格式化字串

這是Python 3.6版之後才有的格式化方式，類似JavaScript的模板字符串(Template literals)。

```python
>>> x,y,z = "測試字串格式化",123,True
>>>
>>> f'x={x}, y={y}, z={z}'
'x=測試字串格式化, y=123, z=True'
>>> f'x={x:<3.2s}, y={y:>5d}, z={z}'
'x=測試 , y=  123, z=True'
```

## 將資料輸出到檔案

`print()` 函數的`file`參數預設使用 `sys.stdout` 來接結果輸出到螢幕上，但可以變更輸出方式，  
例如使用 `open()` 函數來將結果輸出到檔案內。

[`open()`](https://docs.python.org/zh-tw/3/library/functions.html#open) 函數說明如下:

```python
# file(string) 參數表示指定檔案的路徑位置，若不指名路徑，則預設為開啟目前工作資料夾
# mode表示開啟檔案的模式，預設為r(讀取模式)，mode最多可以有兩個字元，
#  第一個字元(r[讀取] | w[寫入] | a[插入:從檔案內容尾部插入新寫入的資料] | x[開啟新檔並寫入,若開啟的檔案已存在則產生錯誤])
#  第二個字元(b[開啟二進位檔案模式] | t[開啟文字檔案模式:預設])
file_Obj = open(file, mode='r', ...) 


```

寫入檔案範例:

```python
>>> file_obj1 = open('04/test.txt', mode="wt")  # 建立檔案test.txt於 當前工作區的'04'資料夾並產生一個檔案資料流
>>> print('Testing mode=w, using utf-8 format 這是中文字, done', file=file_obj1) # 將文字寫入至記憶體並設定輸出至該檔案資料流(因為沒有設定encoding，所以預設為ANSI(cp950編碼)，所以中文字就變亂碼了)
>>> file_obj1.flush() # 將緩衝區的資料開始寫入檔案
>>> file_obj1.close() # 關閉檔案的資料流
>>>
>>> file_obj2 = open('04/test2.txt', mode="wt", encoding="utf-8")  # 這次指定編碼為utf-8，寫入後就會用utf-8編碼，就可以正常顯示中文字
>>> print('Testing mode=w, using utf-8 format 這是中文字, done', file=file_obj2)
>>> file_obj2.close()
```

## `input()` 輸入資料

可透過 `input()` 來從螢幕的console中讀取使用者輸入的資料，使用者輸入的任何內容均為**字串型態**，且執行到此行時，主執行緒會卡者等用戶輸入，不會再往下繼續執行程序。

```python
>>> val = input("請輸入內容\n") # prompt是使用者會看到的提示訊息,value變數表示從螢幕的console接收到用戶的輸入值()
請輸入內容                      # <=== 這個是使用者看到的提示
test 123 看到了嗎               # <=== 這個是使用者輸入的內容
>>> type(val)
<class 'str'>
>>> val
'test 123 看到了嗎'
```

## 處理數學運算的 `eval()` 函數

Python內建一個計算數學表達式的函數 `eval()`，傳入數學表達式字串後返回計算的結果。

```python
>>> expression = '5 * 9 + 10'
>>> result = eval(expression)
>>> result
55
```

## 查詢模組提供了哪些 `方法` 和 `屬性`

Python 提供了一個內建函數 `dir()` 來查詢模組提供了哪些 `方法` 或 `屬性`。

```python
>>> dir(id)   # 查詢 'id()'函數的所有方法與屬性
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
>>> dir(math) # 查詢 'math'模組的所有方法與屬性
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
```
