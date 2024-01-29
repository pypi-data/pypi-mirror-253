import time

chinese = ['〇','一','二','三','四','五','六','七','八','九']
zenkaku_num = ['０','１','２','３','４','５','６','７','８','９']
chinese_wday = ['月','火','水','木','金','土','日']
kanshi = ['ねずみ','うし','とら','うさぎ','たつ','へび','うま','ひつじ','さる','とり','いぬ','いのしし']
kanshi_chinese = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
gengo = ['明治','大正','昭和','平成','令和']

def num_to_kanji(int_num):
    if int_num < 0:
        return '負数入力'
    kanji = ''
    for digit in str(int_num):
        kanji = kanji + chinese[int(digit)]
    return kanji

def num_to_zenkaku(num):
    if num < 0:
        return '負数入力'
    zenkaku = ''
    for digit in str(num):
        zenkaku = zenkaku + zenkaku_num[int(digit)]
    return zenkaku

def to_hankaku(zenkaku):
    """
    zenkaku数字文字列を半角数字文字列に変換する
    """
    hankaku = ''
    for digit in str(zenkaku):
        hankaku = hankaku + str(zenkaku_num.index(digit))
    return hankaku

def wareki(year):
    if year<1868:
        return ('元号未登録', year)
    elif 1868<=year<=1911:
        return ('明治', year - 1867)
    elif 1912<=year<=1925:
        return ('大正', year - 1911)
    elif 1926<=year<=1988:
        return ('昭和', year - 1925)
    elif 1989<=year<=2018:
        return ('平成', year - 1988)
    else:
        return ('令和', year - 2018)

def eto(year):
    num = (year - 2008)%12
    return (kanshi_chinese[num], kanshi[num])

def time_lapse(float_num, mode='k'):
    """
    秒数表示された経過時間を時間、分、秒に直す

    mode : 'k':漢字表記 'e':英字表記 's':記号表記
    """
    hour = int(float_num//3600)
    minute = int((float_num//60)%60)
    second = int(float_num%60)
    if mode=='e':
        return '{}h{}m{}s'.format(hour, minute, second)
    elif mode=='s':
        return '{}:{}:{}'.format(hour, minute, second)
    else:
        return '{}時間{}分{}秒'.format(hour, minute, second)

class JT:
    """
    メソッドの種類
    JTime.year() : yyyy年
    JTime.month() : m月
    JTime.day() : d日
    JTime.hour() : h時
    JTime.min() : m分
    JTime.sec() : s秒
    JTime.youbi() : 曜日
    JTime.wareki() : 元号n年
    JTime.eto() : (干支, えと)
    JTime.ymdhms() : yyyy年m月d日h時m分s秒
    JTime.ymd() : yyyy年m月d日
    JTime.ym() : yyyy年m月
    JTime.md() : m月d日
    JTime.hms() : h時m分s秒
    JTime.hm() : h時m分
    JTime.ms() : m分s秒
    """
    def __init__(self, mode='h'):
        """
        Parameters
        ----------
        mode : 'h':半角数字表示  'z':全角数字表示  'k':漢数字表示
        """
        self.mode = mode
    
    def year(self):
        if self.mode == 'h':
            return str(time.localtime()[0]) + '年'
        elif self.mode == 'z':
            return num_to_zenkaku(time.localtime()[0]) + '年' 
        elif self.mode == 'k':
            return num_to_kanji(time.localtime()[0]) + '年'
        else:
            return 'mode: undefined'
    
    def month(self):
        if self.mode == 'h':
            return str(time.localtime()[1]) + '月'
        elif self.mode == 'z':
            return num_to_zenkaku(time.localtime()[1]) + '月' 
        elif self.mode == 'k':
            return num_to_kanji(time.localtime()[1]) + '月'
        else:
            return 'mode: undefined'
        
    def day(self):    
        if self.mode == 'h':
            return str(time.localtime()[2]) + '日'
        elif self.mode == 'z':
            return num_to_zenkaku(time.localtime()[2]) + '日' 
        elif self.mode == 'k':
            return num_to_kanji(time.localtime()[2]) + '日'
        else:
            return 'mode: undefined'
    
    def hour(self):
        if self.mode == 'h':
            return str(time.localtime()[3]) + '時'
        elif self.mode == 'z':
            return num_to_zenkaku(time.localtime()[3]) + '時' 
        elif self.mode == 'k':
            return num_to_kanji(time.localtime()[3]) + '時'
        else:
            return 'mode: undefined'
    
    def min(self):
        if self.mode == 'h':
            return str(time.localtime()[4]) + '分'
        elif self.mode == 'z':
            return num_to_zenkaku(time.localtime()[4]) + '分' 
        elif self.mode == 'k':
            return num_to_kanji(time.localtime()[4]) + '分'
        else:
            return 'mode: undefined'
    
    def sec(self):
        if self.mode == 'h':
            return str(time.localtime()[5]) + '秒'
        elif self.mode == 'z':
            return num_to_zenkaku(time.localtime()[5]) + '秒' 
        elif self.mode == 'k':
            return num_to_kanji(time.localtime()[5]) + '秒'
        else:
            return 'mode: undefined'
    
    def youbi(self):
        return chinese_wday[time.localtime()[6]] + '曜日'
    
    def wareki(self):
        name, year = wareki(time.localtime()[0])
        if self.mode == 'h':
            return name + str(year) + '年'
        elif self.mode == 'z':
            return name + num_to_zenkaku(year) + '年' 
        elif self.mode == 'k':
            return name + num_to_kanji(year) + '年'
        else:
            return 'mode: undefined'
    
    def eto(self):
        return eto(time.localtime()[0])
    
    def ymdhms(self):
        return self.year() + self.month() + self.day() + self.hour() + self.min() + self.sec()
    
    def ymd(self):
        return self.year() + self.month() + self.day()
    
    def ym(self):
        return self.year() + self.month()
    
    def md(self):
        return self.month() + self.day()
    
    def hms(self):
        return self.hour() + self.min() + self.sec()
    
    def hm(self):
        return self.hour() + self.min()
    
    def ms(self):
        return self.min() + self.sec()
