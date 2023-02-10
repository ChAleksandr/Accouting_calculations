class Stats:
    def __init__(self):
        self.file_name = 'statistic.csv'
        with open(self.file_name, encoding='utf-8') as sett:
            stats = sett.read().split('\n')
            self.cash = stats[0].split(';')[1]
            self.worker1 = stats[1].split(';')[1]
            self.worker2 = stats[2].split(';')[1]

    def get(self, option):
        return eval(f'self.{option}')

    def set(self, option, action):
        if option == 'cash':
            self.cash = int(action)
        elif option == 'worker1':
            self.worker1 = str(action)
        else:
            self.worker2 = str(action)

    def save(self):
        stats_file = open(self.file_name, 'w', encoding='utf-8')
        stats_file.write(f"cash;{self.cash}\nworker1;{self.worker1}\nworker2;{self.worker2}")
        stats_file.close()
