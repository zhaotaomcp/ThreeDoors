import numpy as np
import matplotlib.pyplot as plt

stay = []
switch = []
for i in range(10**3):
    car_door = np.random.randint(1,4)
    contestant_selection = np.random.randint(1,4)
    remaining_goats = [door for door in [1,2,3] if door!= car_door and door != contestant_selection]
    door_revealed = np.random.choice(remaining_goats)
    if_switch = [door for door in [1,2,3] if door != contestant_selection and door != door_revealed][0]
    # Record results if contestant changes door selection
    if if_switch == car_door:
        switch.append(1)
    else:
        switch.append(0)
    # Record results if contestant keep door selection
    if contestant_selection == car_door:
        stay.append(1)
    else:
        stay.append(0)
# Plot the results
plt.plot(range(1,10**3+1), [np.mean(stay[:i]) for i in range(1,10**3+1)], label='Keep Selected Door')
plt.plot(range(1,10**3+1), [np.mean(switch[:i]) for i in range(1,10**3+1)], label='Switch Selected Door')
plt.ylabel('Probability of Winning')
plt.xlabel('Number of Simulations')
plt.title('Simulated Probability of Winning the Monty Hall Game')
plt.legend()
plt.show()
