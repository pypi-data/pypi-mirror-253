import requests, re, json
import logging
from .util.hmd5 import *
from .util.xEncode import *
from .util.ct_base64 import *

logging.basicConfig(format="%(asctime)s |%(filename)s:%(lineno)s| - %(levelname)s: %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)
class UestcNetManager:
    def __init__(self,
                login_url='http://10.253.0.235/srun_portal_pc?ac_id=3&theme=yd',
                login_challenge_api_url='http://10.253.0.235/cgi-bin/get_challenge',
                login_api_url='http://10.253.0.235/cgi-bin/srun_portal',
                # The default login type is china telecom login
                login_type='dx',
                param_acid=3,
                param_n=200,
                param_type=1,
                param_enc='srun_bx1',
                assigned_ip=None):
        self.login_url = login_url
        self.login_challenge_api_url = login_challenge_api_url
        self.login_api_url = login_api_url
        self.login_type = login_type
        self.param_acid = param_acid
        self.param_n = param_n
        self.param_type = param_type
        self.param_enc = param_enc
        self.assigned_ip = assigned_ip
        #self.current_challenge = None
        self.callback = 'jQuery1124027894844948396047_1694524024132'
        self.session = requests.session()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.102 Safari/537.36"
        }
        self.session.headers = headers

    # Do login
    def login(self, username, password):
        if self.login_type == 'cmcc':
            self.username = username + '@cmcc'
        elif self.login_type == 'dx':
            self.username = username + '@dx'
        else:
            raise Exception("login type error, It can only be cmcc or dx!!!")
        self.password = password
        assert username is not None and len(str(username)) > 0, "username is empty!!!"
        assert password is not None and len(str(password)) > 0, "username is empty!!!"

        logging.info(f"Start automatic login to the campus network...")

        # Step1: get assigned ip
        self.get_assigned_ip()
        assert self.assigned_ip is not None, "Cannot get assigned ip, please retry!!!"
        logging.info(f"[Step 1] The allocated ip was obtained successfully, and the assigned ip address is: {self.assigned_ip}")

        # Step2: get a challenge
        challenge = self.__get_challenge()
        assert challenge is not None, "Cannot get challenge, please retry!!!"
        logging.info(f"[Step 2] The challenge was obtained successfully, and the challenge is: {challenge}")

        # Step3: calc challenge and login
        login_success = self.__login_action(challenge)
        if login_success:
            logging.info(f"[Login success✅]")
        else:
            logging.error(f"[Login fail❎]")

    # Get assigned ip address
    def get_assigned_ip(self):
        if self.assigned_ip is None:
            try:
                r = self.session.get(url=self.login_url)
                self.assigned_ip = re.search('id="user_ip" value="(.*?)"', r.text).group(1)
            except Exception as e:
                logging.error(f"Get assigned ip fail, exception: {e}")
                return None
        return self.assigned_ip

    def __get_challenge(self):
        challenge_params = {
            "action": "login",
            "username": self.username,
            "ip": self.assigned_ip,
            "callback": self.callback
        }
        try:
            s = self.session.get(url=self.login_challenge_api_url, params=challenge_params).text
            logging.info(f"Get challenge api response: {s}")
            s = json.loads(s[s.find('(') + 1:-1])
            if s['error'] == 'ok':
                return s['challenge']
            else:
                logging.error(f"Get challenge fail, errmsg is: {s['error_msg']}")
                return None
        except Exception as e:
            logging.error(f"Get challenge fail, exception: {e}")
            return None
    def __login_action(self, challenge):
        pwd_hmd5 = hmd5(self.password, challenge)
        logging.info(f"[Step 3.1] The HMAC value of the password is: {pwd_hmd5}")

        info_params = {
            "username": self.username,
            "password": self.password,
            "ip": self.assigned_ip,
            "acid": self.param_acid,
            "enc_ver": self.param_enc
        }
        info_params_str = json.dumps(info_params).replace(' ', '')
        info = "{SRBX1}" + self_ct_b64encode(xEncode(info_params_str, challenge))
        logging.info(f"[Step 3.2] The information encryption value info is: {info}")

        chkstr = challenge + self.username + challenge + pwd_hmd5 + challenge + str(self.param_acid) + challenge + self.assigned_ip + challenge + str(
            self.param_n) + challenge + str(self.param_type) + challenge + info
        chksum = hashlib.sha1(chkstr.encode()).hexdigest()
        logging.info(f"[Step 3.3] The information checksum is: {chksum}")

        login_params = {
            "callback": self.callback,
            "action": "login",
            "username": self.username,
            "password": "{MD5}" + pwd_hmd5,
            "ac_id": self.param_acid,
            "ip": self.assigned_ip,
            "chksum": chksum,
            "info": info,
            "n": self.param_n,
            "type": self.param_type,
            "double_stack": 0
        }
        try:
            s = self.session.get(url=self.login_api_url, params=login_params).text
            logging.info(f"Login api response: {s}")
            s = json.loads(s[s.find('(') + 1:-1])
            if s['error']=='ok':
                if s['suc_msg']=='ip_already_online_error':
                    logging.warning(f"Login success, But ip already online!!!")
                return True
            else:
                logging.error(f"Login fail, error is {s['error']}, error_msg is {s['error_msg']}")
                return False
        except Exception as e:
            logging.error(f"Login fail, exception: {e}")
            return False


if __name__ == '__main__':
    u = UestcNetManager()
    # print(u.get_assigned_ip())
    u.login(username='************', password='**********')