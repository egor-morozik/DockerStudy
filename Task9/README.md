Creat simple app that shows task list (use nginx, Django, postgreSQL) 
Add task with 
from todo.models import Task
Task.objects.create(title="Test Task 1")
Task.objects.create(title="Test Task 2")
exit()
And see task at http://localhost

Tasks
Test Task 1 (Created: May 11, 2025, 9:42 a.m.)
Test Task 2 (Created: May 11, 2025, 9:42 a.m.)