import pytest
import requests


class TestBaotao():
    #类变量：通过类名称访问
    access_token =""
    csrf_token =""
    cks = ""
    def get_session(self):
        session = requests.session()
        return session
    #获取验证码
    def test_01_mcheckImg(self):
        url = 'http://localhost:8080/shop/mcheckImg'
        res = requests.get(url = url)
        print(res.json())
        print(res.json()['data']['code'])

    #注册
    def test_02_mregist(self):
        url = 'http://localhost:8080/shop/mregist'
        data = {
            'username':'bubu',
            'password':'123',
            'email':'11@qq.com',
            'verifyCode':'uu'
        }
        res = requests.post(url=url,data=data)
        print(res.json())
        print(res.json()['data'])
if __name__ == '__main__':
    pytest.main()


