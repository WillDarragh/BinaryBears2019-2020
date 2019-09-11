# Water

from pprint import pprint

def get_allpaths(node, path):
	global allpaths,graph
	if node == 2:
		allpaths.append(path)
		return
	for key in filter(lambda x:x[0]==node,graph.keys()):
		if key not in path:
			new_path = path.copy()
			new_path.append((key))
			get_allpaths(key[1],new_path)

def valid(paths,graph):
	for path in paths:
		if validp(path,graph):
			return True
	return False

def validp(path,graph):
	for e in path:
		if not graph[e][0] < graph[e][1]:	
			return False
	return True

def mincap(path,fgraph):
	global graph
	m = min(path, key=lambda x: graph[x])
	return fgraph[m][1]-fgraph[m][0]

def maxflow():
	global allpaths,graph
	mflow = 0
	flow_graph = {}
	for key,val in graph.items():
		flow_graph[key] = [0,val]
		flow_graph[(key[1],key[0])] = [val,val]
	while(valid(allpaths,flow_graph)):
		path = []
		for p in allpaths:
			if validp(p,flow_graph):
				path = p
				break
		minc = mincap(path,flow_graph)
		for e in path:
			flow_graph[e][0] += minc
			flow_graph[(e[1],e[0])][0] -= minc
		mflow += minc
	return mflow
	
N,P,K = map(int, input().split())

graph = {}
allpaths = []

for p in range(P):
	a,b,c = map(int, input().split())
	if b == 1:
		b = a
		a = 1
	if a == 2:
		a = b
		b = 2
	graph[(a,b)] = c

get_allpaths(1,[])
print(maxflow())

allpaths = []

for k in range(K):
	a,b,c = map(int, input().split())
	if b == 1:
		b = a
		a = 1
	if a == 2:
		a = b
		b = 2
	if (a,b) not in graph:
		graph[(a,b)] = c
	else:
		graph[(a,b)] += c
	get_allpaths(1,[])
	print(maxflow())
	all_paths = []
