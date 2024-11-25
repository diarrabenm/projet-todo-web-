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
        for index, todo in enumerate(todos):
            print(f"{idx + 1}. {todo['title']} - {todo['status']}")



def toggle_todo_status(index):
    try:
        todo = todos[index - 1]
        if todo["status"] == "À faire":
            todo["status"] = "Fait"
        elif todo["status"] == "Fait":
            todo["status"] = "À fair"  # Erreur volontaire ici
        print(f"Statut de '{todo['title']}' mis à jour : {todo['status']}")
    except IndexError:
        print("Indice invalide. Veuillez entrer un indice valide.")


def toggle_todo_status(index):
    try:
        todo = todos[index - 1]
        if todo["status"] == "À faire":
            todo["status"] = "Fait"
        elif todo["status"] == "Fait":
            todo["status"] = "À faire"  # Correction de l'erreur
        print(f"Statut de '{todo['title']}' mis à jour : {todo['status']}")
    except IndexError:
        print("Indice invalide. Veuillez entrer un indice valide.")
