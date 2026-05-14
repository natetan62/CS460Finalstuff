# The Torchbearer

**Student Name:** Nathan Tan
**Student ID:** 827824355
**Course:** CS 460 – Algorithms | Spring 2026


---

## Part 1: Problem Analysis

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



| Source Node Type | Why it is a source |
|---|---|
|  spawn | Like every game spawn is the start of every game, where you start or go back to need the cheapest from here. |
|The relic chambers | Going from relic to relic we need the chepaest distance and then to the exit. |

### Part 2b: Distance Storage


| Property | Your answer |
|---|---|
| Data structure |dict[tuple[node, node]] |
| What the keys represent | The group of source and desntations of the path from spawn to a relic or relic to another or to the exit|
| What the values represent | The values represent the lowest cost of fule used from a source to the destiation  |
| Lookup time complexity | o(1)|
| Why O(1) lookup is possible |This is possible because the dictionary is a hashmap no need to traverse it |

### Part 2c: Precomputation Complexity


- **Number of Dijkstra runs:** We need to run Dijkstra once for every place we can leave from. 1 run from spawn and then k amount of runs after from each relic so k + 1
- **Cost per run:** O(elogn). e is the # of edges and n is # of nodes with a binary min heap
- **Total complexity:** o(k*elogn)
- **Justification (one line):** K+1 dikjkstra runs costs O(elogn) and then we multiply the two we get (k+1) * (elogn) so we get O(k*elogn).

---

## Part 3: Algorithm Correctness


### Part 3a: What the Invariant Means



- **For nodes already finalized (in S):**
  -Distance[v] would represent the minimum fuel cost from the sources to whatever node v is. 
  -This should be the optimal. 

- **For nodes not yet finalized (not in S):**
  -distance[u] is theshortest ditance djisktra has discovred.
  -It takes the shortest discovered so far but it can be replace by a shorter one.
### Part 3b: Why Each Phase Holds


- **Initialization : why the invariant holds before iteration 1:**
  -At the very beggining of the itertation, distance is 0 so it is the shortest path and there is no path discovered yet
  -So the invariant holds because the initatizliation holds.
- **Maintenance : why finalizing the min-dist node is always correct:**
  -At the beginning of the iterations this would hold because all edge weights cannot be negative and  the node is not set so it is the smallest current u so it should be the same as the optimal. 
  -So therefore at each iterations the distance we see is already optimal and adding u to the path would maintain the invariant for the rest of the nodes.

- **Termination : what the invariant guarantees when the algorithm ends:**
  -After ittering through all the nodes, every node is either added to the optimal shortest path distance from spawn or the node would be unreachable the dictionary.
### Part 3c: Why This Matters for the Route Planner


  -This matters for the route planner because it needs to use the distance to see the actual shortest path to see how much fuel is used and it has to be the total route that is the cheapest and has enough fuel to make it through.

---

## Part 4: Search Design

### Why Greedy Fails


- **The failure mode:** The failure mode for greedy would be to just moving to the closet exit and not really considering the exit. Cheap from one exit does not mean it is cheaper overall to the exit you have to look at the whole thing.
- **Counter-example setup:** From the illustration exampe from the sepcd we have the relic bcd. from s spawn to b is 1, to c is 2, to d is 2. from b to d is 1, from b to t is 1, from b to c is 100.  From c to b is 1, c to T is 1. From d to b is 1, d to c is1, d to t is 100.
- **What greedy picks:**  Greedy would pick to b frist becaues its cheapest then d then c and then T witha  total cost 103.
- **What optimal picks:** Optimal would pick b then d then c and then t because going from c t to 1 would only cost 1 instead of going the otehr way.
- **Why greedy loses:** Greedy loses because it just goes to the nearest relic needed to be collected. It chooses D before going to c because it did not know that picking C last would make it impossbily to dodge the 100 choice. The optimal unlike creedy considers everything before picking

### What the Algorithm Must Explore


-The algorithm must eplore the order of every relic and going through the dungeon and return with the lowest total fuel cost to the exit.
---

## Part 5: State and Search Space

### Part 5a: State Representation



| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_loc| node| The location the torchbearer is at the in the search|
| Relics already collected |relics_reamning | set|The relics still yet not visited or not collected |
| Fuel cost so far |cost_so_far |float |The amount of fuel used from spawn to the current location. |

### Part 5b: Data Structure for Visited Relics



| Property | Your answer |
|---|---|

| Data structure chosen |set |
| Operation: check if relic already collected | Time complexity: o(1) hash |
| Operation: mark a relic as collected | Time complexity: O(1) just removing the relic .remove to the set|
| Operation: unmark a relic (backtrack) | Time complexity: O(1) adding a relic back .add to the set|
| Why this structure fits |The operations just search the set but iterating to find the reamining relics would be O(k). The set would fit because it would tell us whats left to find without storing a different list to find what we still have to collect|

### Part 5c: Worst-Case Search Space


- **Worst-case number of orders considered:**  The worst case number of orders considered would be o(k!)
- **Why:** The worst case search would be k recursove choices at least level so the wrost case before the pruning would be o(k!)

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking


- **What is tracked:** A list of best cost and order and best cost is the least amount of fuel cost for a route from spawn to the relics and exit that is found so far. Best order is the order the relics are visited. 
- **When it is used:** It is used at every recursive call the current iteration of cost so far and the reamin cost is compared with the best, and compared to the base case when there is a complete path that is better it will update best
- **What it allows the algorithm to skip:** it allows the alogrithm to skip routes that already exceeds best because it will not get any better there is no point in going all the way for those.

### Part 6b: Lower Bound Estimation


- **What information is available at the current state:** The information avaiable is the distance table for route we know, the costsofar or the fuel used already and the current location and the relics that still need to be found.
- **What the lower bound accounts for:** The lower bound accounts for seeing the shortest distant to the next relic and adds it and ignores the rest because it would continue to increase the bound
- **Why it never overestimates:** It never overestimates because the going to the next relic is has to be the least amount of fuel used the torchbearer can make. The lower bound is less than or equal to the true reaming cost should always hold because it already includes visiting the other relics. 

### Part 6c: Pruning Correctness

- Pruning is safe because the cost and lower bound has to be greater than or equal to the best solution so far because it cannot be better than what we already found as the best. The pruning condition looks at the lower bound and it is not possible for optimal to be pruned or skipped.

---

## References

-Lecture notes
- Dijkstra's Algorithm – Wikipedia overview of the algorithm, invariant, and complexity:
  https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

- Python heapq documentation – used for the min-heap priority queue in run_dijkstra:
  https://docs.python.org/3/library/heapq.html

- Backtracking – GeeksforGeeks overview of recursive backtracking with state restoration:
  https://www.geeksforgeeks.org/backtracking-algorithms/

- Branch and Bound – explanation of best-so-far pruning and admissible lower bounds:
  https://en.wikipedia.org/wiki/Branch_and_bound

- Travelling Salesman Problem – background on why exhaustive search with pruning is needed
  for combinatorial route optimization:
  https://en.wikipedia.org/wiki/Travelling_salesman_problem

