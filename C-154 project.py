import matplotlib.pyplot as plt

data = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 6, 5, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 10, 6, 5, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 10, 10, 6, 5, 10],
        [10, 10, 10, 10, 10, 10, 10, 9, 9, 1, 9, 10, 6, 5, 10],
        [10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 10, 6, 5, 10],
        [10, 10, 10, 10, 10, 9, 9, 9, 1, 9, 9, 10, 6, 5, 10],
        [10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 10, 6, 5, 10],
        [10, 10, 10, 9, 9, 9, 1, 9, 9, 9, 9, 10, 6, 5, 10],
        [10, 10, 9, 9, 1, 9, 9, 9, 9, 9, 10, 6, 5, 10, 10],
        [10, 6, 10, 10, 9, 9, 9, 9, 10, 10, 6 , 5, 5, 10, 10],
        [10, 5, 6, 10, 10, 10, 10, 10, 10, 6, 5, 5, 10, 10, 10],
        [10, 10, 5, 6, 6, 6, 6, 6, 6, 5, 5, 10, 10, 10, 10],
        [10, 10, 10, 10, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]


plt.imshow(data, cmap="cool")
plt.show()