import sys
import random
import statistics

def generate_numbers(fileName, size, mu, sd):
    try:
        size = int(size) # Converting string to int - number of random numbers to generate
        mu = float(mu)   # Mean of the normal distribution from which random numbers are generated
        sd = float(sd)   # Standard deviation of the normal distribution from which random numbers are generated

        if size <= 0 or sd < 0: # Check-up step to ensure that size is positive and sd is non-negative
            raise ValueError("Size must be positive and sd must be non-negative.")

        numbers = [random.gauss(mu, sd) for _ in range(size)] # Generate random numbers
        
        with open(fileName, "w") as file: # Write the generated numbers to a file; fileName = "numbers.txt"; "w" = write mode, which means that the file is opened for writing
            for num in numbers:           # Every number in the list of generated numbers is written to the file
                file.write(f"{num}\n")    # file.write = function to write to a file; f"{num}\n" = number followed by a newline character
# f = formatted string literal; \n = newline character

        # Calculate actual mean and std of the generated numbers
        actual_mean = statistics.mean(numbers)
        actual_stddev = statistics.stdev(numbers) if size > 1 else 0.0

        print(f"Size: {size}")
        print(f"Mean: requested={mu}, generated={actual_mean}")
        print(f"Stddev: requested={sd}, generated={actual_stddev}")
        print(f"Numbers written to {fileName}")

    except ValueError as e: # If an error occurs, the error message is printed
        print(f"Error: {e}")

if __name__ == "__main__": # If the script is run as a standalone script, the following code is executed
    if len(sys.argv) != 5:
        print("Usage: python gen_norm_nums.py <fileName> <size> <mu> <sd>")
    else:
        _, fileName, size, mu, sd = sys.argv
        generate_numbers(fileName, size, mu, sd)
        
        # Example: python gen_norm_nums.py nums.txt 10 0 1
        # Output: Size: 10  
        #         Mean: requested=0.0, generated=-0.045
        #         Stddev: requested=1.0, generated=0.926
        #         Numbers written to nums.txt
