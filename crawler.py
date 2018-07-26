import requests

url = "http://v1-tt.ixigua.com/b8e9b5eb9e42620eb1ebb469b0c9b3b0/5b59a894/video/m/22080158596d8b2481181fd2bb5b9b15416115967640000679f8ec23ce9/"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36 OPR/54.0.2952.60',
}
res = requests.get(url,headers = headers)
if res.status_code == requests.codes.ok:
    with open('test.mp4','wb')as fl:
        fl.write(res.content)
    print('视频下载成功。')
else:
    print('视频下载失败。错误代码：{}'.format(res.status_code))