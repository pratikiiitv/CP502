9-11/3/2026

Let there be some light!
Quick introduction of participants
Broad Idea about the Program
Program Structure and Schedule
https://docs.google.com/spreadsheets/d/1OWJKATapPSVm--0KP5njE4usdZ11Lku2djIwMele7-I/edit?usp=sharing
Expectations?

Story of halwai making laddoos
Progression of a sequence 1 2 3 4 ... to 2^n

Reality check
Information consumes attention (may the measure of information be defined in terms of the attention that it consumes rather than the entropic one!)

There will be interesting exercises and coding problems but beware!
ChatGPT Example:
Immersive Technologies and Cognitive Systems in Hindi
✅ Simplified Hindi (For broader understanding):
"डूबाने वाली तकनीकें और सोचने-समझने वाली प्रणालियाँ"
(Doobāne Vālī Taknīken aur Sochne-Samajhne Vālī Praṇāliyān)


CP502
Introduction to AI and Search [5-0-8 Hours]
History, The state of the art; intelligent agents; structure; environment; Configuration and Planning Problems, State space representation, Breadth-first search; uniform cost search; depth-first search; depth-limited search; iterative, deepening search; bi-directional search; heuristic search techniques; comparing search strategies, randomized search, adversarial search, alpha-beta pruning

Toy examples

(1) 3 Jugs - 8lt, 5lt, 3lt -> Measure 4lt (conserve water)

(2) Missionaries and Cannibals - 3 Miss, 3 Cann on left bank -> transfer to right bank
A boat with max capacity 2 

(3) Knuth - Sqrt, !, Floor - Start at 5 -> reach 7

3 Jugs Problem:

Configuration -> State -> [8, 0, 0] Index 0, 1, 2 -> 8,5,3 lt jugs resp.
Init_State = [8,0,0]
Goal_State = [4,1,3], [4,4,0], [4,2,2], [4,3,1], ...

Agent                           Environment/ Problem
Init_State
Push(Init_State, Frontier)
Node <- Pop(Frontier)
bool Is_Goal(Node.State)
                                List <- Get_Successor(State)
Pick one Node from List
Node.State in Visited?
Pick another Node from List
...
Node.State in Frontier?
Replace/ Keep Cond. Value
...
Frontier <- push(Node)
Pop Node from Frontier
bool Is_Goal(Succ)

(8,0,0)->(3,5,0)->(3,2,3)->
(6,2,0)->(6,0,2)->(1,5,2)->
(3,5,0)

[[3,5,0],1,[8,0,0]]
[[3,5,0],6,[1,5,2]]

Breadth First Search

Node_under_cons         Frontier(FIFO)          Visited
[[8,0,0],0,{}]          [[8,0,0],0,{}]                  
                                                [[8,0,0],0,{}]              
                        [[3,5,0],1,[8,0,0]]
                        [[5,0,3],1,[8,0,0]]
[[3,5,0],1,[8,0,0]]                             [[8,0,0],0,{}]
                                                [[3,5,0],1,[8,0,0]] 
                        [[5,0,3],1,[8,0,0]]
                        [[0,5,3],2,[3,5,0]]
                        [[3,2,3],2,[3,5,0]]

GIT: pratikiiitv/CP502
three_jugs_bfs.py

Flatland - Romance of many dimensions
Edwin Abott

is_valid() : {state} -> {Y/N}
get_successors() : {state} -> {successor states}
bfs() : {start_state, goal_state} -> {{},path}

AGENT                       ENVIRONMENT (PROBLEM)
                            is_valid()
                            get_successors()
bfs()

Agent has access to the problem/ graph via successor function only!
Init_state
Push(Init_state, Frontier)
Node <- Pop(Frontier)

Is Frontier Empty? ----> No solution
bool Is_Goal(Node.state)
                            List <- get_successors(Node.state)
Pick one Node from the list
Node.state is visited?
Node.state is in Frontier?
Replace/Keep Node
Frontier <- Push(Node, Frontier)
...
Node <- Pop(Frontier)

Missionaries and Cannibals
State representation : (M=3,C=3,L=1/R=0)
is_valid(state)
    # M > C 
    # M, C <= 3
    # M, C >= 0
get_successor(state)


{}          {H,
            (M, 80),
            (N, 70),
            (J, 60),
            (E, 70),
            (K, 40),
            (T, 0)}
{(A, 110),
(D, 120),
(G, 120),
(I, 90),
(P, 80),
(B, 100),
(O, 40),
(F, 50),
}

Matrix ??
A = [1 2 3; 4 5 6; 7 8 9]
A 3x3

A = [1 2 3 4 5 6 7 8 9]
A(0) = 1 ---> (0,0)
A(5) = 6 ---> (1,2)
A(8) = 9 ---> (2,2)

[1 2 3 4 5 6 7 0 8]
    [1 2 3 4 5 6 7 8 0]
    [1 2 3 4 5 6 0 7 8]
    [1 2 3 4 0 6 7 5 8]

[1 0 2 3 4 5 6 7 8]
index = 1 for value 0

AGENT - Aeger - todo
ENVIRONMENT - Problem

--------------------                ____________   
|                   |               |           |      
|       Init        |----------->   |           |
| ENV   Goal_Test   |<---------->   |   AGENT   |
|       Successor   |<---------->   | BFS/DFS   |
|                   |               | A*, etc   |
--------------------                ------------    

a = 2
b = 3
temp = a
a = b
b = temp 

a = 3
b = 2
a = a + b   = 5
b = a - b   = 3  
a = a - b   = 2

Branching Factor of a Tree
4 - 2
1 - 4
4 - 3
Avg Moves = (8 + 4 + 12)/9 = 24/9 = 2.7

A heuristic function that never overestimates the actual 
distance to goal, such a heuristic is said to be admissible.

If h is admissible, then f(n) = g(n) + h(n) gives 
optimal path!!!

A-star