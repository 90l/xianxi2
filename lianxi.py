p_list=['l1','l2','l3','l4','l5','l6']
p_keys=['no','name','sex','school','field','qualification','graduation_year','address','is_boarder']
l1_value=[1,'李冬乐','女','辽宁对外经贸学院','信息管理与信息系统','本科',2021,'宁城','是']
l2_value=[2,'刘明鑫','男','内蒙古农业大学','计算机科学与技术','本科',2022,'松山区','否']
l3_value=[3,'刘鑫浩','男','内蒙古师范大学','计算机科学与技术','本科',2020,'敖汉旗','是']
l4_value=[4,'庞颖超','女','内蒙古工业大学','电子信息工程','本科',2021,'敖汉旗','是']
l5_value=[5,'姚佳雨','女','呼伦贝尔学院','计算机网络工程','本科',2022,'红山区','是']
l6_value=[6,'付健伟','男','江南大学','计算机科学与技术','本科',2022,'元宝山区','否']
#addition list to hold l*_value together
list_value=[
    l1_value,
    l2_value,
    l3_value,
    l4_value,
    l5_value,
    l6_value
]
my_dict={key:dict(zip(p_keys,list_value[i]))for i,key in enumerate(p_list)}
print(my_dict)