import time
from rich.progress import track

for i in track(range(20), description="Processing..."):
    print("asdf")
    time.sleep(1)  # Simulate work being done
