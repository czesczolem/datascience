class DataLoader(codes_names_df_path):
    
    def __init__(self,):
        self.codes_names_df = pd.read_csv(codes_names_df_path)
        
    def get_codes(self, in_name):
    code_list = self.codes_names_df[self.codes_names_df['name'].str.contains(in_name)]['code'].values.tolist()
    self.code_list = code_list
    print(code_list)
    
    def get_data(self, code, start=None, end=None):
    """
    sample param start end '2025-12-31'
    """
    query = 'BUNDESBANK/{}'.format(code)
    if start and end:
        return quandl.get(query, start_date=start, end_date=end)
    else:
        return quandl.get(query)
    
    
