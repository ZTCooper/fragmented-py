import easygui as g

#-----------------------------------------------------
#multenterbox(msg, title, fields=(),values=())
#如果输入值比选项少，返回列表中的值用""填充
#如果输入值比选项多，返回列表中的值被截断
#如果取消操作，则返回域中的列表值或None
#-----------------------------------------------------

msg = '请输入用户信息'
title = '账号中心'
field_names = ['*用户名','*真实姓名','固定电话','手机号码','QQ','*E_mail']
field_value = []
field_value = g.multenterbox(msg, title, field_names)

while 1:
    if field_value == None:
        break
    errmsg = ''
    for i in range(len(field_names)):
        option = field_names[i].strip()
        if field_value[i].strip() == '' and option[0] == '*':
            errmsg += '【%s】为必填项。\n\n'% field_names[i]
    if errmsg == '':
        break
    field_value = g.multenterbox(errmsg, title, field_names, field_value)

print('用户资料如下：%s'%str(field_value))
