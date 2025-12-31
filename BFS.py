'''
from collections import deque

def bfs(start,graph):
    queue=deque([start])
    visited=set()
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node,end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.apeend(neighbor)

'''
from collections import deque


def bfs(start,graph):
    visited=set()
    queue=deque([start])
    visited.add(start)


    while queue:
        node=queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    #print(visited)// visited kiyanne set ekaka nis print klt wadk na dapu order ekat newei inne 

graph={'A':['B','C'],
       'B':['A','D','E'],
       'C':['A','F','G'],
       'D':['B'],
       'E':['B'],
       'F':['C'],
       'G':['C']}
bfs('A',graph)
bfs('B',graph)
