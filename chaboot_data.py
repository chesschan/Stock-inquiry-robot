import random
import re

import itchat
from iexfinance.stocks import Stock, get_historical_data
# 导入rasa_nlu所用到的包，
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config

# Create a trainer that uses this config
# 加载训练所需的yml配置文件
trainer = Trainer(config.load("config_spacy.yml"))

# 加载训练所需的json数据
# Load the training data
training_data = load_data('training_data.json')

# 进行自然语言模型训练
# Create an interpreter by training the model
interpreter = trainer.train(training_data)


class GetData(object):  # 一个类，用于创建股票对象

    def __init__(self, code=None):  # 用于创建对象
        self.aapl = Stock(code)
        # 成交量
        self.data = get_historical_data(code, output_format='pandas').iloc[-1]
        self.aapl2 = Stock(code, output_format='pandas')

    def price(self):  # 用来查询价格
        price_data = self.aapl.get_price()
        return price_data

    def volume(self):  # 查询销量
        volume_data = self.data.loc["volume"]
        return volume_data


    def open_price(self):   #查询开盘价
        openclose = self.aapl.get_open_close()
        open_price = openclose.get('open').get('price')
        return open_price

    def close_price(self):   #查询收盘价
        openclose = self.aapl.get_open_close()
        close_price = openclose.get('close').get('price')
        return close_price

say_hello = ['hey,Which stock do you want to query?', 'hello,Which stock do you want to query?',
             'hi,Which stock do you want to query?', 'hey there,Which stock do you want to query?',
             'how are you,Which stock do you want to query?', 'how are u,Which stock do you want to query?',
             "what's up,Which stock do you want to query?", 'wassup,Which stock do you want to query?',
             "how's it going,Which stock do you want to query?", "what's popping,Which stock do you want to query?",
             "what's good,Which stock do you want to query?",
             'how are we doing today,Which stock do you want to query?']
user_session = []
# 文字消息
@itchat.msg_register(['Text'])  # 装饰器，用于扩充函数的功能，是微信提供的功能，可以接受文本消息
def text_reply(msg):
    # print(msg['Text'])
    # 用训练完的模型，进行自然语言预测
    data = interpreter.parse(msg['Text'])
    # 预测后获取需要的实体和意图
    intent = data.get('intent').get('name')
    cocv = ''
    # greet，stock_search为自然语言的两个意图
    if intent == 'greet':
        # 如果为打招呼的主题，则与对方打招呼
        return random.choice(say_hello)
    # 如果是关于股票查询主题，则进行下一步操作
    if intent == 'stock_search':
        values = data.get('entities')
        # 遍历rsra预测后的一些信息
        for i in range(len(values)):
            # 此条件为判断如果为单轮查询
            if len(values) > 1 and i == 0:
                # 获取rsra预测后的一些信息
                company = data.get('entities')[i].get('value')
                # 创建stock对象
                try:
                    code = GetData(company)
                    user_session.append(code)  # 保存存储对象
                except:
                    pass
                # 拼接训练得到的全部字符串
            cocv +=  data.get('entities')[i].get('value') + ' '
    info_en_list = ['price', 'volume', 'close', 'open']
    # 用正则匹配判断是否输入的是公司
    company_com = re.findall(' ', msg['Text'])
    # 多轮查询操作
    for info in info_en_list:
        # 用刚才的正则作为条件,如果是公司,则创建对象
        if msg['Text'] != 'price' and msg['Text'] != 'volume' and 'market' and not company_com:
            try:
                code = GetData(msg['Text'])
                user_session.append(code)  # 保存存储对象
                return "Hi, I can search for stock info for you.1.price  2.volume  3.open price 4.close price"
            except:
                pass
        # 进行判断rasa训练预测后的信息是属于哪一类
        if info in cocv and user_session:
            message = "This company {} is:\n".format(info)  # -1代表最后一次保存的对象，即最后一次输入的内容
            # 如果是获取价格
            if (info == 'price') and ('close' not in cocv) and ('open' not in cocv):
                message += str(user_session[-1].price())
                return message
            # 如果是获取成交量
            if info == 'volume':
                message += str(user_session[-1].volume())
                return message
            # 如果是获取收盘价
            if info == 'close':
                message += str(user_session[-1].close_price())
                return message
            # 如果是获取开盘价
            if info == 'open':
                message += str(user_session[-1].open_price())
                return message
    return "I'm sorry, I cannot understand you."




# 执行当前文件
if __name__ == '__main__':
    itchat.auto_login()  # 用于微信登陆、接受信息
    friends = itchat.get_friends(update=True)[0:]
    Name = {}
    Nic = []
    User = []
    for i in range(len(friends)):
        Nic.append(friends[i]["NickName"])
        User.append(friends[i]["UserName"])
    for i in range(len(friends)):
        Name[Nic[i]] = User[i]
    itchat.run()  # 执行之后，弹出二维码
