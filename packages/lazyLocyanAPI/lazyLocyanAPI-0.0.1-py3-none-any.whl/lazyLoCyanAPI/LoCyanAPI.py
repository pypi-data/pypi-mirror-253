import random
import string

import requests
from enum import Enum
from typing import Any, Dict, Optional, Union


class DynamicClass:
    def __init__(self, data: Dict[str, Any]) -> None:
        """初始化一个动态类，将字典的键值对转换为类的属性"""
        self.__dict__.update(data)


class ProxyTypes(Enum):
    """代理类型枚举"""
    tcp = "tcp"
    udp = "udp"
    http = "http"
    https = "https"
    stcp = "stcp"
    xtcp = "xtcp"


def generate_random_string(length=10) -> str:
    """生成一个指定长度的随机字符串。

    默认长度是10。字符串包括大写字母、小写字母和数字。

    参数:
        length (int): 随机字符串的长度。默认是10。

    返回:
        str: 生成的随机字符串。
    """
    characters = string.ascii_letters + string.digits  # 包括大写字母、小写字母和数字
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


class LoCyanAPI:
    def __init__(self, base_url: str = "https://api.locyanfrp.cn/") -> None:
        """初始化LoCyanAPI类"""
        self.base_url = base_url
        self.headers: Dict[str, str] = {}
        self.login_token: str = ""
        self.username: str = ""
        self.proxy: Optional[Dict[str, str]] = None

    def login(self, username: str, password: str) -> bool:
        """用户登录"""
        url = self.base_url + "/User/DoLogin?" + f"username={username}&password={password}"
        response = requests.post(url, proxies=self.proxy)
        result = response.json()
        if result.status == 0:
            self.login_token = result.get("token", "")
            return True
        return False

    def get_user_info(self) -> str:
        """获取用户信息"""
        url = self.base_url + f"/Account/info?username={self.username}&token={self.login_token}"
        realname = requests.get(self.base_url + f"/Account/GetRealnameStatus?username={self.username}")
        traffic = requests.get(self.base_url + f"/Account/Status/Check?username={self.username}")
        response = requests.post(url, proxies=self.proxy)
        user_info = DynamicClass(response.json())
        info = f"""
            用户名: {getattr(user_info, "username", "获取失败")}
            邮箱: {getattr(user_info, "email", "获取失败")}
            是否已进行实名认证: {'已认证' if realname == 0 else '未认证'}
            用户密钥: {self.login_token}
            剩余流量: {traffic.json().get("traffic", 1_048_576) / 1_048_576} G
        """
        return info

    def get_user_proxies(self) -> list:
        """获取用户隧道列表"""
        url = self.base_url + f"Proxies/GetProxiesList?username={self.username}&token={self.login_token}"
        response = requests.post(url, proxies=self.proxy)
        return response.json()

    def new_proxy(self, node_id: str, name: str = "", protocol_type: Union[str, ProxyTypes] = ProxyTypes.tcp,
                  local_addr: str = "127.0.0.1", local_port: int = "25565", remote_port: int = 1000000,
                  encrypt: bool = False, zip:bool = False) -> int:
        """创建新隧道"""
        proxy_type = protocol_type.value if isinstance(protocol_type, Enum) else protocol_type

        if remote_port >= 1000000:
            while True:
                remote_port = random.randint(10000, 90000)
                if remote_port != 25565:
                    break

        if name == "":
            name = "lazyLocyanAPI_"
            name += proxy_type
            name += generate_random_string()

        url = self.base_url + f"""add?username={self.username}&name={name}&ip={local_addr}&type={proxy_type}&lp=
        {local_port}&rp={remote_port}&ue={1 if encrypt else 0}&uz={1 if zip else 0}&id={node_id}
        &token={self.login_token}"""
        response = requests.post(url, proxies=self.proxy)
        return response.json().get("status")

    def remove_proxy(self, proxy_id: str) -> bool:
        """删除隧道"""
        url = self.base_url + f"Proxies/remove?username={self.username}&proxyid={proxy_id}&token={self.login_token}"
        response = requests.post(url, proxies=self.proxy)
        return response.json().get("status")

    def get_node_list(self) -> list:
        """获取节点列表"""
        url = self.base_url + f"Proxies/GetProxiesList?username={self.username}&token={self.login_token}"
        response = requests.get(url, proxies=self.proxy)
        return response.json()
