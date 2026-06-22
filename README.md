# Django To-Do List

A to-do list web app built with Django, where every task has a priority coefficient assigned at creation — so the list always shows what matters most, first.

## What this does

Each user has their own private task list, tasks carry a priority value from 0–10, and the list automatically sorts by priority (highest first), then by creation date. You can also search tasks by title and reorder them directly from the list view.

## Features

- **User accounts** : register, log in, log out; each user only sees their own tasks
- **Priority-based sorting** : tasks are ordered by priority (high to low), then by creation date, enforced at the model level (`Meta.ordering`)
- **Task CRUD** : create, view, update, and delete tasks, each scoped to the logged-in user
- **Inline priority updates** : change a task's priority directly from the list view without opening the edit page
- **Search** : filter tasks by title from the list view
- **Drag-and-drop reordering** : a dedicated reorder endpoint for adjusting task order interactively
- **Admin panel** : tasks are registered with Django admin for quick inspection/management

## How priority sorting works

Each `Task` has a `priority` field (integer, 0–10, validated with `MinValueValidator`/`MaxValueValidator`). The model's `Meta.ordering = ['-priority', 'created']` means tasks are sorted by priority descending, with ties broken by creation time — so this ordering applies consistently anywhere the queryset is used, not just in one view.

## Tech Stack

- **Backend**: Django (class-based views: `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`, `FormView`)
- **Auth**: Django's built-in `LoginView`, `UserCreationForm`, `LoginRequiredMixin`
- **Database**: Django ORM (works with SQLite by default, or any Django-supported DB)

## Project Structure

| File | What it is |
|---|---|
| `models.py` | `Task` model — title, description, completion status, priority, user ownership |
| `views.py` | All views: task list/detail/create/update/delete, login, registration, reordering |
| `forms.py` | `TaskForm` for create/update, `PositionForm` for drag-and-drop reorder submissions |
| `urls.py` | URL routes for all task and auth views |
| `admin.py` | Registers `Task` with the Django admin site |
| `tests.py` | Test scaffold (add test cases here) |

## Author

Kritish Sardar — B.Sc. Statistics (Honours), University of Delhi
