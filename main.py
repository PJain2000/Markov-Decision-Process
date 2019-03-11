import copy
print("Enter N and M")
number1 = [int(n) for n in input().split()]

N = number1[0]
M = number1[1]

reward = []

print("Enter Rewards")
for i in range(0, N):
	x = [float(n) for n in input().split()]
	reward.append(x)

print("Enter E and W")
number2 = [int(n) for n in input().split()]

E = number2[0]
W = number2[1]

end_states = []

print("Enter the coordinates of ​end states​")
for i in range(0, E):
	x = tuple(int(n.strip()) for n in input().split())
	end_states.append(x)

walls = []

print("Enter the coordinates of ​walls​")
for i in range(0, W):
	x = tuple(int(n.strip()) for n in input().split())
	walls.append(x)

print("Enter the coordinates of the ​start state")
start_state = tuple(int(n.strip()) for n in input().split())

print("Enter the ​unit step reward")
unit_step_reward = float(input())

for i in range(0, N):
	for j in range(0, M):
		if (i,j) not in walls and (i,j) not in end_states:
			reward[i][j] = reward[i][j] + unit_step_reward

gamma = 0.99
epsilon = 0.01
actlist = ["North", "East", "South", "West"]

states = []
for i in range(0, N):
	for j in range(0, M):
		x = (i,j) 
		if x not in walls:
			states.append(x)

def T(state, action):
	if action == None:
		return [(0.0, state[0], state[1])]
	elif action == "North":
		x = []
		if (state[0]-1, state[1]) in states:
			x.append((0.8, state[0]-1, state[1]))
		else:
			x.append((0.8, state[0], state[1]))
		if (state[0], state[1]-1) in states:
			x.append((0.1, state[0], state[1]-1))
		else:
			x.append((0.1, state[0], state[1]))
		if (state[0], state[1]+1) in states:
			x.append((0.1, state[0], state[1]+1))
		else:
			x.append((0.1, state[0], state[1]))
		return x
	elif action == "East":
		x = []
		if (state[0], state[1]+1) in states:
			x.append((0.8, state[0], state[1]+1))
		else:
			x.append((0.8, state[0], state[1]))
		if (state[0]-1, state[1]) in states:
			x.append((0.1, state[0]-1, state[1]))
		else:
			x.append((0.1, state[0], state[1]))
		if (state[0]+1, state[1]) in states:
			x.append((0.1, state[0]+1, state[1]))
		else:
			x.append((0.1, state[0], state[1]))
		return x
	elif action == "South":
		x = []
		if (state[0]+1, state[1]) in states:
			x.append((0.8, state[0]+1, state[1]))
		else:
			x.append((0.8, state[0], state[1]))
		if (state[0], state[1]-1) in states:
			x.append((0.1, state[0], state[1]-1))
		else:
			x.append((0.1, state[0], state[1]))
		if (state[0], state[1]+1) in states:
			x.append((0.1, state[0], state[1]+1))
		else:
			x.append((0.1, state[0], state[1]))
		return x
	elif action == "West":
		x = []
		if (state[0], state[1]-1) in states:
			x.append((0.8, state[0], state[1]-1))
		else:
			x.append((0.8, state[0], state[1]))
		if (state[0]-1, state[1]) in states:
			x.append((0.1, state[0]-1, state[1]))
		else:
			x.append((0.1, state[0], state[1]))
		if (state[0]+1, state[1]) in states:
			x.append((0.1, state[0]+1, state[1]))
		else:
			x.append((0.1, state[0], state[1]))
		return x
		

def R(state):
		return reward[state[0]][state[1]]

def actions(state):
		if state in end_states:
			return [None]
		else:
			return actlist

policy = dict([(s, "") for s in states])

def value_iteration():
	U1 = dict([(s, 0) for s in states])
	
	while True:
		U = {}
		for key, value in U1.items():
			U[key] = value

		delta = 0
		for s in states:
			m = []
			for a in actions(s):
				d = 0
				for i in T(s,a):
					d = d + i[0] * U[(i[1], i[2])]
				m.append(d)

			U1[s] = R(s) + gamma * max(m)

			delta = max(delta, abs(U1[s] - U[s]))
		if delta < epsilon * (1 - gamma) / gamma:
			 return U

def find_policy(utility):
	for s in states:
		if s not in end_states:
			m = []			
			for a in actions(s):
				d = 0
				for i in T(s, a):
					d = d + i[0] * utility[(i[1], i[2])]
				m.append(d)

			p = 0
			for i in range(0,4):
				if m[i] == max(m):
					p = i

			if (p == 0):
				policy[s] = "North"
			elif (p == 1):
				policy[s] = "East"
			elif (p == 2):
				policy[s] = "South"
			elif (p == 3):
				policy[s] = "West"


answer = value_iteration()

for i in walls:
	answer[i] = '-'

find_policy(answer)

for i in walls:
	policy[i] = '-'
for i in end_states:
	policy[i] = '-'

print(answer)
print(policy)
