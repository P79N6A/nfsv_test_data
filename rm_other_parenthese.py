import re

test_text = u'[文/观察者网 张晨静]竟…竟然失焦了？有网友(NicknameYang)对此表示十分不满，我们花了21亿美元，就给我们看这样模糊的照片？！（注：实际上“洞察号”斥资8.28亿美元）'

result = re.sub('\(.*?\)|（.*?）|\[.*?\]', '', test_text)
# result = re.sub('（.*?）', '', result)

print(result)
