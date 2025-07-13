## CNN Hyperparameter Tuning with Manual Grid Search (MNIST)

This project demonstrates how to manually implement a **grid search with cross-validation** to find the best hyperparameters for a Convolutional Neural Network (CNN) on the MNIST dataset.

---

## 📌 Project Overview

- Build a CNN model using TensorFlow/Keras.
- Perform **manual grid search** over different:
  - Optimizers (`adam`, `rmsprop`)
  - Activation functions (`relu`, `tanh`)
  - Batch sizes (`32`, `64`)
- Use **K-Fold Cross-Validation** on a **random subset** of training data to evaluate hyperparameter combinations.
- Select the best configuration based on average validation accuracy.
- Train the final model on the full training set using the best hyperparameters.
- Plot **training vs. validation accuracy** across epochs.
- Evaluate performance on the **test set**.

---

## 🧱 Project Structure

- `create_model()`: Builds a CNN with customizable optimizer and activation function.
- **Stage 1**: Manual hyperparameter search with 3-fold cross-validation on a subset.
- **Stage 2**: Final model training on the full dataset with best-found parameters.
- Plot accuracy curves (`matplotlib`).
- Final evaluation on the test set.

---

## 🧪 Requirements

- Python 3.x
- TensorFlow
- NumPy
- Matplotlib

Install via pip:

```bash
pip install tensorflow numpy matplotlib
 MNIST-dataset
