## Algorithm Design – Matching students to clubs using the Hungarian algorithm

A bipartite graph is populated with nodes as student IDs and club IDs, and edge weights as the happiness index of a particular student to a particular club.
The Hungarian algorithm then computes the maximum-weighted bipartite matching on the graph and outputs an optimal assignment.

The graph is stored as a 2D matrix.
The rows represent students, and the columns represent clubs. A table cell represents the happiness index of a student being assigned a club.
The following table is a sample with 5 students and 5 clubs.
Happiness scores of 0 signify that the student is ineligible to join the club, so an edge weight of 0 is provided.

```
[[1, 2, 0, 0, 0],
 [1, 0, 0, 0, 0],
 [0, 1, 2, 0, 0],
 [0, 0, 1, 2, 3],
 [0, 0, 0, 0, 1]]
```

This corresponds to the following bipartite graph:

![image](https://user-images.githubusercontent.com/63921209/221356028-8682d9e4-8e9b-48fc-a78a-a9e4ada860b1.png)

The Hungarian algorithm is an $O(𝑛^3)$ algorithm that finds the optimal matching to maximize the total happiness of students.
When run on the above input, it yields the following optimal matching of students to clubs, with a maximised happiness score of 8.
$$s_1 \rightarrow c_2$$ $$s_2 \rightarrow c_1$$ $$s_3 \rightarrow c_3$$ $$s_4 \rightarrow c_4$$ $$s_5 \rightarrow c_5$$

### Quick Note

In the real problem, since one club can accommodate multiple students, the input club nodes are duplicated to the number of students they can each take before the algorithm is run.
For example, if $c_1$ has a capacity $n$ then $n$ clones of $c_1$ are created and the student preferences are assigned accordingly to them.
