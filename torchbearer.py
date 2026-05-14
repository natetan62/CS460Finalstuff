"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Nathan Tan
Student ID: 827824355

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    """
    return(
        """- **Why a single shortest-path run from S is not enough:** 
        -A single shortest path is not enough because it findds the cheapest path to the node indivudally but not the overall cost.
         -We need the cheapest cost overall 

        - **What decision remains after all inter-location costs are known:**
        - the decision that remains even after the costs are known is the order of chambers to visit with the relics. Each different order of vist would lead to different fuel costs.

        - **Why this requires a search over orders (one sentence):**
        -This requeires serch over orders because there isnt a rule or order that can find the optimal path right away. we need to find the globally chepaest ordering after exploring and pruning."""
        )



# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
       # No duplicates. Order does not matter.
    """
    
    
    startingNodes = set([spawn] +list(relics))
    return list(startingNodes)
   

   
    


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

        
    """

    distance = {}
    for node in graph:
        distance[node] = float('inf') #initalize the graph to nothinggg not discovered
    distance[source] = 0

    minHeap = [(0, source)]
    while minHeap:
        entry = heapq.heappop(minHeap) #pop the smallest distance
        fuel= entry[0]
        current =entry[1]
        
        if fuel> distance[current]:
            continue

        for v, weight in graph[current]:
            discovered= distance[current]+ weight
            if discovered<distance[v]:
                distance[v] =discovered
                heapq.heappush(minHeap,(discovered,v))
        
    return distance

def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    
    """
    distanceTable={}
    for source in select_sources(spawn,relics,exit_node): #djisktra from each source
        for dest, cost in run_dijkstra(graph,source).items():
            distanceTable[source,dest]= cost
    return distanceTable


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    
    """
    return("""## Part 3: Algorithm Correctness

    >Document your understanding of why Dijkstra produces correct distances.
    > Bullet points and short sentences throughout. No paragraphs.

    ### Part 3a: What the Invariant Means

    > Two bullets: one for finalized nodes, one for non-finalized nodes.
    >   Do not copy the invariant text from the spec.

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

                """)


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    
    """
    return("""## Part 4: Search Design

    ### Why Greedy Fails

    > State the failure mode. Then give a concrete counter-example using specific node names
    > or costs (you may use the illustration example from the spec). Three to five bullets.

    - **The failure mode:** The failure mode for greedy would be to just moving to the closet exit and not really considering the exit. Cheap from one exit does not mean it is cheaper overall to the exit you have to look at the whole thing.
    - **Counter-example setup:** From the illustration exampe from the sepcd we have the relic bcd. from s spawn to b is 1, to c is 2, to d is 2. from b to d is 1, from b to t is 1, from b to c is 100.  From c to b is 1, c to T is 1. From d to b is 1, d to c is1, d to t is 100.
    - **What greedy picks:**  Greedy would pick to b frist becaues its cheapest then d then c and then T witha  total cost 103.
    - **What optimal picks:** Optimal would pick b then d then c and then t because going from c t to 1 would only cost 1 instead of going the otehr way.
    -**Why greedy loses:** Greedy loses because it just goes to the nearest relic needed to be collected. It chooses D before going to c because it did not know that picking C last would make it impossbily to dodge the 100 choice. The optimal unlike creedy considers everything before picking

    ### What the Algorithm Must Explore

    -The algorithm must eplore the order of every relic and going through the dungeon and return with the lowest total fuel cost to the exit.
    ---




    
    """


    )


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    
    """
    best = [float('inf'), []] #the best relic order total cost found so far
    relics_remaining = set(relics) #holds marking and unmarking etc
    _explore(dist_table, current_loc = spawn, relics_remaining = relics_remaining, relics_visited_order =[], cost_so_far = 0.0, exit_node = exit_node, best = best )
    return(best[0], best[1])


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    if not relics_remaining: #base case all relics are collected already
        total_cost= cost_so_far + dist_table.get((current_loc, exit_node),float('inf')) #seeing if the route is even valid and looking up the fuel cost to the exit
        if total_cost<best[0]: #is this THE BEST?
            best[0] =total_cost #hold on potential save it
            best[1]=list(relics_visited_order)
        return
    
    cheapestNextRelic = min(dist_table.get((current_loc,r), float('inf')) #chepaest distance to remaing relics
                            for r in relics_remaining)
    
    if cost_so_far + cheapestNextRelic >= best[0]: #pruning correctness, only prune when it is is not possible for it to optimal or the best anymore this is part of the pruning afety
        return
    
    for rel in list(relics_remaining): #recursive cases
        fuelCost =dist_table.get((current_loc,rel), float('inf'))

        if fuelCost== float('inf'): #dead end cant reach
            continue
        relics_remaining.remove(rel) #updating
        relics_visited_order.append(rel)

        _explore(dist_table, current_loc = rel,relics_remaining=relics_remaining,relics_visited_order = relics_visited_order, cost_so_far=cost_so_far + fuelCost, exit_node=exit_node, best = best)
        
        relics_remaining.add(rel) #going back 
        relics_visited_order.pop()
    

    

# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    
    """
    dist_table= precompute_distances(graph,spawn, relics, exit_node)
    return find_optimal_route(dist_table,spawn,relics,exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()


