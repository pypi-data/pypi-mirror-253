import numpy as np

def kalman_filter(measurements, initial_state, initial_estimate_error, process_variance, measurement_variance):
    """
    One-dimensional Kalman filter implementation.

    Parameters:
    - measurements (numpy.ndarray): Array of measurements.
    - initial_state (float): Initial estimate of the state.
    - initial_estimate_error (float): Initial estimate error.
    - process_variance (float): Process noise variance.
    - measurement_variance (float): Measurement noise variance.

    Returns:
    - numpy.ndarray: Array of filtered state estimates.
    """
    num_measurements = len(measurements)
    state_estimate = initial_state
    estimate_error = initial_estimate_error
    filtered_states = np.zeros(num_measurements)

    for i in range(num_measurements):
        # Prediction step
        predicted_state = state_estimate
        predicted_error = estimate_error + process_variance

        # Update step
        kalman_gain = predicted_error / (predicted_error + measurement_variance)
        state_estimate = predicted_state + kalman_gain * (measurements[i] - predicted_state)
        estimate_error = (1 - kalman_gain) * predicted_error

        filtered_states[i] = state_estimate

    return filtered_states