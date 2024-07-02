import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

quality.automf(3)
service.automf(3)

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

# Wyświtlenie funkcji przynależności dla zmiennych lingwistycznych
quality['average'].view()

# Definiowanie reguł
rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])

# Tworzenie systemu kontrolnego
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# Tworzenie symulacji
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# Podawanie danych wejściowych
tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8

# Obliczanie wyniku
tipping.compute()

# Wyświetlanie wyniku
print(tipping.output['tip'])