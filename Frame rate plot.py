# import matplotlib.pyplot as plt
# import numpy as np

# # Models
# models = ["Model A", "Model B", "Model C"]

# # Sampling Rates
# sampling_rates = [1, 5, 10, 15]  # frames per second

# # Accuracy data for each model at different sampling rates
# accuracy_data = {
#     "Model A": [0.78, 0.79, 0.80, 0.81],  
#     "Model B": [0.76, 0.77, 0.78, 0.79],
#     "Model C": [0.74, 0.75, 0.76, 0.77]
# }

# # Processing time data for 1-minute video (time in seconds = 60 / sampling rate)
# processing_time = [60 / rate for rate in sampling_rates]  # in seconds

# # Create the figure and axis
# fig, ax1 = plt.subplots(figsize=(8, 6))

# # Plot accuracy on the left y-axis
# for model in models:
#     ax1.plot(
#         sampling_rates, 
#         accuracy_data[model], 
#         marker='o', 
#         label=model
#     )

# ax1.set_title("Accuracy and Processing Time vs. Sampling Rate", fontsize=14)
# ax1.set_xlabel("Sampling Rate (frames per second)", fontsize=12)
# ax1.set_ylabel("Accuracy", fontsize=12, color="blue")
# ax1.set_ylim(0.7, 0.85)
# ax1.tick_params(axis="y", labelcolor="blue")
# ax1.grid(True, linestyle='--', alpha=0.6)

# # Add a second y-axis for processing time
# ax2 = ax1.twinx()
# ax2.plot(
#     sampling_rates, 
#     processing_time, 
#     marker='s', 
#     color="red", 
#     linestyle="--", 
#     label="Processing Time (1-min Video)"
# )
# ax2.set_ylabel("Processing Time (seconds)", fontsize=12, color="red")
# ax2.tick_params(axis="y", labelcolor="red")
# ax2.set_ylim(0, 70)  # Adjust for better visualization

# # Add legends for both y-axes
# lines1, labels1 = ax1.get_legend_handles_labels()
# lines2, labels2 = ax2.get_legend_handles_labels()
# ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper center", title="Legend")

# # Tight layout and show the plot
# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Models
models = ["Model A", "Model B", "Model C"]

# Sampling Rates
sampling_rates = [1, 5, 10, 15]  # frames per second

# Accuracy data for each model at different sampling rates
accuracy_data = {
    "Model A": [0.78, 0.79, 0.80, 0.81],  
    "Model B": [0.76, 0.77, 0.78, 0.79],
    "Model C": [0.74, 0.75, 0.76, 0.77]
}

# Processing time table: keys are sampling rates, values are processing times
processing_time_table = {
    1: 4.0,  # 60 seconds for 1 frame per second
    5: 6.0,  # 60 / 5
    10: 12.0,  # 60 / 10
    15: 60.0  # 60 / 15
}

# Extract processing times as a list based on sampling rates
processing_time = [processing_time_table[rate] for rate in sampling_rates]

# Bar width for grouped bar chart
bar_width = 0.2
x = np.arange(len(sampling_rates))  # x positions for sampling rates

# Create the figure and axes
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot the accuracies as grouped bars
for i, model in enumerate(models):
    ax1.bar(
        x + i * bar_width,  # Shift bars for each model
        accuracy_data[model], 
        width=bar_width, 
        label=model
    )

# Customize the left y-axis
ax1.set_title("Accuracy and Processing Time vs. Sampling Rate", fontsize=14)
ax1.set_xlabel("Sampling Rate (frames per second)", fontsize=12)
ax1.set_ylabel("Accuracy", fontsize=12, color="blue")
ax1.set_xticks(x + bar_width)  # Center ticks between grouped bars
ax1.set_xticklabels(sampling_rates)
ax1.set_ylim(0.7, 0.85)
ax1.tick_params(axis="y", labelcolor="blue")
ax1.grid(True, linestyle='--', alpha=0.6)

# Add a second y-axis for processing time
ax2 = ax1.twinx()
ax2.plot(
    x + bar_width,  # Align line plot with the center of grouped bars
    processing_time, 
    marker='o', 
    color="red", 
    linestyle="--", 
    label="Processing Time (1-min Video)"
)
ax2.set_ylabel("Processing Time (seconds)", fontsize=12, color="red")
ax2.tick_params(axis="y", labelcolor="red")
ax2.set_ylim(0, 70)  # Adjust for better visualization

# Add legends for both plots
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper center", title="Legend", ncol=2)

# Tight layout and show the plot
plt.tight_layout()
plt.show()
