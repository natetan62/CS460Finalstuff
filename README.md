# The Torchbearer

**Student Name:** Nathan Tan
**Student ID:** 827824355
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
 -A single shortest path is not enough because it findds the cheapest path to the node indivudally but not the overall cost.
 -We need the cheapest cost overall 

- **What decision remains after all inter-location costs are known:**
- the decision that remains even after the costs are known is the order of chambers to visit with the relics. Each different order of vist would lead to different fuel costs.

- **Why this requires a search over orders (one sentence):**
  -This requeires serch over orders because there isnt a rule or order that can find the optimal path right away. we need to find the globally chepaest ordering after exploring and pruning.


---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
|  spawn | Like every game spawn is the start of every game, where you start or go back to need the cheapest from here. |
|The relic chambers | Going from relic to relic we need the chepaest distance and then to the exit. |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| dictionary, dict |(dict[node, node])] |
| What the keys represent | The group of source and desntations of the path from spawn to a relic or relic to another or to the exit|
| What the values represent | The values represent the lowest cost of fule used from a source to the destiation  |
| Lookup time complexity | o(1)|
| Why O(1) lookup is possible |This is possible because the dictionary is a hashmap no need to traverse it |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** We need to run Dijkstra once for every place we can leave from. 1 run from spawn and then k amount of runs after from each relic so k + 1
- **Cost per run:** O(elogn). e is the # of edges and n is # of nodes with a binary min heap
- **Total complexity:** o(k*elogn)
- **Justification (one line):** K+1 dikjkstra runs costs O(elogn) and then we multiply the two we get (k+1) * (elogn) so we get O(k*elogn).

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  -Distance[v] would represent the minimum fuel cost from the sources to whatever node v is. 
  -This should be the optimal. 

- **For nodes not yet finalized (not in S):**
  -distance[u] is theshortest ditance djisktra has discovred.
  -It takes the shortest discovered so far but it can be replace by a shorter one.
### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  -At the very beggining of the itertation, distance is 0 so it is the shortest path and there is no path discovered yet
  -So the invariant holds because the initatizliation holds.
- **Maintenance : why finalizing the min-dist node is always correct:**
  -At the beginning of the iterations this would hold because the node is not set, it is the smallest current u so it should be the same as the optimal. 
  -So therefore at each iterations the distance we see is already optimal and adding u to the path would maintain the invariant for the rest of the nodes.

- **Termination : what the invariant guarantees when the algorithm ends:**
  -After ittering through all the nodes, every node is either added to the optimal shortest path distance from spawn or the node would be unreachable the dictionary.
### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

  -This matters for the route planner because it needs to use the distance to see the actual shortest path to see how much fuel is used.
  -It has to be the total route that is the cheapest and has enough fuel to make it through.

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** The failure mode for greedy would be to just moving to the closet exit and not really considering the exit. Cheap from one exit does not mean it is cheaper overall to the exit you have to look at the whole thing.
- **Counter-example setup:** From the illustration exampe from the sepcd we have the relic bcd. from s spawn to b is 1, to c is 2, to d is 2. from b to d is 1, from b to t is 1, from b to c is 100.  From c to b is 1, c to T is 1. From d to b is 1, d to c is1, d to t is 100.
- **What greedy picks:**  Greedy would pick to b frist becaues its cheapest then d then c and then T witha  total cost 103.
- **What optimal picks:** Optimal would pick b then d then c and then t because going from c t to 1 would only cost 1 instead of going the otehr way.
- **Why greedy loses:** Greedy loses because it just goes to the nearest relic needed to be collected. It chooses D before going to c because it did not know that picking C last would make it impossbily to dodge the 100 choice. The optimal unlike creedy considers everything before picking

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

-The algorithm must eplore the order of every relic and going through the dungeon and return with the lowest total fuel cost to the exit.
---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | currentLocation| node| The location the torchbearer is at the in the search|
| Relics already collected |relicsreamning | set|The relics still yet not visited or not collected |
| Fuel cost so far |fuelUsed |float |The amount of fuel used from spawn to the current location. |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|

| Data structure chosen |set |
| Operation: check if relic already collected | Time complexity: o(1) hash |
| Operation: mark a relic as collected | Time complexity: O(1) just removing the relic .remove to the set|
| Operation: unmark a relic (backtrack) | Time complexity: O(1) adding a relic back .add to the set|
| Why this structure fits |The operations just search the set but iterating to find the reamining relics would be O(k). The set would fit because it would tell us whats left to find without storing a different list to find what we still have to collect|

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:**  The worst case number of orders considered would be o(k!)
- **Why:** The worst case search would be k recursove choices at least level so the wrost case before the pruning would be o(k!)

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._

