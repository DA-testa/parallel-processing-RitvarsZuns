# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)] # (completion_time, index)
    heapq.heapify(threads)

    for job_time in data:
        completion_time, thread_idx = heapq.heappop(threads)
        output.append((thread_idx, completion_time))
        heapq.heappush(threads, (completion_time + job_time, thread_idx))
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)

    for thread_idx, start_time in result:
        print(thread_idx, start_time)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
