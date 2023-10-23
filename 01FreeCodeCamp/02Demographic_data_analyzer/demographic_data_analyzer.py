import pandas as pd



def demographic_data_analysis():
    # Load the dataset
    data = pd.read_csv('census_data.csv')  # Replace with the actual file name
    
    df = pd.DataFrame(data)

    # 1. Count of people of each race
    race_count = data['race'].value_counts()

    # 2. Average age of men
    average_age_men = data[data['sex'] == 'Male']['age'].mean()

    # 3. Percentage of people with a Bachelor's degree
    percentage_bachelors = (len(data[data['education'] == 'Bachelors']) / len(data)) * 100

    # 4. Percentage of people with advanced education making more than 50K
    advanced_education = data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = len(advanced_education[advanced_education['salary'] == '>50K']) / len(advanced_education) * 100

    # Filter for individuals without advanced education
    without_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Calculate the percentage with salary > 50K
    percentage_high_income_no_advanced_edu = (len(without_advanced_education[without_advanced_education['salary'] == '>50K']) / len(without_advanced_education)) * 100

    min_hours_per_week = df['hours-per-week'].min()
    
    min_hours_workers = df[df['hours-per-week'] == min_hours_per_week]
    percentage_high_income_min_hours = (len(min_hours_workers[min_hours_workers['salary'] == '>50K']) / len(min_hours_workers)) * 100


    # Group by 'native-country' and calculate the percentage of people earning >50K
    percentage_high_income_by_country = df[df['salary'] == '>50K'].groupby('native-country')['salary'].count() / df.groupby('native-country')['salary'].count() * 100

    # Find the country with the highest percentage of people earning >50K
    highest_percentage_country = percentage_high_income_by_country.idxmax()
    highest_percentage = percentage_high_income_by_country.max()
    
    
    # Filter for individuals who earn more than 50K
    high_income_earners = df[df['salary'] == '>50K']

    # Further filter for individuals from India
    high_income_earners_india = high_income_earners[high_income_earners['native-country'] == 'India']

    # Find the most common occupation
    most_popular_occupation_india = high_income_earners_india['occupation'].mode()[0]

    
    print(f"""
          Race Count            : {race_count} '\n'
          Average age of man    : {average_age_men} '\n'
          Percentage Bachelors  : {percentage_bachelors} '\n'
          Higher Education Rich : {higher_education_rich} '\n'
          Percentage of without advance education : {percentage_high_income_no_advanced_edu: .1f}% '\n',
          min_hours_per_week : {min_hours_per_week} '\n'
          High income in min hours : {percentage_high_income_min_hours: .1f}% '\n'
          Highest percentage country is {highest_percentage_country} and the max is {highest_percentage:.1f}% '\n'
          Most Popular occupation : {most_popular_occupation_india}
                 
          """)



