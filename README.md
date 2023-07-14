# Evolutionary Prisoner's Dilemma Tournament

A tournament of competing Prisoner's Dilemma strategies, for the attendees of AMSI Winter School 2023.

## The Game

The game is iterated Prisoner's Dilemma, with an uncertain length to prevent a collapse to the static game Nash equilibrium.

The payoff matrix is as follows:
|               | Cooperate | Defect |
|:-------------:|:---------:|:------:|
| **Cooperate** | R,R       | S,T    |
| **Defect**    | T,S       | P,P    |

where T > R > P > S.
Further, 2R > T + S (both players always cooperating is better than alternating cooperating and defecting).
The game is played at least once, and after each game is played again with probability 𝛿.

For the duration of a single iterated game, algorithms will have access to all previous decisions by both players as part of that game, but not to any moves from any other games.
Algorithms will also be given the values or T, R, P, S, and 𝛿, in case they wish to make decisions on that basis.

By default, the game will run with T = 5, R = 3, P = 1, S = 0 and 𝛿 = 0.99.
That is, the payoff matrix will be as follows:
The payoff matrix is as follows:
|               | Cooperate | Defect |
|:-------------:|:---------:|:------:|
| **Cooperate** | 3,3       | 0,5    |
| **Defect**    | 5,0       | 1,1    |

and the game will run for an average of 100 iterations.

To control for the random length of games, the total payoff of the iterated game will be divided by the number of iterations of the game.

### The Metagame

The tournament will run in an evolutionary manner, over several generations, where the abundance of each strategy in each generation is determined by the total payoff it achieved in previous generations.
In this way, the other strategies present will shift over time, and so the success of a strategy might change over time as its competition changes.

Each strategy will begin the tournament constituting the same proportion of the population.
Every strategy in a generation will play against every other strategy in that generation (and against itself), and will earn offspring in the next generation proportional to its payoff in each game.

## How to Compete

To compete, you must write a strategy and enter it to this GitHub repository.
Each strategy will be contained in a separate `.py` file in the `strategies` directory.
Either send me your GitHub account so that I can add you as a collaborator, send a pull request, or just send me your file on Slack and I can submit it on your behalf.

### Writing a Strategy File

A strategy file consists of three parts:
- A `name` variable, giving the name of your strategy, e.g. `Grim Trigger`. Be creative!
- An `owner` variable, giving your name, so we know who won.
- A `play` function, containing your algorithm.

Your strategy file may also contain anything else you wish: other variables, helper functions, imports, etc.
In particular, you may wish to `import random` to implement a mixed strategy.

#### The `play` Function

The `play` function is the heart of your strategy file.
It is called once for each iteration of the Prisoner's Dilemma game.
It must take seven arguments, and return either `True` or `False`.
`True` represents the choice to cooperate, and `False` the choice to defect.

The seven arguments, in order, are as follows:
- `p1_moves`:
	A list of your previous moves, using `True` to represent cooperate, and `False` to represent defect.
	In the first iteration of each game, this list will be an empty list `[]`.
- `p2_moves`:
	A list of your opponent's previous moves, as above.
- `T`:
	The temptation payoff, if you defect and your opponent cooperates.
- `R`:
	The reward payoff, if you both cooperate.
- `P`:
	The punishment payoff, if you both defect.
- `S`:
	The sucker payoff, if you cooperate and your opponent defects.
- `delta`:
	The probability of playing another game after this one.

Your function is under no obligation to make use of all, or even any, of these arguments, but they must all be in the function signature.

### Testing Your Strategy

If you want to test your strategy before submitting it (always highly recommended), you can use the provided `test.py` file.
First, clone this repository, and put your strategy file in the `strategies` directory.
Take note of the name of your file.
Then, run `test.py`, passing it two arguments on the command line: the names of the files (without the `.py`) for the two strategies you want to run against one another.
For example:
```
python3 test.py always_cooperate always_defect
```
You can pass it the same name twice if you want it to run the strategy against itself.

### Notes

Multiple submissions from the same person are very welcome!
Collaboration is also welcome: feel free to put multiple names in the `owner` string.

For this to work, some people are going to need to submit some nasty (as in, not nice) strategies: strategies that will defect without provocation.
I know we've learned all about how nice strategies are great, but if everyone submits only nice strategies, everything will cooperate all the time, and we'll never see any changes in the population.
So we need some nasty strategies.
Try and take advantage of the nice strategies other people will be submitting!

## Reinforcement Learning

To tie this in with the reinforcement learning module of the winter school, I wrote an environment for using reinforcement learning to train agents to play Prisoner's dilemma.
The environment definition is in `utils/rl/environment.py`, and `train.py` contains a program to train agents using that environment and save them in `rl/agents/`.
You can then add strategies into `strategies/` that load those trained agents and use them to play in the tournament.

### Training an Agent

`train.py` requires a few parameters: the name of the agent to save, then two integer parameters `n` and `m`.
`n` and `m` define the set of moves shown to the agent to hep it make its decision.
At each time step, it sees the first `n` moves of the game, and the most recent `m` moves.
If you want to show it all the moves, just set `n` to something really huge (and `m` to zero); `utils/rl/observe.py` contains a utility function `calculate_size()` for taking a desired probability of a game overrunning `n` moves (using a certain value of 𝛿) and giving the required value of `n`.

Currently, training uses curriculum learning, training the model against every strategy present in the `strategies` directory, including textbook , with equal probability.
This could definitely be updated by changing `utils/rl/environment.py`.
`train.py` also always uses an `ARS` model; this is easy enough to change, but I'd like to set it up to change with a command line argument.

`tensorboard.sh` simply launches tensorboard with the correct log directory set.

### Submitting a Strategy Using an Agent

To submit a strategy using an agent, add your trained agent's zip file into the Git repository (forget that it's an intermediate product) and add a file to the `strategies` directory (as described above) that loads this agent and uses its `predict` method to decide upon moves.
Feel free to use my `ars_all_opponents_20_20.py` as a template.
Just make sure that your model type (e.g. `ARS`) and your observation parameters (`n` and `m`) match the model type and parameters that the model was trained with.
Please don't submit *too* many RL strategies, as they're quite slow to run, but feel free to have some fun playing around with things!
