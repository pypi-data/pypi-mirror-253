from http_api_lambda import App
from http_api_lambda.models import Response
from pydantic import BaseModel
from datetime import datetime
from tests.data.example_api_gateway_events import build_example_event
from http import HTTPMethod


class Task(BaseModel):
    id: int | None
    name: str
    due_date: datetime


app = App()

tasks: list[Task] = []


@app.post("/tasks")
def create_task(task: Task)-> Task:
    tasks.append(task)
    return task


@app.get("/tasks/{task_id}")
def get_task(task_id: int)-> Task:
    return next((task for task in tasks if task.id == task_id), None)


def test_create_task():
    task = Task(id=None, name="Test Task", due_date=datetime.now())
    event = build_example_event(
        method=HTTPMethod.POST,
        route="/tasks",
        body=task.model_dump_json()
    )
    response: str = app.handle_request(event=event, context=None)
    assert len(response) > 0

def test_get_task():
    tasks.append(Task(id=1, name="Test Task", due_date=datetime.now()))
    event = build_example_event(
        method=HTTPMethod.GET,
        route="/tasks/1",
        body=""
    )
    response: str = app.handle_request(event=event, context=None)
    assert len(response) > 0