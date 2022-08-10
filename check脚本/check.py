# -*- coding:utf8 -*-
import requests

#除了返回的正常/错误，其余不输出任何信息，且需要设置超时时间！

safe_code=[302,200]

def check_sign_up(ip,url):
    try:
        res = requests.get(url, timeout=10)
        code = res.status_code
        if code not in safe_code:
            raise Exception("Load failed")
        data = {
            'email' : '123@abc.com',
            'nickname' : 'nickname_test',
            'password1' : 'pwd_test',
            'password2' : 'pwd_test'
            }
        res = requests.post(url, data)
        if res.url == 'http://'+ip+'/' :
            pass
        else:
            raise Exception("Sign up failed.")
    except Exception as e:
        raise Exception("Page 'sign up' error",e) 
    return True

def check_login(url):
    try:
        res = requests.get(url,timeout=10)
        code = res.status_code
        if code not in safe_code:
            raise Exception("Load failed")
        data = {
            'email' : '123@abc.com',
            'password' : 'pwd_test',
            }
        res = requests.post(url, data)
        if res.url == 'http://'+ip+'/' :
            pass
        else:
            raise Exception("Sign up failed.")
    except Exception as e:
        raise Exception("Page 'login' error.",e) 
    return True

def check_profile(url):
    try:
        session = requests.session()
        res = session.get(url,timeout=10)
        data = {
            'email' : '123@abc.com',
            'password' : 'pwd_test',
            }
        res0 = session.post(res.url, data)
        res1 = session.get(res0.url+'profile/1')
        code = res1.status_code
        if code not in safe_code:
            raise Exception("Load profile failed")
    except Exception as e:
        raise Exception("Page 'profile' error.",e) 
    return True

def check_edit(url):
    try:
        session = requests.session()
        res = session.get(url,timeout=10)
        data = {
            'email' : '123@abc.com',
            'password' : 'pwd_test',
            }
        res0 = session.post(res.url, data)
        res1 = session.get(res0.url+'edit')
        code = res1.status_code
        if code not in safe_code:
            raise Exception("Load edit failed")
    except Exception as e:
        raise Exception("Page 'edit' error.",e) 
    return True

def check_upload(url):
    try:
        session = requests.session()
        res = session.get(url,timeout=10)
        data = {
            'email' : '123@abc.com',
            'password' : 'pwd_test',
            }
        res0 = session.post(res.url, data)
        res1 = session.get(res0.url+'upload')
        code = res1.status_code
        if code not in safe_code:
            raise Exception("Load upload failed")
    except Exception as e:
        raise Exception("Page 'upload' error.",e) 
    return True

def check_changepassword(url):
    try:
        session = requests.session()
        res = session.get(url,timeout=10)
        data = {
            'email' : '123@abc.com',
            'password' : 'pwd_test',
            }
        res0 = session.post(res.url, data)
        res1 = session.get(res0.url+'change-password')
        code = res1.status_code
        if code not in safe_code:
            raise Exception("Load change-password failed")
    except Exception as e:
        raise Exception("Page 'change-password' error.",e) 
    return True

def check_logout(url):
    try:
        session = requests.session()
        res = session.get(url,timeout=10)
        data = {
            'email' : '123@abc.com',
            'password' : 'pwd_test',
            }
        res0 = session.post(res.url, data)
        res1 = session.get(res0.url+'logout')
        code = res1.status_code
        if code not in safe_code:
            raise Exception("Logout failed")
    except Exception as e:
        raise Exception("Logout error",e) 
    return True

def check_index(url):
    try:
        res = requests.get(url+'/index')
        if res.status_code != 500:
            raise Exception("SSTI is not available")
    except Exception as e:
        raise Exception("SSTI error",e) 
    return True

def checker(host):
    try:
        url = "http://"+ip
        if check_sign_up(ip,url+'/sign-up') and check_login(url+'/login') and check_profile(url) and check_edit(url) and check_upload(url) and check_changepassword(url) and check_logout(url) and check_index(url):
            return (True, "IP: " + host + " is OK")
    except Exception as e:
        return (False, "IP: "+host+" is down, "+str(e) + " Are you sure the IP you just entered is right?")

if __name__ == '__main__':
    ip = input('Enter the IP you want to Check like "1.1.1.1:80" : ')
    ip = str(ip)
    print("\n" + 'Checking...' + '\n')
    print(checker(ip))
