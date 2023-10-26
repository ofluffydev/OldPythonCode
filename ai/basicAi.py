import tensorflow as tf

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, input_shape=(4,), activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
data = [[0.5, 0.5, 0.5, 0.5], [0.1, 0.2, 0.3, 0.4], [0.9, 0.8, 0.7, 0.6]]
labels = [[0], [1], [0]]
model.fit(data, labels, epochs=10)

# Use the trained model to make predictions
predictions = model.predict([[0.5, 0.5, 0.5, 0.5]])
print(predictions)
