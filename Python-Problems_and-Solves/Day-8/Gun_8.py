if __name__ == '__main__':
    n = int(input(""))
    arr = map(int, input("").split())

    unique_scores = list(set(arr))  # Convert scores to a set to remove duplicates
    unique_scores.sort(reverse=True)  # Sort the unique scores in descending order

    # The runner-up score will be the second highest score in the sorted list
    runner_up_score = unique_scores[1]

    print(runner_up_score)
