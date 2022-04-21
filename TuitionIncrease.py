
tuition_increased = 0.03  
tuitionPerSemester = 8000
years = 5

print ('year\tTotal-Tuition')
print('-----------------------')
print(0, '\t', tuitionPerSemester)

for years in range (1, years + 1):
    
    tuitionPerSemester *= (1 + tuition_increased)

    print (years, '\t', tuitionPerSemester)
