## [Throttle](https://www.greatfrontend.com/interviews/study/gfe75/questions/javascript/throttle)

Three types of throttle
1. Leading throttle (ring immediately)
    👉 Bell rings the moment you press first time
    👉 Then ignores presses for 5 seconds
    👉 After 5s, next press rings again

    or (speedometer update)

    When scrolling:

    You want immediate UI response.
    Later positions aren’t critical. -> Leading.

2. Trailing throttle (ring after burst)
    👉 Bell waits
    👉 Keeps resetting timer if pressed again
    👉 Rings once after you stop pressing

    autosave  - Typing in Google Docs:
        You don’t want save every keystroke.
        You want save after user pauses.

    User drags slider quickly:
    You only care final value. -> Trailing.

3. Leading + trailing (both)
    👉 Ring immediately
    👉 Also ring once more after spam ends

