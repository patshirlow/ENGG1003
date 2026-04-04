import utils
a = utils.percent_change(1, 2)
b = utils.percent_change(-87, 72)
c = utils.percent_change(0, 27)

for value in [a, b, c]:
    print(f"Percent Change: {value:.2f}")