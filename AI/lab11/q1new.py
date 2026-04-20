# GUJARAT MAP COLORING (CSP)


# Colors available
colors = ["Red", "Green", "Blue", "Yellow"]

# Districts (variables)
districts = [
    "Kutch", "Banaskantha", "Patan", "Mehsana", "Sabarkantha",
    "Gandhinagar", "Ahmedabad", "Surendranagar", "Rajkot",
    "Jamnagar", "Porbandar", "Junagadh", "Amreli", "Bhavnagar",
    "Anand", "Kheda", "Vadodara", "Panchmahal", "Dahod",
    "Bharuch", "Narmada", "Surat", "Navsari", "Valsad", "Dang"
]

# Adjacency list (constraints)
neighbors = {
    "Kutch": ["Banaskantha", "Surendranagar"],
    "Banaskantha": ["Kutch", "Patan", "Sabarkantha"],
    "Patan": ["Banaskantha", "Mehsana"],
    "Mehsana": ["Patan", "Gandhinagar", "Ahmedabad", "Sabarkantha"],
    "Sabarkantha": ["Banaskantha", "Mehsana", "Gandhinagar"],
    "Gandhinagar": ["Sabarkantha", "Mehsana", "Ahmedabad", "Kheda"],
    "Ahmedabad": ["Mehsana", "Gandhinagar", "Kheda", "Anand", "Surendranagar"],
    "Surendranagar": ["Kutch", "Ahmedabad", "Rajkot", "Bhavnagar"],
    "Rajkot": ["Surendranagar", "Jamnagar", "Junagadh", "Amreli"],
    "Jamnagar": ["Rajkot", "Porbandar"],
    "Porbandar": ["Jamnagar", "Junagadh"],
    "Junagadh": ["Rajkot", "Porbandar", "Amreli"],
    "Amreli": ["Rajkot", "Junagadh", "Bhavnagar"],
    "Bhavnagar": ["Surendranagar", "Amreli", "Anand"],
    "Anand": ["Ahmedabad", "Kheda", "Vadodara", "Bhavnagar"],
    "Kheda": ["Ahmedabad", "Gandhinagar", "Anand", "Vadodara"],
    "Vadodara": ["Kheda", "Anand", "Panchmahal", "Bharuch", "Narmada"],
    "Panchmahal": ["Vadodara", "Dahod"],
    "Dahod": ["Panchmahal"],
    "Bharuch": ["Vadodara", "Narmada", "Surat"],
    "Narmada": ["Vadodara", "Bharuch", "Surat"],
    "Surat": ["Bharuch", "Narmada", "Navsari"],
    "Navsari": ["Surat", "Valsad", "Dang"],
    "Valsad": ["Navsari", "Dang"],
    "Dang": ["Navsari", "Valsad"]
}


# CHECK CONSTRAINT

def is_valid(district, color, assignment):
    for neighbor in neighbors[district]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


# BACKTRACKING ALGORITHM

def backtrack(assignment, available_colors):
    # If all districts assigned → solution found
    if len(assignment) == len(districts):
        return assignment

    # Select unassigned district
    unassigned = [d for d in districts if d not in assignment]
    current = unassigned[0]

    # Try all colors
    for color in available_colors:
        if is_valid(current, color, assignment):
            assignment[current] = color

            result = backtrack(assignment, available_colors)
            if result:
                return result

            # Backtrack
            del assignment[current]

    return None

# RUN CSP

def find_chromatic_number():
    for i in range(1, len(colors) + 1):
        
        
        # Try to find a solution with i colors
        solution = backtrack({}, colors[:i])
        
        if solution:
            print(f"Solution found with {i} colors.")
            print(f"The chromatic number is {i}.\n")
            for district in sorted(solution):
                print(f"{district}: {solution[district]}")
            return
    
    print("No solution found with the given colors.")

find_chromatic_number()