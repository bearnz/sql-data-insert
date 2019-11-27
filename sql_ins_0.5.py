"""
    Bear's shitty csv->SQL database insertion script v0.5
    Press run and follow the instructions onscreen
    0.5 changes:
    Modified for linux terminal usage:
        - cd Desktop
        - python3 sql_ins_0.5.py
    -readded .sql file creation
        - @output.sql in MySQL
    
"""

def isInt(s):
    #Checks whether inputted string is valid int
    try: 
        int(s)
        return True
    except ValueError:
        return False

def data(source, target):
    data = open(source + ".csv", 'r');
    output = open("output.sql", 'w+');
    lines = data.read().splitlines();
    for i in range(len(lines)):
        line = lines[i].split(",")
        SQL_line = "";        
        for j in range(len(line)):
    
            if isInt(line[j]) or line[j] == "null":
                SQL_line += (str(line[j])+",")
            else:
                SQL_line += ("\'" + line[j] + "\',")
        SQL_line = SQL_line[:-1]
        output.write("insert into " + target +  " values(" + SQL_line + "); \n")
    output.close()
    
if __name__ == "__main__":
    main()
    
def main():
    #These print statements could be commented out in future once you know how to run this script
    print("Your data is assumed to be in .csv format")
    print("Enter the filename of your data minus the extension:")
    source_data = input()
    print("Enter the name of your target database:")
    target = input()
    data(source_data, target)
    
main()
