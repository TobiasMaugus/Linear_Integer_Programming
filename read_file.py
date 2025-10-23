from typing import List, Tuple, Optional

def read_file(file_path: str) -> Tuple[int, int, List[List[Optional[float]]], List[Tuple[int, int]]]:
    times: List[List[Optional[float]]] = []
    precedences: List[Tuple[int, int]] = []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    # --- 1. Primeira linha: número de tarefas ---
    num_tasks = int(lines[0])

    # --- 2. Linhas seguintes: tempos das tarefas ---
    idx = 1
    for _ in range(num_tasks):
        row = lines[idx].split()
        # Converter "Inf" → None, e o resto para float
        parsed_row = [None if x.lower() == "inf" else float(x) for x in row]
        times.append(parsed_row)
        idx += 1

    # Número de trabalhadores é o número de colunas
    num_workers = len(times[0])

    # --- 3. Linhas seguintes: precedências ---
    for line in lines[idx:]:
        i, j = map(int, line.split())
        if i == -1 and j == -1:
            break
        precedences.append((i, j))

    return num_tasks, num_workers, times, precedences
