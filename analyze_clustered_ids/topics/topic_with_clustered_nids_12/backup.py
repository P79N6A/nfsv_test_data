# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
################################################################################

"""
Cut all the videos for one topic into video snippets. For example,
v_123.json, v_456.json are video meta data for one topic. We will download the video
from each JSON and cut it based on fast-cut criteria. Tools needs are as below:

PySceneDetect
OpenCV (required by PySceneDetect)
ffmpeg

For v_123.json, we will create a folder : v_123/, and download the video as v_123.mp4.
We then will cut the video into snippets based on its content. For example, v_123.mp4 might be
cut into

v_123-001.mp4
v_123-002.mp4
v_123-003.mp4

"""

from subprocess import call
import os
import sys
import json
import codecs
import requests
import pdb;pdb.set_trace()
# scenedetect -i yansehu1.mp4 detect-content -t 40   split-video
# scenedetect_cmd = 'scenedetect -i yansehu1.mp4 detect-content -t 40 split-video'
# call(scenedetect_cmd.split())


def process_one_video_file(topic_path, video_json_filename):
    print('video_json_filename')
    print(video_json_filename)
    filename = video_json_filename.split('.')[0]
    split_vidoes_folder = topic_path + filename + '/'

    try:
        if not os.path.exists(split_vidoes_folder):
            os.makedirs(split_vidoes_folder)
    except OSError:
        print ('Error: Creating directory of ' + split_vidoes_folder)
        return

    try:
        with codecs.open(topic_path + video_json_filename, encoding='utf8') as f:
            video_json = json.load(f)
    except Exception as e:
        print(e)
        return

    if ('data' not in video_json
            or len(video_json['data']) != 1
            or 'realurl' not in video_json['data'][0]
            or '.mp4' not in video_json['data'][0]['realurl']):
        print('Video JSON is missing required fields')
        return

    realurl = video_json['data'][0]['realurl']
    get_response = requests.get(realurl, stream=True)
    video_file_position = split_vidoes_folder + filename + '.mp4'
    with open(video_file_position, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

    ###
    print('download done')

    ### scenedetect template
    scenedetect_cmd = 'scenedetect -i %s detect-content -t 40 split-video --output %s'
    try:
        call((scenedetect_cmd % (video_file_position, split_vidoes_folder)).split())
    except Exception as e:
        print('Cannot cut video into snippets. Maybe because the whole video is continuous.')
        print(e)

    video_files = [item for item in os.listdir(split_vidoes_folder)
                   if os.path.isfile(os.path.join(split_vidoes_folder, item))]

    print('video_files')
    print(video_files)
    raw_video_filename = video_json_filename.split('.')[0] + '.mp4'

    for video_file in video_files:
        if raw_video_filename == video_file:
            continue
        if 'Scene-001' in video_file:
            continue
        # ffmpeg -ss 00:00:01 -i v_10259870823270508927-Scene-002.mp4 -c copy v_10259870823270508927-Scene-002_headcut.mp4
        headcut_cmd = 'ffmpeg -ss 00:00:01 -i %s -c copy %s'

        try:
            headcut_filename = video_file.split('.')[0]+'_headcut'+'.mp4'
            call((headcut_cmd % (split_vidoes_folder+video_file, split_vidoes_folder+headcut_filename)).split())
        except Exception as e:
            print('Cannot cut the heading 1 sec by ffmpeg.')
            print(e)

def cut_videos(topic_path):
    if topic_path[-1] != '/':
        topic_path += '/'
    news_files = [item for item in os.listdir(topic_path)
             if os.path.isfile(os.path.join(topic_path, item))]
    print(news_files)
    n = 5
    for news_file in news_files:
        if news_file[0] == 'v':
            # This is a video file, we need to
            process_one_video_file(topic_path, news_file)
            if n == 1:
                break
            n += 1
if __name__ == '__main__':
    topic_path = './topic_with_clustered_nids_12/'

    cut_videos(topic_path)
