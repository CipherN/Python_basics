#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

# Timtactoe游戏完整代码

import itertools

def win(current_game):

    # 定义该函数，用于对角线输赢判断的公用代码
    def all_same(l):

        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # 判断横向输赢
    for row in game:
        if all_same(row):
            print("Player %d is the winner vertically!" % row[0])

    # 判断竖线输赢
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print("Player %d is the winner vertically!" % check[0])

    # 方法1
    # # 判断对角线\的情况
    # diags_1 = []
    # for ix in range(len(game)):
    #     diags_1.append(game[ix][ix])
    #
    # if diags_1.count(diags_1[0]) == len(diags_1) and diags_1[0] != 0:
    #     print("Player %d has won Diagonally (\)" % diags_1[0])

    # # 判断对角线/的情况
    # diags_2 = []
    # for ix, reverse_ix in enumerate(reversed(range(len(game)))):
    #     diags_2.append(game[ix][reverse_ix])
    #
    # if diags_2.count(diags_2[0]) == len(diags_2) and diags_2[0] != 0:
    #     print("Player %d has won Diagonally (/)" % diags_2[0])

    # 方法2，win函数下再加一个all_same函数
    # # 判断对角线\的情况
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print("Player %d has won Diagonally (/)" % diags[0])
        return True

    # 判断对角线/的情况
    diags = []
    for ix, reverse_ix in enumerate(reversed(range(len(game)))):
        diags.append(game[ix][reverse_ix])

    if all_same(diags):
        print("Player %d has won Diagonally (/)" % diags[0])
        return True
    return False


def game_board(game_map, player=0, row=0, col=0, just_display=False):
    try:
        if game_map[row][col] != 0:
            print('This space is occupied, pls try another!')
            return False

        print("     " + "  ".join([str(i) for i in range(len(game_map))]))

        if not just_display:
            game_map[row][col] = player
        for col, row in enumerate(game_map):
            print(col, row)
        return game_map
    except IndexError:
        print("Did you attempt to play a row or col outside the range: [0,2]? (IndexError)")
        return False
    except Exception as e:
        print(str(e))
        return False

# 初始条件：开始玩游戏、2位玩家、game的初始值
play = True
players = [1, 2]
while play:

    game_size = int(input("What size game Timtactoe?"))
    game = ([[0 for i in range(game_size)] for i in range(game_size)])

    game_won = False
    player_cycle = itertools.cycle([1, 2])
    game_board(game, just_display=True)

# 玩家交替进行输入
    while not game_won:
        current_player = next(player_cycle)
        played = False
        while not played:
            print("Player: %d " % current_player)
            col_choice = int(input("Which col? "))
            row_choice = int(input("Which row? "))
            played = game_board(game, player = current_player, row = row_choice, col = col_choice)

        if win(game):
            game_won = True
            again = input("Game over, would you like to play again? (y/n)")
            if again.lower() == "y":
                print('Restarting')
            elif again.lower() == "n":
                print("Byeeee!")
                play = False
            else:
                print("No valid answer, but ......c ya!")
                play = False