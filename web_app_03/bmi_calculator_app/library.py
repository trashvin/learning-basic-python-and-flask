def compute_bmi(weight, height):
    return round(weight/((height/100) ** 2),2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return 'underweight'
    elif bmi >=18.5 and bmi <=24.9:
        return 'healthy'
    elif bmi >= 25.0 and bmi <= 29.9:
        return 'overweight'
    else:
        return 'obese'