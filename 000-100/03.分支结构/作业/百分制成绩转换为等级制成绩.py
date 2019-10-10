"""
要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
百分制成绩转换为等级制成绩

Version: 0.1
Author: eraser
"""
fraction = float(input('请输入考生成绩：'))

if fraction >= 90 :
    grade = 'A'
elif 80 <= fraction < 90:
    grade = 'B'
elif 70 <= fraction < 80:
    grade = 'C'
elif 60 <= fraction < 70:
    grade = 'D'
elif 0 <= fraction < 60:
    grade = 'E'
else:
    grade = 'xxx'

if grade == 'A' or grade == 'B' or grade == 'C' or grade == 'D' or grade == 'E':
    print('该学生成绩等级为：%s' % grade)
else:
    print('请输入正确分数')