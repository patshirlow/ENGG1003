# a)
def dist_between_points(pt_a, pt_b):
    x_1, y_1 = pt_a
    x_2, y_2 = pt_b
    return ((x_2-x_1)**2 + (y_2-y_1)**2)**0.5
print(dist_between_points([0, 0], [1, 0]))

# b)
def average_dist_from_bullseye(pts):
    total = 0
    for p in pts:
        total += dist_between_points(p, [0, 0])
    return total / len(pts)
print(average_dist_from_bullseye([[1, 0], [0, 1], [-1, 0], [0, -1]]))

# c)
def compute_dart_spread(pts):
    total = 0
    count = 0
    n = len(pts)

    for i in range(n):
        for j in range(i+1, n):
            total += dist_between_points(pts[i], pts[j])
            count += 1
        return total / count
print(compute_dart_spread([[0, 0], [1, 0]]))

# d)
import math
def dart_score(pt):
    x, y = pt
    dist = math.sqrt((x*x)+(y*y))
    if dist <= 1:
        return 10
    elif dist <= 2:
        return 5
    elif dist <= 3:
        return 2
    else:
        return 0
print(dart_score([0, 1]))
print(dart_score([0.5, 0.5]))
print(dart_score([2, 0]))
print(dart_score([0.5 / math.sqrt(2), 0.5 / math.sqrt(2)]))

# e)
def game_score(pts):
    total = 0
    for p in pts:
        total += dart_score(p)
    return total
print(game_score([[0.8, 0.1], [1.1, 0.1], [-0.8, 2.5], [2.8, -2.8]]))
print(game_score([[0, 10], [-1.5, -4]]))

# f)
def play_dart_game(player_a_darts, player_b_darts):
    if len(player_a_darts) != len(player_b_darts):
        return "Invalid Game"
    total_a = 0
    total_b = 0
    for i in range(len(player_a_darts)):
        total_a += dart_score(player_a_darts[i])
        total_b += dart_score(player_b_darts[i])
    if total_a > total_b:
        return "Player A has won!"
    elif total_b > total_a:
        return "Player B has won!"
    else:
        return "We are all winners here!"
print(play_dart_game([[0, 0]], [[0, 0.5]]))
print(play_dart_game([[0, 0.5], [0, 1.5], [0, 2]], [[0, 1], [0, 2.1], [0, 3]]))




