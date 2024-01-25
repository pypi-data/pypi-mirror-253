# encoding: utf-8
"""
-------------------------------------------------
@author: haohe
@email: haohe@nocode.com
@software: PyCharm
@file: __init__.py
@time: 2023/1/28 14:16
@description:
-------------------------------------------------
"""
import os

from nocode_utils.http_utils import http_post
from functools import wraps
import json
import inspect
import time
from datetime import datetime

info_template = {
    "config": {
        "wide_screen_mode": True
    },
    "header": {
        "title": {
            "tag": "plain_text",
            "content": "通知"
        },
        "template": "blue"
    },
    "elements": [{
        "tag": "markdown",
        "content": ""
    }]
}

alert_template = {
    "config": {
        "wide_screen_mode": True
    },
    "header": {
        "title": {
            "tag": "plain_text",
            "content": "警报"
        },
        "template": "red"
    },
    "elements": [{
        "tag": "div",
        "fields": [
            {
                "is_short": False,
                "text": {
                    "tag": "lark_md",
                    "content": "**函数路径：**\n"
                }
            },
            {
                "is_short": False,
                "text": {
                    "tag": "lark_md",
                    "content": ""
                }
            },
            {
                "is_short": True,
                "text": {
                    "tag": "lark_md",
                    "content": "**函数名称：**\n"
                }
            },
            {
                "is_short": True,
                "text": {
                    "tag": "lark_md",
                    "content": "**时间：**\n"
                }
            },
            {
                "is_short": False,
                "text": {
                    "tag": "lark_md",
                    "content": ""
                }
            },
            {
                "is_short": False,
                "text": {
                    "tag": "lark_md",
                    "content": "**警报信息**\n"
                }
            }
        ]
    }]
}


class FeishuBot:

    def __init__(self, app_secret, interval=1800):
        self.app_id = "cli_a33507c352b9900d"
        self.app_secret = app_secret
        self.encrypt = "9znJHzl7ilK01ZXIskFJQdkRkGv7MJQd"
        self.rate_limit = {}
        self.interval = interval

    def decrept(self, encrypt):
        from nocode_utils.feishu_utils.AESCipher import AESCipher
        cipher = AESCipher(self.encrypt)
        user_msg = json.loads(cipher.decrypt_string(encrypt))
        message = user_msg['event']['message']
        open_id = user_msg['event']['sender']['sender_id']['open_id']
        message_id = message['message_id']
        chat_id = message['chat_id']
        content = json.loads(message['content'])
        return message_id, open_id, chat_id, content

    def get_tenant_access_token(self):

        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        data = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }
        tenant_access_token = http_post(url, data=data)['tenant_access_token']
        return tenant_access_token

    def get_user_openid(self, emails, tenant_access_token):
        url = "https://open.feishu.cn/open-apis/contact/v3/users/batch_get_id?user_id_type=open_id"
        headers = {
            "Authorization": "Bearer " + tenant_access_token,
        }
        data = {"emails": emails}
        re = http_post(url, data, headers=headers)

        user_openids = []
        for user in re['data']['user_list']:
            user_openids.append(user['user_id'])
        return user_openids

    def send_message(self, open_id, tenant_access_token, msg):
        url = "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id"
        headers = {
            "Authorization": "Bearer " + tenant_access_token,
        }
        data = {
            "receive_id": open_id,
            "msg_type": "interactive",
            "content": json.dumps(msg),
        }
        _ = http_post(url, data, headers)

    def quate_reply(self, message_id, content):
        url = f"https://open.feishu.cn/open-apis/im/v1/messages/{message_id}/reply"
        tenant_access_token = self.get_tenant_access_token()

        headers = {
            "Authorization": "Bearer " + tenant_access_token,
        }

        msg = info_template
        msg['elements'][0]['content'] = str(content)
        data = {
            "msg_type": "text",
            "content": json.dumps(msg)
        }
        _ = http_post(url, data, headers)

    def rate_limiter(self, path, function_name, line_number, emails):

        """
        self.rate_limit = {
            "1@com": [
                {
                    "path": "xxxx",
                    "lasttime": 1657839574
                    "count": 2
                }
            ],
            "2@com": []
        }
        :param path:
        :param function_name:
        :param line_number:
        :param emails:
        :return:
        """

        key = f"{path}#{function_name}#{line_number}"
        current_time = time.time()
        valid_emails = []
        for email in emails:

            if email not in self.rate_limit:
                self.rate_limit[email] = [{
                    "path": key,
                    "lasttime": current_time,
                    "count": 1
                }]
                valid_emails.append(email)
            else:
                all_path = [item['path'] for item in self.rate_limit[email]]
                if key not in all_path:
                    self.rate_limit[email].append({
                        "path": key,
                        "lasttime": current_time,
                        "count": 1
                    })
                    valid_emails.append(email)
                else:
                    for item in self.rate_limit[email]:
                        if item['path'] == key:
                            if item['count'] < 3 and int(current_time) - int(item['lasttime']) > self.interval:
                                item['lasttime'] = current_time
                                item['count'] += 1
                                valid_emails.append(email)

                            elif int(current_time) - int(item['lasttime']) > 3600 * 24:
                                item['lasttime'] = current_time
                                item['count'] = 1
                                valid_emails.append(email)

        return valid_emails

    def alert_message(self, content, emails=[]):
        tenant_access_token = self.get_tenant_access_token()
        open_ids = []
        # 获取调用函数信息
        stack = inspect.stack()
        caller_frame = stack[1]
        frame_info = inspect.getframeinfo(caller_frame[0])
        path = frame_info.filename
        function_name = frame_info.function
        line_number = frame_info.lineno
        emails = self.rate_limiter(path, function_name, line_number, emails)
        if emails:
            open_ids.extend(self.get_user_openid(emails, tenant_access_token))

        msg = info_template
        msg['elements'][0]['content'] = str(content)
        msg['header']['template'] = "red"
        msg['header']['title']['content'] = "警报"

        for open_id in open_ids:
            self.send_message(open_id, tenant_access_token, msg)

    def alert(self, content, emails=[]):
        """
        用于发送飞书机器人警报，警报会包括文件和函数信息
        :param emails: 用户邮箱列表
        :param content:
        :return:
        """
        # 获取调用函数信息
        stack = inspect.stack()
        caller_frame = stack[1]
        frame_info = inspect.getframeinfo(caller_frame[0])
        path = frame_info.filename
        function_name = frame_info.function
        line_number = frame_info.lineno
        open_ids = []
        # 流控
        emails = self.rate_limiter(path, function_name, line_number, emails)
        if emails:
            tenant_access_token = self.get_tenant_access_token()
            open_ids.extend(self.get_user_openid(emails, tenant_access_token))

            msg = alert_template
            # 文件路径
            msg['elements'][0]['fields'][0]['text']['content'] = f"**函数路径：**\n {path}"
            # 函数名称
            msg['elements'][0]['fields'][2]['text']['content'] = f"**函数名称：**\n {function_name}:{str(line_number)}"
            # 时间
            msg['elements'][0]['fields'][3]['text'][
                'content'] = f"**时间：**\n {datetime.now().strftime('%Y/%m/%d %H:%M:%S')}"
            # 信息
            msg['elements'][0]['fields'][5]['text']['content'] = f"**警报信息**\n {str(content)}"

            for open_id in open_ids:
                self.send_message(open_id, tenant_access_token, msg)

    def info(self, content, emails=[]):
        """
        用于发送飞书机器人消息
        emails 和 open_ids 两个取一个即可，两者都有的时候会合并发送
        :param emails: 用户邮箱列表
        :param content:
        :return:
        """
        tenant_access_token = self.get_tenant_access_token()
        # 获取调用函数信息
        stack = inspect.stack()
        caller_frame = stack[1]
        frame_info = inspect.getframeinfo(caller_frame[0])
        path = frame_info.filename
        function_name = frame_info.function
        line_number = frame_info.lineno
        open_ids = []
        # 流控
        emails = self.rate_limiter(path, function_name, line_number, emails)
        if emails:
            open_ids.extend(self.get_user_openid(emails, tenant_access_token))

        msg = info_template
        msg['elements'][0]['content'] = str(content)

        for open_id in open_ids:
            self.send_message(open_id, tenant_access_token, msg)

    # def setup_webhook(self):
    #     @app.post('/feishubot')
    #     async def feishubot(request: Request):
    #         body = json.loads(await request.bodys())
    #         encrypt = body['encrypt']
    #         cipher = AESCipher("u1CfN4kxWV66a9IBaTOXmMdalGiewgw5")
    #         print(json.loads(cipher.decrypt_string(encrypt)))
    #         challenge = json.loads(cipher.decrypt_string(encrypt))['challenge']
    #         return JSONResponse(content={"challenge": challenge})


if __name__ == "__main__":
    bot = FeishuBot("4skVjTVX0PQUssK8FVbBhYBpy5F6qeat")
    bot.info("123", ["haohe@nocode.com"])
