import multiprocessing

def worker_function(task_id):
    print(f"Task {task_id} started")
    # Simulando algum processamento da tarefa
    result = task_id * 2
    print(f"Task {task_id} completed with result: {result}")

if __name__ == "__main__":
    num_tasks = 10000000
    process_number = multiprocessing.cpu_count()  
    with multiprocessing.Pool(processes=process_number) as pool:
        pool.map(worker_function, range(num_tasks))

    print("All tasks completed")