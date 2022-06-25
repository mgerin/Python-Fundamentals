def lift_func(waiting_people, current_state_of_lift):
    for i in range(len(current_state_of_lift)):
        if waiting_people > 3:
            current_num_of_people = abs(4 - int(current_state_of_lift[i]))
            waiting_people -= current_num_of_people
            current_state_of_lift[i] += current_num_of_people
        else:
            current_state_of_lift[i] += waiting_people
            waiting_people = 0

    if waiting_people > 0:
        print(f"There isn't enough space! {waiting_people} people in a queue!")
    elif sum(current_state_of_lift) != len(current_state_of_lift) * 4:
        print(f"The lift has empty spots!")

    return ' '.join([str(num) for num in current_state_of_lift])


number_of_people = int(input())
lift_condition = list(map(int, input().split(' ')))
print(lift_func(number_of_people, lift_condition))