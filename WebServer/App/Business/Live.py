import time
import os
import re
import pickle
from urllib.parse import urlparse
from Lib.Visitor import Visitor


class Live():
    'live'

    __config = {}

    def __init__(self, config):
        self.__config = config
        pass

    def douyu(self, room):
        parse = urlparse(room)
        api = self.__config['api']['douyu'] + parse.path
        body = self.__visitor.send_request(api).visit()
        if(body is not None):
            data = eval(body)
            nickname = data['data']['owner_name']
            room_name = data['data']['room_name']
            category = data['data']['cate_name']
            screenshot = data['data']['room_thumb']
            state = True if data['data']['room_status'] == '1' else False
            return {'nickname': nickname, 'state': state, 'room_name': room_name, 'category': category, 'screenshot': screenshot}

    def huya(self, room):
        body = self.__visitor.send_request(room).visit()
        if(body is not None):
            # 房间信息
            room_data = re.findall(r' var TT_ROOM_DATA = (.+?);', body)
            room_data = room_data[0].replace('true', 'True')
            room_data = room_data.replace('false', 'False')
            room_data = room_data.replace('null', 'None')
            room_data = eval(room_data)
            # 主播信息
            profile_info = re.findall(r'var TT_PROFILE_INFO = (.+?);', body)
            profile_info = eval(profile_info[0])
            state = True if(room_data['state'] == 'ON') else False
            nickname = profile_info['nick']
            room_name = room_data['introduction']
            category = room_data['gameFullName']
            screenshot = room_data['screenshot']
            return {'nickname': nickname, 'state': state, 'room_name': room_name, 'category': category, 'screenshot': screenshot}

    def panda(self, room):
        body = self.__visitor.send_request(room).visit()
        if(body is not None):
            # 房间信息
            room_data = re.findall(r'window._config_roominfo = ([\s\S]+?);\s', body)
            room_data = room_data[0].replace('true', 'True')
            room_data = room_data.replace('false', 'False')
            room_data = room_data.replace('null', 'None')
            room_data = eval(room_data)
            nickname = room_data['hostinfo']['name']
            room_name = room_data['roominfo']['name']
            screenshot = room_data['roominfo']['pictures']['img']
            state = True if(room_data['videoinfo']['status'] == '2') else False
            category = room_data['roominfo']['classification']
            return {'nickname': nickname, 'state': state, 'room_name': room_name, 'category': category, 'screenshot': screenshot}

    def longzhu(self, room):
        body = self.__visitor.send_request(room).visit()
        if(body is not None):
            # 房间信息
            room_data = re.findall(r'var roomInfo = ([\s\S]+?);', body)
            room_data = room_data[0].replace('true', 'True')
            room_data = room_data.replace('false', 'False')
            room_data = room_data.replace('null', 'None')
            room_data = eval(room_data)
            nickname = room_data['Name']
            room_name = '德云色'
            screenshot = room_data['Logo']
            category = ''
            hour = time.strftime('%H', time.localtime(time.time()))
            state = True if(int(hour) >= 20 or int(hour) <= 2) else False
            return {'nickname': nickname, 'state': state, 'room_name': room_name, 'category': category, 'screenshot': screenshot}

    def run(self):
        self.__visitor = Visitor()
        path = os.path.join(self.__config['storage_path'], 'live.pkl')
        print('开始爬取数据...')
        if(os.path.exists(path) is not True):
            rooms = {}
        else:
            fo = open(path, 'rb+')
            ret = fo.read()
            fo.close()
            rooms = {}
        for host in self.__config['rooms']:
            rooms[host] = {}
            for room in self.__config['rooms'][host]:
                if('douyu' == host):
                    ret = self.douyu(room)
                elif('huya' == host):
                    ret = self.huya(room)
                elif('panda' == host):
                    ret = self.panda(room)
                elif('longzhu' == host):
                    ret = self.longzhu(room)
                # print("{nickname} {state} 分类：{category} 标题：{room_name} 封面：{screenshot}".format(nickname=ret['nickname'], state=ret['state'], room_name=ret['room_name'], category=ret['category'], screenshot=ret['screenshot']))
                rooms[host][room] = ret
                time.sleep(1)
        fo = open(path, 'wb+')
        fo.write(pickle.dumps(rooms))
        fo.close()
        print('结束...')
        return rooms

    def get(self):
        path = os.path.join(self.__config['storage_path'], 'live.pkl')
        fo = open(path, 'rb+')
        ret = fo.read()
        live_list = pickle.loads(ret)
        for x in live_list:
            live_list[x] = sorted(live_list[x].items(), key=lambda item: item[1]['state'], reverse=True)
        return live_list
