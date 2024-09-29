"""Using metric units"""

import physical_activities_table


def calculate_bmi(weight, height, age) -> float:
    """Calculates the Body Mass Index (BMI)."""
    bmi = weight / height**2
    """Adjust BMI based on person's age."""
    age = age
    if age >= 65:
        bmi *= 1.1
    elif age < 18:
        bmi *= 0.95
    return round(bmi, 2)


def calculate_calories_burned(weight, duration, physical_activity_type) -> float:
    def MET_number_index(x, y, physical_activity_type):
        MET_number_list = []
        z = 1    
        while x < y:
            MET_number_list.append(physical_activity_type[x])
            x += z
        return MET_number_list
    
    start = physical_activity_type.find("~")
    end = len(physical_activity_type)
    x = start + 1
    y = end
    MET_number_list = MET_number_index(x, y, physical_activity_type)
    MET_number_string = ''.join(MET_number_list)
    MET_number = float(MET_number_string)

    calories_burned = MET_number * 3.5 * weight / 200
    return round(calories_burned, 2)


def filter_people_status(people_data) -> dict:
    anorexic_people = []
    underweight_people = []
    ideal_range_people = []
    marginally_overweight_people = []
    overweight_people = []
    obese_people = []
    person_gender = ""
    person_weight = ""
    person_height = ""
    for person in people_data:
        person_gender = person["gender"]
        person_weight = person["weight"]
        person_height = person["height"]
        person_age = person['age']
        bmi = calculate_bmi(person_weight, person_height, person_age)
        
        if person_gender == "f":
            if bmi <= 17.50:
                anorexic_people.append(person)
            elif bmi <= 19.10:
                underweight_people.append(person)
            elif bmi <= 25.80:
                ideal_range_people.append(person)
            elif bmi <= 27.30:
                marginally_overweight_people.append(person)
            elif bmi <= 32.30:
                overweight_people.append(person)
            elif bmi > 32.30:
                obese_people.append(person)
        elif person_gender == "m":
            if bmi <= 17.50:
                anorexic_people.append(person)
            elif bmi <= 20.70:
                underweight_people.append(person)
            elif bmi <= 26.40:
                ideal_range_people.append(person)
            elif bmi <= 27.80:
                marginally_overweight_people.append(person)
            elif bmi <= 31.10:
                overweight_people.append(person)
            elif bmi > 31.10:
                obese_people.append(person)
    
    people_status_dict = {
    'anorexic_people': anorexic_people,
    'underweight_people': underweight_people,
    'ideal_range_people': ideal_range_people,
    'marginally_overweight_people': marginally_overweight_people,
    'overweight_people': overweight_people,
    'obese_people': obese_people
    }
    return people_status_dict


def fitness_analysis(people_data) -> None:
    print("\nFitness Analysis:")
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'], person['age'])
        calories_burned = calculate_calories_burned(person['weight'], person['duration'], person['physical_activity_type'])
        print(f"{person['name']}: BMI = {bmi}, Calories burned = {calories_burned}")
    
    people_status_dict = filter_people_status(people_data)
    
    anorexic_people = people_status_dict['anorexic_people']
    underweight_people = people_status_dict['underweight_people']
    ideal_range_people = people_status_dict['ideal_range_people']
    marginally_overweight_people = people_status_dict['marginally_overweight_people']
    overweight_people = people_status_dict['overweight_people']
    obese_people = people_status_dict['obese_people']
    
    print("\nAnorexic people:")
    for person in anorexic_people:
        bmi = calculate_bmi(person['weight'], person['height'], person['age'])
        print(f"{person['name']}: BMI = {bmi}")
        
    print("\nUnderweight people:")
    for person in underweight_people:
        bmi = calculate_bmi(person['weight'], person['height'], person['age'])
        print(f"{person['name']}: BMI = {bmi}")
    
    print("\nIdeal range people:")
    for person in ideal_range_people:
        bmi = calculate_bmi(person['weight'], person['height'], person['age'])
        print(f"{person['name']}: BMI = {bmi}")

    print("\nMarginally overweight people:")
    for person in marginally_overweight_people:
        bmi = calculate_bmi(person['weight'], person['height'], person['age'])
        print(f"{person['name']}: BMI = {bmi}")

    print("\nOverweight people:")
    for person in overweight_people:
        bmi = calculate_bmi(person['weight'], person['height'], person['age'])
        print(f"{person['name']}: BMI = {bmi}")
        
    print("\nObese people:")
    for person in obese_people:
        bmi = calculate_bmi(person['weight'], person['height'], person['age'])
        print(f"{person['name']}: BMI = {bmi}")


def main():
    people_data = []

    print("Enter fitness data for each person (Enter a blank name to finish): ")
    while True:
        name = input("Enter person's name: ").strip()
        if not name:
            break
        
        
        """Gender verification"""
        while True:
            gender = input("Enter person's gender (m - male or f - female): ")
            if gender == "f" or gender == "m":
                break
            print("Invalid")
            
        
        """Age verification"""
        while True:
            age = int(input("Enter person's age: "))
            if age in range(1, 131):
                break
            print("Invalid")
            
            
        """Weight verification"""
        while True:
            weight = int(input("Enter person's weight in kilograms: "))
            if weight in range(1, 635):
                break
            print("Invalid")

    
        """Height verification""" 
        def valid_heights(min_height, max_height, height_step): # IMPORTANT: This function deals with Python's
            allowed_heights = []                                #            inabillity to use floats in for loop
            x = min_height
            y = max_height
            z = height_step
            x1 = f"{x:.2f}"    
            while x < y:
                allowed_heights.append(x1)
                x += z
                x1 = f"{x:.2f}"    
            return allowed_heights

        min_height = 0.50
        max_height = 2.81
        height_step = 0.01
        valid_heights_list = valid_heights(min_height, max_height, height_step)

        while True:
            height = input("Enter person's height in meters: ") 
            if height in valid_heights_list:
                height = float(height)
                break    
            print("Invalid")

    
        """Physical activities verification"""
        range_of_total_activities = physical_activities_table.physical_activities_table()
        while True:
            activity_index = int(input("Choose activity number from table of physical activities: "))
            if activity_index in range(len(range_of_total_activities)):
                physical_activity_type = range_of_total_activities[activity_index-1]
                break
            print("Invalid")
     
    
        """Exercise duration verification"""
        while True:
            duration = int(input("Enter exercise duration in minutes: "))
            if duration in range(1, 121):
                break
            elif duration in range(121, 181):
                print("Exercise duration is too high, beware of possible injuries!")
                break
            else:
                print("Number too high. Enter lower number.")
    
        person = {'name': name, 'gender': gender, 'age': age, 'weight': weight, 'height': height,
                  'physical_activity_type': physical_activity_type, 'duration': duration}
        people_data.append(person)
        
    fitness_analysis(people_data)

if __name__ == '__main__':
    main()
