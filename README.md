<h1 align="center">
   Graph Playground
</h1>

### About the project:
This project arises from the idea of starting to learn python and improve my knowledge of algorithms on graphs. I'm sure that a lot of code can be improved, since it is my first time in this language, but if you have any improvement, do not hesitate to make a pull request! 😁

### Dependencies:

- [graphics.py](https://pypi.org/project/graphics.py/)

### How to install and use:
    
    1. Install graphics.py:

        $ pip install graphics.py

    2. Represent your graph inside the graph.txt file

    3. Execute the program:

        $ python GraphPlayground.py

#### File Format for representing the graph:
First, you have to specify the graph you want to analyze inside the graph.txt file. The format of this file has to be the adjacency list of the graph following this format:

```
VERTEX1: ADJACENT1, ADJACENT2, ADJACENT2 |
VERTEX2: ADJACENT1, ADJACENT2, ADJACENT2 |
.......
VERTEXN: ADJACENT1, ADJACENT2
```

For example, this lines represents the graph cycle of 4 vertex:

```
A: B, D|
B: A, C|
C: B, D|
D: A, C
```

Once the file is configured, we can see graphically the graph and even the result of applying certain algorithms on it (such as BFS, DFS and GreedyColoring). Following the example of the cycle graph:

#### Representation of Graph Cycle (4)
![graph_cycle_4_final](https://user-images.githubusercontent.com/18640261/107013253-6ad68400-679a-11eb-9963-030f5ee7ba4a.png)

#### BFS from A
![bfs_A_graph_cycle_4](https://user-images.githubusercontent.com/18640261/107013248-69a55700-679a-11eb-9057-d82a5ba30859.png)

#### DFS from A
![dfs_A_graph_cycle_4](https://user-images.githubusercontent.com/18640261/107013251-6ad68400-679a-11eb-8964-41aa01747d6e.png)

#### Greedy Coloring Algorithm from A
![greedy_coloring_graph_cycle_4](https://user-images.githubusercontent.com/18640261/107013256-6b6f1a80-679a-11eb-81be-4414e1f5550e.png)
