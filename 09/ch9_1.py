fruits = { '西瓜': 15, '香蕉': 20, '榴槤': 25 }
var = input('請輸入要刪除的字典變數名稱')
if var in locals():   # 檢查變數名稱是否存在於當下環境
    var = eval(var)   # 執行該敘述(run express, ex: fruits)
    if isinstance(var, dict):  # 若var是dict資料類型返回True
        print(f'"fruits"字典變數存在,開始刪除...')
        del fruits
        print(f'"fruits"刪除成功')
    else:
        print(f'"fruits"字典變數不存在')
else:
    print(f'{var}字典變數不存在')