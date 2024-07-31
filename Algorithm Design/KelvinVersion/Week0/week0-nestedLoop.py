import time

k = int(input())
user_list = list(map(int, input().split()))
answer = []

start_time = time.process_time()

for i in range(0, len(user_list)) :
    for j in range(i, len(user_list)) :
        if user_list[j] * user_list[i] == k :
            answer.append(user_list[j])
            answer.append(user_list[i])
            break

end_time = time.process_time()
completion_time = end_time - start_time

if len(answer) > 0 :
    print("The answer is ", answer[0] * answer[1])
    print("The completion time is ", completion_time)



