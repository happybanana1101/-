#-*-coding:utf-8 -*-
import re
import json
list1 = ['北京','天津','上海', '重庆' ,'河北省', '山西省', '内蒙古自治区', '辽宁省', '吉林省', '黑龙江省', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区', '海南省', '重庆市', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区', '台湾省', '香港特别行政区', '澳门特别行政区']
list2 = ['石家庄市', '唐山市', '秦皇岛市', '邯郸市', '邢台市', '保定市', '张家口市', '承德市', '沧州市', '廊坊市', '衡水市', '太原市', '大同市', '阳泉市', '长治市', '晋城市', '朔州市', '晋中市', '运城市', '忻州市', '临汾市', '吕梁市', '呼和浩特市', '包头市', '乌海市', '赤峰市', '通辽市', '鄂尔多斯市', '呼伦贝尔市', '巴彦淖尔市', '乌兰察布市', '兴安盟', '锡林郭勒盟', '阿拉善盟', '沈阳市', '大连市', '鞍山市', '抚顺市', '本溪市', '丹东市', '锦州市', '营口市', '阜新市', '辽阳市', '盘锦市', '铁岭市', '朝阳市', '葫芦岛市', '长春市', '吉林市', '四平市', '辽源市', '通化市', '白山市', '松原市', '白城市', '延边朝鲜族自治州', '哈尔滨市', '齐齐哈尔市', '鸡西市', '鹤岗市', '双鸭山市', '大庆市', '伊春市', '佳木斯市', '七台河市', '牡丹江市', '黑河市', '绥化市', '大兴安岭地区', '南京市', '无锡市', '徐州市', '常州市', '苏州市', '南通市', '连云港市', '淮安市', '盐城市', '扬州市', '镇江市', '泰州市', '宿迁市', '杭州市', '宁波市', '温州市', '嘉兴市', '湖州市', '绍兴市', '金华市', '衢州市', '舟山市', '台州市', '丽水市', '合肥市', '芜湖市', '蚌埠市', '淮南市', '马鞍山市', '淮北市', '铜陵市', '安庆市', '黄山市', '滁州市', '阜阳市', '宿州市', '六安市', '亳州市', '池州市', '宣城市', '福州市', '厦门市', '莆田市', '三明市', '泉州市', '漳州市', '南平市', '龙岩市', '宁德市', '南昌市', '景德镇市', '萍乡市', '九江市', '新余市', '鹰潭市', '赣州市', '吉安市', '宜春市', '抚州市', '上饶市', '济南市', '青岛市', '淄博市', '枣庄市', '东营市', '烟台市', '潍坊市', '济宁市', '泰安市', '威海市', '日照市', '临沂市', '德州市', '聊城市', '滨州市', '菏泽市', '郑州市', '开封市', '洛阳市', '平顶山市', '安阳市', '鹤壁市', '新乡市', '焦作市', '濮阳市', '许昌市', '漯河市', '三门峡市', '南阳市', '商丘市', '信阳市', '周口市', '驻马店市', '武汉市', '黄石市', '十堰市', '宜昌市', '襄阳市', '鄂州市', '荆门市', '孝感市', '荆州市', '黄冈市', '咸宁市', '随州市', '恩施土家族苗族自治州', '长沙市', '株洲市', '湘潭市', '衡阳市', '邵阳市', '岳阳市', '常德市', '张家界市', '益阳市', '郴州市', '永州市', '怀化市', '娄底市', '湘西土家族苗族自治州', '广州市', '韶关市', '深圳市', '珠海市', '汕头市', '佛山市', '江门市', '湛江市', '茂名市', '肇庆市', '惠州市', '梅州市', '汕尾市', '河源市', '阳江市', '清远市', '东莞市', '中山市', '潮州市', '揭阳市', '云浮市', '南宁市', '柳州市', '桂林市', '梧州市', '北海市', '防城港市', '钦州市', '贵港市', '玉林市', '百色市', '贺州市', '河池市', '来宾市', '崇左市', '海口市', '三亚市', '三沙市', '儋州市', '成都市', '自贡市', '攀枝花市', '泸州市', '德阳市', '绵阳市', '广元市', '遂宁市', '内江市', '乐山市', '南充市', '眉山市', '宜宾市', '广安市', '达州市', '雅安市', '巴中市', '资阳市', '阿坝藏族羌族自治州', '甘孜藏族自治州', '凉山彝族自治州', '贵阳市', '六盘水市', '遵义市', '安顺市', '毕节市', '铜仁市', '黔西南布依族苗族自治州', '黔东南苗族侗族自治州', '黔南布依族苗族自治州', '昆明市', '曲靖市', '玉溪市', '保山市', '昭通市', '丽江市', '普洱市', '临沧市', '楚雄彝族自治州', '红河哈尼族彝族自治州', '文山壮族苗族自治州', '西双版纳傣族自治州', '大理白族自治州', '德宏傣族景颇族自治州', '怒江傈僳族自治州', '迪庆藏族自治州', '拉萨市', '日喀则市', '昌都市', '林芝市', '山南市', '那曲市', '阿里地区', '西安市', '铜川市', '宝鸡市', '咸阳市', '渭南市', '延安市', '汉中市', '榆林市', '安康市', '商洛市', '兰州市', '嘉峪关市', '金昌市', '白银市', '天水市', '武威市', '张掖市', '平凉市', '酒泉市', '庆阳市', '定西市', '陇南市', '临夏回族自治州', '甘南藏族自治州', '西宁市', '海东市', '海北藏族自治州', '黄南藏族自治州', '海南藏族自治州', '果洛藏族自治州', '玉树藏族自治州', '海西蒙古族藏族自治州', '银川市', '石嘴山市', '吴忠市', '固原市', '中卫市', '乌鲁木齐市', '克拉玛依市', '吐鲁番市', '哈密市', '昌吉回族自治州', '博尔塔拉蒙古自治州', '巴音郭楞蒙古自治州', '阿克苏地区', '克孜勒苏柯尔克孜自治州', '喀什地区', '和田地区', '伊犁哈萨克自治州', '塔城地区', '阿勒泰地区']
list1less=[]#无后缀一级地址列表
list2less=[]#无后缀二级地址列表
test = input()
test = test[:-1]
rank = re.match(r'\d(?=!)',test).group()
test = re.sub(r'\d!','',test,1)
name = re.match(r'\w+',test)
pnum = re.search(r'\d{11}',test)
test = re.sub(r'\w+,','',test,1)
test = re.sub(r'\d{11}','',test,1)
addressregex = re.compile(r'(?P<one>[^省]+自治区|.*?省|.*?行政区|)(?P<two>[^市]+自治州|.*?地区|.*?行政单位|.+盟|.*?市|)(?P<three>[^县]+县|.+?区|.+市|.+旗|.+林区|.+特区|)?(?P<four>.+?镇|.+?街道|.+?乡|.+?苏木|.+?县辖区|)(?P<five>.+)')
addressmatch = re.match(addressregex,test)
addresslist=[addressmatch.group(1),addressmatch.group(2),addressmatch.group(3),addressmatch.group(4),addressmatch.group(5)]
for s in range(0,len(list1)):#删除一级地址后缀
    if s <= 3:
        list1less.append(list1[s])
    else:
        linshi = re.match(r'([^省]+(?=自治区))|(.*?(?=省))|(.*?(?=行政区))|(.*?(?=市)|)',list1[s])
        list1less.append(linshi.group())
for s in range(0,len(list2)):#删除二级地址后缀
    linshi = re.match(r'[^市]+(?=自治州)|.*?(?=地区)|.*?(?=行政单位)|.+(?=盟)|.*?(?=市)|',list2[s])
    list2less.append(linshi.group())
if addresslist[0] == '' and addresslist[1] != '': #一级地址缺失
    for s in range(0,len(list1less)):
        regexad1 = re.compile(r''+list1less[s])
        linshi = re.search(regexad1,addresslist[1])
        if linshi != None:
            if s <=3:
                addresslist[0] = list1[s]
                break
            else:
                addresslist[1] = re.sub(regexad1, '', addresslist[1], 1)
                addresslist[0] = list1[s]
                break
elif addresslist[0] != '' and addresslist[1] == '' and addresslist[2] != '' : #二级地址缺失
    for s in range(0,len(list2less)):
        regexad2 = re.compile(r''+list2less[s])
        linshi = re.search(regexad2,addresslist[2])
        if linshi != None:
            addresslist[2] = re.sub(regexad2,'',addresslist[2],1)
            addresslist[1] = list2[s]
            break
elif addresslist[0] == '' and addresslist[1] == '': #一级，二级地址同时缺失
    for s in range(0,len(list1less)):
        regexad1 = re.compile(r'' + list1less[s])
        linshi = re.search(regexad1, addresslist[2])
        if linshi != None:
            addresslist[2] = re.sub(regexad1, '', addresslist[2], 1)
            addresslist[0] = list1[s]
            break
    for s in range(0,len(list2less)):
        regexad2 = re.compile(r''+list2less[s])
        linshi = re.search(regexad2,addresslist[2])
        if linshi != None:
            addresslist[2] = re.sub(regexad2,'',addresslist[2],1)
            addresslist[1] = list2[s]
            break
# print(name,pnum,addresslist)
if rank == '2':
    addresslist.append('')
    addresslist.append('')
    addnum = re.search(r'\d+号',addresslist[4]).group()
    if addnum != None:  # 存在门牌号
        addresslist[6] = re.sub(r'.*?号','',addresslist[4],1)
        addresslist[5] = addnum
        addresslist[4] = re.sub(r''+addresslist[5]+addresslist[6],'',addresslist[4],1)
    else:
        ad5 = re.search(r'.*?街|.*?路|.*?巷|.*?道',addresslist[4]).group()
        addresslist[5] = ''
        addresslist[6] = re.sub(r''+ad5,'',addresslist[4],1)
        addresslist[4] = ad5
datedict = {'姓名':name.group(),'手机':pnum.group(),'地址':addresslist}
datejson = json.dumps(datedict,ensure_ascii=False,indent=4)
print(datejson)