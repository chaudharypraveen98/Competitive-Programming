def person_lister(formatter):
    """Decorator factory: sorts people by age before formatting them.

    `formatter` is the function being decorated (name_format below).
    The returned `inner` replaces it and receives the WHOLE list of people.
    """

    def inner(people):
        # Sort by age (index 2). Ages arrive as strings ("20", "9", ...),
        # so int() is required: string sorting would put "100" before "9".
        # sorted() is STABLE -> people of equal age stay in input order.
        # The key function runs only once per element, so this stays O(n log n).
        return [formatter(person) for person in sorted(people, key=lambda p: int(p[2]))]

    return inner


@person_lister
def name_format(person):
    """Return 'Mr. First Last' or 'Ms. First Last' for one person.

    A person is a list: [first_name, last_name, age, sex].
    """
    title = "Mr. " if person[3] == "M" else "Ms. "
    return title + person[0] + " " + person[1]


if __name__ == "__main__":
    # Read all N people; each line -> [first_name, last_name, age, sex]
    n = int(input())
    people = [input().split() for _ in range(n)]
    # Print one formatted name per line, youngest first.
    print(*name_format(people), sep="\n")
