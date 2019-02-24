"""
    Bear's shitty csv->SQL database insertion script v0.4
    Press run and follow the instructions onscreen
    v0.4 changes:
        -added warning about commas in data
        -initial git commit
    
"""

def isInt(s):
    #Stole this function off the internet whoops
    #This techinically works with any number type and as long as it's also
    #a valid number type in the sql table then there shouldn't be
    #any issues with it (floats, doubles etc)
    try: 
        int(s)
        return True
    except ValueError:
        return False

def data(source, target):
    file = open("output.sql", 'w')
    data = open(source + ".txt", 'r');
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
    print("Your data is assumed to be in .txt format and not contain any commas")
    print("Enter the filename of your data minus the extension:")
    source_data = input()
    print("Enter the name of your target database:")
    target = input()
    print("Your converted code is in output.sql in this directory")
    data(source_data, target)
    
main()