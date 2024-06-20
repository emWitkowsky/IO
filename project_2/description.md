# Blackjack (gym) training

## Wstęp

Blackjack to gra karciana oparta na losowości, w której gracz "mierzy" się z krupierem.
Prawdziwy Blackjack może być grany nawet do 7 osób, natomiast w naszym przypadku gra, którą
pozyskaliśmy z popularnej biblioteki Gymnasium jest potyczką jeden an jeden z krupierem.
Polega ona na uzyskaniu kart o łącznej wartości punktów jak najbliższej liczbie 21 punktów, ale nie przekroczeniu jej.
Gracz ma możliwość dobierania kart, aż do momentu, w którym zdecyduje się zatrzymać.
Krupier natomiast musi dobrać kartę jeśli suma jego punktów jest mniejsza niż 17.
Wygrywa ten kto jest bliżej 21 punktów, ale nie przekroczył tej liczby.

## Własny skrypt

```python3
import gym

env = gym.make("Blackjack-v1", natural=True, sab=False)

observation, _ = env.reset()

while True:
    print("Player's sum: ", observation)
    player_sum, dealer_card, usable_ace = observation

    action = 1 if player_sum < 17 else 0

    print(env.step(action))
    observation, reward, done, info, _ = env.step(action)

    if done:
        print("The game has been finished.", reward)
        print("Final observation: ", observation)
        observation, _ = env.reset()

env.close()
```

Na początku pierwszym podejściem, które miało mnie też zaznajomić
z grą w Blackjacka było napisanie własnego skryptu. Skrypt działa w taki sposób, że
dobieramy kartę zawsze, gdy suma punktów naszej ręce jest mniejsza niż 17. Jeśli jednak
przekroczymy ten próg, pasujemy, przestajemy dobierać karty.

## Q-Learing, czyli Uczenie Przez Wzmacnianie

```python
        q_table[player_sum, dealer_card, int(usable_ace), action] = \
            old_value + alpha * (reward + gamma * next_max - old_value)

        state = next_state

        # Update wins and losses counters
        if done:
            if reward == 1:
                wins += 1
            elif reward == -1:
                losses += 1
```

Kolejnym krokiem było zastosowanie algorytmu Q-Learningu, który pozwolił na
uczenie się agenta w grze w Blackjacka. W tym przypadku, agent działa na zasadzie
uczenia przez wzmacnianie. W każdym kroku, agent oblicza wartość Q dla danego stanu
i akcji, a następnie aktualizuje wartość Q dla danego stanu i akcji na podstawie
nagrody, którą otrzymał oraz wartości Q dla kolejnego stanu. W ten sposób agent
uczy się, które akcje są dla niego korzystne i kończą się wygraną, a które nie.


## Kontroler Rozmyty

Tworząc kontroler rozmyty, zdefiniowałem reguły gry, którymi kieruje się agent.
Reguły te są oparte na zasadach gry w Blackjacka, a także na moich własnych przemyśleniach.
Kontroler rozmyty to nic innego jak zestaw instrukcji, którymi program operuje i na ich podstawie
opiera decyzje. W moim przypadku, kontroler rozmyty działa na zasadzie "jeśli to, to tamto".

```python
# We define the membership functions for each variable
# setting the sets for every point so that the fuzzy system can work on them
player_sum['low'] = fuzz.trimf(player_sum.universe, [0, 0, 15])
player_sum['medium'] = fuzz.trimf(player_sum.universe, [10, 15, 20])
player_sum['high'] = fuzz.trimf(player_sum.universe, [15, 30, 30])

dealer_card['low'] = fuzz.trimf(dealer_card.universe, [0, 0, 5])
dealer_card['medium'] = fuzz.trimf(dealer_card.universe, [2, 5, 8])
dealer_card['high'] = fuzz.trimf(dealer_card.universe, [5, 10, 10])

action['stick'] = fuzz.trimf(action.universe, [0, 0, 0.5])
action['hit'] = fuzz.trimf(action.universe, [0.5, 1, 1])

# We define set of rules that will determine the action
rule1 = ctrl.Rule(player_sum['low'], action['hit'])
rule2 = ctrl.Rule(player_sum['medium'] & dealer_card['low'], action['stick'])
rule3 = ctrl.Rule(player_sum['medium'] & dealer_card['medium'], action['hit'])
rule4 = ctrl.Rule(player_sum['medium'] & dealer_card['high'], action['hit'])
rule5 = ctrl.Rule(player_sum['high'], action['stick'])
```

## Algorytm Genetyczny

```python
def on_generation(ga_instance):
    best_fitness.append(ga_instance.best_solution()[1])

game_by_ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       sol_per_pop=num_parents_mating,
                       num_genes=num_states,
                       init_range_low=0,
                       init_range_high=1,
                       parent_selection_type="sss",
                       keep_parents=1,
                       crossover_type="single_point",
                       mutation_type="random",
                       mutation_percent_genes=10,
                       initial_population=initial_population,
                       on_generation=on_generation)

game_by_ga_instance.run()
```


Ostatnim krokiem było zastosowanie algorytmu genetycznego, który pozwolił na



## Ostatni krok

Posiadając już wszystkie algorytmy, które pozwoliły na uczenie się agenta w grze w Blackjacka,
jedyne co zostało do zrobienia to zabawa parametrami, takimi jak ilość epizodów, ilość generacji,
wielkość populacji, współczynnik mutacji, współczynnik krzyżowania, współczynnik uczenia, współczynnik dyskontowania
oraz inne parametry, które pozwoliły na uzyskanie jak najlepszych wyników. Następnie porównywałem te
algorytmy między soba by zobaczyć, który z nich osiąga najlepsze wyniki.

Najlepiej wyszkolony został algorytm genetyczny

Algorytm genetyczny 52% wygranych
Uczenie przez wzmacnianie 41% wygranych
Kontroler rozmyty daje nam 23% wygranych
Mój skrypt całe 5% wygranych