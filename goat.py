import random
from argparse import ArgumentParser
import sys

DEFAULT_TRIES = 100000
DEFAULT_SEED = 1234


def setup_args():
    parser = ArgumentParser(description="Simulates the probability of getting car in Monty Hall problem")
    parser.add_argument("-n", "--number-of-tries", dest="iterations", type=int, default=DEFAULT_TRIES,
                        help=f"number of tries to simulate in this run, default is {DEFAULT_TRIES}")
    parser.add_argument("-s", "--seed", dest="seed", type=int, default=DEFAULT_SEED,
                        help=f"random seed to use in the simulation, default is {DEFAULT_SEED}")
    return parser


if __name__ == "__main__":
    arg_parser = setup_args()
    args = arg_parser.parse_args(sys.argv[1:])

    random.seed(args.seed)
    iterations = args.iterations

    switch_hit = 0
    no_switch_hit = 0

    for _ in range(iterations):
        doors = set(range(1, 4))
        car_door = random.randint(1, 3)
        no_switch_choice = random.randint(1, 3)

        # initial choice before switch
        switch_choice = random.randint(1, 3)
        remain_doors = doors.copy()

        # remove the chosen door and car door for host to open
        remain_doors.remove(switch_choice)
        try:
            remain_doors.remove(car_door)
        except KeyError:
            pass

        # host choose a random door to open from the remaining
        host_door = random.choice(list(remain_doors))
        remain_doors.remove(host_door)

        # remaining doors to choose, need to add car door back when initial choice is not the car
        if switch_choice != car_door:
            remain_doors.add(car_door)
        switch_choice = random.choice(list(remain_doors))

        if switch_choice == car_door:
            switch_hit += 1
        if no_switch_choice == car_door:
            no_switch_hit += 1

    print("Switch hits: {switch_hit} / {iterations} = {percentage}%".format(switch_hit=switch_hit,
                                                                            iterations=iterations,
                                                                            percentage=100.0 * float(
                                                                                switch_hit) / iterations))
    print("No-switch hits: {no_switch_hit} / {iterations} = {percentage}%".format(no_switch_hit=no_switch_hit,
                                                                                  iterations=iterations,
                                                                                  percentage=100.0 * float(
                                                                                      no_switch_hit) / iterations))
