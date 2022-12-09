# baseUrl
baseUrl = 'https://spla3.yuu26.com/api'
# p1
regular = '/regular'
bankara_challenge = '/bankara-challenge'
bankara_open = '/bankara-open'
fest = '/fest'
x = '/x'
samonrun = '/coop-grouping'
# p2
now = '/now'
next = '/next'
schedule = '/schedule'

rules = {"LOFT": "真格塔楼", "GOAL": "真格鱼虎", "AREA": "真格区域", "CLAM": "真格蛤蜊"}


def get_rule(key):
    return rules.get(key)

