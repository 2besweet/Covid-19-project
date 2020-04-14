def estimator(data):
    return data
    def __init__(self,reportedCases,name,days,totalHospitalbeds,avgDailyIncomeInUsd,avgDailyIncomePopulation):
        self.reportedCases=reportedCases
        self.name=name
        self.days=days
        self.totalHospitalbeds=totalHospitalbeds
        self.avgDailyIncomeInUsd=avgDailyIncomeInUsd
        self.avgDailyIncomePopulation=avgDailyIncomePopulation
    def covid19Estimator(self):
        myinputs = {
            "region": {
                "name": self.name,
                "avgAge": 19.7,
                "avgDailyIncomeInUSD": self.avgDailyIncomeInUsd,
                "avgDailyIncomePopulation": self.avgDailyIncomePopulation
            },
            "periodType": self.days,
            "timeToElapse": 58,
            "reportedCases": self.reportedCases,
            "population": 66622705,
            "totalHospitalBeds": self.totalHospitalbeds}
        
        currentlyInfected = self.reportedCases * 10
        currentlyInfectedSevere = self.reportedCases * 50
        factor = self.days / 3
        factorRounded = math.trunc(factor)
        InfectionsByRequestedTime = currentlyInfected * (2 ** factorRounded)
        InfectionsByRequestedTimeSevere = currentlyInfectedSevere * (2 ** factorRounded)
        ImpactSevereCasesByRequestedTime = InfectionsByRequestedTime * 15 / 100
        SevereCasesByRequestedTime = InfectionsByRequestedTimeSevere * 15 / 100
        hospitalBedsByRequestedTime1 = self.totalHospitalbeds * 35 / 95
        hospitalBedsByRequestedTimeAtFullCapacity1 = self.totalHospitalbeds * 35 / 100
        hospitalBedsByRequestedTime = math.trunc(hospitalBedsByRequestedTime1)
        hospitalBedsByRequestedTimeAtFullCapacity = math.trunc(hospitalBedsByRequestedTimeAtFullCapacity1)
        casesForICUByRequestedTime = InfectionsByRequestedTime * 5 / 100
        casesForICUByRequestedTimeSevere = InfectionsByRequestedTimeSevere * 5 / 100
        casesForVentilatorsByRequestedTime = InfectionsByRequestedTime * 2 / 100
        casesForVentilatorsByRequestedTimeSevere = InfectionsByRequestedTimeSevere * 2 / 100
        dollarsInFlight = InfectionsByRequestedTime * 0.65 * 1.5 * 30
        dollarsInFlightSevere = InfectionsByRequestedTimeSevere * self.avgDailyIncomePopulation * self.avgDailyIncomeInUsd * 30
        myoutputs = {
            'data': {'inputData': myinputs},
            'impact': {
                'currentlyInfected': currentlyInfected,
                'InfectionsByRequestedTime': InfectionsByRequestedTime,
                'SevereCasesByRequestedTime': ImpactSevereCasesByRequestedTime,
                'HospitalBedsByRequestedTime': hospitalBedsByRequestedTime,
                'hospitalBedsByRequestedTimeFullCapacity': hospitalBedsByRequestedTimeAtFullCapacity,
                'casesForICUByRequestedTime': casesForICUByRequestedTime,
                'casesForVentilatorsByRequestedTime': casesForVentilatorsByRequestedTime,
                'dollarsInFlight': dollarsInFlight,
            },
            'severeImpact': {
                "currentlyInfected": currentlyInfectedSevere,
                "InfectionsByRequestedTime": InfectionsByRequestedTimeSevere,
                "SevereCasesByRequestedTime": SevereCasesByRequestedTime,
                'HospitalBedsByRequestedTime': hospitalBedsByRequestedTime,
                'hospitalBedsByRequestedTimeFullCapacity': hospitalBedsByRequestedTimeAtFullCapacity,
                'casesForICUByRequestedTime': casesForICUByRequestedTimeSevere,
                "casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTimeSevere,
                'dollarsInFlight': dollarsInFlightSevere

            }
            

        }
    
        print(myoutputs)
    day=estimator(674,"Africa",28,1380614,1.5,0.65)
    day.covid19Estimator()



reportedCases=eval(input('Enter the number of reported cases:-'))
name=input('Enter the name of the region:-')
days=eval(input('Enter the number of days:-'))
totalHospitalbeds=eval(input('Enter the total number of beds available in the region:'))
avgDailyIncomeInUsd=eval(input('Enter the Average income:-'))
avgDailyIncomePopulation=eval(input('Enter the average daily income of the population:-'))/100
reportedCases=674
name="Africa"
days=28
totalHospitalbeds=1380614
avgDailyIncomeInUsd=1.5
avgDailyIncomePopulation=0.65




















