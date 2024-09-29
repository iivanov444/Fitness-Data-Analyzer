"""
Here you can add, remove and delete physical activitites.
Important: Not following the naming convention will break the main program!
/Unless the main program is modified to new naming convention from
calculate_calories_burned function (lines 28 and 29)/
'number. Physical activity (additional info /optional/) -> MET~number'
Example: '10. Jogging (9.0 km/h) -> MET~8.8'
"""


def physical_activities_table() -> list:
    light_intensity_activities = [    # MET < 3
    '1. Writing, desk work, using computer -> MET~1.5',
    '2. Walking slowly -> MET~2.0',
    '3. Stretching/yoga -> MET~2.5',
    '4. Home activities (cleaning, dusting, straightening up,\nchanging linen, carrying out the trash) -> MET~2.5'
    ]
    moderate_intensity_activities = [    # 3 >= MET < 6
    '5. Walking (5 km/h) -> MET~3.0',
    '6. Sweeping or mopping floors, vacuuming carpets -> MET~3.3',
    '7. Yoga session with asanas and pranayama -> MET~3.3',
    '8. Tennis doubles -> MET~5.0',
    '9. Weight lifting (moderate intensity) -> MET~5.0',
    '10. Sexual activity -> MET~5.8'
    ]
    vigorous_intensity_activities = [    # MET >= 6
    '11. Aerobic dancing, medium effort -> MET~6.0',
    '12. Bicycling (on flat, 16–19 km/h, light effort) -> MET~6.0',
    '13. Jumping jacks -> MET~6.0',
    '14. Swimming laps (freestyle, slow, moderate, or light effort) -> MET~7.0',
    '15. Sun salutation (Surya Namaskar, vigorous with transition jumps) -> MET~7.4',
    '16. Basketball game -> MET~8.0',
    '17. Running (8 km/h) -> MET~8.8',
    '18. Jogging (9 km/h) -> MET~8.8',
    '19. Rope jumping (66/min) -> MET~9.8',
    '20. Football -> MET~10.3',
    '21. Rope jumping (84/min) -> MET~10.5',
    '22. Rope jumping (100/min) -> MET~11.0',
    '23. Jogging (11 km/h) -> MET~11.3',
    '24. Boxing -> MET~12.0'
    ]
    
    print("MET = Metabolic Equivalent of Task")
    print("Table of physical activities:")
    print("\nLight-intensity activities, MET < 3:")
    for activity_index in light_intensity_activities:
        print(activity_index)
    print("\nModerate-intensity activities, 3 <= MET < 6:")
    for activity_index in moderate_intensity_activities:
        print(activity_index)
    print("\nVigorous-intensity activities, MET >= 6:")
    for activity_index in vigorous_intensity_activities:
        print(activity_index)
        
    total_activities = light_intensity_activities + moderate_intensity_activities + vigorous_intensity_activities
    return total_activities