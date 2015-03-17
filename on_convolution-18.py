neural_vector = np.reshape(neural_signal, (1, N))
# The scaling and summing by the magic of matrix multiplication
bold_signal_again = neural_vector.dot(shifted_hrfs)
# This gives exactly the same result as previously, yet one more time
assert np.all(bold_signal == bold_signal_again)