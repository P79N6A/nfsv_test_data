from bs4 import BeautifulSoup

test_text = '据报道，美国国家航空航天局（NASA）于去年启动姓名征集活动。全球各地的申请者在NASA官网填写自己的姓名信息，这些名字被刻在特制芯片上，搭载&quot;洞察&quot;号（InSight）探测器前往火星。最终，搭车奔赴火星的姓名达到240万个，约26万来自中国。'


result = BeautifulSoup(test_text,features="html.parser")

import pdb;pdb.set_trace()
print(result)


re.sub('\(.*?\)|（.*?）|\[.*?\]|【.*?】', '', summary[summary_idx])
