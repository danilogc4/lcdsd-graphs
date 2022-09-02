from re import I
import pandas as pd
import plotly.graph_objects as go
import csv  

fig = go.Figure()
filePreffix = 'F0004CH'
count = 2

def getReadyCsv(inputFile, outputFile):
    with open(outputFile, 'w', newline='') as out_f:
        writer = csv.writer(out_f)

        with open(inputFile, newline='') as in_f:
            reader = csv.reader(in_f)

            # Read the first row
            first_row = next(reader)
            # Count the columns in first row; equivalent to your `for i in range(len(first_row)): ...`
            header = ['', '', '', 'X', 'Y', '']

            # Write header and first row
            writer.writerow(header)
            writer.writerow(first_row)

            # Write rest of rows
            for row in reader:
                writer.writerow(row)
                
                
def addCurve(df, i):
    name = 'entrada' if i == 1 else 'saida'
    fig.add_trace(go.Scatter(x=df['X'], y=df['Y'], name=name, mode="lines"))
    
for i in range(1, count+1):
    inputFile = f'{filePreffix}{i}.CSV'
    outputFile = f'ready{filePreffix}{i}.CSV'

    getReadyCsv(inputFile, outputFile)
    df = pd.read_csv(outputFile)
    df.head()

    addCurve(df, i)

fig.show()


