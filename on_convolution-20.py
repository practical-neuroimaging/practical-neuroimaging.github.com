i = 25
M = n_hrf_points
neural_signal_part = neural_signal[i - M + 1 : i + 1]
hrf_column_part = shifted_hrfs[i - M + 1 : i + 1, i]
output_value = np.sum(neural_signal_part * hrf_column_part)
# It gives the right value
assert output_value == bold_signal[i]