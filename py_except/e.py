import codecs
import json

def open_file(file_name):
    try:
        with codecs.open(file_name, encoding='utf8') as f:
            video_json = json.load(f)
    except Exception as e:
        print('open_file')
        print(e)
        raise e

    if video_json1 is None:
        print('what???')
    else:
        return video_json


def get_json_field(file_name, field_name):
    try:
        video_json = open_file(file_name)
    except Exception as e:
        print('get_json_field')
        print(e)
        return e
    if field_name in video_json:
        return video_json[field_name]

if __name__ == '__main__':
    file_name = 'v_16787259158239898906.json'
    # file_name = 'v_16787259158239898906.json1'
    value = get_json_field(file_name, 'errno')
    print(value)
