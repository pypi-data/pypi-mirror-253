from requests import Session
from ._utils import base64_decode, get_headers, DefaultFuncs
from ._api import API
import re
import random
from urllib.parse import urlparse, parse_qs


default_options = {
    "self_listen": False,
    "listen_events": True,
    "listen_typing": False,
    "update_presence": False,
    "force_login": False,
    "auto_mark_delivery": True,
    "auto_mark_read": False,
    "auto_reconnect": True,
    "log_record_size": 100,
    "online": True,
    "emit_ready": False,
    "user_agent": "Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
}


class Client:
    def __init__(self) -> None:
        self.__session = Session()
        self.options = default_options.copy()
        pass

    def login(self, appstate: str, options: dict = {}):
        """
        Login to facebook with appstate

        :param appstate: base64 encoded appstate
        :param options: fca options
        """

        appstateList = base64_decode(appstate)

        for each in appstateList:
            self.__session.cookies.set(
                each["key"], each["value"], path=each["path"], domain=each["domain"]
            )

        for key in options:
            self.options[key] = options[key]

        url = "https://www.facebook.com/"
        self.__headers = get_headers(url, self.options)

        res = self.__session.get(url, headers=self.__headers, timeout=60)

        reg = r'<meta http-equiv="refresh" content="0;url=([^"]+)[^>]+>'
        pattern = re.compile(reg)

        redirect = pattern.search(res.text)
        
        if redirect and redirect.group(1):
            self.__headers = get_headers(redirect.group(1), self.options)
            res = self.__session.get(redirect.group(1), headers=self.__headers, timeout=60)

        if not self.__is_login():
            return None

        (ctx, defailt_funcs, api) = self.__build_API(res.text)

        return api

    def __is_login(self):
        user_id = self.__get_user_id()
        if not user_id:
            print(
                "Error retrieving user_id. This can be caused by a lot of things, including getting blocked by Facebook for logging in from an unknown location. Try logging in with a browser to verify."
            )
            return False

        print("Logged in as " + user_id)

        self.user_id = user_id

        return True

    def __build_API(self, html: str) -> tuple[dict[str, any], DefaultFuncs, API]:
        cookies: list = []

        for cookie in self.__session.cookies:
            if cookie.domain == "facebook.com":
                cookies.append(
                    {
                        "name": cookie.name,
                        "value": cookie.value,
                        "path": cookie.path,
                        "domain": cookie.domain,
                    }
                )

        # if html has /checkpoint/block/?next, then it's checkpoint
        if "/checkpoint/block/?next" in html:
            print("checkpoint")
            return

        client_id = hex(int(random.random() * 2147483648))[2:]

        old_fb_mqtt_match = re.search(
            r'irisSeqID:"(.+?)",appID:219994525426954,endpoint:"(.+?)"', html
        )

        new_fb_mqtt_match = re.search(
            r'{"app_id":"219994525426954","endpoint":"(.+?)","iris_seq_id":"(.+?)"}',
            html,
        )

        legacy_fb_mqtt_match = re.search(
            r'(\["MqttWebConfig",\[\],{fbid:")(.+?)(",appID:219994525426954,endpoint:")(.+?)(",pollingEndpoint:")(.+?)(3790])',
            html,
        )

        self.__mqtt = {
            "iris_seq_id": None,
            "mqtt_endpoint": None,
            "region": None,
            "no_mqtt_data": None,
        }

        if old_fb_mqtt_match is not None:
            self.__mqtt["iris_seq_id"] = old_fb_mqtt_match.group(1)
            self.__mqtt["mqtt_endpoint"] = old_fb_mqtt_match.group(2)
            self.__mqtt["region"] = (
                parse_qs(urlparse(self.__mqtt["mqtt_endpoint"]).query)
                .get("region")[0]
                .upper()
            )
            print("Got this account's message region: " + self.__mqtt["region"])
        elif new_fb_mqtt_match:
            self.__mqtt["iris_seq_id"] = new_fb_mqtt_match.group(2)
            self.__mqtt["mqtt_endpoint"] = re.sub(r"\\/", "/", new_fb_mqtt_match.group(1))
            self.__mqtt["region"] = (
                parse_qs(urlparse(self.__mqtt["mqtt_endpoint"]).query)
                .get("region")[0]
                .upper()
            )
            print("Got this account's message region: " + self.__mqtt["region"])
        elif legacy_fb_mqtt_match:
            self.__mqtt["mqtt_endpoint"] = legacy_fb_mqtt_match.group(4)
            self.__mqtt["region"] = (
                parse_qs(urlparse(self.__mqtt["mqtt_endpoint"]).query)
                .get("region")[0]
                .upper()
            )

            print(
                "Cannot get sequence ID with new RegExp. Fallback to old RegExp (without seqID)..."
            )
            print("Got this account's message region: " + self.__mqtt["region"])
            print("[Unused] Polling endpoint: " + legacy_fb_mqtt_match.group(6))
        else:
            print("Cannot get MQTT endpoint")
            self.__mqtt["no_mqtt_data"] = html

        ctx = {
            "user_id": self.user_id,
            "client_id": client_id,
            "logged_in": True,
            "access_token": None,
            "client_mutation_id": 0,
            "mqtt_client": None,
            "last_seq_id": self.__mqtt["iris_seq_id"],
            "sync_token": None,
            "mqtt_endpoint": self.__mqtt["mqtt_endpoint"],
            "region": self.__mqtt["region"],
            "first_listen": True,
            "options": self.options,
            "ws_task_number": 0,
            "ws_req_number": 0,
            "req_callbacks": {},
        }

        default_funcs = DefaultFuncs(self.__session, html, self.user_id, ctx)
        api = API(default_funcs, ctx)

        return ctx, default_funcs, api


    def __get_user_id(self):
        url_profile = self.__session.get("https://www.facebook.com/me").url
        profile = self.__session.get(url_profile).text
        user_id = None

        # Attempt to extract user_id using the first pattern
        try:
            user_id = profile.split('","viewer_actor":{"__typename":"User","id":"')[
                1
            ].split('"},"')[0]
        except IndexError:
            pass

        # If the first pattern fails, attempt to extract user_id using the second pattern
        if user_id is None:
            try:
                user_id = profile.split('{"u":"\/ajax\/qm\/?__a=1&__user=')[1].split(
                    "&__comet_req="
                )[0]
            except IndexError:
                return None

        return user_id
