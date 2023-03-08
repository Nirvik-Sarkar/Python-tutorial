"""When we use else with for loop, the compiler will only go into the else 
block of code when two conditions are satisfied:
The loop is normally executed without any error.
We are trying to find an item that is not present inside the list or data structure on which
we are implementing our loop."""
khana = ["roti", "Sabzi", "chawal"]

for item in khana:
    if item == "rotiroll":
        break

else:
    print("Your item was not found")


