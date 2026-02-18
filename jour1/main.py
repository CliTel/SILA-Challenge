from compte_epargne import CompteEpargne
from compte_pro import ComptePro
from exceptions import SoldeInsuffisantError, PlafondDepasserError

# création de comptes
compte1 = CompteEpargne(3640650897, "tedy", 50000)
compte2 = ComptePro(9665085667, "CliTel", 20000)

# opérations
try:
    compte1.deposer(10000)
except PlafondDepasserError as e:
    print(e)

try:
    compte2.retirer(25000)
except SoldeInsuffisantError as e:
    print(e)

try:
    compte1.virement(compte2, 30000)
except SoldeInsuffisantError as e:
    print(e)
except PlafondDepasserError as e:
    print(e)

print("Historique tedy:", compte1.historique)
print("Historique CliTel:", compte2.historique)
