from pprint import pprint as pp


def make_day(num_teams, day):
    # using circle algorithm, https://en.wikipedia.org/wiki/Round-robin_tournament#Scheduling_algorithm
    assert not num_teams % 2, "Number of teams must be even!"
    # generate list of teams
    lst = list(range(1, num_teams + 1))
    # rotate
    day %= (num_teams - 1)  # clip to 0 .. num_teams - 2
    if day:                 # if day == 0, no rotation is needed (and using -0 as list index will cause problems)
        lst = lst[:1] + lst[-day:] + lst[1:-day]
    # pair off - zip the first half against the second half reversed
    half = num_teams // 2
    return list(zip(lst[:half], lst[half:][::-1]))


def PrintTable(schedule):
    days = [f"Day {i+1}" for i in range(len(schedule))]
    for i in range(len(schedule)):
        print(f"|Day {i+1}: ", end="")
        for j in schedule[i]:
            print("{} - {}| ".format(j[0], j[1]), end="")
        if len(schedule) == 5:
            print(f"\n{'-'*28}")
        else:
            print(f"\n{'-'*71}")

def make_schedule(num_teams):
    """
    Produce a one round schedule
    """
    # number of teams must be even
    if num_teams % 2:
        num_teams += 1  # add a dummy team for padding

    # build round-robin
    schedule = [make_day(num_teams, day) for day in range(num_teams - 1)]

    return schedule

def main():
    num_teams = int(input("How many teams? "))
    schedule = make_schedule(num_teams)
    PrintTable(schedule)
    # pp(schedule)
    

if __name__ == "__main__":
    main()

