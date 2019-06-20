import csv

# create list holders for our data.
Id = []
Name = []
ShapeLibrary = []
PageID = []
ContainedBy = []
Group = []
LineSource = []
LineDestination = []
SourceArrow = []
DestinationArrow = []
Destination = []
TextArea1 = []
TextArea2 = []

# open file
with open('/home/asus/Descargas/casos.csv', 'rb') as f:
    reader = csv.reader(f)

# read file row by row
rowNr = 0
for row in reader:
    # Skip the header row.
    if rowNr >= 1:
        Id.append(row[0])
        Name.append(row[1])
        ShapeLibrary.append(row[2])
        PageID.append(row[3])
        ContainedBy.append(row[4])
        Group.append(row[5])
        LineSource.append(row[6])
        LineDestination.append(row[7])
        SourceArrow.append(row[8])
        DestinationArrow.append(row[9])
        Destination.append(row[10])
        TextArea1.append(row[11])
        TextArea2.append(row[12])

# Increase
# the
# row
# number
rowNr = rowNr + 1
# Print
# data 
print Id
print Name
print ShapeLibrary
print PageID
print ContainedBy
print Group
print LineSource
print LineDestination
print SourceArrow
print DestinationArrow
print Destination
print TextArea1
print TextArea2

