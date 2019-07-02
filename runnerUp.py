def runnerUp(arr):
    new_arr=sorted(set(arr), reverse=True)
    runner_up=new_arr[1]
    return runner_up

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(runnerUp(arr))