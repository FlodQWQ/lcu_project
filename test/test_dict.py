if __name__ == '__main__':
    my_dict = {'actions': [
        [
            {'actorCellId': 0, 'championId': 0, 'completed': False, 'id': 1, 'isAllyAction': True, 'isInProgress': True,
             'pickTurn': 1, 'type': 'pick'
             },
        ]
    ], 'allowBattleBoost': False, 'allowDuplicatePicks': False, 'allowLockedEvents': False, 'allowRerolling': False,
        'allowSkinSelection': True, 'bans': {'myTeamBans': [], 'numBans': 0, 'theirTeamBans': []
                                             }, 'benchChampionIds': [], 'benchEnabled': False, 'boostableSkinCount': 1,
        'chatDetails': {'chatRoomName': 'c1~15e1850f0a5f85bc2a274cadcac14d37dd1b88d2@sec.pvp.net',
                        'chatRoomPassword': 'XiSSTSa59EFULRV3'
                        }, 'counter': -1, 'entitledFeatureState': {'additionalRerolls': 0, 'unlockedSkinIds': []
                                                                   }, 'gameId': 0, 'hasSimultaneousBans': False,
        'hasSimultaneousPicks': True, 'isCustomGame': True, 'isSpectating': False, 'localPlayerCellId': 0,
        'lockedEventIndex': -1, 'myTeam': [
            {'assignedPosition': '', 'cellId': 0, 'championId': 0, 'championPickIntent': 0, 'entitledFeatureType': '',
             'selectedSkinId': 0, 'spell1Id': 4, 'spell2Id': 14, 'summonerId': 2440321375152224, 'team': 1,
             'wardSkinId': 132
             },
            {'assignedPosition': '', 'cellId': 1, 'championId': 0, 'championPickIntent': 0, 'entitledFeatureType': '',
             'selectedSkinId': 0, 'spell1Id': 1, 'spell2Id': 3, 'summonerId': 2968149215311328, 'team': 1,
             'wardSkinId': -1
             }
        ], 'recoveryCounter': 0, 'rerollsRemaining': 0, 'skipChampionSelect': False, 'theirTeam': [],
        'timer': {'adjustedTimeLeftInPhase': 89119, 'internalNowInEpochMs': 1652772564672, 'isInfinite': False,
                  'phase': 'BAN_PICK', 'totalTimeInPhase': 92307
                  }, 'trades': [
            {'cellId': 1, 'id': 101, 'state': 'INVALID'
             }
        ]
    }

    for player in my_dict['myTeam']:
        print(player['summonerId'])
