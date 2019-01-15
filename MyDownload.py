#coding:utf-8
import sys, os
import json,time
import requests
requests.packages.urllib3.disable_warnings()
def download(url, file_path):
    # verify=False 这一句是为了有的网站证书问题，为True会报错
    r = requests.get(url, stream=True, verify=False)
    if r.status_code == 200:
        chunk_size=1024
        start = time.time()
        total_size = int(r.headers['Content-Length'])
        temp_size = 0
        print('[文件大小]：%0.2f MB'%(total_size / chunk_size / 1024))
        with open(file_path+'.mp4', "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    temp_size += len(chunk)
                    f.write(chunk)
                    f.flush()
                    done = int(50 * temp_size / total_size)
                    sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                    sys.stdout.flush()
        end=time.time()
        print('\n'+'下载完成！用时%.2f秒'%(end-start))
    else:
        print('请求失败')
