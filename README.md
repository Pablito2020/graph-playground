<h1 align="center">
   Graph Playground
</h1>

### About the project:
This project arises from the idea of starting to learn python and improve my knowledge of algorithms on graphs. I'm sure that a lot of code can be improved, since it is my first time in this language, but if you have any improvement, do not hesitate to make a pull request! 😁

### Dependencies:

- [graphics.py](https://pypi.org/project/graphics.py/)

### How to install and use:
    
    1. Install graphics.py dependency:

        $ pip install graphics.py

    2. Represent your graph inside the graph.txt file

    3. Execute the program:

        $ python main.py

#### File Format for representing the graph:
First, you have to specify the graph you want to analyze inside the graph.txt file. The format of this file has to be the adjacency list of the graph following this format:

```
VERTEX: ADJACENT1, ADJACENT2, ADJACENT2 |
.......
FINAL_VERTEX: ADJACENT1, ADJACENT2 |
```

For example, this lines represents the graph cycle of 4 vertex:

```
A: B, D|
B: A, C|
C: B, D|
D: A, C
```

#### Showing the results on screen:

Once you have the correct syntax, the program will ask if you want to show the graph (pressing g or G) or apply BSF to any of its vertices (pressing b or B and specifying the vertex). Continuing with the example of the cycle graph:

Following the example, the output when you press g or G would be the graph cycle of 4 vertex (the representation may vary because its representation is chosen randomly):

<p align="center">
  <img src="https://user-images.githubusercontent.com/18640261/106574937-cbb45100-653b-11eb-8fdb-8bec8a8ebc51.png" alt="graph cycle 4 vertex">
</p>


the output of applying bfs to vertex A in the cycle graph would be the following spanning tree:

<p align="center">
  <img src="https://user-images.githubusercontent.com/18640261/106574934-ca832400-653b-11eb-9b14-073e4e631d8a.png" alt="BFS(cycle_4, A)">
</p>

