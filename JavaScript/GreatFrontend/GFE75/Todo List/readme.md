## [Todo List](https://www.greatfrontend.com/interviews/study/gfe75/questions/user-interface/todo-list)

### Follow up questions
1) Mark todo as completed ✅

They may ask:

"Can you add a checkbox to mark items complete?"

Then each item becomes:

{
  key,
  value,
  completed: false
}

and toggle with:

completed: !item.completed

This tests:

✅ immutable updates
✅ array mapping

2) Edit existing todo ✏️

Question:

"Can user edit a task after adding?"

This tests:

✅ conditional rendering
✅ local edit state
✅ controlled inputs inside list

3) Add Enter key support ⌨️

Very common:

"Submit when user presses Enter"

onKeyDown={(e) => {
  if (e.key === "Enter") addItem();
}}

Tests keyboard UX awareness.

4) Prevent duplicate todos 🚫

Question:

"Should duplicate tasks be allowed?"

Example:

items.some(item => item.value === value.trim())

Tests validation thinking.

5) Persist after refresh 💾

Question:

"How will you save todos after page reload?"

Expected:

Use localStorage.

Possible answer:

useEffect(() => {
  localStorage.setItem("todos", JSON.stringify(items));
}, [items]);

Tests side effects.

6) Delete all completed todos 🗑️

Question:

"Add clear completed"

Tests filter logic.

7) Performance follow-up ⚡

If list grows large:

"How to optimize?"

Expected concepts:

✅ React.memo
✅ split item component
✅ avoid unnecessary rerenders

8) Accessibility question ♿

Strong interviewers ask:

"Any accessibility improvement?"

Expected:

✅ label for input
✅ button accessible text
✅ keyboard support

9) Why use functional update here?

They may ask:

"Why better to write setItems(prev => ...)?"

Expected answer:

Because state updates are async and previous state may be stale.

10) Why not use index as key?

Very common React interview question:

"Why not key={index}?"

Expected answer:

Because delete/reorder breaks identity.