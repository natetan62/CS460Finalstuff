# Development Log – The Torchbearer

**Student Name:** Nathan Tan    
**Student ID:** 827824355

---

## Entry 1 – [5/6/2026]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

 After initially reading it I think obviously implementing a dijkstras to solve a directed graph problem ending at a specific point. Using a distance table and backtracking with what we learned the most opimtal so far and the lower bound estimating the lowest possible cost. I think the hardest part will be to workaround the backtracking and making sure its inputing the right things and additionally dealing with the many edge cases this specific assignment will produce.
---

## Entry 2 – [5/7/2026]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

One assumption I had was putting the exit node in the select sources but the person with the tourch wouldnt depart or leave from there so that was not an option.
---

## Entry 3 – [5/13]: [Trying to figure out search and pruning]

-This has genuinely made my head hurt and taken a good chunk of time. I think I figured out the base case, but implementing the lower bound is kind of tricky while trying to maange the recursive cases and back tracking.

---

## Entry 4 – [5/14]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

If i had more time I would try to clean up or make the lower bound better. It only goes to the next cheapest relic. I would add a tighter bound that can estimate teh cost of all remaining relics and the exit. The design I had worked relatively well I think the flat dictionry was a good use for this problem but im sure there is a better design.
---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis |1-1.5 hrs reading and then deciding the plan |
| Part 2: Precomputation Design | 1 hr |
| Part 3: Algorithm Correctness | 1 hr|
| Part 4: Search Design | 45 min ish |
| Part 5: State and Search Space | 45 min ish|
| Part 6: Pruning |2hr |
| Part 7: Implementation |8 ish hrs |
| README and DEVLOG writing |2 hrs |
| **Total** | 15ish hours across a week so maybe more idk these are rough estimate because I did a little bit each day|
