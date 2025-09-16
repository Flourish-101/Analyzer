import matplotlib.pyplot as plt

print("Hello, your script is running!")

# simple plot
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

plt.plot(x, y, marker='o')
plt.title("Test Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()
