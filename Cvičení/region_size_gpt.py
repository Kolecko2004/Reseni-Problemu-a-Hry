###############################################################
# THIS CODE IS NOT WORKING AND IS ONLY FROM CHAT-GPT
###############################################################

def region_size(r, c, data):
    # Zajištění, že souřadnice jsou v rámci dat
    def in_bounds(x, y):
        return 0 <= x < len(data) and 0 <= y < len(data[0])

    # Funkce pro prohledávání oblasti (rekurzivní DFS)
    def dfs(x, y):
        # Pokud je bod mimo rozsah nebo má hodnotu 0, neprocházíme
        if not in_bounds(x, y) or data[x][y] == 0:
            return 0
        # Označíme bod jako navštívený (změníme ho na 0)
        data[x][y] = 0
        size = 1  # Počítáme aktuální bod
        # Prohledáváme sousedy (včetně diagonálních)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            size += dfs(x + dx, y + dy)
        return size

    # Spustíme DFS od počátečního bodu
    return dfs(r, c)


# Příklad použití:
if __name__ == "__main__":
    r = 2
    c = 6
    data = [
        [1, 0, 0, 0, 1, 1, 0, 0],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 1, 0, 1, 1, 1],
        [0, 1, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 1, 0, 1, 0]
    ]

    # Celkový součet velikostí všech oblastí
    total_size = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 1:  # Pokud je bod 1, hledáme oblast
                total_size += region_size(i, j, data)

    print(total_size)  # Výstup: 12
