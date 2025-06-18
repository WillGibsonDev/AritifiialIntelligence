def formatRow(row, path):
    outputSring = ""  
    for i in row:
        if (i, row) in path:
            outputSring.join(".")
        else:
            outputSring.join(row[i])
    return outputSring