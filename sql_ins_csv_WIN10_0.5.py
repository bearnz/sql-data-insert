"""
    csv->SQL database insertion script v0.4
    
    USE THIS SCRIPT FOR INPUT OF .csv FILES ON WINDOWS
    
    Press run and follow the instructions onscreen
    v0.4 changes:
        -added warning about commas in data
    
"""

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def data(source, target):
    file = open("output.sql", 'w')
    data = open(source + ".csv", 'r');
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
        file.write("insert into " + target +  " values(" + SQL_line + ");\n")
        
def main():
    #These print statements could be commented out in future once you know how to run this script
    print("Your data is assumed to be in .csv format and not contain any commas")
    print("Enter the filename of your data minus the extension:")
    source_data = input()
    print("Enter the name of your target database:")
    target = input()
    print("Your converted code is in output.sql in this directory")
    data(source_data, target)
    
if __name__ == "__main__":
    main()
    
main()
