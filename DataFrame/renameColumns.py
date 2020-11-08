#Rename Selected Columns
df.rename(columns = {'old1':'new1', 'old2':'new2'}, inplace = True)

#Rename all columns
df.columns = ['new1', 'new2', 'new3']
