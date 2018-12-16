from sklearn.externals import joblib
import numpy as np

def setupMenu():
    print('Flight Delay Calculator')
    print('-----------------------')
    print()
    print('1. Calculate Delay.')
    print("2. Calculate amount of flights needed for one to be delayed.")
    print('3. Stop.')
    print()
    return getInput()


def getModel():
    print("Loading model...")
    clf = joblib.load('modeldump.pkl') 
    return clf

def getAirportMapping():
    airport_mapping = np.load("airport_mapping.npy").item()
    return airport_mapping


def getInput():
    invoer = int(input('Invoer: '))
    while invoer < 1 or invoer > 3:
        print('fout')
        invoer = int(input('invoer '))
    return invoer


def predictFlight(clf, airport_mapping):
    airline_code = int(input("Airline Code: "))
    departure_airport = input("Departure Airport: ")
    arrival_airport = input("Arrival Airport: ")
    departure_schedule_hour = int(input("Departure hour: "))
    arrival_schedule_hour = int(input("Arrival hour: "))

    for i in airport_mapping:
        if i == departure_airport:
            departure_airport_int = airport_mapping[i]
    
    for i in airport_mapping:
        if i == arrival_airport:
            arrival_airport_int = airport_mapping[i]

    flight = [airline_code, departure_schedule_hour,
              arrival_schedule_hour, departure_airport_int, arrival_airport_int]
    y_new = clf.predict([flight])

    if (y_new[0] == False):
        print("Your flight will not be delayed.")
    else :
        print("Your flight will be delayed.")
    return

def generateRandomFlight():
    airline_code = [20355, 19704, 19977, 19790, 19393, 20436, 20366,
                20437, 20304, 19805, 20378, 20398, 19930, 20409, 19690, 21171, 20374]
    airports = list(range(1, 161))
    flight = [np.random.choice(airline_code), np.random.choice(list(range(25))), np.random.choice(list(range(
                25))), np.random.choice(airports), np.random.choice(airports)]
    return flight


def predictListOfFlights(clf, amount):
    y_new = clf.predict([generateRandomFlight()])
    aantal_pos = 0
    for i in range(amount):
        if y_new[0]:
            aantal_pos += 1
        y_new = clf.predict([generateRandomFlight()])
    print(str(round((aantal_pos / amount) * 100, 2)) + " percent of flights were delayed.")
    return 


def main():
    clf = getModel()
    airport_mapping = getAirportMapping()
    invoer = setupMenu()
    if invoer == 1:
        predictFlight(clf, airport_mapping)
    elif invoer == 2:
        amount = int(input("Give amount of test flights: "))
        predictListOfFlights(clf, amount)
    return


if __name__ == '__main__':
    main()
