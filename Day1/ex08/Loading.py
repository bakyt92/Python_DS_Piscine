import os 
import time 

def time_format(sec):
    min, s = divmod(sec, 60)
    return f"{int(min):02d}:{int(s):02d}"

def ft_tqdm(lst: range) -> None:
    total_elem = len(lst)
    start = time.time()
    try: 
        size = os.get_terminal_size().columns
    except OSError:
        size = 20
    progress_bar_w = size - 10
    for x, name in enumerate(lst, start=1):
        
        time_used = time.time() - start
        formatted_time_used = time_format(time_used)
        speed = x / time_used if time_used > 0 else 0
        to_finish = (total_elem - x) / speed
        formatted_to_finish = time_format(to_finish)
        print(f"\r{formatted_time_used} {formatted_to_finish}", end="")
        yield name

def main():
    for x in ft_tqdm(range(0, 5000000)):
        pass

if __name__ == "__main__":
    main()
