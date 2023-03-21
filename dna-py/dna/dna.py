import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage-> python dna.py database.csv sequence.txt")
        sys.exit(1)

    # TODO: Read database file into a variable
    dna_Databases = []
    with open(sys.argv[1], "r") as dna_file:
        Reader = csv.DictReader(dna_file)
        Database = list(Reader)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as N:
        Sequence = N.read()

    # TODO: Find longest match of each STR in DNA sequence
    matches = {}

    for i in Database[0]:
        matches[i] = (longest_match(Sequence, i))

    # TODO: Check database for matching profiles
    S = 'No Match'
    S_counter = 1

    for i in range(len(Database)):
        for j in matches:
            if str(matches[j]) == Database[i][j]:
                S_counter += 1
        if S_counter == len(matches):
            S = Database[i]['name']
            break
        else:
            S_counter = 1

    print(S)
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
