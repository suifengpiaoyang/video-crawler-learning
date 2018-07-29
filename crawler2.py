"""

流式下载视频文件

"""
import requests
import time

url = "http://v11-tt.ixigua.com/b2c6ea9f33f78434684e72a7585402a5/5b59b7cf/video/m/22080158596d8b2481181fd2bb5b9b15416115967640000679f8ec23ce9/"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36 OPR/54.0.2952.60',
}
res = requests.get(url,headers = headers,stream = True)
video_size = 0
"""
iter_content后面的参数chunk_size的单位是字节，chunk_size = 1024，内存每次读取 1 k .
res.headers['content-length']
"""
if res.status_code == requests.codes.ok:
    print('视频访问成功，现在开始下载...')
    with open('test2.mp4','wb')as fl:
        for chunk in res.iter_content(chunk_size = 1024):
            if chunk:
                # time.sleep(3)
                fl.write(chunk)
                video_size += 1
    print('视频下载成功，大小为{}k。'.format(video_size))
    print(video_size)
else:
    print('视频下载失败。错误代码：{}'.format(res.status_code))
