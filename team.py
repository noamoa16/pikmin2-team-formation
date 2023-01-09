# 大会参加者リスト
# ピクミン2の合計スコアが一定(e.g. 698000)以上の人全員
# name: 名前, ability: 実力, participation_prob: 参加確率
players = [
    {
        'name': 'ごれい',
        'ability': 1492,
        'participation_prob': 0.5
    },
    {
        'name': 'mercysnow',
        'ability': 1492,
        'participation_prob': 0.7
    },
    {
        'name': 'iid01',
        'ability': 1468,
        'participation_prob': 0.4
    },
    {
        'name': '不時着',
        'ability': 1309,
        'participation_prob': 0.6
    },
    {
        'name': 'albut3',
        'ability': 1382,
        'participation_prob': 0.9
    },
    {
        'name': 'flyinghawk',
        'ability': 1309,
        'participation_prob': 0.2
    },
]

# 平均実力
def mean_ability():
    return sum(player['ability'] for player in players) / len(players)

# 仮想実力で降順ソート
def players_sort():
    # 仮想実力を計算
    for player in players:
        prob = player['participation_prob']
        ability = player['ability']
        virtual_ability = prob *  ability + (1 - prob) * mean_ability()
        player['virtual_ability'] = virtual_ability

    players.sort(key=lambda player: player['virtual_ability'], reverse=True)
players_sort()

# 参加者リスト
participants = ['新参者', 'mercysnow', '不時着', 'ごれい', 'albut3', 'iid01']

# 推定最小参加者数
min_participants = 4

ATeam = []
BTeam = []

for participant in participants:
    # 大会に参加したことがある
    if participant in [player['name'] for player in players]:
        player = players[[player['name'] for player in players].index(participant)]
        player['participation_prob'] = 1
    # ない
    else:
        players.append({
            'name': participant, 
            'ability': mean_ability(), 
            'participation_prob': 1,
        })
    players_sort() 

    if len(ATeam) + len(BTeam) < min_participants or len(ATeam) == len(BTeam):
        index = [player['name'] for player in players].index(participant)
        if index % 4 == 0 or index % 4 == 3:
            ATeam.append(participant)
        else:
            BTeam.append(participant)
    else:
        if len(ATeam) < len(BTeam):
            ATeam.append(participant)
        else:
            BTeam.append(participant)

print(ATeam, BTeam)