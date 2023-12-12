def find_bigrams(sentence):
    words = sentence.lower().split()  # Convert to lowercase and split into words
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
    return bigrams



#alternative

def find_bigrams_2(sentence):
    left, right = 0,1
    words = sentence.lower().split()
    bigrams = []

    while right < len(words):
        bigrams.append((words[left],words[right]))
        left += 1
        right += 1

    return bigrams




import timeit


# Set up input data or any necessary variables
string1 = "In a world constantly evolving with technological advancements the pace of change is palpable From artificial intelligence shaping industries to renewable energy redefining sustainability innovation is the driving force People connect globally sharing ideas through digital platforms fostering a sense of interconnectedness Amid challenges resilience prevails inspiring collective efforts toward a better future Cultures intertwine celebrating diversity and education becomes a beacon for enlightenment In this dynamic landscape curiosity thrives pushing the boundaries of what's possible The journey unfolds with possibilities as humanity navigates the complex tapestry of progress weaving dreams into reality"
#but
string2 = "Within this dynamic terrain, curiosity blossoms and thrives pushing against the boundaries that define what is deemed possible The journey unfolds with boundless possibilities as humanity navigates the intricate and complex tapestry of progress Dreams weave seamlessly into reality in a dance of ideas and aspirations that transcend the limitations of the present"

string3 = "As the collective consciousness of societies evolves communication becomes the lifeblood that courses through the veins of this interconnected world Individuals from disparate corners of the globe find themselves engaged in a silent conversation that spans distances and defies traditional constraints The digital realm becomes a meeting ground where ideas flow freely like a river carving its path through the vast expanse of human knowledge"

string4 = "Challenges, like turbulent waves, test the resilience of the human spirit Yet, in the face of adversity, the collective resolve stands unyielding Individuals, communities, and nations alike find strength in unity forging bonds that withstand the tests of time The intricate dance of cultures takes center stage, each one adding a unique hue to the canvas of the global narrative"

string = string1 + string2 + string3 + string4

# Measure the execution time of function 1
time_function_1 = timeit.timeit(lambda: find_bigrams(string), number=1000)

# Measure the execution time of function 2
time_function_2 = timeit.timeit(lambda: find_bigrams_2(string), number=1000)

# Compare the execution times
print(f"Execution time for function 1: {time_function_1:.5f} seconds")
print(f"Execution time for function 2: {time_function_2:.5f} seconds")

# Optionally, compare the relative speed
if time_function_1 < time_function_2:
    print("Function 1 is faster.")
elif time_function_1 > time_function_2:
    print("Function 2 is faster.")
else:
    print("Both functions have similar execution times.")