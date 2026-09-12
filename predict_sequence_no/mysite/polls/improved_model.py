import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import os

def generate_training_data():
    """Generate diverse training sequences for better generalization"""
    sequences = []
    
    # Arithmetic progressions with different steps
    for step in [2, 3, 5, 7, 10, 11, 13]:
        start = np.random.randint(1, 50)
        seq = [start + i * step for i in range(20)]
        sequences.extend(seq)
    
    # Geometric progressions
    for ratio in [2, 3]:
        start = np.random.randint(1, 10)
        seq = [start * (ratio ** i) for i in range(10)]
        sequences.extend(seq)
    
    # Fibonacci-like sequences
    for _ in range(5):
        seq = [np.random.randint(1, 10), np.random.randint(1, 10)]
        for i in range(15):
            seq.append(seq[-1] + seq[-2])
        sequences.extend(seq)
    
    # Square and cube sequences
    for i in range(1, 15):
        sequences.extend([i**2, i**3])
    
    return sequences

def split_sequence(seq, n_steps):
    """Split sequence into training samples"""
    X, y = [], []
    for i in range(len(seq)):
        end_ix = i + n_steps
        if end_ix > len(seq) - 1:
            break
        seq_x, seq_y = seq[i:end_ix], seq[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return np.array(X), np.array(y)

def create_improved_model():
    """Create and train an improved model with diverse data"""
    print("Generating diverse training data...")
    data = generate_training_data()
    
    # Create sequences
    n_steps = 7
    X, y = split_sequence(data, n_steps)
    X = X.reshape((X.shape[0], X.shape[1], 1))
    
    # Create model
    model = Sequential([
        LSTM(100, activation='relu', input_shape=(n_steps, 1), return_sequences=True),
        LSTM(50, activation='relu'),
        Dense(25, activation='relu'),
        Dense(1)
    ])
    
    model.compile(optimizer='adam', loss='mse')
    
    # Train
    print("Training improved model...")
    model.fit(X, y, epochs=200, batch_size=32, validation_split=0.2, verbose=0)
    
    return model

def detect_pattern(sequence):
    """Detect simple patterns for rule-based prediction"""
    if len(sequence) < 3:
        return None, None
    
    # Check for arithmetic progression
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    if all(abs(d - diffs[0]) < 0.001 for d in diffs):
        return 'arithmetic', diffs[0]
    
    # Check for geometric progression
    if all(x != 0 for x in sequence):
        ratios = [sequence[i+1] / sequence[i] for i in range(len(sequence)-1)]
        if all(abs(r - ratios[0]) < 0.001 for r in ratios):
            return 'geometric', ratios[0]
    
    return None, None

def hybrid_predict(sequence):
    """Hybrid prediction combining rule-based and ML approaches"""
    # Detect pattern
    pattern_type, pattern_value = detect_pattern(sequence)
    
    if pattern_type == 'arithmetic':
        next_val = sequence[-1] + pattern_value
        confidence = 0.95
        method = f"Arithmetic progression (+{pattern_value})"
    elif pattern_type == 'geometric':
        next_val = sequence[-1] * pattern_value
        confidence = 0.90
        method = f"Geometric progression (×{pattern_value})"
    else:
        # Use ML model for complex patterns
        try:
            model_path = os.path.join(os.path.dirname(__file__), 'NumberSequence.h5')
            model = tf.keras.models.load_model(model_path)
            
            # Prepare input
            input_seq = np.array(sequence[-7:]).reshape(1, 7, 1)
            prediction = model.predict(input_seq, verbose=0)
            next_val = float(prediction[0][0])
            confidence = 0.70
            method = "Neural Network (LSTM)"
        except Exception as e:
            # Fallback to simple average of last few differences
            diffs = [sequence[i+1] - sequence[i] for i in range(-3, 0)]
            avg_diff = np.mean(diffs)
            next_val = sequence[-1] + avg_diff
            confidence = 0.50
            method = "Simple extrapolation"
    
    return next_val, confidence, method

if __name__ == "__main__":
    # Test the hybrid approach
    test_sequences = [
        [90, 100, 110, 120, 130, 140, 150],  # Arithmetic
        [2, 4, 8, 16, 32, 64, 128],          # Geometric
        [1, 1, 2, 3, 5, 8, 13],              # Fibonacci
        [10, 30, 50, 70, 90, 110, 130],      # Arithmetic (+20)
    ]
    
    for seq in test_sequences:
        pred, conf, method = hybrid_predict(seq)
        print(f"Sequence: {seq}")
        print(f"Prediction: {pred:.2f} (Confidence: {conf:.2f})")
        print(f"Method: {method}")
        print("-" * 50)
