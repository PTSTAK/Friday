

import os

# gcp
project_id = 'tribal-datum-340202'
dataset_id = 'digital_pmo'

# table -> Exploration_Plan
table_id = 'Exploration_Plan'

# table -> Seismic_Plan
table_id = 'Seismic_Plan'


# sharepoint
SERCRET = os.getenv('SERCRET', 'credentials\secret.json')
server_url = "https://pttep.sharepoint.com/teams/SoftwareDevelopmentwithExternalParty"
rel_path = "/teams/SoftwareDevelopmentwithExternalParty/Shared Documents/Digital PMO/99 Test Source Files/Digital_PMO_Test_Data.xlsx"

# rel_path = "/teams/SoftwareDevelopmentwithExternalParty/Shared Documents/Digital PMO"