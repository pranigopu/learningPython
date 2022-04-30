def bpStage(systolic, diastolic):
    if systolic > 180 or diastolic > 120:   return "Hypertensive Crisis"
    if systolic >= 140 or diastolic >= 90:  return "High Blood Pressure - Stage 2"
    if systolic >= 130 or diastolic >= 80:  return "High Blood Pressure - Stage 1"
    if systolic >= 120 and diastolic < 80:  return "Elevated"
    if systolic < 120 and diastolic < 80:   return "Normal"

def listifyData(line):
    i = 0
    max = len(line) - 1
    processedData = []
    while i < max:
        myString = str()
        while i < max and line[i].isspace(): i = i + 1
        if line[i] != ",":
            while i < max and line[i] != ",":
                if (line[i] + line[i - 1]).isspace(): continue
                # The above statement skips excessive spaces.
                # line[i] + line[i - 1] concatenates the current and previous characters of the line.
                myString = myString + line[i]
                i = i + 1
            processedData.append(myString)
        else: i = i + 1
    return processedData

def validateData(processedData):
    errorMessage = "Non-numeric measurements!" # Default error message
    try:
        if len(processedData) != 3:
            errorMessage = "Invalid length of data list!"
            i = 1 / 0 # Throws exception
        [processedData[1], processedData[2]] = [float(processedData[1]), float(processedData[2])]
        # Above is an example of packing variables and unpacking a list.
        if processedData[1] < 0 or processedData[2] < 0: i = 1 / 0
    except:
        print(errorMessage)
        processedData = []
    return processedData

def processData(line):
    processedData = listifyData(line)
    processedData = validateData(processedData)
    return processedData

if __name__ == "__main__":
    print("\nContains functions for data processing performed in 'bpEvaluator.py'\n")