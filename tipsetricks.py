#---rimozione elementi da una lista (ottimizzato)---
#versione lenta
items = [1,2,3,4,5]
for x in items:
    if cond(x):
        items.remove(x)

#versione ottimizzata
items = [x for x in items if not cond(x)]

#---BFS su grafo---
from collections import deque

def bfs(adj, s):
    q, seen = deque([s]), {s}
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                q.append(w)
    return order


