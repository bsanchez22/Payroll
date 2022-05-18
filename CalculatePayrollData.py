import sys

#I start by defining a class that organizes my methods
#In the methods, self is a parameter that refers to
#the specific object that invokes or calls the method
class employee:

       #This is a constructor
       # This is the method that's 
       # called when you construct objects.
       def __init__(self, name=' ',hours=0,rate=0):
           self.name = name
           self.hours = hours
           self.rate = rate
 
       # This method assigns a value 
       # to the instance variable name,
       # hours, and rate.
       # This is a setter or mutator
       def set_name(self, name):
           self.name = name
       def set_hours(self, hours):
           if hours > 0:
            self.hours = hours

       def set_rate(self, rate):
           if rate > 0 :
            self.rate = rate


       # This method returns the value 
       # of the instance variable name,
       # hours, rate.
       # It must be set first.
       # This is a getter or accessor.
       def get_name(self):
           return self.name
       def get_hours(self):
           return self.hours
       def get_rate(self):
           return self.rate

       #This prints out the users information
       def get_input(self):
                #I set up a try and except for human input error
                #for name, hours, and rate

                class AutomaticZeroHours(ValueError):
                    pass
                class AutomaticZeroRate(ValueError):
                    pass

                while True:
                    try:
                        emergency_exit = print("\nPress Enter Twice To exit at anytime")

                        name = input("\nEnter a name: ")
                        self.set_name(name)


                        hours = float(input("Enter hours worked: "))
                        self.set_hours(hours)
                        if hours <= 0:
                            raise AutomaticZeroHours

                        rate = float(input("Enter hourly rate: "))
                        self.set_rate(rate)
                        if rate <= 0:
                            raise AutomaticZeroRate

                        if name == "":
                            raise ValueError

                        else:
                            break

                    except AutomaticZeroHours as hr:
                        print("You entered a 0, if employees hour <=0, no need to enter data")
                        print(hr)
                        break
                    except AutomaticZeroRate as rt:
                        print("You entered a 0, if employees rate <=0, no need to enter data")
                        print(rt)
                        break
                    except ValueError as ve:
                        print("either your Name, hours, or rate are incorrect, please try again.\n")
                        print(ve)
                        break

       def calc_pay(self):
           
            #This function returns a float
            if self.hours <= 40:

                return self.hours * self.rate

            else:

                return ((self.hours - 40) * (1.5 * self.rate)) + (self.rate * 40)
         
def main():

    #This prints the Title
    print("*"*80 + "\n\t\t\tEmployee Data Entry Application\n" + "*"*80)

    #This lets the user decide to input data or quitapplication
    grouping_employees = []
    start_up = input("1: Enter an employee \nq: Quit the application\n")
    if start_up == '1':
        #This is instantiation
        #emp is an instance of 
        #the employee class
        emp = employee()

        # Here we are calling the instance method named get_input
        # on the employee object named emp.
        emp.get_input()

        grouping_employees.append(emp)
        # I use this for loop to
        # eliminate the inputs who have zero hours
        # or 0 rates
        for i in grouping_employees:

            if i.get_name() == "":
                grouping_employees.pop()

            elif i.get_hours() == 0:
                grouping_employees.pop()

            elif i.get_rate() == 0:
                grouping_employees.pop()

    else:
        start_up.lower()
        sys.exit(print("\nNo data was entered, Good-bye"))



    #This while True loop will continue until the user quits the application
    #Inside I give them the option to enter employee data, print the current 
    #data they had inputted, or quit the application
    while True:

        user_options = input("\n1: Enter an employee \n2: Print employee list \nq: Quit the application\n")
        if user_options == '1':
            emp = employee()
            emp.get_input()
            grouping_employees.append(emp)

            #I use this for loop to
            #eliminate the inputs who have zero hours
            #or 0 rates
            for i in grouping_employees:
                if i.get_name() == "":
                    grouping_employees.pop()
                elif i.get_hours() == 0:
                    grouping_employees.pop()

                elif i.get_rate() == 0:
                    grouping_employees.pop()


        elif user_options == '2':
            #This inner if/else statement
            #Instructs the user that their
            #has been no data saved or
            #it shows data that has been saved.
            if len(grouping_employees) == 0:
                print("\nNo data has been entered yet. Try again or exit the program")
            else:
                # We call the get_name, get_hours, and get_rate
                # method to get the value of the instance
                # variable name, hours, and rate.
                for i in grouping_employees:
                    print("\nName: " + " " * 23 + "{}".format(i.get_name()))
                    print("Hours Worked: " + " " * 15 + "{}".format(i.get_hours()))
                    print("Hourly Rate: " + " " * 16 + "${}".format(i.get_rate()))



        else:
            user_options.lower()
            break

    #This section prints the Total amount that has been paid for every employee
    #It also prints the average spent per employee
    #This will only print if the previous while loop is broken
    total_amount = 0

    for employees in grouping_employees:
        total_amount +=employees.calc_pay()

    if len(grouping_employees) == 0:
        print("\nNo Employees Entered")
        print("The total amount to be paid is ${:,.2f}".format(total_amount))
        print("The average employee is paid ${:,.2f}".format(0))

    else:
        print("\nThe total amount to be paid is ${:,.2f}".format(total_amount))
        print("The average employee is paid ${:,.2f}".format(total_amount/len(grouping_employees)))

    print("\nGood-bye")

main()
