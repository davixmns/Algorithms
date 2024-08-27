import matplotlib.pyplot as plt
import random
import time
from sort.merge_sort import merge_sort
from sort.quick_sort import quick_sort
from sort.selection_sort import selection_sort
from search.binary_search import binary_search
from search.linear_search import linear_search

def measure_sort_time(algorithm, array):
    start_time = time.time()
    algorithm(array.copy())
    end_time = time.time()
    return (end_time - start_time) * 1500

def measure_search_time(algorithm, array, value):
    start_time = time.time()
    algorithm(array, value)
    end_time = time.time()
    return (end_time - start_time) * 1500


def plot_dynamic_curves(algorithms, random_array, sorted_array, step):
    plt.figure(figsize=(10, 6))
    
   # Inicializar gráficos vazios para cada algoritmo
    lines = {}
    
    search_algorithms_random = algorithms['search']['random']
    search_algorithms_sorted = algorithms['search']['sorted']
    sort_algorithms = algorithms['sort']['random']
    
    all_algorithms = search_algorithms_sorted + search_algorithms_random + sort_algorithms
    
    for algorithm in all_algorithms:
        lines[algorithm.__name__] = plt.plot([], [], label=algorithm.__name__)[0]

    plt.xlabel('Number of Items')
    plt.ylabel('Execution Time (ms)')
    plt.title('Performance Curves of Algorithms')
    plt.legend()

    times = {algorithm.__name__: [] for algorithm in all_algorithms}
    
    for i in range(1, len(random_array) + 1, step):
        random_sliced_array = random_array[:i]
        sorted_sliced_array = sorted_array[:i]
        
        # Medir tempos de execução para algoritmos de ordenação
        for algorithm in sort_algorithms:
            exec_time = measure_sort_time(algorithm, random_sliced_array)
            times[algorithm.__name__].append(exec_time)

        # Search with sorted array
        for algorithm in search_algorithms_sorted:
            exec_time = measure_search_time(algorithm, sorted_sliced_array, random.choice(sorted_sliced_array))
            times[algorithm.__name__].append(exec_time)
        
        # Search with random array    
        for algorithm in search_algorithms_random:
            exec_time = measure_search_time(algorithm, random_sliced_array, random_sliced_array[len(random_sliced_array) - 1])
            times[algorithm.__name__].append(exec_time)
            
        for algorithm in search_algorithms_random + search_algorithms_sorted + sort_algorithms:
            lines[algorithm.__name__].set_xdata(range(1, i + 1, step))
            lines[algorithm.__name__].set_ydata(times[algorithm.__name__])
        
        # Ajustar os limites do gráfico dinamicamente
        plt.xlim(0, len(random_array))
        plt.ylim(0, max(max(time_list) for time_list in times.values()))

        # Pausa para atualizar o gráfico
        plt.pause(0.00001)
    
    # Exibir o gráfico final
    plt.show()


max_items = 1000
random_numbers = [random.randint(1, max_items) for _ in range(max_items)]
sorted_numbers = [i for i in range(1, max_items + 1)]


algorithms_to_test = {
    'sort': {
        'random': [selection_sort, merge_sort, quick_sort],
    },
    'search': {
        'sorted': [binary_search],
        'random': [linear_search]
    }
}

plot_dynamic_curves(
    algorithms_to_test, 
    random_numbers, 
    sorted_numbers, 
    step=2
)
