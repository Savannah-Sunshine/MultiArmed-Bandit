slot_machine = SlotMachine()

reward_hist = [0,0,0]
counts = [0, 0, 0]


justexplore = 1
epsilon = 0.1  # 10% chance to explore
decay_factor = 0.9  # Decay factor

def epsilon_greedy(machine):
    global justexplore
    global epsilon
    global reward_hist, counts

    # Degrades saved history of rewards
    for i in range(len(reward_hist)):
        reward_hist[i] *= decay_factor

    # Tells algorithm to explore
    if random.random() < epsilon or justexplore < 10:
      arm_choice = random.randint(0,2)
      justexplore += 1

    else:
      # Chooses action based its knowledge of best reward
      bestVal = max(reward_hist)
      arm_choice = reward_hist.index(bestVal)

    counts[arm_choice] += 1
    reward = pullArm(machine, armChoice)
    reward_hist[arm_choice] += reward


# Method for convenience
def pullArm(machine, armNum):
    if armNum == 0:
        context = machine.get_context()
        reward = machine.pull_arm_a()
        return reward
    elif armNum == 1:
        context = machine.get_context()
        reward = machine.pull_arm_b()
        return reward
    elif armNum == 2:
        context = machine.get_context()
        reward = machine.pull_arm_c()
        return reward

for _ in range(1_000_000): #1_000_000
    epsilon_greedy(slot_machine)

print(reward_hist)
print(counts)
