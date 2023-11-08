import multiprocessing

def write_numbers(start, end, filename):
    with open(filename, 'w') as file:
        for num in range(start, end + 1):
            file.write(f"{num}\n")

def main():
    filename = 'passwords.txt'
    num_processes = 10
    num_passwords = 100000
    chunk_size = num_passwords // num_processes
    processes = []

    for i in range(num_processes):
        start = i * chunk_size + 1
        end = start + chunk_size - 1 if i < num_processes - 1 else num_passwords
        process = multiprocessing.Process(target=write_numbers, args=(start, end, filename))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == '__main__':
    main()
