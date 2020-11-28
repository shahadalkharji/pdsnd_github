import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #  get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # The user will input one of the specified cities in the question, if an invalid input is entered the user will be asked to enter a valid input.
    cities = ['chicago','new york city','washington']
    city= input('Please select a city (Chicago, New York City, Washington): ')
    while city.lower() not in cities:
        city= input('Wrong selection! Please select a city (Chicago, New York City, Washington): ')


    #  get user input for month (all, january, february, ... , june)
    # The user will input one of the specified months in the question, if an invalid input is entered the user will be asked to enter a valid input.
    months=['all','january','february', 'march', 'april', 'may', 'june']
    month=input('Please select a month (all, january, february, march, april, may, june): ')
    while month.lower() not in months:
        month = input('Wrong selection! Please select a month (all, Jan, Jan, Feb, Mar, Apr, May, Jun): ')

    #get user input for day of week (all, monday, tuesday, ... sunday)
    # The user will input one of the specified day in the question, if an invalid input is entered the user will be asked to enter a valid day.
    days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day=input('Please select a day (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ')
    while day.lower() not in days:
        day= input('Wrong selection! Please select a day (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ')

    print('-'*40)
    return city.lower(),month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
    if day != 'all':
       df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    # Display time statistics
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Display the most common month.
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The most common month is: ' + str(common_month))
    #Display the most common day of week.
    df['day'] = df['Start Time'].dt.weekday_name
    common_day = df['day'].mode()[0]
    print('The most common day is: ' + common_day)
    #Display the most common start hour.
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is: ' + str(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    #Display most commonly used start station.
    start_station=df['Start Station'].mode()[0]
    print('The most commonly used start station is: ' + start_station)
    #Display most commonly used end station.
    end_station=df['End Station'].mode()[0]
    print('The most commonly used end station is: ' + end_station)
    #Display most frequent combination of start station and end station trip.
    combination_trip= (df['Start Station']+' and '+df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station trip: ' + combination_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    #Display trip duration statistics
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: ' + str(total_travel_time))
    #display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time is: ' + str(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The user types are: ' + str(user_types))
    if city == 'chicago' or city == 'new york city':
    # Display counts of gender
        gender = df['Gender'].value_counts()
        print('The gender counts are: ' + str(gender))
    # Display earliest, most recent, and most common year of birth
        earliest = min(df['Birth Year'])
        recent = max(df['Birth Year'])
        common_year_of_birth = (df['Birth Year'].value_counts()).head(1)
        print('The earliest year of birth is: ' + str(earliest))
        print('The most recent year of birth is: ' + str(recent))
        print('The most common year of birth is: ' + str(common_year_of_birth))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display(city):

    ## This function displays rows each time the user chooses to display raw data.
    count = 1
    df = pd.read_csv(CITY_DATA[city])
    options=['yes','no']
    display_raw_data= input('Would you like to display 5 lines of raw data? (Yes/No) ? ')
    while display_raw_data.lower() not in options:
        display_raw_data= input('Invalid input! Would you like to display raw data? (Yes/No) ? ')

    if display_raw_data.lower() == 'yes':
        while True:
            print('Data: \n')
            print(df.head(5*count))
            count+=1
            display_raw_data= input('Would you like to display 5 more lines of raw data (Yes/No) ? ')
            while display_raw_data.lower() not in options:
                display_raw_data= input('Invalid input! Would you like to display raw data (Yes/No) ? ')
            if display_raw_data.lower() != 'yes':
                return
    else:
        return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display(city)

        options=['yes','no']
        restart = input('Would you like to restart (Yes/No) ? ')
        while restart.lower() not in options:
            restart = input('Inavlid input! Would you like to restart (Yes/No) ? ')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
