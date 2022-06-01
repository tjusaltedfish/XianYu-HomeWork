import time

def display(t):
    start = time.perf_counter()
    for i in range(t + 1): 
        finshed = "*" * i 
        need_do = "-" * (t - i) 
        progress = (i / t) * 100 
        durtime = time.perf_counter() - start 
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress, finshed, need_do, durtime), end="") 
        time.sleep(0.1)

def main():
    t = 60
    print("进度条如下：")
    display(t)
    
if __name__ == "__main__":
    main()