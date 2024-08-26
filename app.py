import matplotlib.pyplot as plt
from datetime import datetime
import random
import time
from search.binary_search import binary_search
from sort.merge_sort import merge_sort
from sort.quick_sort import quick_sort

def execute_sort_algorithms(algorithms, iterations, array_size=10000):
    results = {}
    
    for sort_func in algorithms:
        results[sort_func.__name__] = []
    
    for i in range(iterations):
        random_numbers = [random.randint(1, array_size) for _ in range(array_size)]
        
        for sort_func in algorithms:
            start_time = time.time()
            sort_func(random_numbers.copy())
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000 # Milliseconds
            execution_time = round(execution_time, 3)
            results[sort_func.__name__].append(execution_time)
            
    return results

def plot_results(results, iterations, array_size):
    avg_exec_times = {algo: sum(exec_times) / len(exec_times) for algo, exec_times in results.items()}

    print(avg_exec_times)

    # Create bar plot
    plt.figure(figsize=(8, 6))
    plt.bar(avg_exec_times.keys(), avg_exec_times.values(), color=['blue', 'orange'])

    # Add labels and title
    plt.ylabel('Execution Time (ms)')
    plt.title(f'Comparison of Sorting Algorithms\n{iterations} Iteration(s) - Array Size: {array_size}')

    # Add exact values on top of the bars
    for i, v in enumerate(avg_exec_times.values()):
        plt.text(i, v, str(round(v, 7)), ha='center', va='bottom')

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # plt.show()
            
algorithms_to_compare = [merge_sort, quick_sort]

exec_times_result = execute_sort_algorithms(algorithms_to_compare, iterations=1, array_size=1000)

plot_results(exec_times_result, iterations=1, array_size=1000)