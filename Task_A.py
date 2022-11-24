class Clst:
    def __init__(self, link):
        with open(link) as file:
            lines = file.read().split('\n')
            self.n, self.l = (int(_) for _ in lines[0].split())
            self.numbers = sorted([int(_) for _ in lines[1].split()])
            self.clusters = []
            
    def count(self):
        prev_num = self.numbers.pop(0)
        cur_cluster = [prev_num]
        for number in self.numbers:
            if abs(number - prev_num) <= self.l:
                cur_cluster.append(number)
            else:
                self.clusters.append(cur_cluster)
                cur_cluster = [number]
            prev_num = number
        self.clusters.append(cur_cluster)

    def file_write(self, file_name):
        self.count()
        with open(file_name, "w") as file:
            total_clusters = len(self.clusters)
            file.write(f"{total_clusters}\n")
            for cluster in self.clusters:
                cluster = [str(numb) for numb in cluster]
                file.write(f'{" ".join(cluster)}\n')


clusters = Clst("input.txt")
clusters.file_write("output.txt")
