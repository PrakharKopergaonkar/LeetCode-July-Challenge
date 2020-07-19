<h1> Week 3 solutions </h1>

<h3> Table of Content </h3>

| Day| Question | Link |
| --------------- | --------------- | --------------- | 
| 15 | Reverse Words in a String | [String_Reverse.py](./String_Reverse.py) |
| 17 | Top K Frequent Elements | [K_frequent.py](./K_frequent.py) |
| 18 | Course Schedule II | [Course_ScheduleII.py](./Course_ScheduleII.py) |


<h3> Notes regarding Question 18: Course Schedule II</h3>
<ul>
    <li> In this problem We need to find topological order of the graph. </li>
    <li> The algorithm works with two things : Topological sorting and cycle detection.</l1>
    <li> Topological sorting is done using DFS(depth first search).</li>
    <li> The list of edges given as input are first converted into dictonary. For ex: [[1,0],[2,0],[3,1],[3,2]] is converted into {0:[1,2], 1:[3], 2:[3]}</li>
    <li> Cycle detection is done using evaluating value of node currently being visited during DFS in visited array.</li>
    <li> Visited array can contain three values for a particular node -
        <ul>
            <li> 0 : The node is unvisited</li>
            <li> 1 : The node is visited and is currently being explored </li>
            <li> 2 : The node is visited and has been explored </li>
        </ul> 
    </li>
    <li> During DFS if we encounter node with value 0, We start exploring it and set it's value to 1.</li>
    <li> If the value is 1, that means there is a cycle so no Topological order is possible, So we return True. </li>
    <li> If the value is 2, them we ignore the node.</li>
    <li> At the in DFS method we add the node node values in the array storing topologial order and sets its visited to 2 and return False.</li>
    <li> Function that's finding order returns empty list if get's "True" from DFS. </li>
</ul>