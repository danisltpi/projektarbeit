## Todo-App

Als Letztes möchten wir noch Code-Generierung
bzgl. Web-Entwicklung ausprobieren, bei dem die Aufgabenstellung ist,
eine einfache Todo-App zu entwickeln,
in der man Aufgaben erstellen kann,
diese bearbeiten, löschen und abhaken kann.
Damit es einfacher ist, um die App zu testen,
sollte die App mithilfe von HTML, CSS und JavaScript
erstellt werden ohne jegliche Frameworks.

**Prompt:**

Create a todo-app running in the browser, where it’s possible to create entries,
to edit, to delete and to complete them.

**Code Llama:**

_Here is an example of a simple todo-app that runs in the browser:_

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Todo App</title>
    <style>
      body {
        font-family: Arial, sans-serif;
      }

      .todo-list {
        list-style: none;
        padding: 0;
        margin: 0;
      }

      .todo-list li {
        padding: 10px;
        margin-bottom: 10px;
        background-color: #f4f4f4;
        border: 1px solid #ddd;
      }

      .todo-list li:last-child {
        border-bottom: none;
      }

      .todo-list li.completed {
        text-decoration: line-through;
      }

      .todo-list li.editing {
        background-color: #ffc;
      }

      .todo-list li.editing input {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border: none;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
      }

      .todo-list li.editing button {
        background-color: #4caf50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
      }

      .todo-list li.editing button:hover {
        background-color: #45a049;
      }
    </style>
  </head>
  <body>
    <h1>Todo App</h1>
    <ul class="todo-list">
      <li>
        <input type="checkbox" id="todo1" />
        <label for="todo1">Todo 1</label>
        <button class="edit">Edit</button>
        <button class="delete">Delete</button>
      </li>
      <li>
        <input type="checkbox" id="todo2" />
        <label for="todo2">Todo 2</label>
        <button class="edit">Edit</button>
        <button class="delete">Delete</button>
      </li>
      <li>
        <input type="checkbox" id="todo3" />
        <label for="todo3">Todo 3</label>
        <button class="edit">Edit</button>
        <button class="delete">Delete</button>
      </li>
    </ul>
    <script>
      const todoList = document.querySelector(".todo-list");
      const todoInput = document.querySelector(".todo-input");
      const todoButton = document.querySelector(".todo-button");

      todoButton.addEventListener("click", addTodo);

      function addTodo() {
        const todo = todoInput.value;
        if (todo.length > 0) {
          const todoItem = document.createElement("li");
          todoItem.innerHTML = `
					<input type="checkbox" id="todo${todoList.children.length + 1}" />
					<label for="todo${todoList.children.length + 1}">${todo}</label>
					<button class="edit">Edit</button>
					<button class="delete">Delete</button>
				`;
          todoList.appendChild(todoItem);
          todoInput.value = "";
        }
      }

      todoList.addEventListener("click", function (event) {
        if (event.target.tagName === "INPUT") {
          const todoItem = event.target.parentNode;
          todoItem.classList.toggle("completed");
        } else if (event.target.tagName === "BUTTON") {
          const todoItem = event.target.parentNode;
          if (event.target.classList.contains("edit")) {
            todoItem.classList.add("editing");
          } else if (event.target.classList.contains("delete")) {
            todoItem.remove();
          }
        }
      });
    </script>
  </body>
</html>
```

_This code creates a simple todo app that allows you to add, edit, and delete todo items. When you click on a todo item, it will be marked as completed. When you click on the “Edit” button, the todo item will be editable. When you click on the “Delete” button, the todo item will be removed.
You can add more functionality to this app by adding more buttons and event listeners. For example, you could add a “Clear completed” button that removes all completed todo items, or a “Sort by date” button that sorts the todo items by date.
I hope this helps! Let me know if you have any questions._

Leider funktioniert der generierte Code von Code Llama wieder nicht ganz wie gewollt.

Die App bietet nicht die Möglichkeit neue Einträge hinzuzufügen und auch die
Buttons funktionieren nicht, da beim Klicken nichts geschieht.

Wir möchten dass dies korrigiert wird.

![Todo-App von Code Llama](assets/img/code-llama-todo.png)

**Prompt:**

This app doesn’t work because the buttons don’t work when clicking them. Additionally I don’t see the possibility to add new entries to my todo list

**Code Llama:**
_I apologize for the inconvenience. The issue with the buttons not working is due to a mistake in the code. I’ve updated the code to fix the issue.
Regarding adding new entries to the todo list, you can do so by clicking the “Add” button at the bottom of the page. This will open a form where you can enter the details of the new todo item, such as the title, description, and due date. Once you’ve filled out the form, click the “Add” button to save the new todo item to the list.
Here’s the updated code:_

_[…]_

Ein sehr ernüchterndes Ergebnis. Der neu generierte Code ist nahezu Deckungsgleich zum vorherigen Code mit
der Neuerung eines “Add”-Buttons, welcher, wie üblich, nicht funktioniert.

Dieselbe Aufgabenstellung wird wieder einmal ChatGPT gestellt.

**ChatGPT:**

_Certainly! Below is a simple example of a todo-app using HTML, CSS, and JavaScript. For simplicity, I’m not using any external frameworks, but you can easily extend this example with a framework like React, Vue.js, Angular, etc., for a more scalable and maintainable solution._

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Todo App</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 20px;
      }

      #todoList {
        max-width: 400px;
        margin: auto;
      }

      .task {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 8px;
        border-bottom: 1px solid #ccc;
        margin-bottom: 5px;
      }

      .task input[type="text"] {
        flex-grow: 1;
        margin-right: 10px;
      }

      .task button {
        background-color: #4caf50;
        color: white;
        border: none;
        padding: 5px 10px;
        cursor: pointer;
      }

      .task button.delete {
        background-color: #f44336;
      }
    </style>
  </head>
  <body>
    <div id="todoList">
      <h2>Todo List</h2>
      <div id="tasks"></div>
      <div>
        <input type="text" id="newTask" placeholder="New task" />
        <button onclick="addTask()">Add</button>
      </div>
    </div>

    <script>
      function addTask() {
        const taskText = document.getElementById("newTask").value.trim();
        if (taskText === "") return;

        const taskList = document.getElementById("tasks");

        const taskDiv = document.createElement("div");
        taskDiv.className = "task";

        const taskInput = document.createElement("input");
        taskInput.type = "text";
        taskInput.value = taskText;
        taskInput.disabled = true;

        const editButton = document.createElement("button");
        editButton.innerText = "Edit";
        editButton.onclick = function () {
          taskInput.disabled = !taskInput.disabled;
          taskInput.focus();
        };

        const deleteButton = document.createElement("button");
        deleteButton.innerText = "Delete";
        deleteButton.className = "delete";
        deleteButton.onclick = function () {
          taskDiv.remove();
        };

        taskDiv.appendChild(taskInput);
        taskDiv.appendChild(editButton);
        taskDiv.appendChild(deleteButton);
        taskList.appendChild(taskDiv);

        document.getElementById("newTask").value = "";
      }
    </script>
  </body>
</html>
```

_This example provides a simple interface with the ability to add, edit, and delete tasks. You can further enhance it by adding functionality to mark tasks as completed and by storing tasks in local storage for persistence between browser sessions. Additionally, integrating a front-end framework would improve the maintainability and scalability of the application._

ChatGPT hat eine vollfunktionsfähige Todo-App generiert, wie
man sie auch erwartet. Leider wurde aber die Funktion, erledigte Todo-Einträge
abzuhaken weggelassen. Von dem ausgenommen ist das Ergebnis hier
äußerst zufriedenstellend.

![Todo-App von ChatGPT](assets/img/chatgpt-todo.png)
