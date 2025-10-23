import read_file as rf

file_path = "alwabp/1_hes"
num_tasks, num_workers, times, precedences = rf.read_file(file_path)

print(f"Número de tarefas: {num_tasks}")
print(f"Número de trabalhadores: {num_workers}")
print("\nMatriz de tempos:")
for i, row in enumerate(times, start=1):
    print(f"Tarefa {i}: {row}")
print("\nPrecedências:")
for p in precedences:
    print(f"{p[0]} -> {p[1]}")