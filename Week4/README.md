<h1> Week 4 solutions </h1>

<h3> Table of Content </h3>

| Day| Question | Link |
| --------------- | --------------- | --------------- | 
| 22 | Binary Tree Zigzag Level Order Traversal | [BinaryTree_zigzag.py](./BinaryTree_zigzag.py) |
| 23 | Sinlge Number 3 | [Single_Number3.py](./Single_Number3.py) |
| 24 | All Paths From Source to Target | [All_paths.py](./All_paths.py) |
| 28 | Task Schduler | [Task_Scheduler.py](./Task_Scheduler.py) |

### Notes Regarding Task Scheduler

<ul>
    <li> In this question we need to find minimum time in which we can complete the task.</li>
    <li> For this we first covert task list into heap of tuples of task and their frequency.</li>
    <li> In order to use heap as maxheap we consider negative frequency </li>
    <li> Then we pop the most frequent element and store its frequency.</li>
    <li> Then we evaluate number of elements with same frequency (included one poped above) using counter</li>
    <li> We evaluate time required using following formula = (max_frequency - 1)*(n+1) + counter</li>
    <li> It may be possible that all elements cannot be filled inside this slots created by element with max_frequency</li>
    <li> So we return max of number of elements and the time we evaluated. </li>
</ul>
