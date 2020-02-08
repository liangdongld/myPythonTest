# 正则表达式 —— 字符串匹配
# [121234] 一个中括号只能匹配一个字符
# . 匹配除了换行符以外的任意字符
# \w 匹配字母数字下划线 word     \W 匹配非字母数字下划线
# \s 匹配任意的空白符 space      \S 匹配非空白符
# \d 匹配数字 digit             \D 匹配非数字
# [\s\S] [\d\D] [\w\W]与 . 的区别是可以匹配换行符
# \n 匹配一个换行符  \t 匹配一个制表符
# \b 匹配一个单词的结尾
# ^ 匹配字符串的开头（相当于startwith）    $ 匹配字符串的结尾（相当于endwith)  两个一起用会约束整个字符串
# a|b 匹配a或者b  优先匹配a  因此长的放前
# [^a-z]匹配除a-z之外的字符
""" 量词 """
# * 匹配0次或多次 贪婪匹配（越多越好）
# + 匹配1次或多次
# ? 重复0次或1次
# {n} 重复n次
# {n,} 重复n次以上
# {n,m} 重复n到m次
# 所有的量词只能跟在匹配规则的后边 先规则后量词
# 量词后加上?表示非贪婪匹配
