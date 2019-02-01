test_list = ['邓(aas )ababab(紫棋)(资料图):', '原文如下：', '所有专门来看我的歌迷，你们的留言我看到，也很理解大家的心情，很抱歉让你们受了这些委屈！我已经跟公司沟通了，会让主办方给大家一个说法！对不起！！！”', '“今日我司所属艺人G.E.M.邓紫棋在广东省中山市参加的《All In 2 VIP》演出，为普通商业演出合作，约定演出曲目为4首歌。演出主办方擅自将此活动篡改为演唱会形式，以此为名义进行误导性宣传，蒙骗广大歌迷。', '前述行为引发了非常恶劣的影响，我司已收到众多被误导购票的歌迷投诉！此举严重违反双方合作协议，我司予以强烈谴责，并保留对主办方追究法律责任的权利！”(新娱)']

import re
import pdb;pdb.set_trace()
def cleanup(summary):
    for summary_idx in range(0, len(summary)):
        # cur_sentence = summary[summary_idx]
        summary[summary_idx] = re.sub('\(.*?\)', '', summary[summary_idx])
        summary[summary_idx] = re.sub(':', u'说', summary[summary_idx])

        # left_parenthesis = []
        # right_parenthesis = []
        # for word_idx in range(0, len(cur_sentence)):
        #     cur_word = cur_sentence[word_idx]
        #     if cur_word == '(':
        #         left_parenthesis.insert(0, word_idx)
        #     if cur_word == ')':
        #         right_parenthesis.insert(0, word_idx)
        # print(left_parenthesis)
        # print(right_parenthesis)
        #
        # print('splice')
        # pieces = list(cur_sentence)
        # for parenthesis_idx in range(0, min(len(left_parenthesis), len(right_parenthesis))):
        #     left_parenthesis_idx = left_parenthesis[parenthesis_idx]
        #     right_parenthesis_idx = right_parenthesis[parenthesis_idx]
        #     del pieces[left_parenthesis_idx:(right_parenthesis_idx+1)]
        # summary[summary_idx] = ''.join(pieces)
        # break


print(test_list)
print('after')
cleanup(test_list)
print(test_list)
