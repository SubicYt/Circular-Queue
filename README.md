# Circular-Queue
Implement a circular queue ADT to simulate and operating system juggling multiple processes on a single CPU. 
The circular queue is similar to a doubly linked list, with Processes serving as nodes, except for a few changes.
- There is no tail attribute
- The link attribute of the final node circles back to the head.
- the prev attribute points to the final node.
- Supports O(1) removal time by keeping track of a dictionary of pid:process pairs.

My own unit tests are included, but feel free to make your own. 

shaka!
