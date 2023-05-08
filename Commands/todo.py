from events.speak import speak

todo_list = []
number_words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven":7,
    "eight": 8,
    "nine": 9,
    "ten": 10
}



def add_todo(task):
    task = task.replace("to do add", "").strip()
    with open("todo.txt", "a") as f:
        f.write(task + "\n")
    return f"Added '{task}' to your todo list."

        
def read_todo():
    with open("todo.txt", "r") as f:
        tasks = f.readlines()
        if not tasks:
            return "Your todo list is empty."
        else:
            task_list = "\n".join([f"{i+1}. {task.strip()}" for i, task in enumerate(tasks)])
            return f"Here are your tasks:\n{task_list}"
        
def remove_todo(task_num):
    try:
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        task_num -= 1  # adjust task_num to account for 0-based indexing
        if task_num < 0 or task_num >= len(tasks):
            return "Invalid task number. Please try again."
        task = tasks.pop(task_num)
        with open("todo.txt", "w") as f:
            f.writelines(tasks)
        return f"Task '{task.strip()}' removed from your todo list."
    except FileNotFoundError:
        return "Todo list not found. Please create one first." 
