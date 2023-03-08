
f1 = open("sample.txt")
"""else keyword:-
Now moving on to the else keyword. We use an else keyword to print something in cases where no 
exception occurs. Suppose that an exception occurred, and the except block is printing the error;
likewise, if the exception does not occur, we can print a statement that no error occurred, using
an else keyword."""

"""finally:-
Now the last keyword for this tutorial, i.e., finally, will run in either case.
It is also known as code cleaner because it will perform its action, either an exception 
occurs or not. We write such commands in the finally part of the code that we want to execute,
even an exception occurs or not. It is mostly used to clean resources or close files. """
try:
    f = open("does2.txt")

except EOFError as e:
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)
else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")
