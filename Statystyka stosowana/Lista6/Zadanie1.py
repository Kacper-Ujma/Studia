import numpy as np
import scipy

n = 12
x_srednia = 231.33
s_kwadrat = 31.44
alhpa = 0.05
kwantyle_t_student = 2.20099
kwantyle_chi_kwadrat_1 = 21.9201
kwantyle_chi_kwadrat_2 = 3.81575

przedial_ufnosci_srenia = [x_srednia-np.sqrt(s_kwadrat/n)*kwantyle_t_student,x_srednia+np.sqrt(s_kwadrat/n)*kwantyle_t_student]
przedial_ufnosci_s = [(n-1)*s_kwadrat/kwantyle_chi_kwadrat_1,(n-1)*s_kwadrat/kwantyle_chi_kwadrat_2]

print(przedial_ufnosci_srenia)
print(przedial_ufnosci_s)
