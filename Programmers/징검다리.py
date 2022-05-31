def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)

    left = 1
    right = distance

    while left <= right:
        mid = (left + right) // 2

        removed = 0
        pre = 0

        for i in range(len(rocks)):
            if rocks[i] - pre < mid:
                removed += 1
            else:
                pre = rocks[i]

        if removed > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer