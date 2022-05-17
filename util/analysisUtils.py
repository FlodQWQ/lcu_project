def tier_analysis(tier, division, point):
    tier_map = {'IRON': '坚韧黑铁', 'BRONZE': '英勇黄铜', 'SILVER': '不屈白银', 'GOLD': '荣耀黄金', 'PLATINUM': '华贵铂金',
                'DIAMOND': '璀璨钻石', 'MASTER': '超凡大师', 'GRANDMASTER': '傲世宗师', 'CHALLENGER': '最强王者'}
    if division != 'NONEED':
        return tier_map[tier] + division + " " + str(point) + "胜点"
    else:
        return tier_map[tier] + " " + str(point) + "胜点"
