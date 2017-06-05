
def pow(number, power):
    def worker(number,workerPower,accum = 1):
        if (workerPower == 0):
            return accum
        return worker(number,workerPower - 1, accum * number)
    return worker(number,power,1)
