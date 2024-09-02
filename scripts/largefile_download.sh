#!/bin/bash

# Define URLs and file names
TENSORFLOW_CC_URL="https://drive.google.com/uc?export=download&id=1wUNWgNXHZ-OQs01fLypidSbrU8T-1pOs"
TENSORFLOW_FRAMEWORK_URL="https://drive.google.com/uc?export=download&id=1jnQubtAnSJ1elN_RqhbpAyikO3LpHGCC"

TENSORFLOW_CC_FILE="libtensorflow_cc.so.2"
TENSORFLOW_FRAMEWORK_FILE="libtensorflow_framework.so.2"

# Define target directory
TARGET_DIR="enviro/lib/python3.12/site-packages/tensorflow"

# Create the target directory if it doesn't exist
mkdir -p "$TARGET_DIR"

# Download the files
echo "Downloading TensorFlow shared libraries..."
wget "$TENSORFLOW_CC_URL" -O "$TENSORFLOW_CC_FILE"
wget "$TENSORFLOW_FRAMEWORK_URL" -O "$TENSORFLOW_FRAMEWORK_FILE"

# Move the files to the target directory
echo "Moving files to $TARGET_DIR..."
mv "$TENSORFLOW_CC_FILE" "$TARGET_DIR/"
mv "$TENSORFLOW_FRAMEWORK_FILE" "$TARGET_DIR/"

echo "Download and move complete."
