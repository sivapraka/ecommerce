from abc import ABC, abstractmethod

from insurance.services import *


class TravelInsuranceAdapter(ABC):
    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def add_claim(self):
        pass


class TravelGuardAdapter(TravelInsuranceAdapter):
    def __init__(self, api: TravelGuardApi = None):
        self.travel_guard_api = api or TravelGuardApi()

    def get_status(self, reference:str)->AutoProtectStatus:
        return self.travel_guard_api.get_claim_status(reference)

    def add_claim(self, reference:str, amount:float)->AutoProtectStatus:
         return self.travel_guard_api.submit_claim(reference, amount)


class AutoProtectAdapter(TravelInsuranceAdapter):
    def __init__(self, api: AutoProtectApi = None):
        self.auto_protect_api = api or AutoProtectApi()

    def get_status(self, reference:str)->AutoProtectStatus:
        return self.auto_protect_api.get_status(reference)

    def add_claim(self,reference:str,amount:float)->AutoProtectStatus:
        return self.auto_protect_api.add_claim(amount)
