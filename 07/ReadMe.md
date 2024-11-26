# 迴圈

## 基本for

for迴圈讓程式可以將整個物件內的元素**遍歷(也稱迭代)**，在遍歷期間，可記錄或輸出每次的狀態或**軌跡**。  
可迭代物件可以是串列、元祖、字典、集合、或`range()`，`enumerate`也可迭代，但須注意跑完一次loop後指標就轉移到底部了。  
注意Python須留意縮排是否對齊。  

```python
for var in 可迭代物件:
  程式碼區塊

>>> mobiles = ['Apple', 'Oppo', 'Samsung', 'Vivo', 'Mi', ]
>>> for mobile in mobiles:
>>>     print(f'mobile={mobile}')
mobile=Apple
mobile=Oppo
mobile=Samsung
mobile=Vivo
mobile=Mi
>>> enumerate_mobiles = enumerate(mobiles)
>>> for index, mobile in enumerate_mobiles: print(f'index={index}, data={mobile}') # 跑第一次可將所有數據與索引依序輸出
index=0, data=Apple
index=1, data=Oppo
index=2, data=Samsung
index=3, data=Vivo
index=4, data=Mi
>>> for index, mobile in enumerate_mobiles: print(f'index={index}, data={mobile}') # 跑第二次則沒有任何輸出
```

## `range()` 函數

Python可使用 `range()` 函數產生一個**等差級序列**，此物件也是一個**可迭代物件(iterable object)**。  
用法類似 `slice()` 函數，由於可迭代物件占用一些記憶體空間，所以這類的物件跑迴圈時，需要較多的系統資源，此時可使用 `range()` 函數，因這類迭代只有迭代時的計數指標需要記憶體，可節省許多記憶體空間。

```python
    range(start=0, stop, step=1)
    # stop是唯一必要的值，型態為整數
    # start預設為0，step預設為1，即可迭送物件的範圍起始從start開始到stop - 1為止，每次跑step次
    # 若將step設為 -1，表示此迭代物件是遞減的方式跑回圈

>>> for x in range(0, 3): print(x)
0
1
2
>>> for x in range(3): print(x)
0
1
2
>>> for x in range(3, 0, -1): print(x)
3
2
1
>>> for x in range(3, -3, -2): print(x)
3
1
-1
>>> sum_ = sum(range(0, 10))   # 此方式不是每次都預留0,1,2, ...10的記憶空間，而是只有一個記憶體空間，每次將迭代的指標放在此空間，然後執行sum()運算，所以可增加工作效率並節省系統記憶體空間
>>> print(f'總和:{sum_}')
總和:45
```

## 串列生成(list generator)的應用

**生成式(generator)**是一種使用迭代方式產生Python數據資料的方式。

> 新串列 = [運算式 for 項目 in 可迭代物件]  
> 運算式會將每次的項目套入該運算並產生結果

```python
>>> xlist = [n for n in range(6)]
>>> xlist
[0, 1, 2, 3, 4, 5]
>>> square = [num * 2 for num in range(1, 10)]  # 每次的迭代後的值會去執行運算 也就是num * 2，然後記錄在該串列上
>>> square
[2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> # 以下是應用於畢氏定理(a^2 + b^2 = c^2: c是斜邊長)上的範例: (3個for迴圈是3層內嵌迴圈,第一層是a,第二層是b,第三層是c,最內層是一個判斷條件成立才返回該次迭代用的)
>>> x = [[a, b, c] for a in range(1, 20) for b in range(a, 20) for c in range(b, 20) if a ** 2 + b ** 2 == c ** 2]
>>> x
[[3, 4, 5], [5, 12, 13], [6, 8, 10], [8, 15, 17], [9, 12, 15]]
>>> result = [[color, shape] for color in colors for shape in shapes] 
>>> result
[['Red', 'Circle'], ['Red', 'Square'], ['Green', 'Circle'], ['Green', 'Square'], ['Blue', 'Circle'], ['Blue', 'Square']]
'''
上面generator方式類似，只是比較省記憶體空間
x = []
for color in colors:
    for shape in shapes:
        x.append([color, shape])
'''
```

## for...else 迴圈

跑for迴圈時，若希望所有的if判斷均是 `False` 時，在最後一次迴圈後，可執行特定程式區塊，可使用此指令。  
此指令通常和 `if` 和 `break` 配合使用，語法如下:

```python
for var in 可迭代物件:
    if 條件運算式:     # 若條件運算為True，則離開for迴圈      
        程式碼區塊1
        break
else:
    程式碼區塊2        # 最後一次迴圈的條件運算式是 False 就會執行此區塊
```

範例:  

```python
>>> for n in range(2, 7):
...     print(f'n={n}')
...     if n > 5:
...         print(f'n={n} > 5')
... else:                                           # 執行到最後一次迴圈後，會執行else的區塊
...     print('完整執行完所有迴圈後，就會執行此區塊')
...     
n=2
n=3
n=4
n=5
n=6
n=6 > 5
完整執行完所有迴圈後，就會執行此區塊
>>> for n in range(2, 6):
...     print(f'n={n}')
...     if n > 5:
...         print(f'n={n} > 5, 跳過after')
...         continue
...     print(f'n={n}[after]')
... else:                                            # 執行到最後一次迴圈後，會執行else的區塊
...     print('完整執行完所有迴圈後，就會執行此區塊')
... 
n=2
n=2[after]
n=3
n=3[after]
n=4
n=4[after]
n=5
n=5[after]
完整執行完所有迴圈後，就會執行此區塊
>>> for n in range(2, 7):
...     print(f'n={n}')
...     if n > 5:
...         print(f'n={n} > 5, 離開for loop...')     
...         break
...     print(f'n={n}[after]')
... else:                                           # 因不會執行到最後一次迴圈，所以不會執行else的區塊
...     print('完整執行完所有迴圈後，就會執行此區塊')
... 
n=2
n=2[after]
n=3
n=3[after]
n=4
n=4[after]
n=5
n=5[after]
n=6
n=6 > 5, 離開for loop...
```

## while 迴圈

類似for迴圈，但是執行到條件運算為 `False` 才會離開迴圈。

語法如下:

```python
while 條件運算:
    程式碼區塊
```

範例:

```python
>>> index = 0
>>> while index <= 10:
...     index += 1
...     if index % 2:
...         continue              # 執行continue後，就會跳過後面的敘述並執行下一次的迴圈
...     print(f'index={index}')
... 
index=2
index=4
index=6
index=8
index=10
>>> index = 1
>>> while index <= 10:
...     index += 1
...     if index % 2:
...         break                # 執行break後，就會跳離 while 迴圈
...     print(f'index={index}')
... 
index=2
```

## while迴圈的條件運算式與可迭代物件

while迴圈也可與迭代物件配合使用，語法如下:

```python
# 方式1
while var in 可迭代物件:                 # 若var in 可迭代物件是True，則繼續該迴圈
    程式碼區塊

# 方式2
while 可迭代物件:                        # 若迭代物件是空的才結束迴圈
    程式碼區塊
```

範例:

```python
>>> nums = [5, 4, 3, 2, 1]
>>> key = 3
>>> while key in nums:             # 當key值存在於nums就執行迴圈內容，否則就離開while迴圈
...     print(f'開始移除{key}')
...     nums.remove(key)
... 
開始移除3
>>> nums
[5, 4, 2, 1]
>>> while nums:                    # 當nums仍可迭代就繼續該迴圈，否則離開while迴圈
...     print(f'pop nums, num={nums.pop()}')
... 
pop nums, num=1
pop nums, num=2
pop nums, num=3
pop nums, num=4
pop nums, num=5
>>> nums
[]
```

## 無限迴圈與`pass`

若想建立一個無限迴圈，可使用以下寫法:

```python
## 方式1
while True:
    pass
## 方式2
while 1:
   pass
```

## enumerate物件與for迴圈

enumerate物件由`索引`與`元素值`組成，可用for loop，一般物件是無法得知每個元素的索引，所以需要用enumerate物件來列舉索引資訊。

```python
>>> num_list = ['a', 'b', 'c']
>>> for index, num in enumerate(num_list):
...     print(f'index={index}, num={num}')
... 
index=0, num=a
index=1, num=b
index=2, num=c
```
