import random

if __name__ == "__main__":
    random.seed(1234)

    iterations = 10000
    switch_hit = 0
    no_switch_hit = 0

    for _ in range(iterations):
        doors = set(range(1, 4))
        goat_door = random.randint(1, 3)
        no_switch_choice = random.randint(1, 3)

        # initial choice before switch
        switch_choice = random.randint(1, 3)
        remain_doors = doors.copy()

        # remove the chosen door and goat door for host to open
        remain_doors.remove(switch_choice)
        try:
            remain_doors.remove(goat_door)
        except KeyError:
            pass

        # host choose a random door to open from the remaining
        host_door = random.choice(list(remain_doors))
        remain_doors.remove(host_door)

        # remaining doors to choose, need to add goat door back
        remain_doors.add(goat_door)
        switch_choice = random.choice(list(remain_doors))

        if switch_choice == goat_door:
            switch_hit += 1
        if no_switch_choice == goat_door:
            no_switch_hit += 1

    print("Switch hits: {switch_hit} / {iterations}".format(switch_hit=switch_hit, iterations=iterations))
    print("No switch hits: {no_switch_hit} / {iterations}".format(no_switch_hit=no_switch_hit, iterations=iterations))
