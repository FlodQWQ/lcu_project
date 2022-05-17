import operator


def tier_analysis(tier, division, point):
    tier_map = {'IRON': '坚韧黑铁', 'BRONZE': '英勇黄铜', 'SILVER': '不屈白银', 'GOLD': '荣耀黄金', 'PLATINUM': '华贵铂金',
                'DIAMOND': '璀璨钻石', 'MASTER': '超凡大师', 'GRANDMASTER': '傲世宗师', 'CHALLENGER': '最强王者'}
    if division != 'NONEED':
        return tier_map[tier] + division + " " + str(point) + "胜点"
    else:
        return tier_map[tier] + " " + str(point) + "胜点"


def client_status_analysis(status):
    status_map = {'None': '大厅中', 'Lobby': '房间中', 'Matchmaking': '匹配中', 'ReadyCheck': '找到对局', 'InProgress': '游戏中',
                  'WaitingForStats': '等待结算页面', 'PreEndOfGame': '对局结束', 'Reconnect': '重新连接中', 'ChampSelect': '选择英雄'}
    if status in status_map:
        return status_map[status]
    else:
        return '未知状态' + '(' + status + ')'


def game_zone_analysis(zone):
    HN = ["艾欧尼亚", "祖安", "诺克萨斯", "班德尔城", "皮尔特沃夫", "战争学院", "巨神峰", "雷瑟守备", "裁决之地", "黑色玫瑰", "暗影岛", "钢铁烈阳", "水晶之痕",
          "均衡教派",
          "影流", "守望之海", "征服之海", "卡拉曼达", "皮城警备"]
    WT = ["比尔吉沃特", "德玛西亚", "弗雷尔卓德", "无畏先锋", "恕瑞玛", "扭曲丛林", "巨龙之巢"]
    EDU = ["教育网"]
    BGP = ["男爵领域", "峡谷之巅"]
    if operator.contains(zone['environment'], 'HN'):
        list_str = list(zone['environment'])
        list_str.pop(0)
        list_str.pop(0)
        game_zone_num = int(''.join(list_str))
        game_zone = HN[game_zone_num - 1]
    elif operator.contains(zone['environment'], 'WT'):
        list_str = list(zone['environment'])
        list_str.pop(0)
        list_str.pop(0)
        game_zone_num = int(''.join(list_str))
        game_zone = WT[game_zone_num - 1]
    elif operator.contains(zone['environment'], 'EDU'):
        list_str = list(zone['environment'])
        list_str.pop(0)
        list_str.pop(0)
        list_str.pop(0)
        game_zone_num = int(''.join(list_str))
        game_zone = EDU[game_zone_num - 1]
    else:
        list_str = list(zone['environment'])
        list_str.pop(0)
        list_str.pop(0)
        list_str.pop(0)
        game_zone_num = int(''.join(list_str))
        game_zone = BGP[game_zone_num - 1]
    return game_zone
