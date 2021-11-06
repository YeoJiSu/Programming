def start():
    A, B = input().split()
    A = int(A)
    B = int(B)
    timer = (A * 60) + B - 45

    if timer < 0:
        timer = 24 * 60 - (-timer) 

    format_timer_h = str(timer/60).split('.')[0]
    format_time_m = timer - int(format_timer_h) * 60

    
    print("{} {}".format(format_timer_h, format_time_m))
    
    # print("format_timer_h : {}".format(format_timer_h))
    # print("format_time_m : {}".format(format_time_m))
    
    

if __name__ == "__main__":
    start()

#  (0 ≤ H ≤ 23, 0 ≤ M ≤ 59)