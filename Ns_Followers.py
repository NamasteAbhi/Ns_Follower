import json
import os
import random
import time
import requests
from Utils import AES_CBC_NoPadding

class Ns_Followers:
    def __init__(self):

        self.requests=requests
        self.__AES_NoPadding = AES_CBC_NoPadding()

        self.__userid='1098333715' #Enter UserID Here
        self.__username='hackingghu' #Enter UserName Here
        self._session='54648738718:LWG0i7Vpl5J45M:9:AYfeeRVVPXilpzn6cr3pIRn-TlB0pmfVivQI_05vpA' #Enter SessionID Here

        self.__Pk=self.__userid.encode()+b'*'+str(random.randint(111,999)).encode()
        self.__Ip=os.urandom(8).hex().encode()+b'*'+str(random.randint(111,999)).encode()
        self.__Device=b'model:'+str(random.randint(111111,999999)).encode()+b'MI|id:QP1A.190711.020|manufacture:Xiaomi|brand:POCO|type:user|user:builder|base:1|sdk:REL|board: angelicain|host:c5-miui-ota-bd238.bj|release:10|product:angelicain_in|fingerprint:POCO/angelicain_in/angelicain:10/QP1A.190711.020/V12.0.3.0.QCRINRF:user/release-keys|hardware:mt6765|device:angelicain*'+str(random.randint(111,999)).encode()

    def Login_v61(self):

        self.headers = {
            'Host': 'nitrofollow.com',
            'App-Source': 'com.ns.socialf',
            'App-Version': '193',
            'App-Language': 'en',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'okhttp/3.12.1',
        }
        data = {
            'pk': self.__AES_NoPadding.encrypt(self.__Pk).hex(),
            'ip': self.__AES_NoPadding.encrypt(self.__Ip).hex(),
            'properties': self.__AES_NoPadding.encrypt(self.__Device).hex(),
            'user': json.dumps({'api_token':'', 'pk':self.__userid, 'profile_image':'', 'fullname':self.__username, 'sessionid':self._session, 'sessionid_threads':'null', 'is_threads_enabled':'1', 'csrftoken':'', 'coins_count':'0', 'username':self.__username, 'device_id':'', 'family_device_id':'', 'android_id':'', 'user_agent':'', 'ig_did':'', 'ig_nrcb':'', 'mid':'', 'rur':f'', 'shbid':'', 'shbts':'', 'datr':'null', 'dpr':'null', 'region_hint':'null', 'diamonds_count':'0', 'is_miner':'-1', 'www_claim':'', 'phone_id':'', 'nitrogen_status':'0', 'nitrogen_coins':'0', 'last_follow_session_time':'0', 'followSessionCount':'0', 'isMarked':'false', 'isBlocked':'false', 'isBreathed':'false', 'isWaitingForPosts':'false', 'breathTime':'0', 'bio':'null', 'isWorkingAutoPlus':'false', 'status':'0', 'statusMessage':'null', 'LimitCount':'99999', 'pigeon_session_id':''}),
            'req_type': self.__AES_NoPadding.encrypt(b'login*'+str(random.randint(111,999)).encode()).hex(),
            'req_token1': self.__AES_NoPadding.encrypt(self.__AES_NoPadding.encrypt(b'tZZfV*'+str(random.randint(111,999)).encode()).hex().encode()+b'aNw90zallcQ3BSf9866xaNw90zallc'+self.__AES_NoPadding.encrypt(self.__Pk).hex().encode()+b'*'+str(random.randint(111,999)).encode()).hex(),
            'req_token2': self.__AES_NoPadding.encrypt(self.__AES_NoPadding.encrypt(self.__AES_NoPadding.encrypt(b'tZZfV*'+str(random.randint(11,99)).encode()).hex().encode()+b'aNw90zallc1l8IY40pjuaNw90zallc'+self.__AES_NoPadding.encrypt(self.__Pk).hex().encode()+b'*'+str(random.randint(111,999)).encode()).hex().encode()+b'*'+str(random.randint(111,999)).encode()).hex(),
        }


        response = self.requests.post('https://nitrofollow.com/nitrof/api/v3/login-v6', headers=self.headers, data=data)
        print(response.text)
        self.__api_token=self.__AES_NoPadding.decrypt(bytes.fromhex(response.json()['user']['api_token']))
        self.__coins = self.__AES_NoPadding.decrypt(bytes.fromhex(response.json()['user']['coins_count']))

        return response.text

    def Login_v62(self):

        data = {
            'pk': self.__AES_NoPadding.encrypt(self.__Pk).hex(),
            'ip': self.__AES_NoPadding.encrypt(self.__Ip).hex(),
            'properties': self.__AES_NoPadding.encrypt(self.__Device).hex(),
            'user': json.dumps({'api_token':self.__api_token.decode().split('#')[0], 'pk':self.__userid, 'profile_image':'', 'fullname':self.__username, 'sessionid':self._session, 'sessionid_threads':'null', 'is_threads_enabled':'1', 'csrftoken':'', 'coins_count':'0', 'username':self.__username, 'device_id':'', 'family_device_id':'', 'android_id':'', 'user_agent':'', 'ig_did':'', 'ig_nrcb':'', 'mid':'', 'rur':f'', 'shbid':'', 'shbts':'', 'datr':'null', 'dpr':'null', 'region_hint':'null', 'diamonds_count':'0', 'is_miner':'-1', 'www_claim':'', 'phone_id':'', 'nitrogen_status':'0', 'nitrogen_coins':'0', 'last_follow_session_time':'0', 'followSessionCount':'0', 'isMarked':'false', 'isBlocked':'false', 'isBreathed':'false', 'isWaitingForPosts':'false', 'breathTime':'0', 'bio':'null', 'isWorkingAutoPlus':'false', 'status':'0', 'statusMessage':'null', 'LimitCount':'99999', 'pigeon_session_id':''}),
            'req_type': self.__AES_NoPadding.encrypt(b'initial-user*'+str(random.randint(111,999)).encode()).hex(),
            'api_token': self.__AES_NoPadding.encrypt(self.__api_token.decode().split('#')[0].encode()+b'*'+str(random.randint(111,999)).encode()).hex(),
            'req_token1': self.__AES_NoPadding.encrypt(self.__AES_NoPadding.encrypt(b'KfOcV*'+str(random.randint(111,999)).encode()).hex().encode()+b'aNw90zallcQ25cVoETzyaNw90zallc'+self.__AES_NoPadding.encrypt(self.__Pk).hex().encode()+b'*'+str(random.randint(111,999)).encode()).hex(),
            'req_token2': self.__AES_NoPadding.encrypt( self.__AES_NoPadding.encrypt(self.__AES_NoPadding.encrypt(b'KfOcV*'+str(random.randint(111,999)).encode()).hex().encode()+b'aNw90zallcFZAshMghpwaNw90zallc'+self.__AES_NoPadding.encrypt(self.__Pk).hex().encode()+b'*'+str(random.randint(11,99)).encode()).hex().encode()+b'*'+str(random.randint(111,999)).encode()).hex(),
        }
        response = self.requests.post('https://nitrofollow.com/nitrof/api/v3/login-v6', headers=self.headers, data=data)
        print(response.text)

        return response.text


    def Get_Suggest(self):

        data = {
            'user_pk': self.__AES_NoPadding.encrypt(self.__Pk).hex(),
            'req_token1': self.__AES_NoPadding.encrypt(str(random.randint(11111111,99999999)).encode()+b'pzmq').hex(),
            'req_token2':self.__AES_NoPadding.encrypt( str(random.randint(111111111,999999999)).encode()+b'pzmq').hex(),
        }
        response = self.requests.post('https://nitrofollow.com/nitrof/api/v3/suggest-v4', headers=self.headers, data=data)
        return response

    def PlaceOrder(self,items):

        self.req_user_pk=self.__AES_NoPadding.decrypt(bytes.fromhex(items['req_user_pk'])).decode().replace('#','*')
        self.__id=self.__AES_NoPadding.decrypt(bytes.fromhex(items['id'])).decode().replace('#','*')
        data = {
            'request_id': self.__AES_NoPadding.encrypt(self.__id.encode()).hex(),
            'api_token': self.__AES_NoPadding.encrypt(self.__api_token.decode().split('#')[0].encode()+b'*'+str(random.randint(111,999)).encode()).hex(),
            'follow_result': self.__AES_NoPadding.encrypt( b'0*'+str(random.randint(111,999)).encode()).hex(),
            'action_type': self.__AES_NoPadding.encrypt(b'3*'+str(random.randint(111,999)).encode()).hex(),
            'req_user_pk':self.__AES_NoPadding.encrypt(self.req_user_pk.encode()).hex(),
            'sessionid': self.__AES_NoPadding.encrypt(self._session.encode()+b'*'+str(random.randint(111,999)).encode()).hex(),
            'csrftoken': self.__AES_NoPadding.encrypt(b'*'+str(random.randint(111,999)).encode()).hex(),
            'ig_did': self.__AES_NoPadding.encrypt(b'*'+str(random.randint(111,999)).encode()).hex(),
            'ig_direct_region_hint': self.__AES_NoPadding.encrypt(b'--*'+str(random.randint(111,999)).encode()).hex(),
            'mid': self.__AES_NoPadding.encrypt(b'3*'+str(random.randint(111,999)).encode()).hex(),
            'rur':  self.__AES_NoPadding.encrypt(b'*'+str(random.randint(111,999)).encode()).hex(),
            'shbid': self.__AES_NoPadding.encrypt(b'*'+str(random.randint(111,999)).encode()).hex(),
            'shbts': self.__AES_NoPadding.encrypt(b'*'+str(random.randint(111,999)).encode()).hex(),
            'urlgen':  self.__AES_NoPadding.encrypt(b'--*'+str(random.randint(111,999)).encode()).hex(),
            'android_id': self.__AES_NoPadding.encrypt(b'*'+str(random.randint(111,999)).encode()).hex(),
            'device_id':  self.__AES_NoPadding.encrypt(b'*'+str(random.randint(111,999)).encode()).hex(),
            'www_claim': self.__AES_NoPadding.encrypt(b'*'+str(random.randint(111,999)).encode()).hex(),
            'user_agent': self.__AES_NoPadding.encrypt(b'*'+str(random.randint(111,999)).encode()).hex(),
            'req_token1': self.__AES_NoPadding.encrypt( self.__AES_NoPadding.encrypt(b'tysJn*'+str(random.randint(111,999)).encode()).hex().encode()+b'aNw90zallc999od7mT6MaNw90zallc'+self.__AES_NoPadding.encrypt(self.__userid.encode()+self.__id.encode()).hex().encode()+b'*'+str(random.randint(111,999)).encode()).hex(),
            'req_token2': self.__AES_NoPadding.encrypt(self.__AES_NoPadding.encrypt(self.__AES_NoPadding.encrypt(b'tZZfV*'+str(random.randint(111,999)).encode()).hex().encode()+b'aNw90zallcwZHLmJ29qmaNw90zallc'+self.__AES_NoPadding.encrypt(self.__userid.encode()+self.__id.encode()).hex().encode()+b'*'+str(random.randint(111,999)).encode()).hex().encode()+b'*'+str(random.randint(111,999)).encode()).hex(),
        }

        response = self.requests.post('https://nitrofollow.com/nitrof/api/v3/follow-v4', headers=self.headers, data=data)
        return response.json()

if __name__ == '__main__':

    cl=Ns_Followers()
    cl.Login_v61()
    cl.Login_v62()
    while True:
        try:
            suff=cl.Get_Suggest()
            if "suggests" in suff.text:
                for items in suff.json()['suggests']:
                    print(cl.PlaceOrder(items))
                    time.sleep(random.randint(10,15))
            else:
                print(suff.text)
                time.sleep(10)
        except Exception as E:
            print(E)
            time.sleep(5)
