#Q1:find the odd numbers in data1 and represents as a set odd. print(odd)
data1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even = {2, 4, 6, 8, 10}
odd = (data1 ^ even)
print(odd)


#Q2:find the index of '歡樂水' in data2 and print '歡樂水', print(data2...)
data2 = ('moda', ('走', '了'), ('買', '肥宅', '歡樂水'))
print(data2[2][2])

# Q3:
# 3.1 計算data3所有數字的總和
data3 = {39, 12, 61, 10, 3, 99, 78, 87, 93, 11, 666, 999}
print(sum(data3))
# 3.2 找出data3內最大的數字, data3_max, 及最小的數字 data3_min, print(data3_max), print(data3_min)
print((max(data3)))
print((min(data3)))

# 3.3 分別將 data3 的數字由大到小排序 print(data_desc), 由小到大排序 print(data_asc)
print(sorted(data3,reverse = True))
print(sorted(data3))
# Q4:
#4.1 將'moda'換成'米血', 並將data4 轉成字串, 印出 '米血走了~ 買肥宅歡樂水'
data = ['moda', '走', '了', '~ ', '買', '肥宅', '歡樂水']
data [0]='米血'
data=''.join(data)
print(data)


# 4.2 將data4轉成字串, 順序跟原本的data4相反, 印出 '歡樂水肥宅買~ 了走moda'
data4 = ['moda', '走', '了', '~ ', '買', '肥宅', '歡樂水']
data4=''.join(data4[::-1])
print(data4)


