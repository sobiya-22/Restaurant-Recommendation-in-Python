import tkinter as tk
from tkinter import ttk
import pandas as pd


class RestaurantRecommendationApp:
    def __init__(self, master, excel_file_path):
        self.master = master
        master.title("Restaurant Recommendation App")


        # Reading the Excel file and displaying the suitable data
        self.df = pd.read_excel(r'C:\Users\ASUS\Documents\Main_RestroNsk_data_new.xlsx')

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 14))

        # Creating the main frame
        main_frame = ttk.Frame(master)
        main_frame.place(relwidth=0.8, relheight=1, relx=0.3, rely=0.3)

        # #Background Image on the first interface


        # Buttons on the first interface
        button1 = ttk.Button(main_frame, text="Recommend popular by location", command=self.recommend_by_location, )
        button2 = ttk.Button(main_frame, text="Recommend popular by dish", command=self.recommend_by_dish)
        button3 = ttk.Button(main_frame, text="Recommend most popular restaurant",
                             command=self.recommend_popular_restaurant)
        button4 = ttk.Button(main_frame, text="Recommend best cafes in Nashik", command=self.recommend_best_cafes)

        # Styling of the buttons
        button1.grid(row=0, column=0, pady=20)
        button2.grid(row=1, column=0, pady=20)
        button3.grid(row=2, column=0, pady=20)
        button4.grid(row=3, column=0, pady=20)

    def open_new_window(self, title, columns, data, background_image_path):
        new_window = tk.Toplevel(self.master)
        new_window.title(title)

        # Adding a bg image to the sub-windows
        background_image = tk.PhotoImage(file=background_image_path)
        background_label = tk.Label(new_window, image=background_image)
        background_label.photo = background_image
        background_label.place(relwidth=1, relheight=1)

        # Create Treeview
        tree = ttk.Treeview(new_window, columns=columns, show='headings')

        # Adding columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor='center')  # Adjust the width as needed

        # Inserting data row by row
        for row in data:
            tree.insert('', 'end', values=row)

        # Center the text in each cell
        for col in columns:
            tree.heading(col, text=col, anchor='center')
            tree.column(col, anchor='center')

        # Set the scrollbars
        y_scrollbar = ttk.Scrollbar(new_window, orient="vertical", command=tree.yview)
        y_scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=y_scrollbar.set)

        x_scrollbar = ttk.Scrollbar(new_window, orient="horizontal", command=tree.xview)
        x_scrollbar.pack(side="bottom", fill="x")
        tree.configure(xscrollcommand=x_scrollbar.set)

        # Update the window to get the correct geometry information
        new_window.update()

        # Calculate the center position for the table
        screen_width = new_window.winfo_screenwidth()
        screen_height = new_window.winfo_screenheight()
        table_width = 800  # Set your desired width
        table_height = 600  # Set your desired height

        x_position = (screen_width - table_width) // 2
        y_position = (screen_height - table_height) // 2

        # Place the treeview in the center of the subwindow
        tree.place(relx=0.5, rely=0.5, anchor='center')

        # Center the window on the screen
        new_window.geometry(f"{table_width}x{table_height}+{x_position}+{y_position}")

    def recommend_by_location(self):
        columns = ['Location', 'Restaurant']
        location_data = self.df[columns].values.tolist()
        background_image_path = r'C:\Users\ASUS\Pictures\Screenshots\Screenshot 2023-11-24 083557.png'
        self.open_new_window("Recommendation by Location", columns, location_data, background_image_path)

    def recommend_by_dish(self):
        columns = ['Dish', 'Popularity','Restaurant', 'Location']
        dish_data = self.df[columns].values.tolist()
        background_image_path = r'C:\Users\ASUS\Pictures\Screenshots\Screenshot 2023-11-24 083715.png'
        self.open_new_window("Recommendation by Dish", columns, dish_data, background_image_path)

    def recommend_popular_restaurant(self):
        columns = ['Restaurant', 'Popularity', 'Location']
        popular_data = self.df[self.df['Popularity'] >= 4][columns].values.tolist()
        background_image_path = r'C:\Users\ASUS\Pictures\Screenshots\Screenshot 2023-11-24 083816.png'
        self.open_new_window("Popular Restaurant Recommendation", columns, popular_data, background_image_path)

    def recommend_best_cafes(self):
        columns = ['Restaurant', 'Location']
        cafes_data = self.df[self.df['Dish'] == 'Cafe'][columns].values.tolist()
        background_image_path = r'C:\Users\ASUS\Pictures\Screenshots\Screenshot 2023-11-24 103414.png'
        self.open_new_window("Best Cafes in Nashik", columns, cafes_data, background_image_path)


if __name__ == "__main__":
    excel_file_path = r'C:\Users\ASUS\Documents\Main_RestroNsk_data_new.xlsx'

    root = tk.Tk()
    app = RestaurantRecommendationApp(root, excel_file_path)
    root.geometry("800x600")
    root.mainloop()
