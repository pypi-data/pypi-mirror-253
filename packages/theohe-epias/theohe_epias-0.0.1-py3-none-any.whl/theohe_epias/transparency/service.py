from epias.transparency.data.reports import Reports
from epias.transparency.data.dam import DAM
from epias.transparency.data.idm import IDM
from epias.transparency.data.bpm import BPM
from epias.transparency.data.ancillary_services import AS
from epias.transparency.data.bilateral_contracts import BC
from epias.transparency.data.imbalance import IB
from epias.transparency.data.general_data import GD
from epias.transparency.data.production import Production
from epias.transparency.data.consumption import Consumption
from epias.transparency.data.renewables import Renewables
from epias.transparency.data.transmission import Transmission
from epias.transparency.data.dams import Dams
from epias.transparency.data.mms import MMS
from epias.transparency.data.yekg import YEKG
from epias.transparency.data.pfm import PFM

class WebServiceTransparency():
    def __init__(self):
        self.reports = Reports()
        self.dam = DAM()        
        self.idm = IDM()        
        self.bpm = BPM()
        self.ancillary_services = AS()
        self.bilateral_contracts = BC()
        self.imbalance = IB()
        self.general_data = GD()
        self.production = Production()
        self.consumption = Consumption()
        self.renewables = Renewables()
        self.transmission = Transmission()
        self.dams = Dams()
        self.mms = MMS()        
        self.yekg = YEKG()
        self.pfm = PFM()

        self.services = ['ancillary_services', 'bilateral_contracts', 'bpm', 'consumption', 'dam', 'dams', 'general_data', 'idm', 'imbalance', 'mms', 'pfm', 'production', 'renewables', 'reports', 'transmission', 'yekg']
