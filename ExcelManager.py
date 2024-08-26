import xlwings as xw

class ExcelManager:
    def __init__(self, path):
        self.path = path
        self.wb = xw.Book(path)
        self.ws = self.wb.sheets['Sheet1']
        self.values_dict = self.load_data()

    def load_data(self):
        # Define the used range
        used_range = self.ws.range("A1:AC112")
        values = used_range.value
        
        # Create a dictionary to store cell positions for fast lookup
        values_dict = {}
        for i in range(len(values)):
            for j in range(len(values[i])):
                cell_value = values[i][j]
                if cell_value not in values_dict:
                    values_dict[cell_value] = []
                values_dict[cell_value].append((i + 1, j + 1))
        
        return values_dict

    def mark_drafted_player(self, drafted_player, is_mine):
        # Define the fill color
        fill_color = (0, 255, 0) if is_mine else (255, 0, 0)  # Green for is_mine=True, Red for is_mine=False
        
        # Debugging: Print the drafted player and fill color
        print(f"Drafted player: {drafted_player}")
        print(f"Fill color: {fill_color}")

        # Get cell positions for the drafted player
        if drafted_player in self.values_dict:
            position = self.values_dict[drafted_player]
            
            # Set the fill color for the corresponding cells
            cell = self.ws.range(position[0])
            cell.color = fill_color

        # Save the changes
        self.wb.save()
