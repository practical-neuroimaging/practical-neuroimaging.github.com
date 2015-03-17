bold_signal_again = shifted_hrfs.T.dot(neural_vector.T)
# Exactly the same, but transposed
assert np.all(bold_signal == bold_signal_again.T)