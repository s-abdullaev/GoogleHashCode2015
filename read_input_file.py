from itertools import izip


def get_line(line):
    return map(lambda s: int(s), line.split(' '))


def load_configuration(config_file):
    with open(config_file, 'r') as f:
        config = {}

        R, C, A = get_line(f.readline())
        config['R'] = R
        config['C'] = C
        config['A'] = A

        L, V, B, T = get_line(f.next())
        config['L'] = L
        config['V'] = V
        config['B'] = B
        config['T'] = T

        start_cell = tuple(get_line(f.next()))
        config['start_cell'] = start_cell

        targets = []
        for l in range(L):
            targets.append(tuple(get_line(f.next())))
        config['targets'] = targets

        A_MAP = []
        for a in range(A):
            a_map = []
            for r in range(R):
                a_map.append(list(izip(*[iter(get_line(f.next()))]*2)))
            A_MAP.append(a_map)
        config['a_map'] = A_MAP

        return config
