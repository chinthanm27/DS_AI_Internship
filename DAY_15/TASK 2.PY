P_heads = 1/2
P_six = 1/6
P_heads_and_six = P_heads * P_six
print(f"Probability of Heads AND 6: {P_heads_and_six} (1/12)")
total_marbles = 10
red_marbles = 5
P_first_red = red_marbles / total_marbles
P_second_red_given_first_red = (red_marbles - 1) / (total_marbles - 1)
P_both_red = P_first_red * P_second_red_given_first_red
print(f"Probability both marbles are Red: {P_both_red} (2/9)")
print("\nReflection:")
print("The denominator changes for the second marble because after removing one marble, only 9 remain. The events are dependent: the first pick affects the second.")
