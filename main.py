import simulate, straight_compare

function_dict = {'straight_compare_fg': straight_compare.straight_compare_fg,
                 'straight_compare_fga': straight_compare.straight_compare_fga,
                 'straight_compare_fg_pct': straight_compare.straight_compare_fg_pct,
                 'straight_compare_fg2': straight_compare.straight_compare_fg2,
                 'straight_compare_fg2a': straight_compare.straight_compare_fg2a,
                 'straight_compare_fg2_pct': straight_compare.straight_compare_fg2_pct,
                 'straight_compare_fg3': straight_compare.straight_compare_fg3,
                 'straight_compare_fg3a': straight_compare.straight_compare_fg3a,
                 'straight_compare_fg3_pct': straight_compare.straight_compare_fg3_pct,
                 'straight_compare_ft': straight_compare.straight_compare_ft,
                 'straight_compare_fta': straight_compare.straight_compare_fta,
                 'straight_compare_ft_pct': straight_compare.straight_compare_ft_pct,
                 'straight_compare_orb': straight_compare.straight_compare_orb,
                 'straight_compare_drb': straight_compare.straight_compare_drb,
                 'straight_compare_trb': straight_compare.straight_compare_trb,
                 'straight_compare_ast': straight_compare.straight_compare_ast,
                 'straight_compare_stl': straight_compare.straight_compare_stl,
                 'straight_compare_blk': straight_compare.straight_compare_blk,
                 'straight_compare_tov': straight_compare.straight_compare_tov,
                 'straight_compare_pf': straight_compare.straight_compare_pf,
                 'straight_compare_pts': straight_compare.straight_compare_pts,
                 'straight_compare_pts_per_g': straight_compare.straight_compare_pts_per_g}
def main():
    while(True):
        print('What function would you like to use?')
        x = input()
        if x in function_dict:
            simulate.run_tournament(function_dict[x])
        else:
            print('That aint a function')
if __name__ == '__main__':
    main()