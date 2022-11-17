# https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true
from utils import get_obstacles
def maxium_cell_can_attach(r_q,c_q,n):
    nb_up = n - r_q
    nb_down = r_q - 1
    nb_left = c_q - 1
    nb_right = n - c_q

    nb_up_left = min(nb_up,nb_left)
    nb_up_right = min(nb_up,nb_right)
    nb_down_left = min(nb_down,nb_left)
    nb_down_right = min(nb_down,nb_right)

    return [
            nb_up,
            nb_down,
            nb_left,
            nb_right,
            nb_up_left,
            nb_up_right,
            nb_down_left,
            nb_down_right,
    ]


def get_relative_postion(r_q, c_q, obstacle):
    obstacle_x,obstacle_y = obstacle
    if obstacle_x == r_q and obstacle_y < c_q:
        return 'L'
    if obstacle_x == r_q and obstacle_y > c_q:
        return 'R'
    if c_q == obstacle_y and obstacle_x > r_q:
        return 'U'
    if c_q == obstacle_y and obstacle_x < r_q:
        return 'D'
    if abs(r_q - obstacle_x) == abs(c_q - obstacle_y): #filter out irrelevant pawns
        if obstacle_y < c_q and obstacle_x > r_q:
            return 'UL'
        if obstacle_y > c_q and obstacle_x > r_q:
            return 'UR'
        if obstacle_y > c_q and obstacle_x < r_q:
            return 'DR'
        if obstacle_y < c_q and obstacle_x < r_q:
            return 'DL'
        

def queensAttack(n, k, r_q, c_q, obstacles):
    block_cells = set()
    for obstacle in obstacles:
        obstacle_x,obstacle_y = obstacle
        if get_relative_postion(r_q, c_q, obstacle)=='U':
            for x in range(obstacle_x,n+1):
                block_cells.add(
                    (x,obstacle_y)
                )
        
        
        if get_relative_postion(r_q, c_q, obstacle)=='D':
            for x in range(obstacle_x,0,-1):
                block_cells.add(
                    (x,obstacle_y)
                )

        if get_relative_postion(r_q, c_q, obstacle)=='L':
            for y in range(obstacle_y,0,-1):
                block_cells.add(
                    (obstacle_x,y)
                )

        if get_relative_postion(r_q, c_q, obstacle)=='R':
            for y in range(obstacle_y,n+1):
                block_cells.add(
                    (obstacle_x,y)
                )

        if get_relative_postion(r_q, c_q, obstacle)=='UL':
            step = min(
                n-obstacle_x,obstacle_y-1
            )
            for i_step in range(step+1):
                block_cells.add(
                    (obstacle_x+i_step, obstacle_y-i_step)
                )

        if get_relative_postion(r_q, c_q, obstacle)=='UR':
            step = min(
                n-obstacle_x,n-obstacle_y
            )
            for i_step in range(step+1):
                block_cells.add(
                    (obstacle_x+i_step, obstacle_y+i_step)
                )

        if get_relative_postion(r_q, c_q, obstacle)=='DL':
            step = min(
                obstacle_x-1,obstacle_y-1
            )
            for i_step in range(step+1):
                block_cells.add(
                    (obstacle_x-i_step, obstacle_y-i_step)
                )
        
        if get_relative_postion(r_q, c_q, obstacle)=='DR':
            step = min(
                obstacle_x-1,n-obstacle_y
            )
            for i_step in range(step+1):
                block_cells.add(
                    (obstacle_x-i_step, obstacle_y+i_step)
                )

        

    # print(maxium_cell_can_attach(r_q,c_q,n)[0])
    # print(maxium_cell_can_attach(r_q,c_q,n)[1])
    # print(maxium_cell_can_attach(r_q,c_q,n)[2])
    # print(maxium_cell_can_attach(r_q,c_q,n)[3])
    # print(maxium_cell_can_attach(r_q,c_q,n)[4])
    # print(maxium_cell_can_attach(r_q,c_q,n)[5])
    # print(maxium_cell_can_attach(r_q,c_q,n)[6])
    # print('len(block_cells)',len(block_cells))

    return sum(maxium_cell_can_attach(r_q,c_q,n))- len(block_cells)
    


# if __name__ =="__main__":
n,k=100,100
r_q,c_q = 48,81
obstacles ='''
54 87
64 97
42 75
32 65
42 87
32 97
54 75
64 65
48 87
48 75
54 81
42 81
45 17
14 24
35 15
95 64
63 87
25 72
71 38
96 97
16 30
60 34
31 67
26 82
20 93
81 38
51 94
75 41
79 84
79 65
76 80
52 87
81 54
89 52
20 31
10 41
32 73
83 98
87 61
82 52
80 64
82 46
49 21
73 86
37 70
43 12
94 28
10 93
52 25
50 61
52 68
52 23
60 91
79 17
93 82
12 18
75 64
69 69
94 74
61 61
46 57
67 45
96 64
83 89
58 87
76 53
79 21
94 70
16 10
50 82
92 20
40 51
49 28
51 82
35 16
15 86
78 89
41 98
70 46
79 79
24 40
91 13
59 73
35 32
40 31
14 31
71 35
96 18
27 39
28 38
41 36
31 63
52 48
81 25
49 90
32 65
25 45
63 94
89 50
43 41
'''
obstacles = get_obstacles(obstacles)

block_cells = queensAttack(n, k, r_q, c_q, obstacles)
print(block_cells)
