def calculate_cumulative_oil_production(nx, ny, nz, N, Boi, Bob, ce, co, Pb, Pi_values, Pnow_values):
    total_np = 0
    block_np_list = []

    for k in range(1, nz + 1):
        Pi = Pi_values[k - 1]
        for j in range(1, ny + 1):
            for i in range(1, nx + 1):
                block_n_order = (nx * ny * (k - 1)) + (nx * (j - 1)) + i
                Pnow = Pnow_values[block_n_order - 1]
                bo = Bob * (1 - co * (Pnow - Pb))
                block_np = (N * Boi * ce * (Pi - Pnow)) / bo
                total_np += block_np
                block_np_list.append(block_np)

    return total_np, block_np_list
