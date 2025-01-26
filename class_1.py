from datetime import datetime

class Operations:
    """Класс работы с операциями"""

#Инициализация
    def __init__(self,operation_data_time,operation_description,operation_from,operation_to,operation_amount,operation_name):
        self.operation_data_time = operation_data_time
        self.operation_description = operation_description
        self.operation_from = operation_from
        self.operation_to = operation_to
        self.operation_amount = operation_amount
        self.operation_name = operation_name

    def correct_data(self):
        for operations_data_time in self.operation_data_time:
            date_obj = datetime.strptime(operations_data_time, '%Y-%m-%dT%H:%M:%S.%f')
            return date_obj




operation = Operations(["2018-07-11T02:26:18.671407"],1,1,1,1,1)
print(operation.correct_data().strftime('%d-%m-%Y %H:%M:%S'))



