# 定义字符串 a
a = '[XIAOYU语画界] VOL.598 梦心月性感粉色服饰配开档肉丝裤袜秀高挑身材诱惑写真56P'

# 使用空格作为分隔符，将 a 拆分为多个子字符串，并将前两个子字符串保存到变量 vol 和 title 中
vol, title = a.split(' ')[:2]

# 将 vol 和 title 进行拼接，并保存到新变量 new_a 中
new_a = vol + ' ' + title

# 输出 new_a
print(new_a)