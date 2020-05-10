### FUNCTION TO TELL WHETHER A FILE IS WITHIN A CERTAIN THRESHOLD
def is_file_within_threshold(file_path, threshold):
    unix_time = os.path.getctime(file_path)
    modified_date = datetime.datetime.fromtimestamp(unix_time)
    today_date = datetime.datetime.now()
    diff_date = today_date - modified_date
    if diff_date < threshold:
        return True
    else:
        return False
    
### ITERATE AND GRAB ALL CSV PATHs THAT FIT THE THRESHOLD CONDITION
confirmed_trade_path = ""
threshold = 24
latest_csv_path = []
for folder_name in os.listdir(confirmed_trade_path):
    ### ITERATE OVER ALL FOLDERS 
    folder_path = os.path.join(confirmed_trade_path, folder_name)
    ### ITERATE OVER ALL CSV PATHs AND APPEND THE ONES THAT ARE LATEST
    for csv_file in os.listdir(folder_path):
        csv_path = os.path.join(folder_path, csv_file)
        is_latest_file = is_file_within_threshold(csv_path, threshold)
        if is_latest_file:
            latest_csv_path.append(csv_path)
            
### CONCATENATE LATEST CSVs INTO A GIANT DATAFRAME AND SAVE
df = pd.DataFrame()
for csv_path in latest_csv_path:
    df_sub = pd.read_csv(csv_path, header = 1)[:-3]
    today = datetime.datetime.today().strftime('%m%d%Y')  
    df_sub["date_processed"] = today
    df = df.append(df_sub)
    
### CREATE FOLDER 
output_root_path = "
today = str(datetime.datetime.today().strftime('%d-%m-%Y'))
output_folder_name =  today
output_folder_path = os.path.join(output_root_path, output_folder_name)
if not os.path.exists(output_folder_path):os.makedirs(output_folder_path)
output_csv_name = "confirmed_trade_{}".format(today)
output_csv_path = os.path.join(output_folder_path, output_csv_name)
df.to_csv(output_csv_path, index = None)

### Append to Master
master_csv_path = ""
master_df = pd.read_csv(master_csv_path)
master_df = pd.concat([master_df,df], axis =1)
master_df.to_csv("master_csv_path", index = None)



