# -*- coding: utf-8 -*-
"""
SDK 链接: http://ytx-sdk.oss-cn-shanghai.aliyuncs.com/dysms_python.zip?spm=5176.doc55359.2.6.OI9EZK&file=dysms_python.zip
- 我了解了一下，应该无法连接Python 3.3+版本。 需要额外调用Python 3.3-来执行。
"""
import sys
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid
from aliyunsdkcore.profile import region_provider
import warnings

from __future__ import print_function
from sys import version_info

"""
短信业务调用接口示例，版本号：v20170525

Created on 2017-06-12

"""

if version_info.major is 2:
    reload(sys)
    sys.setdefaultencoding('utf8')

# 注意：不要更改
REGION = "cn-hangzhou"
PRODUCT_NAME = "Dysmsapi"
DOMAIN = "dysmsapi.aliyuncs.com"

# # ACCESS_KEY_ID/ACCESS_KEY_SECRET 根据实际申请的账号信息进行替换
# ACCESS_KEY_ID = "$AccessKeyId"
# ACCESS_KEY_SECRET = "$AccessKeySecret"

class MsgManager:
    def __init__(product_name,
                 access_key_id,  
                 access_key_secret, 
                 region=REGION):
        self.acs_client = AcsClient(access_key_id, access_key_secret, region)
        region_provider.add_endpoint(product_name, region, DOMAIN)
        self.tasks = {}
    
    def add_tasks(business_id, 
                  func:'local_namespace: dict -> dosomething with local_namespace'):

        func.has_done = False
        self.tasks[business_id] = func

    # 阿里云的文档看得我人都傻了，水平能再垃圾点吗?
    def send_sms(business_id: '* 业务请求流水号', 
                 phone_numbers: '* 短信发送的号码列表. 以逗号分隔的形式进行批量调用.',
                 sign_name: '短信签名. 可在短信控制台中找到.',
                 template_code: '* 短信模板编码. 可在短信控制台中找到.',
                 template_param: '短信模板变量参数'=None):

        """
        额外说明:
            我们发出去的短信应该是如下机制生成的:
                msg = get_template_by_code(template_code).format(**template_param)
        """
        if business_id not in self.tasks:
            warnings.warn('未指定流水号 {business_id} 的工作!'.format(business_id))
            task = lambda local_namespace: None
            task.has_done = False
            self.tasks[business_id] = task


        smsRequest = SendSmsRequest.SendSmsRequest()
        smsRequest.set_TemplateCode(template_code)

        if template_param is not None: 
            smsRequest.set_TemplateParam(template_param)
        
        smsRequest.set_OutId(business_id)
        smsRequest.set_SignName(sign_name)
        smsRequest.set_PhoneNumbers(phone_numbers)

        # 调用短信发送接口，返回json
        smsResponse = self.acs_client.do_action_with_exception(smsRequest)

        # TODO 业务处理
        self.tasks[business_id](locals())
        self.tasks[business_id].has_done = True

        return smsResponse
    
    def query_send_detail(biz_id: '流水号', 
                          phone_number: '* 查询的手机号码', 
                          page_size: '* 页大小', 
                          current_page: '* 当前页码(从1开始计数)', 
                          send_date: '* 发送日期 支持30天内记录查询，格式yyyyMMdd'):

        if biz_id not in self.tasks:
            warnings.warn('未指定流水号 {business_id} 的工作!'.format(biz_id))
            task = lambda local_namespace: None
            task.has_done = False
            self.tasks[biz_id] = task
    
        queryRequest = QuerySendDetailsRequest.QuerySendDetailsRequest()
        queryRequest.set_PhoneNumber(phone_number)
        queryRequest.set_BizId(biz_id)
        queryRequest.set_SendDate(send_date)
        queryRequest.set_CurrentPage(current_page)
        queryRequest.set_PageSize(page_size)

        # 调用短信记录查询接口，返回json
        queryResponse = self.acs_client.do_action_with_exception(queryRequest)

        # TODO 业务处理
        self.tasks[business_id](locals())
        self.tasks[business_id].has_done = True

        return queryResponse


# Test
if __name__ == '__main__':
    import json
    # TODO : product_name, access_key_id, access_key_secret 未定义，根据具体情况修改。
    msg_manager = MsgManager(product_name, access_key_id, access_key_secret) 
    business_id = uuid.uuid1()
    print (business_id)
    params = json.dumps({'code':'12345', 'product':'云通信'})
    print(msg_manager.send_sms(
        business_id=business_id, 
        phone_numbers= ','.join(["13000000000"]), 
        sign_name="云通信测试", 
        template_code="SMS_5250008", 
        template_param=params))
            
    print(msg_manager.query_send_detail(
            biz_id="1234567^8901234", 
            phone_number="13000000000", 
            page_size=10, 
            current_page=1, 
            send_date="20170612"))
