import math

class PlaneSeatingChart:

    def __init__(self):
        self.occupied_seats = [False] * 1023
    
    def update_seat(self, seat_path):
        start = {
            'row_start': 0,
            'row_end': 127,
            'col_start': 0,
            'col_end': 7,
        }

        for step in seat_path:
            # lower half of row
            if step == 'F':
                start['row_end'] = math.floor((start['row_end'] + start['row_start']) / 2)
            # upper half of row
            elif step == 'B':
                start['row_start'] = math.ceil((start['row_end'] + start['row_start']) / 2)
            # lower half of row
            elif step == 'L':
                start['col_end'] = math.floor((start['col_end'] + start['col_start']) / 2)
            # upper half of row
            elif step == 'R':
                start['col_start'] = math.ceil((start['col_end'] + start['col_start']) / 2)

        self.occupied_seats[start['row_start'] * 8 + start['col_start']] = True

    def find_empty_seat(self):
        for idx, seat_id in enumerate(self.occupied_seats):
            if idx == 0 or idx == len(self.occupied_seats) - 1:
                continue
            if not self.occupied_seats[idx-1] or not self.occupied_seats[idx+1]:
                continue
            if self.occupied_seats[idx]:
                continue
            else:
                return idx

if __name__ == '__main__':
    binary_seats = None
    with open('Day_5_input.txt', 'r') as f:
        seat_paths = f.read().splitlines()
    plane_seating_chart = PlaneSeatingChart()
    for seat_path in seat_paths:
        plane_seating_chart.update_seat(seat_path)

    print(plane_seating_chart.find_empty_seat())
