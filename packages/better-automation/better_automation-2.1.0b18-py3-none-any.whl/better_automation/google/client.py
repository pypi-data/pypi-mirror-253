"""
Если этот код заработает, фиг я его выложу в паблик...
"""

from typing import Literal
from datetime import datetime

from yarl import URL

from better_automation.base import BaseClient
from better_automation.utils import to_json

from .models import GoogleAccountData

# https://developers.google.com/identity/protocols/oauth2/javascript-implicit-flow#redirecting
PromptType = Literal["consent", "select_account"]


def _referrer_url(**bind_payload) -> str:
    return str(URL("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount").with_query(**bind_payload))


def _continue_url(client_id: str, current_time_with_milliseconds: int) -> str:
    continue_url_params = {
        # TODO параметр as изменчив: as=S-1107092599:1704645143377026
        'as': f'S118374196:{current_time_with_milliseconds}',
        #
        'authuser': 'unknown',
        'client_id': client_id,
        # TODO параметр part изменчив
        'part': 'AJi8hAM10gN03GEzqyv-T5HOnWXaAgNCkRNxL7W3qkj40wVxz_iW3KVaBsD9Ln3Z0pS0C8oYzllffQO-klibpEvBTKubiNDrlHhrSuSRKTmaOanJXoE-CXvVcZtB79DoDltu28ZF-uRn6DuqIUa59YsG5Ucf05X1MQT3WHeiJAy5FVCxOuVuO02I4t54i1rc0XEgFsu5btbHsZbvC4oi95rbMlOK2GcrDS5_puCM7Ye1QVYetODMYfRhFrbBUzxt95nrkrRmBxpWcikoZqktK83ZVvY4IzeqfwcmJXVxfIq5bbauooCFs0SuM-b9rsNNhYbgNtsemfz7KkwAV5xZwsN_eVkGhVLwubSGYm0hRFEStIKyxafrmO2WE49-6-XQUHszlkB2V89wSftaPYhTpSWCu8RGFMg4eUrhDwK4YLvIpLxIbUhwcOhAvEQHPGtVxIIb2P8dktoXbqgpQ0M-4mJj2nUEJegrHg',
        'theme': "glif#",
    }
    return str(URL("https://accounts.google.com/signin/oauth/consent").with_query(**continue_url_params))


def _payload(client_id: str, current_datetime: datetime) -> dict:
    current_time_with_milliseconds = int(current_datetime.timestamp() * 1000000)
    current_time = int(current_datetime.timestamp())
    flow_name = "GeneralOAuthFlow"
    bg_request = [
        "oauth-account-chooser",
        "<m1dqVw8CAAbBwkrJ4cKN8og_h42xmOz0ADQBEArZ1M2W1E1GYLsYZv5-DiRc8bGCRjnJRmHOvDwBLEEYPP_kxVrHjdrCGzlJBYpGZadgzQAAAICdAAAABKcBB1YGMJk3Cy12utdgB5x5dU1KjKSuaHLwISrKnxWwbrY8Yk_yYQMAm2vP8tRHQBvLJHtyGrHaNVsW33HKY-Gh4gjr6jtb521K9HRUinPDWkb_gXSyb5_E-F5DrtHH4HPpEKNX0Fbrljj5STVY3Moq4_OBDS0M82yg0FcCJHGoB5sHUCcxyGdqxeHIQ_hlzJf9YmdNHH2DR58Cuww6ocANknEmV41ixG6_a2D8Y_bZTIb_dzmK3gdGtCmxSJo3UPsVUKzgAcN4JuL7jdbOIYt0ZkdXT_S6Uq1M0iCtvNCW0MnYAAK1mjaoh7s94MhLpVm6igk546q_OhWuLKQ4gk2YW-XzDL8zN22eJSrkGo1tv7q_3G7BEdM3WT840wBtcSmvBXMaBDGhwhqp9e19I4Uld9bHIdJQ_LhFUXSw4ZmKv7e1ifpJnhlZZjK-fqrZ_gouJij-S-S4BRc_ClVL3peUYZ_mZt8CP_vWjXMhvKrAziJc-CSyF4-JtQsixlFvTkp6ec3VsFtLoS4Bbq2K0byQq0CqkZstCXWbECnonWznR_YvIh5x_vDYzQcIWwNVpnuS3f3F9NWlNkzfSa8RW-J2Ze-IPd5eHInhcQ2mJIh_sh05jiZ5Mn4abPEBKpNd2bZb2oV8-8DxJ-77njqzNjHGBaXwsCt5oU_8OGVucSeRssm5hxXYZwGw-zlvIpbG0BSdUR76jisEMlkZM60B6Y-EJyaWuinMkKJZdeaKTMaDxwys0QvajH8u4OwZ-wcgh77aetN_wzi2ERM3-hvQ8H6TvcrLPNp09-TKZQYxkG37CS545mN3TQWO2OU65e-3EMht7dXUBgSRn8BHvJbO1JAadPdhX_yGF_iTM2pAWTTPdLselh0EKZX7YrBxkMTNmoYbgv8vCKyauj-oOW-QUmh80CLzKabfl5JWHJbJIH1mc5S_4eQWU4QV-_9GhiDAXLLS0ccM4m4JYEoypjm4OuDVMzUwCmJLqDJRAE8hJmVRddGL4Xl6sLwPmDGu-5912PTX7O4ObFpxqTs3sjXkXr5oocRBbWDnIMlD7vLEykQRxZbRwKH-lOfxkoz77o8yGvWRJg_tNVW_Io0oUymAY1fgxUrm0jN-T7SFP2r6Aqpf4Y_p-2kkk83Q0lWVpDpyhCfKD_1nWKj9QG5aFoeWm-cUCbU7HsxvHEUjQ5g01Ps8Wl67TBR_gPOECXbfYS0p0yfiF-caZvT1K11w_u42-zwgaIOnkX8R1aEP-xQxtd0OCWyoMB-jtBy4GUQeU7ro6BI-gfOKK1MTfvu8kdt1gvEoUaVTcojT4SK77djjNxq5MXIGMLnfDPnlU0P7ghN1PL_yXFbGsqH-SITLOruq_50io8tfu4XjbKGWBgrHBf-98GR-WUNSeP6_3be3CfG1qKUOmZgqsXWA6OmDO7ugwH8ITs-QC1BRNuxY-fen7G0qR2UTlqy9Mn9dDRxG69vcn11JwyRvY1uXX64qaPu-Z0y5EJzkmjq9sovjf6TY-eAHSfUtx1wvu1d_kkMifwB3SdTx6-8FxaNNBqdIzTmwYBLOW6OjuRq-sdXOsxaL2vNSCQ_dRBHD-FQJDqgAggHGepeu3DIU1ojkPJF40v4kImi7AmvrQaGet_QiU3bBgRXCVjeeYSK_7BZwI24AMGFZfrsnFG2MTcUHcINpTy8zKmcYIzrqVXqgru7Iva4qLFBF4TgWaAxpWf22zsKk94MOY69ikY8AK0KDKLKzq0I3qYavfNk--ERdTD0OnJy7qk86C5rsY9AVVgOiXi6QWoZqPRlukeD49SDh9F6b4UxBWnLgJPQhLjPATe5aqJ1KJ5ouHlOZVq1fD88Q9PJI5YHMIMAToA79_y_2Uj2pB2KzpfFvBoOTKZH_tcKY0Vdi_yw5LyRoZLE8HNgQTaYa642kouRjTrReWqHlHeB9yh8THFygQi83Jraeg_qswUkB4H2srpzE1TAb8nbWT8gdUZoFhqIk33MPWFfOnTiYDBVzEpWafMewf40mroxK_pFmCdjJZezTh1JlUVXWXJqOWHRaAWewSzmfja0jyC7RZTDvmUC8NwVP4yLWDER-v2t5JKkxyR0JL8vSW-TjGKx14SAj_oJsbq2bMg"
    ]
    f_req = [
        # TODO этот параметр изменчив
        "AEThLlwSApN39ij_LIvwDx90E4xGGvn4fbEegbNpEGiMeh2AhS7LOM3TH5ZRCty34T-TkNNRZC5YNBcthqe7wXWzQuQpBVj-OTuGh8FvjTp0s4y1wzS3upCCk3CnWh67bIQ90EjTwMf42ccWzwQiWoxfP_FLYKXZRstfsbzC8UcOKGzSKWrVWlBZf--YyxOy4b0cGvha6lnX-b6yFQ2-HRANvow1ndMPSboPgkTp6wS_9i8e8ayg9K7kVt8ikyIHsrI1T9N4mkNgpH3v4JzoJdbv9HmIXPtI18CahN1K8rme995o9Tbijp_qWsQkwaxn_21em1-sarkFKdOsaQZzhKQ5tAMDbSRl-moN6_tMqqo7lvVw7A6e6C69u-5rn7wdsfI8wiKi3UtuAiZ7foHMK03K49FlOXU4vDAa2gWD-9xitIneRPYqreqNvJe88XckT4mSMlx9sMYpWKfOemVbcmYKV_7NA_vBaXsea8QvOCuXySg-NirAarTZ9kbcnTJ3fapfViyDu8db",
        # TODO это device info
        0, 0, None, [None, None, [2, 1, None, 1,
                                  # TODO собрать ссылку
                                  "https://accounts.google.com/signin/oauth?client_id=968583257586-kljtp79kj8nc53gocd7lmo3sfgbd2i1f.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&redirect_uri=https%3A%2F%2Fairdrop.gomble.io%2Flogin&prompt=consent&gsiwebsdk=3&access_type=offline&response_type=code&include_granted_scopes=true&enable_granular_consent=true",
                                  None, None, 4, None,
                                  flow_name,
                                  None, None, 1], 10, [None, client_id, None,
                                                       "!ChREeHdtVjRYM0I4bkFDMUFBSFJ4YhIfVThjbHR4Q3NHaTBaOERFdWhZOThQYzkxdF9VSHpoZw∙AHkTZLMAAAAAZZsLtG-mLSf6L6c9A0qw-Bu0HbeCQNmD",
                                                       None, None, None, None, None, None, None,
                                                       # TODO вставлять верную ссылку
                                                       "https://airdrop.gomble.io",
                                                       f"S118374196:{current_time_with_milliseconds}",
                                                       0, None, None, None, None, [5,
                                                                                   # TODO another_client_id
                                                                                   "77185425430.apps.googleusercontent.com",
                                                                                   [
                                                                                       "https://www.google.com/accounts/OAuthLogin"],
                                                                                   None, None,
                                                                                   # TODO device_id
                                                                                   "44a22fdf-84ac-4f1f-b2cc-4911e62f955f",
                                                                                   None, None, None, None, None,
                                                                                   None, None, None, None, None,
                                                                                   None, None, None, None, None,
                                                                                   None, 5], None, None, None, 25,
                                                       None, None, None, 1, None, None, None,
                                                       [[None, 202], [None, 9315]], None, 1, None, None, 1], None,
                     None, None, 1, None, None, None, None, None, None, None, None, [], None, None, 3]]
    device_info = [
        None, None, None, None, None,
        "EN", None, None, None,
        flow_name, None,
        [None, client_id, None,
         # TODO этот параметр изменчив
         "!ChREeHdtVjRYM0I4bkFDMUFBSFJ4YhIfVThjbHR4Q3NHaTBaOERFdWhZOThQYzkxdF9VSHpoZw∙AHkTZLMAAAAAZZsLtG-mLSf6L6c9A0qw-Bu0HbeCQNmD",
         None, None, None, None, None, None, None,
         "https://airdrop.gomble.io", f"S118374196:{current_time_with_milliseconds}", 0, None, None, None, None,
         # TODO another_client_id
         [5, "77185425430.apps.googleusercontent.com",
          ["https://www.google.com/accounts/OAuthLogin"], None, None,
          # TODO device_id
          "44a22fdf-84ac-4f1f-b2cc-4911e62f955f",
          None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 5], None,
         None, None, 25, None, None, None, 1, None, None, None, [[None, 202], [None, 9315]], None, 1, None, None,
         1], None, None, None, None, 1, None, 0, 1, "", None, None, 1, 1
    ]

    payload = {
        # TODO параметры at и azt изменчивы: AFoagUVZK44l9a8PZIB4DhOheiGdHOkfDw:1704645143440
        'at': f'AFoagUVij2Eb9qDG4z_VA5IKP9oH-I2auw:{current_time}',
        'azt': f'AFoagUVij2Eb9qDG4z_VA5IKP9oH-I2auw:{current_time}',
        'checkConnection': 'youtube:332',
        'checkedDomains': 'youtube',
        'cookiesDisabled': 'false',
        'flowName': flow_name,
        'gmscoreversion': 'undefined',
        'continue': _continue_url(client_id, current_time_with_milliseconds),
        'bgRequest': to_json(bg_request),
        'f.req': to_json(f_req),
        'deviceinfo': to_json(device_info),
    }
    return payload


class GoogleOAuthClient(BaseClient):
    DEFAULT_HEADERS = {
        'authority': 'accounts.google.com',
    }

    def __init__(self, cookies: list[dict], **session_kwargs):
        cookies = [(cookie['name'], cookie['value']) for cookie in cookies]
        super().__init__(cookies=cookies, **session_kwargs)
        self.account_data: GoogleAccountData | None = None

    @property
    def _x_chrome_id_consistency_request(self) -> str:
        if self.account_data is None:
            raise ValueError("First request account data")

        x_chrome_id_consistency_request_dict = {
            "version": 1,
            # TODO another_client_id
            "client_id": "77185425430.apps.googleusercontent.com",
            # TODO device_id
            "device_id": "44a22fdf-84ac-4f1f-b2cc-4911e62f955f",
            "sync_account_id": self.account_data.id,
            "signin_mode": "all_accounts",
            "signout_mode": "show_confirmation",
        }

        return ','.join(f"{key}={value}" for key, value in x_chrome_id_consistency_request_dict.items())

    async def request_account_data(self):
        url = "https://accounts.google.com/ListAccounts"
        params = {
            "listPages": 0,
            "pid": 243,
            "gpsia": 1,
            "source": "ogb",
            "atic": 1,
            "mo": 1,
            "mn": 1,
            "hl": "en",
            "ts": 157,
        }
        payload = {}
        headers = {
            'origin': 'https://ogs.google.com',
            'referer': 'https://ogs.google.com/',
            'x-client-data': 'CIq2yQEIpbbJAQipncoBCNX/ygEIk6HLAQib/swBCIWgzQEIoe7NAQiD8M0BGPTJzQEYp+rNAQ=='
        }
        response = await self.session.request("POST", url, headers=headers, data=payload, params=params)
        self.account_data = GoogleAccountData.from_account_list(response.json())
        print(self.account_data)

    async def oauth_2(
            self,
            client_id: str,
            redirect_uri: str,
            scope: str,
            gsiwebsdk: int = 3,
            access_type: str = "offline",
            response_type: str = "code",
            state: str = None,
            prompt: PromptType = None,
            login_hint: str = None,
            include_granted_scopes: bool = None,
            enable_granular_consent: bool = None,
    ):
        if self.account_data is None:
            await self.request_account_data()

        url = "https://accounts.google.com/_/signin/oauth"
        params = {
            "authuser": 0,
            "hl": "en",
            "_reqid": 185158,  # 70399 - плохой
            "rt": "j",
        }

        current_datetime = datetime.now()
        payload = _payload(client_id, current_datetime)
        bind_payload = {
            "client_id": client_id,
            "scope": scope,
            "redirect_uri": redirect_uri,
            "prompt": prompt,
            "gsiwebsdk": gsiwebsdk,
            "access_type": access_type,
            "response_type": response_type,
            "service": "lso",
            "o2v": 2,
            "theme": "glif",
        }
        if state: bind_payload["state"] = state
        if state: bind_payload["prompt"] = prompt
        if login_hint: bind_payload["login_hint"] = login_hint
        if include_granted_scopes: bind_payload["include_granted_scopes"] = str(include_granted_scopes).lower()
        if enable_granular_consent: bind_payload["enable_granular_consent"] = str(enable_granular_consent).lower()
        payload.update(bind_payload)
        headers = {
            'authority': 'accounts.google.com',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': _referrer_url(**bind_payload),
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            # 'sec-ch-ua-full-version': '"120.0.6099.199"',
            # 'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.199", "Google Chrome";v="120.0.6099.199"',
            # 'sec-ch-ua-mobile': '?0',
            # 'sec-ch-ua-model': '""',
            # 'sec-ch-ua-platform': '"Windows"',
            # 'sec-ch-ua-platform-version': '"15.0.0"',
            # 'sec-ch-ua-wow64': '?0',
            # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'x-chrome-id-consistency-request': self._x_chrome_id_consistency_request,
            'x-client-data': 'CIq2yQEIpbbJAQipncoBCNX/ygEIk6HLAQib/swBCIWgzQEI3L3NAQiP4c0BCOLszQEIoe7NAQi87s0BCIrvzQEIg/DNAQiG8M0BCLLxzQEIp/LNARj0yc0BGKfqzQE=',
            'x-same-domain': '1'
        }

        response = await self.session.request("POST", url, headers=headers, data=payload, params=params)

        print(response.text)
