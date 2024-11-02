from collections import deque

def min_moves_to_destination(grid, M, N, src, dest, move_rule):
    dx, dy = move_rule
    # Directions based on the move rule (dx, dy)
    directions = [
        (dx, dy),       # Forward
        (dy, -dx),      # Right (90 degrees clockwise)
        (-dy, dx),      # Left (90 degrees counterclockwise)
        (-dx, -dy)      # Backward (180 degrees)
    ]

    # Breadth-First Search (BFS) setup
    queue = deque([(src[0], src[1], 0)])  # (row, col, steps)
    visited = set()
    visited.add((src[0], src[1]))

    # BFS Loop
    while queue:
        x, y, steps = queue.popleft()

        # Check if we’ve reached the destination
        if (x, y) == (dest[0], dest[1]):
            return steps

        # Explore all four possible moves
        for direction in directions:
            new_x, new_y = x + direction[0], y + direction[1]

            # Check boundaries and accessibility of the new cell
            if 0 <= new_x < M and 0 <= new_y < N and (new_x, new_y) not in visited and grid[new_x][new_y] == 0:
                queue.append((new_x, new_y, steps + 1))
                visited.add((new_x, new_y))

    # If destination is unreachable
    return -1

def main():
    # Input format explanation for the user
    print("Input format example:")
    print("6 6")
    print("0 1 0 0 0 0")
    print("0 0 0 0 0 1")
    print("0 1 0 0 0 0")
    print("1 1 0 0 0 1")
    print("0 0 0 0 0 0")
    print("1 1 0 0 1 0")
    print("1 0")
    print("5 3")
    print("1 2")
    print("\nExplanation:")
    print("6 6: Grid dimensions (6x6)")
    print("Next 6 lines: Grid cells (0 = open, 1 = blocked)")
    print("1 0: Source cell coordinates (row, col)")
    print("5 3: Destination cell coordinates (row, col)")
    print("1 2: Move rule (dx, dy) for direction vectors.\n")

    # Taking user input
    M, N = map(int, input("Enter M and N (grid dimensions): ").split())
    print("Enter the grid rows with 0 (open) and 1 (blocked) cells:")
    grid = [list(map(int, input().split())) for _ in range(M)]
    src = tuple(map(int, input("Enter source coordinates (row and column): ").split()))
    dest = tuple(map(int, input("Enter destination coordinates (row and column): ").split()))
    move_rule = tuple(map(int, input("Enter move rule as two integers: ").split()))

    # Calculate and display result
    result = min_moves_to_destination(grid, M, N, src, dest, move_rule)
    print("\nMinimum moves required to reach the destination:", result)

# Run the main function
if __name__ == "__main__":
    main()
