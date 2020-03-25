# Create the model: model
model = Sequential()

# Add the first hidden layer
model.add(Dense(50, activation='relu', input_shape=(784,)))

# Add the second hidden layer
model.add(Dense(50, activation='relu', input_shape=(784,)))

# Add the output layer
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile('adam','categorical_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(X, y, validation_split=0.3)
