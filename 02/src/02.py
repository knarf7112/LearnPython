import math

r = 5
area = math.pi * r * r # math為Python內建模組,使用前須import導入模組,就可使用模組內的pi屬性
print('園面積:')
print(area)

# 輸出內建函數
print('輸出內建函數名稱')
builtin_functions = dir(__builtins__)
for function_name in builtin_functions:
  print('方法名稱:' + function_name)

