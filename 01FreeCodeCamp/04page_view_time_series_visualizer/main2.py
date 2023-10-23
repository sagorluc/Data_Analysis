from main import import_data, clean_data, draw_line_plot, draw_bar_plot, draw_box_plot

# Task 1
df = import_data()
print(df)

# Task 2
df_cleaned = clean_data(df.copy())
print(df_cleaned)

# Task 3
line_plot = draw_line_plot(df_cleaned.copy())
print(line_plot)

# Task 4
bar_plot = draw_bar_plot(df_cleaned.copy())
print(bar_plot)

# Task 5
box_plot = draw_box_plot(df_cleaned.copy())
print(box_plot)