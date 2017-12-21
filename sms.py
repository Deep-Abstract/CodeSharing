sms.send_single(phone_number: str, sign_name: str, template_code: str, template_param=None)
sms.send_group(phone_numbers: List[str], sign_name: str, template_code: str, template_param=None)

#例如
sms.send_single('18934521234', Sign_Name, Template_Code, {'code': 12345})

# 测试用
Access_Key_ID = "LTAI2t84jhtJ69vY"
Access_Key_Secret = "aC8rOMSLMxIU8lDwYhjblF7tCYlGZy"
Sign_Name = "智慧校园"
Template_Code = "SMS_117521047"

