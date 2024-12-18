import numpy as np
import joblib

# Load scaler
scaler_path=f'./static/scaler.save'
scaler = joblib.load(scaler_path)


def my_inverse_scaler(y: np.ndarray, X: np.ndarray) -> np.ndarray:
    """
    Inverse scale the prediction result.
    """
    tmp = y.reshape((-1, 1))  # Reshape to 2D
    X_reshaped = X.reshape(1, -1)  # Reshape X to 2D
    tmp = np.concatenate((tmp, X_reshaped), axis=1)
    tmp = scaler.inverse_transform(tmp)  # Inverse scale
    return tmp[:, 0]  # Return only the target column
