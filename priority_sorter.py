from datetime import datetime

print("📋 Priority Sorter CLI")

tasks = []
today = datetime.today().date()

while True:
    task = input("📝 Enter task (or type 'done' to finish): ").strip()
    if task.lower() == "done":
        break

    due_date_input = input("📅 Enter due date (YYYY-MM-DD): ").strip()
    try:
        due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
        days_left = (due_date - today).days

        tasks.append({"task": task, "due_date": due_date, "days_left": days_left})
    except ValueError:
        print("❗ Invalid date format. Please use YYYY-MM-DD.")

# Sort tasks by days left
tasks.sort(key=lambda x: x["days_left"])

print("\n🧠 Sorted Task List:\n" + "-" * 45)

for i, t in enumerate(tasks, 1):
    if t["days_left"] < 0:
        status = "❗ OVERDUE"
    elif t["days_left"] == 0:
        status = "🔥 DUE TODAY"
    else:
        status = f"⏳ In {t['days_left']} day(s)"

    formatted_due = t["due_date"].strftime("%a %b %d")  # e.g., Mon Apr 22
    print(f"{i}. {t['task']:<30} | {formatted_due} | {status}")
