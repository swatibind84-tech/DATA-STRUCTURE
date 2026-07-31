import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class PriorityQueue:
    def __init__(self, max_capacity):
        self.queue = []
        self.max_capacity = max_capacity

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.max_capacity

    def enqueue(self, item, priority):
        if self.is_full():
            print(Fore.RED + "Priority Queue is full. Cannot enqueue.")
            return

        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])

        print(Fore.GREEN + f"Enqueued: {item} with priority {priority}")
        self.loading_animation()

    def dequeue(self):
        if self.is_empty():
            print(Fore.RED + "Priority Queue is empty. Cannot dequeue.")
            return

        item = self.queue.pop(0)[0]
        print(Fore.GREEN + f"Dequeued: {item}")
        self.loading_animation()
        return item

    def traverse(self):
        if self.is_empty():
            print(Fore.YELLOW + "Priority Queue is empty.")
        else:
            print(Fore.CYAN + "\nPriority Queue contains:")
            for item, priority in self.queue:
                print(f"Item: {item}, Priority: {priority}")

    def show_ascending(self):
        if self.is_empty():
            print(Fore.YELLOW + "Priority Queue is empty.")
        else:
            print(Fore.CYAN + "\nAscending Order:")
            for item, priority in sorted(self.queue, key=lambda x: x[1]):
                print(f"Item: {item}, Priority: {priority}")

    def show_descending(self):
        if self.is_empty():
            print(Fore.YELLOW + "Priority Queue is empty.")
        else:
            print(Fore.CYAN + "\nDescending Order:")
            for item, priority in sorted(self.queue, key=lambda x: x[1], reverse=True):
                print(f"Item: {item}, Priority: {priority}")

    def loading_animation(self):
        for _ in range(2):
            for ch in "-\\|/":
                print(Fore.BLUE + f"\rLoading {ch}", end="", flush=True)
                time.sleep(0.1)
        print("\rDone!      ")


def Main():
    while True:
        try:
            max_capacity = int(input("Enter the maximum capacity of the Priority Queue: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    pq = PriorityQueue(max_capacity)

    while True:
        print("\n===== Priority Queue Menu =====")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Traverse")
        print("4. Check if Empty")
        print("5. Check if Full")
        print("6. Show Ascending Order")
        print("7. Show Descending Order")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 8.")
            continue

        if choice == 1:
            item = input("Enter item: ")
            try:
                priority = int(input("Enter priority: "))
                pq.enqueue(item, priority)
            except ValueError:
                print("Priority must be an integer.")

        elif choice == 2:
            pq.dequeue()

        elif choice == 3:
            pq.traverse()

        elif choice == 4:
            if pq.is_empty():
                print("Priority Queue is Empty.")
            else:
                print("Priority Queue is Not Empty.")

        elif choice == 5:
            if pq.is_full():
                print("Priority Queue is Full.")
            else:
                print("Priority Queue is Not Full.")

        elif choice == 6:
            pq.show_ascending()

        elif choice == 7:
            pq.show_descending()

        elif choice == 8:
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    Main()
