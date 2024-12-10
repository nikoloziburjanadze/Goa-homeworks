def human_years_cat_years_dog_years(humanYears):
   
    if humanYears == 1:
        return [humanYears, 15, 15]
    elif humanYears == 2:
        return [humanYears, 15 + 9, 15 + 9]
 
    catYears = 15 + 9 + (humanYears - 2) * 4
    dogYears = 15 + 9 + (humanYears - 2) * 5
    
    return [humanYears, catYears, dogYears]