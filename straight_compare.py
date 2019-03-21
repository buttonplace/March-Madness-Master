import random

def straight_compare(name1, name2, stat, data, team):
    n1s = float(data[name1][team][stat])
    n2s = float(data[name2][team][stat])
    # print(f'{name1} has {n1s} {stat} and {name2} has {n2s} {stat}.')
    if n1s > n2s:
        return name1
    elif n1s < n2s:
        return name2
    else:
        if random.random() < .5:
            return name1
        else:
            return name2

def straight_compare_fg(name1, name2, data):
    return straight_compare(name1, name2, 'fg', data, 'Team')

def opp_straight_compare_fg(name1, name2, data):
    return straight_compare(name1, name2, 'fg', data, 'Opponent')

def straight_compare_fga(name1, name2, data):
    return straight_compare(name1, name2, 'fga', data, 'Team')

def opp_straight_compare_fga(name1, name2, data):
    return straight_compare(name1, name2, 'fga', data, 'Opponent')

def straight_compare_fg_pct(name1, name2, data):
    return straight_compare(name1, name2, 'fg_pct', data, 'Team')

def opp_straight_compare_fg_pct(name1, name2, data):
    return straight_compare(name1, name2, 'fg_pct', data, 'Opponent')

def straight_compare_fg2(name1, name2, data):
    return straight_compare(name1, name2, 'fg2', data, 'Team')

def opp_straight_compare_fg2(name1, name2, data):
    return straight_compare(name1, name2, 'fg2', data, 'Opponent')

def straight_compare_fg2a(name1, name2, data):
    return straight_compare(name1, name2, 'fg2a', data, 'Team')

def opp_straight_compare_fg2a(name1, name2, data):
    return straight_compare(name1, name2, 'fg2a', data, 'Opponent')

def straight_compare_fg2_pct(name1, name2, data):
    return straight_compare(name1, name2, 'fg2_pct', data, 'Team')

def opp_straight_compare_fg2_pct(name1, name2, data):
    return straight_compare(name1, name2, 'fg2_pct', data, 'Opponent')

def straight_compare_fg3(name1, name2, data):
    return straight_compare(name1, name2, 'fg3', data, 'Team')

def opp_straight_compare_fg3(name1, name2, data):
    return straight_compare(name1, name2, 'fg3', data, 'Opponent')

def straight_compare_fg3a(name1, name2, data):
    return straight_compare(name1, name2, 'fg3a', data, 'Team')

def opp_straight_compare_fg3a(name1, name2, data):
    return straight_compare(name1, name2, 'fg3a', data, 'Opponent')

def straight_compare_fg3_pct(name1, name2, data):
    return straight_compare(name1, name2, 'fg3_pct', data, 'Team')

def opp_straight_compare_fg3_pct(name1, name2, data):
    return straight_compare(name1, name2, 'fg3_pct', data, 'Opponent')

def straight_compare_ft(name1, name2, data):
    return straight_compare(name1, name2, 'ft', data, 'Team')

def opp_straight_compare_ft(name1, name2, data):
    return straight_compare(name1, name2, 'ft', data, 'Opponent')

def straight_compare_fta(name1, name2, data):
    return straight_compare(name1, name2, 'fta', data, 'Team')

def opp_straight_compare_fta(name1, name2, data):
    return straight_compare(name1, name2, 'fta', data, 'Opponent')

def straight_compare_ft_pct(name1, name2, data):
    return straight_compare(name1, name2, 'ft_pct', data, 'Team')

def opp_straight_compare_ft_pct(name1, name2, data):
    return straight_compare(name1, name2, 'ft_pct', data, 'Opponent')

def straight_compare_orb(name1, name2, data):
    return straight_compare(name1, name2, 'orb', data, 'Team')

def opp_straight_compare_orb(name1, name2, data):
    return straight_compare(name1, name2, 'orb', data, 'Opponent')

def straight_compare_drb(name1, name2, data):
    return straight_compare(name1, name2, 'drb', data, 'Team')

def opp_straight_compare_drb(name1, name2, data):
    return straight_compare(name1, name2, 'drb', data, 'Opponent')

def straight_compare_trb(name1, name2, data):
    return straight_compare(name1, name2, 'trb', data, 'Team')

def opp_straight_compare_trb(name1, name2, data):
    return straight_compare(name1, name2, 'trb', data, 'Opponent')

def straight_compare_ast(name1, name2, data):
    return straight_compare(name1, name2, 'ast', data, 'Team')

def opp_straight_compare_ast(name1, name2, data):
    return straight_compare(name1, name2, 'ast', data, 'Opponent')

def straight_compare_stl(name1, name2, data):
    return straight_compare(name1, name2, 'stl', data, 'Team')

def opp_straight_compare_stl(name1, name2, data):
    return straight_compare(name1, name2, 'stl', data, 'Opponent')

def straight_compare_blk(name1, name2, data):
    return straight_compare(name1, name2, 'blk', data, 'Team')

def opp_straight_compare_blk(name1, name2, data):
    return straight_compare(name1, name2, 'blk', data, 'Opponent')

def straight_compare_tov(name1, name2, data):
    return straight_compare(name1, name2, 'tov', data, 'Team')

def opp_straight_compare_tov(name1, name2, data):
    return straight_compare(name1, name2, 'tov', data, 'Opponent')

def straight_compare_pf(name1, name2, data):
    return straight_compare(name1, name2, 'pf', data, 'Team')

def opp_straight_compare_pf(name1, name2, data):
    return straight_compare(name1, name2, 'pf', data, 'Opponent')

def straight_compare_pts(name1, name2, data):
    return straight_compare(name1, name2, 'pts', data, 'Team')

def opp_straight_compare_pts(name1, name2, data):
    return straight_compare(name1, name2, 'pts', data, 'Opponent')

def straight_compare_pts_per_g(name1, name2, data):
    return straight_compare(name1, name2, 'pts_per_g', data, 'Team')

def opp_straight_compare_pts_per_g(name1, name2, data):
    return straight_compare(name1, name2, 'pts_per_g', data, 'Opponent')
