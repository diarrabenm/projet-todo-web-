code python
todos = []

def create_todo(title):
    todo = {"title": title, "status": "À faire"}
    todos.append(todo)
    print(f"Todo '{title}' créé avec succès.")

def list_todos():
    if not todos:
        print("Aucun todo disponible.")
    else:
        print("Liste des todos :")
        for idx, todo in enumerate(todos):
            print(f"{idx + 1}. {todo['title']} - {todo['status']}")