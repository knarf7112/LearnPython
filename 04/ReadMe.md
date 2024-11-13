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
