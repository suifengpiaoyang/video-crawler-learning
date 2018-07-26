import requests

url = "http://v6-tt.ixigua.com/video/m/22080158596d8b2481181fd2bb5b9b15416115967640000679f8ec23ce9/?Expires=1532593706&AWSAccessKeyId=qh0h9TdcEMoS2oPj7aKX&Signature=MJr9MRUQZOxHa7CyNrX5W8pm7NM%3D"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36 OPR/54.0.2952.60',
}
res = requests.get(url,headers = headers)
with open('test.mp4','wb')as fl:
    fl.write(res.content)
