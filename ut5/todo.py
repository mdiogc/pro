from __future__ import annotations

import sqlite3

DB_PATH = 'todo.db'
TASK_DONE_SYMBOL = '✔'
TASK_PENDING_SYMBOL = '⎕'


def create_db(db_path: str) -> None:
    """Crea la base de datos y la siguiente tabla:
    - tasks (id, name, done)
        └ id es la clave primaria identificador numérico
        └ name es el nombre/descripción de la tarea
        └ done indica si la tarea está hecha o no"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            done BOOLEAN NOT NULL CHECK (done IN (0, 1))
        )
    ''')
    con.commit()
    con.close()



class Task:
    """Crear atributos de clase:
    - con: para la conexión a la base de datos. Establecer consultas como "filas".
    - cur: para el cursor de manejo."""

    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, name: str, done: bool = False, id: int = -1):
        """Crea los atributos homónimos a los parámetros"""
        self.id = id
        self.name = name
        self.done = done

    def save(self):
        """Guarda esta tarea en la base de datos.
        El identificador asignado en la base de datos se debe usar para actualizar el
        atributo id de la tarea."""
        Task.cur.execute('INSERT INTO tasks (name, done) VALUES (?, ?)', (self.name, int(self.done)))
        Task.con.commit()
        self.id = Task.cur.lastrowid


    def update(self):
        """Actualiza la tarea (nombre y estado) en la base de datos"""
        Task.cur.execute('UPDATE tasks SET name = ?, done = ? WHERE id = ?', (self.name, int(self.done), self.id))
        Task.con.commit()


    def check(self):
        """Marca la tarea como completada. Haz uso también de .update()"""
        self.done = True
        self.update()

    def uncheck(self):
        """Marca la tarea como no completada. Haz uso también de .update()"""
        self.done = False
        self.update()

    def __repr__(self):
        """Muestra la tarea en formato:
        <SYMBOL> <name> (id=<id>)"""
        symbol = TASK_DONE_SYMBOL if self.done else TASK_PENDING_SYMBOL
        return f'{symbol} {self.name} (id={self.id})'

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Task:
        """Construye una nueva tarea a partir de una fila de consulta devuelta por execute()"""
        return cls(name=row['name'], done=bool(row['done']), id=row['id'])


    @classmethod
    def get(cls, task_id: int) -> Task:
        """Devuelve un objeto Task desde la consulta a la base de datos"""
        Task.cur.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        row = Task.cur.fetchone()
        if row:
            return cls.from_db_row(row)
        return None


class ToDo:
    """Crear atributos de clase:
    - con: para la conexión a la base de datos. Establecer consultas como "filas".
    - cur: para el cursor de manejo."""

    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def get_tasks(self, *, done: int = -1):
        """Devuelve todas las tareas como objetos de tipo Task consultando la BBDD.
        - Si done = 0 se devuelven las tareas pendientes.
        - Si done = 1 se devuelven las tareas completadas.
        Ojo! Esto es una función generadora."""
        query = 'SELECT * FROM tasks'
        params = ()
        if done == 0:
            query += ' WHERE done = ?'
            params = (0,)
        elif done == 1:
            query += ' WHERE done = ?'
            params = (1,)
        ToDo.cur.execute(query, params)
        rows = ToDo.cur.fetchall()
        for row in rows:
            yield Task.from_db_row(row)

    def add_task(self, name: str):
        """Añade la tarea con nombre 'name'"""
        task = Task(name)
        task.save()

    def complete_task(self, task_id: int):
        """Marca la tarea con identificador 'task_id' como completada"""
        task = Task.get(task_id)
        if task:
            task.check()

    def reopen_task(self, task_id: int):
        """Marca la tarea con identificador 'task_id' como pendiente"""
        task = Task.get(task_id)
        if task:
            task.uncheck()
