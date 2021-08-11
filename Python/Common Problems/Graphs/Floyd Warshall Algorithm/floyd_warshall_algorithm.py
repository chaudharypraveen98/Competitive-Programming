def floyd_warshal(v,e):
    distance_arr = [[None]*v for _ in range(v)]
    inf = float("inf")
    for i in range(v):
        for j in range(v):
            if i==j:
                distance_arr[i][j] = 0
            else:
                distance_arr[i][j] = inf

    for _ in range(e):
        start, end, weight = map(int, input().split())
        distance_arr[start][end]= weight 

    for k in range(v):
        for i in range(v):
            for j in range(v):
                if distance_arr[i][k]+distance_arr[k][j]< distance_arr[i][j]:
                    distance_arr[i][j]==distance_arr[i][k]+distance_arr[k][j]

    for row in distance_arr:
        print(f'{" ".join(row)}\n')
