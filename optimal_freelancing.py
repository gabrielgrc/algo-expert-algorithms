#Complexity Analysis : T O(nlog(n)) | S O(1)
def optimalFreelancing(jobs):
    LENGTH_OF_WEEK = 7
    profit = 0
    jobs.sort(key=lambda job: job["payment"], reverse=True)
    timeline = [False] * LENGTH_OF_WEEK

    for job in jobs:
        maxTime = min(job["deadline"], LENGTH_OF_WEEK)
        for time in reversed(range(maxTime)):
            if timeline[time] == False:
                timeline[time] = True
                profit += job["payment"]
                break
    return profit

# Test the function
jobs = [
    {"payment": 2, "deadline": 2},
    {"payment": 3, "deadline": 4},
    {"payment": 1, "deadline": 5},
    {"payment": 2, "deadline": 7},
    {"payment": 1, "deadline": 3},
    {"payment": 2, "deadline": 3},
    {"payment": 3, "deadline": 1},
]

profit = optimalFreelancing(jobs)
print(f"Total profit: {profit}")
