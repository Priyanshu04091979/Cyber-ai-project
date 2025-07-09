import matplotlib.pyplot as plt

epochs = list(range(1, 6))
accuracy = [91.5, 92.1, 91.8, 92.4, 92.6]

plt.plot(epochs, accuracy, marker='o')
plt.title("Model Accuracy Over Epochs")
plt.xlabel("Epoch")
plt.ylabel("Accuracy (%)")
plt.grid(True)
plt.savefig("model_accuracy.png")
