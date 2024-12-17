from template import AlgorithimTemplate



class CSV_Processor(AlgorithimTemplate):
    def insert_value_in_doc(self, formatted_data_with_id):
        print('Connecting to CSV')
        print(formatted_data_with_id)
        print('Saving Data')



csv = CSV_Processor()
csv.insert_data(["João","Silva","São Paulo"])


# from template import AlgorithimTemplate

# class CSV_Processor(AlgorithimTemplate):
#     def insert_value_in_doc(self, formatted_data_with_id):
#         print('Connecting to CSV')
#         print(formatted_data_with_id)
#         print('Saving Data')

# csv = CSV_Processor()
# csv.insert_data(["João","Silva","São Paulo"])