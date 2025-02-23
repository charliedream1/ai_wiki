对于for循环，一个break只能结束一个对应的for循环，对于嵌套循环，需要多个break才能终止

```python
break_flag = False
for i in range(3):
    for j in range(3):
        print(f'i={i}, j={j}')
        if j == 1:
            # 终止内层循环
            break_flag = True
            break
    # 终止外层循环
    if break_flag:
        break
```