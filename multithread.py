import threading

def reverse(input_str):
    reversed_str = input_str[::-1]
    print("Reversed string:", reversed_str)
input_str = input("Enter a string to reverse : ")
thread = threading.Thread(target=reverse, args=(input_str,))
thread.start()
thread.join()
