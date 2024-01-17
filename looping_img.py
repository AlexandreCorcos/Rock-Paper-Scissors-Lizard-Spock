import time
import sys


def show_loading_symbols():
    symbols = ["👊", "✋", "✌️", "🤏", "🖖"]

    for _ in range(10):
        for symbol in symbols:
            sys.stdout.write('\r' + symbol)
            sys.stdout.flush()
            time.sleep(0.1)


# Your code before the 10 seconds wait
# ...
print("test")

# Show loading symbols while waiting
show_loading_symbols()

# Continue with your code after the 10 seconds wait
# ...
