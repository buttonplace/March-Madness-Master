import json
import random
import straight_compare
import bracketeer

with open('seeded.json') as f:
    seeded_data = json.load(f)
with open('stats.json') as f:
    named_data = json.load(f)
def return_pair(pairs, set, compare_function, data):
    team1 = compare_function(pairs[2*set][0], pairs[2*set][1], data)
    team2 = compare_function(pairs[2*set+1][0], pairs[2*set+1][1], data)
    return team1, team2
def run_round(pairs, compare_function, data):
    pair_ret = []
    for i in range(0, len(pairs)//2):
        pair_ret.append(return_pair(pairs, i, compare_function, data))
    return pair_ret
#Implement more comparisons here!



def run_tournament(compare_function):
    conferences = ['East', 'West', 'Midwest', 'South']
    ro64_seeds = [('1', '16'), ('8', '9'), ('5', '12'), ('4', '13'), ('6', '11'), ('3', '14'), ('7', '10'),
                  ('2', '15'), ]
    final_four = {}
    finals = []
    all64 = {}
    all32 = {}
    all16 = {}
    all8 = {}
    for conference in conferences:
        ro64 = []
        ro32 = []
        ro16 = []
        ro8 = []
        ro4 = []
        ro2 = []
        for pair in ro64_seeds:
            ro64.append((seeded_data[conference][pair[0]]['Name'], seeded_data[conference][pair[1]]['Name']))
        print(f'{conference} Conference Round of 64:')
        all64[conference] = ro64
        print(ro64)
        ro32 = run_round(ro64, compare_function, named_data)
        print(f'{conference} Conference Round of 32:')
        all32[conference] = ro32
        print(ro32)
        ro16 = run_round(ro32, compare_function, named_data)
        print(f'{conference} Conference Round of 16:')
        all16[conference] = ro16
        print(ro16)
        ro8 = run_round(ro16, compare_function, named_data)
        print(f'{conference} Conference Round of 8:')
        all8[conference] = ro8
        print(ro8)
        winner = compare_function(ro8[0][0], ro8[0][1], named_data)
        print(f'{conference} Conference Winner:')
        print(winner)
        final_four[conference] = winner
    print(final_four)
    print('East West Final Four Game:')
    print(f"{final_four['East']} vs {final_four['West']}")
    winner = compare_function(final_four['East'], final_four['West'], named_data)
    finals.append(winner)
    print('Midwest South Final Four Game:')
    print(f"{final_four['Midwest']} vs {final_four['South']}")
    winner = compare_function(final_four['Midwest'], final_four['South'], named_data)
    finals.append(winner)
    print('Championship Game:')
    print(f'{finals[0]} vs {finals[1]}')
    winner = compare_function(finals[0], finals[1], named_data)
    print(f'Winner is {winner}')
    bracketeer.bracket(all64, all32, all16, all8, final_four, finals, winner)


