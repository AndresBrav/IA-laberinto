def solve_maze(maze):
    # Obtiene las dimensiones del laberinto
    rows = len(maze)
    cols = len(maze[0])
    
    # Define una función auxiliar para realizar la búsqueda DFS
    def dfs(row, col):
        # Verifica si se alcanzó la meta (posición de salida)
        if maze[row][col] == 'G':
            return True
        
        # Verifica si la posición actual es válida y no ha sido visitada
        if maze[row][col] == ' ':
            # Marca la posición actual como visitada
            maze[row][col] = '.'
            
            # Verifica recursivamente las posiciones vecinas
            if (row > 0 and dfs(row - 1, col)) or \
               (row < rows - 1 and dfs(row + 1, col)) or \
               (col > 0 and dfs(row, col - 1)) or \
               (col < cols - 1 and dfs(row, col + 1)):
                return True
            
            # Si no se encontró una solución, desmarca la posición actual
            maze[row][col] = ' '
        
        return False
    
    # Busca la posición de inicio
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start_row, start_col = i, j
                break
    
    # Resuelve el laberinto
    if dfs(start_row, start_col):
        print("Laberinto resuelto:")
        for row in maze:
            print(''.join(row))
    else:
        print("No se encontró una solución.")


# Ejemplo de laberinto representado como matriz
maze = [
    ['S', '#', ' ', ' ', ' ', ' ', ' '],
    ['#', '#', ' ', '#', '#', '#', ' '],
    ['#', ' ', ' ', ' ', ' ', '#', ' '],
    ['#', '#', '#', '#', ' ', '#', 'G'],
    [' ', ' ', ' ', '#', ' ', ' ', ' '],
    [' ', '#', ' ', '#', '#', '#', '#'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

# Resuelve el laberinto
solve_maze(maze)
