normative_time = 150
participants = []
for _ in range(5):
    surname = input("Enter surname of participant: ")
    group = input("Enter group of participant: ")
    instructor_surname = input("Enter surname of instructor: ")
    result = float(input("Enter result (in seconds): "))
    participants.append({
        'surname': surname,
        'group': group,
        'instructor_surname': instructor_surname,
        'result': result,
        'normative_passed': result <= normative_time
    })
participants.sort(key=lambda x: x['result'])
print("\nCross-country runs on 500 metres results:")
print(f"{'Surname':<20} {'Group':<10} {'Instructor':<20} {'Result (sec)':<15} {'The standard is fulfilled':<20}")
for participant in participants:
    print(
        f"{participant['surname']:<20} {participant['group']:<10} {participant['instructor_surname']:<20} {participant['result']:<15} {'Да' if participant['normative_passed'] else 'Нет':<20}")
count_passed = sum(1 for p in participants if p['normative_passed'])
print(f"\nThe total number of participants who fulfilled the standard: {count_passed}")