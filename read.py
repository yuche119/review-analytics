data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
print('總共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)
    print(sum_len)

print('平均留言', sum_len/len(data))
#         count += 1
#         if count % 10000 == 0:
#             print(len(data))
# print(data[0])
