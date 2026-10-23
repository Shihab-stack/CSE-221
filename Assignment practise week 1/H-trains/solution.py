import sys

def solve():
    read = sys.stdin.readline
    write = sys.stdout.write
    
    n_line = read().strip('\n')
    if not n_line:
        return
    n = int(n_line)
    
    trains = []
    for i in range(n):
        desc = read().strip()  # Keep original content
        tokens = desc.split()
        name = tokens[0]
        hour_min = tokens[-1]
        
        h, m = int(hour_min.split(':')[0]), int(hour_min.split(':')[1])
        minutes = h * 60 + m
        trains.append((name, -minutes, i, desc))
    
    # Sort by (train_name, -departure_minutes, original_index)
    trains.sort(key=lambda x: (x[0], x[1], x[2]))
    
    result = [desc for _, _, _, desc in trains]
    output = '\n'.join(result) + '\n'
    write(output)

if __name__ == '__main__':
    solve()