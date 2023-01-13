#Lists
FBE = ["4054683"]							

UEC =[
"4053577"
,"4053428"
,"4052753"
,"4052629"
,"4054350"
,"97136118"
,"2700655"
]

LFT =[
"4052635"
,"4052500"
,"4052612"
,"4052496"
,"4053255"
,"4053736"
,"4052489"
,"4053257"
]

CMP = [
"4052668"
,"4052683"
,"4053675"
,"4053554"
    ]
		
BG = ["11340886"]

CS = ["9641993"]

TFT = ["12781681"]

IS = ["9641618"]

HBA1C = ["11340917"]
							
VitD = ["12781698"]	





# Create a dataframe filtered with only UEC tests
UEC_tests_df = dataframe_1[dataframe_1['EVENT-CODE'].isin(UEC)]

#variable for counting UEC tests
count_UEC = int(0)

# Get a list of all unique test samples patient id and datetime keys
unique_test_batches = UEC_tests_df['PATIENT-ID-AND-DT'].unique()

for a_batch_key in unique_test_batches:
    #create a temporary dataframe of all the results with just that combination of datetime and patientid
    df_temp_filtered = UEC_tests_df[UEC_tests_df['PATIENT-ID-AND-DT'] == a_batch_key]
    # Check if all elements are in the list
    TF_bool = all(elem in df_temp_filtered['EVENT-CODE'].values for elem in UEC)
    if TF_bool == True:
        count_UEC += 1

print(count_UEC)