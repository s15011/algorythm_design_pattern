#!/usr/bin/env python3
GU = 1
CHOKI = 2
PA = 3
DRAW = 1
WIN = 2
LOSE = 3
judge = 0
LOOP_COUNT = 1000000

def hand_generate():
    import random

    player = random.randint(1, 3)
    computer = random.randint(1, 3)

    return(player, computer)

def janken(player, computer):
    if player == GU and computer == GU:
        return DRAW
    elif player == GU and computer == CHOKI:
        return WIN
    elif player == GU and computer == PA:
        return LOSE
    elif player == CHOKI and computer == GU:
        return LOSE
    elif player == CHOKI and computer == CHOKI:
        return DRAW
    elif player == CHOKI and computer == PA:
        return WIN
    elif player == PA and computer == GU:
        return WIN
    elif player == PA and computer == CHOKI:
        return LOSE
    elif player == PA and computer == PA:
        return DRAW

def janken2(player, computer):
    if player == computer:
        judge = DRAW
    elif (player == GU and computer == CHOKI or
            player == CHOKI and computer == PA or
            player == PA and computer == GU):
        judge = WIN
    else:
        judge = LOSE

def janken3(player, computer):
    DRAW2 = 0
    WIN2 = 1
    LOSE2 = 2

    judge = (player - computer + 3) % 3

    if(judge == DRAW2):
        return
    if(judge == WIN2):
        return
    if(judge == LOSE2):
        return

def janken4(player, computer):
    judge = [[DRAW, WIN, LOSE],
            [LOSE, DRAW, WIN],
            [WIN, LOSE, DRAW]]

    if (judge[player - 1][computer - 1] == DRAW):
        return
    elif (judge[player - 1][computer - 1] == WIN):
        return
    elif (judge[player - 1][computer - 1] == LOSE):
        return

if __name__ == '__main__':

    import time
    import sys


    #phand, chand = hand_generate
    #janken4(phand,chand)

    start = time.time()
    for _ in range(LOOP_COUNT):
        phand, chand = hand_generate()
        janken(phand, chand)
        sys.stdout.flush()
    end = time.time()
    print('else if9パターン')
    print('経過時間', (end - start))

    start = time.time()
    for _ in range(LOOP_COUNT):
        phand, chand = hand_generate()
        janken2(phand, chand)
        sys.stdout.flush()
    end = time.time()
    print('else if3パターン')
    print('経過時間', (end - start))

    start = time.time()
    for _ in range(LOOP_COUNT):
        phand, chand = hand_generate()
        janken3(phand, chand)
        sys.stdout.flush()
    end = time.time()
    print('計算式パターン')
    print('経過時間', (end - start))

    start = time.time()
    for _ in range(LOOP_COUNT):
        phand, chand = hand_generate()
        janken4(phand, chand)
        sys.stdout.flush()
    end = time.time()
    print('配列パターン')
    print('経過時間', (end - start))
