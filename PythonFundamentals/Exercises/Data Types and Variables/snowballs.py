number_of_snowballs = int(input())
snowball_value = 0
snowball_weight = 0
time_needed_for_snowball = 0
snowball_quality = 0
best_snowball_value = 0
for i in range(number_of_snowballs):
    snowball_weight_input = int(input())
    time_needed_for_ball_input = int(input())
    snowball_quality_input = int(input())
    snowball_value = (snowball_weight_input / time_needed_for_ball_input) ** snowball_quality_input
    if snowball_value > best_snowball_value:
        best_snowball_value = int(snowball_value)
        snowball_weight = snowball_weight_input
        time_needed_for_snowball = time_needed_for_ball_input
        snowball_quality = snowball_quality_input
print(f"{snowball_weight} : {time_needed_for_snowball} = {best_snowball_value} ({snowball_quality})")


