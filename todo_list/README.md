# **To-Do List Application**

This is a simple command-line To-Do List application that allows users to manage their tasks efficiently. Users can add, remove, edit, and mark tasks as completed, all while saving their progress in a JSON file for persistence across sessions.

---

### **Features**
1. **View tasks**: Display all tasks, including their completion status.
2. **Add task**: Add a new task to the to-do list.
3. **Remove task**: Delete a specific task by its number.
4. **Mark as completed**: Mark tasks as done.
5. **Edit task**: Update the name of an existing task.
6. **Data persistence**: Tasks are saved in a `tasks.json` file and reloaded each time the program starts.

---

### **Usage instructions**
1. Clone the repository or copy the `main.py` file to your local machine.
2. Install Python (if not already installed).
3. Run the program:
   ```bash
   python to_do_list.py
   ```
4. Interact with the menu to:
   - View tasks.
   - Add new tasks.
   - Remove or edit tasks.
   - Mark tasks as completed.
5. Exit the program, and your tasks will be automatically saved in a `tasks.json` file.

---

### **File structure**
- `main.py`: The main script for the application.
- `tasks.json`: The file where all tasks are stored. It is auto-generated if it doesn't exist.

---

### **Example JSON structure**
Below is a sample structure of the `tasks.json` file:

```json
[
    {
        "task": "Finish Python project",
        "completed": false
    },
    {
        "task": "Read a book",
        "completed": true
    },
    {
        "task": "Call Mom",
        "completed": false
    }
]
```

---

### **Requirements**
- Python 3.x
- No additional libraries are required as it uses the built-in `json` module.

---

### **Sample interaction**
```plaintext
Welcome to the To-Do List App!

Options:
1. View tasks
2. Add a task
3. Remove a task
4. Mark a task as completed
5. Edit a task
6. Exit

Choose an option: 1

Your To-Do List:
1. [✗] Finish Python project
2. [✓] Read a book
3. [✗] Call Mom

Choose an option: 2
Enter the task: Buy groceries
Task 'Buy groceries' added!

Choose an option: 6
Goodbye! Your tasks have been saved.
```

---

### **Future enhancements**
- Add due dates to tasks.
- Introduce categories for better organization.
- Include a search/filter feature to find tasks quickly.