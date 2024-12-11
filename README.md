# Introduction

## Dataset Background
League of Legends is a MOBA game developed by Riot Games. Its success in the professional scene has made it known as the best e-sports game. The dataset I used is a professional dataset developed by Oracle Elixir. The dataset I used contains the match data of the entire 2024 professional competition.

This dataset contains key game statistics and results for every professional match.

In League of Legends, the dragon appears in the lower jungle, and it refreshes after 4 minutes of the start of every game, and again 4 minutes after either side kills it. When one of the teams obtains four baby dragons, they will obtain the powerful Dragon Soul buff. After a team obtains the Dragon Soul buff, the next refresh will be called the Elder Dragon, and killing it will obtain an even more powerful buff. This means that the team that obtains both the Dragon Soul and the Elder Dragon is almost guaranteed to win, while the team that doesn't obtain the Dragon Soul but obtains the Elder Dragon buff has a chance to turn the game around.

Against this background, we wonder: does getting the first baby dragon have a significant impact on the course of the game? Teams that are strong in the early game want to get the first baby dragon, which will give them the initiative and maintain their early-game dominance. They will keep killing dragons and make the arrival of the dragon soul and ancient dragon buffs as fast as possible.
On the other hand, a team that is strong in the mid to late game does not mean that they getting the first dragon is meaningless. They can still take the initiative. After getting the first dragon, strategically abandon the subsequent dragons. This can delay the opponent's time to get the dragon soul by 4 minutes, which is very important for teams that are weak in the early game.

Therefore, my research question is: What impact does the team that gets the first dragon have on the rest of the data in the dataset? I hope to prove through data analysis that the team that gets the first dragon has a significant impact on the data, including the overall performance of the team, individual data, and the outcome of the game. At the same time, a predictive model will be built using the data to predict what position this player will be. This predictive model is interesting because we can understand the focus and importance of different positions without watching the game or even understanding the game.


## Column Introduction
The dataset contains the following columns relevant to our analysis:

- **gameid**: Unique identifier for each match, ensuring that rows can be linked to the same game.
- **league**: The league or tournament in which the game took place (e.g., LCK, LCS, MSI).
- **patch**: The game version used during the match, corresponding to specific updates in the game (e.g., 13.24).
- **side**: The team's side in the match, either "blue" or "red," representing their starting position on the map.
- **result**: The match outcome for the team, represented as `1` for a win and `0` for a loss.
- **kills**: Total number of enemy champions eliminated by the team.
- **deaths**: Total number of deaths experienced by the team during the match.
- **assists**: Total number of assists (helping to eliminate enemy champions) achieved by the team.
- **firstdragon**: Indicates whether the team secured the first dragon in the match (`1` for yes, `0` for no).
- **dragons**: Total number of dragons secured by the team.
- **opp_dragons**: Total number of dragons secured by the opposing team.
- **elders**: Total number of Elder Dragons secured by the team.
- **firstherald**: Indicates whether the team secured the first Rift Herald (`1` for yes, `0` for no).
- **position**: The specific role of the player within the game (e.g., "top," "jungle," "mid," "bot," "support").

This curated subset focuses on essential team and player performance metrics for the research question.


# Data Cleaning and Exploratory Data Analysis


## Data Cleaning
As mentioned above, I only kept the relevant columns I think are potentially useful: ‘gameid’, ‘league’, ‘patch’, ‘side’, ‘result’ ,‘kills’, ‘deaths’, ‘assists’, ‘firstdragon’ ,‘dragons’, ‘opp_dragons’ ,‘elders’ ,‘firstherald’ ,‘position’. In addition, each game uses twelve lines, which are ten lines of player information and two lines of team information. To facilitate data research, I have divided them into ‘team_data’ and ‘player_data’. ‘team_data’ is used to study the impact of obtaining the first dragon on the team. And ‘player_data’ is used to predict the position of the player through the data.

In addition, #since the game IDs are all duplicated with even numbers, we can assume that there are 17 games missing version numbers, and 1391 games that do not record the dragon, or it can be assumed that neither team played the dragon in these 1391 games. We will change the value of the missing version number to ‘unknown’ and the value of the missing dragon record to ‘unknown’. Apart from this, there are no missing values.

The following is the header of the ‘team_data’ datasets.

| gameid             | league | patch | side | result | kills | deaths | assists | firstdragon | dragons | opp_dragons | elders  | firstherald | position |
|---------------------|--------|-------|------|--------|-------|--------|---------|-------------|---------|-------------|---------|-------------|----------|
| 10660-10660_game_1 | DCup   | 13.24 | Blue | False  | 3     | 16     | 7       | unknown     | 2       | 3           | unknown | unknown     | team     |
| 10660-10660_game_1 | DCup   | 13.24 | Red  | True   | 16    | 3      | 43      | unknown     | 3       | 2           | unknown | unknown     | team     |
| 10660-10660_game_2 | DCup   | 13.24 | Blue | False  | 3     | 17     | 8       | unknown     | 0       | 4           | unknown | unknown     | team     |
| 10660-10660_game_2 | DCup   | 13.24 | Red  | True   | 17    | 3      | 42      | unknown     | 4       | 0           | unknown | unknown     | team     |
| 10660-10660_game_3 | DCup   | 13.24 | Blue | True   | 21    | 3      | 32      | unknown     | 2       | 1           | unknown | unknown     | team     |




## Univariate Analysis

I performed a univariate analysis of the homicide statistics in the dataset.
### Team Kills Distribution
<iframe
  src="assets/team_kills_distribution.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

The histogram shows that the team's kills are close to a near-normal distribution, slightly skewed to the right. This suggests that the image is good and the team kill count is logical, which is a typical distribution for professional League of Legends matches.



I performed a bivariate analysis of the Getting the First Dragon and Outcome stats in the dataset so that I could directly see if Getting the First Dragon had an impact on winning or losing the match.
## Bivariate Analysis
### Win/Loss Distribution for Teams that Got First Dragon
<iframe
  src="assets/win_loss_distribution_first_dragon.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>
It can be seen that the team that gets the first dragon has a 56.8% probability of winning, which is already an exaggerated statistic in a statistic that is relatively large. It can be said that getting the first dragon is very helpful in winning the game.


## Interesting Aggregates
| firstdragon   |   result |   kills |   deaths |   assists |   dragons |   opp_dragons |
|:--------------|---------:|--------:|---------:|----------:|----------:|--------------:|
| False         |     3616 |  120256 |   135504 |    275586 |     12960 |         24063 |
| True          |     4740 |  135037 |   120334 |    308969 |     24063 |         12960 |
| unknown       |     1390 |   38998 |    39071 |     92801 |      6244 |          6244 |

I grouped the dataset by teams that got the first dragon and those that didn't, and then calculated the sum of all the data. The more interesting findings were that the team that got the first dragon, won, had more total kills, fewer deaths, more assists, and got more total dragons. This pretty much shows that getting the first dragon is extremely helpful in improving the team's stats.






# Assessment of Missingness


## NMAR Analysis
Among the data, I think the following missing values may be considered NMAR:
patch: The missing version number may be due to incomplete or incorrect recording when entering the game data, and is not related to other characteristics of the game (such as the game result, number of kills, etc.).
firstdragon and firstherald: The missing values may be because the game does not clearly record whether these events occurred, which may be related to the recording mechanism or entry rules.
Since the mechanism for generating missing values in these columns is more likely to be directly related to their own recording process rather than the characteristics of other columns, I believe that the missing values in these columns are NMAR.

If more information about the data generation and recording process can be obtained, for example, the habit of not recording these in some competitions, or what special circumstances occurred that day, this may help us to change the missing values in these columns from NMAR to MAR.


## Missingness Dependency

I will test whether the firstdragon column does indeed depend on other columns. The other two columns I use are ‘league’ and ‘patch’. The significance level I have chosen is 0.05, and the test statistic is TVD.
First, let's replace the test to see if the absence of the ‘firstdragon’ column depends on the ‘league’ column.

Null hypothesis: The distribution of the ‘league’ column is the same when the ‘firstdragon’ column is missing as when it is not.

Alternative hypothesis: The distribution of the ‘league’ column is not the same when the ‘firstdragon’ column is missing as when it is not.
Below is a graph of the distribution of the ‘league’ column.

| league          |   fb_missing = True |   fb_missing = False |
|:----------------|--------------------:|---------------------:|
| DCup            |          0.0129403  |           0          |
| LDL             |          0.406183   |           0          |
| LPL             |          0.515457   |           0          |
| MSI             |          0.0560748  |           0          |
| WLDs            |          0.00934579 |           0.0142396  |
| AC              |          0          |           0.00418811 |
| AL              |          0          |           0.018308   |
| CBLOL           |          0          |           0.0314706  |
| CBLOLA          |          0          |           0.0330262  |
| CDF             |          0          |           0.00825655 |
| CT              |          0          |           0.00466675 |
| EBL             |          0          |           0.0169917  |
| EBLPA           |          0          |           0.0029915  |
| EM              |          0          |           0.0477444  |
| EPL             |          0          |           0.017949   |
| ESLOL           |          0          |           0.0348211  |
| EWC             |          0          |           0.00227354 |
| GLL             |          0          |           0.018308   |
| GLLPA           |          0          |           0.00454709 |
| HC              |          0          |           0.0132823  |
| HM              |          0          |           0.0185473  |
| HW              |          0          |           0.0100515  |
| IC              |          0          |           0.00813689 |
| KeSPA           |          0          |           0.00574369 |
| LAS             |          0          |           0.0345818  |
| LCK             |          0          |           0.0576762  |
| LCKC            |          0          |           0.0611463  |
| LCO             |          0          |           0.018667   |
| LCS             |          0          |           0.0229748  |
| LEC             |          0          |           0.0351801  |
| LFL             |          0          |           0.0283595  |
| LFL2            |          0          |           0.0205815  |
| LIT             |          0          |           0.0178294  |
| LJL             |          0          |           0.0177097  |
| LLA             |          0          |           0.0254876  |
| LPLOL           |          0          |           0.0184277  |
| LRN             |          0          |           0.0107694  |
| LRS             |          0          |           0.0122053  |
| LVP SL          |          0          |           0.0289578  |
| NACL            |          0          |           0.0583942  |
| NEXO            |          0          |           0.0192653  |
| NLC             |          0          |           0.019026   |
| NLC Aurora Open |          0          |           0.00921383 |
| PCS             |          0          |           0.0354194  |
| PRM             |          0          |           0.0288381  |
| PRMP            |          0          |           0.0160345  |
| TCL             |          0          |           0.0216585  |
| TSC             |          0          |           0.0124447  |
| UL              |          0          |           0.0189063  |
| USP             |          0          |           0.00454709 |
| VCS             |          0          |           0.0301544  |

After the permutation test, the observation statistic is 0.0024468826290344773 and the p-value is 1.
The following figure shows the empirical TVD distribution of this test:

### Permutation Test: TVD Distribution for Firstdragon vs League
<iframe
  src="assets/firstdragon_vs_league_tvd.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>
Since the p-value is much larger than 1, we cannot reject the null hypothesis, so the missing values of firstdragon do not depend on the ‘league’ column.




Next, we test the relationship between the ‘patch’ column and ‘firstdragon’.
The null hypothesis: the distribution of the ‘patch’ column is the same when the ‘firstdragon’ column is missing as when it is not.

The alternative hypothesis: the distribution of the ‘patch’ column is not the same when the ‘firstdragon’ column is missing as when it is not.

Here is a graph of the ‘patch’ column.
| patch   |   fb_missing = True |   fb_missing = False |
|:--------|--------------------:|---------------------:|
| 13.24   |           0.0129403 |           0          |
| 14.01   |           0.109993  |           0.0749073  |
| 14.02   |           0.136592  |           0.0630609  |
| 14.04   |           0.123652  |           0.0589925  |
| 14.05   |           0.0826743 |           0.0662917  |
| 14.06   |           0.0366643 |           0.0256073  |
| 14.08   |           0.136592  |           0.00694029 |
| 14.09   |           0.0805176 |           0.0215388  |
| 14.1    |           0.0625449 |           0.0534881  |
| 14.11   |           0.0460101 |           0.0677277  |
| 14.13   |           0.0740474 |           0.114515   |
| 14.14   |           0.0431344 |           0.0287184  |
| 14.15   |           0.0424155 |           0.0696422  |
| unknown |           0.0122214 |           0          |
| 14.03   |           0         |           0.0705995  |
| 14.07   |           0         |           0.0217782  |
| 14.12   |           0         |           0.0780184  |
| 14.16   |           0         |           0.0291971  |
| 14.17   |           0         |           0.0201029  |
| 14.18   |           0         |           0.0869929  |
| 14.19   |           0         |           0.0108891  |
| 14.2    |           0         |           0.00981213 |
| 14.21   |           0         |           0.0106498  |
| 14.22   |           0         |           0.00478641 |
| 14.23   |           0         |           0.00574369 |

After the permutation test, the observed statistic is 0.2511157600695836 and the p-value is 0.0.

The following figure shows the empirical TVD distribution for this test:
### Permutation Test: TVD Distribution for Firstdragon vs Patch
<iframe
  src="assets/firstdragon_vs_patch_tvd.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

Since the p-value is much smaller than 0.05, we reject the null hypothesis, and therefore the missing values of firstdragon do not depend on the ‘patch’ column.



# Hypothesis Testing

In the hypothesis test, I want to assess whether there is a difference in the number of deaths between teams that won the first dragon and those that did not. Because the number of deaths is often an important measure of whether a team is at a disadvantage in professional competitions, we can use this to assess whether the winning team won a hard fight.

I have chosen a significance level of 0.05. The Test Statistics is the absolute mean death count difference with and without the first dragon.

The null hypothesis is that the death count distribution of the winning team with the first dragon is the same as the death count distribution of the winning team without the first dragon.
The alternative hypothesis is that the death count distribution of the winning team with the first dragon is different from the death count distribution of the winning team without the first dragon.

Here is the histogram:
<iframe
  src="assets/deaths_difference_distribution.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

The p-value is 0.001, which is much smaller than 0.05, so we reject the null hypothesis. This shows that there is indeed a difference between the death toll of teams that get the first dragon and those that don't. Teams that get the first dragon will win more easily.



# Framing a Prediction Problem

My prediction problem is to predict whether a player is a ‘bot’ player or not. This is a binary classification problem, which is ‘bot’ (True) or not (False). I think it is very interesting to predict who is a ‘bot’ just by using the post-game data, which shows the charm of data. We don't even need to spend half an hour watching the game. I encoded the position as a one-hot encoding, with players in the ‘bot’ position being True and players in other positions being False. This is our response variable position_bot. I chose to use accuracy as the main metric because this is a binary classification problem, and I am more concerned about the accuracy of the classification than the preference function of a particular class. I chose ‘kills’, ‘assists’, ‘deaths’ and ‘dpm’ as our features. These are all information we can get after the game.

|   kills |   deaths |   assists |     dpm | position_bot   |
|--------:|---------:|----------:|--------:|:---------------|
|       1 |        3 |         1 | 225.62  | False          |
|       0 |        4 |         3 | 234.178 | False          |
|       0 |        2 |         0 | 318.293 | False          |
|       2 |        4 |         0 | 346.511 | True           |
|       0 |        3 |         3 | 205.228 | False          |




# Baseline Model
I built a baseline model using simple logistic regression. Since the difference in the length of the game can cause the difference in Kill/Dead/Assist to become very large, and such a difference is not beneficial to my prediction model, I divided them by the length of the game so that their K/D/A would not be affected by the length of the game. These four are quantitative features, so I used StandardScaler for standardization.
After fitting the model, the accuracy on the test set was 0.80, which means that in 80% of cases, the model can correctly predict whether the player is in the ‘bot’ position. I can only say that the current model is acceptable and there is still much room for improvement.


# Final Model
In the final model, I added two new features, ‘damageshare’ and ‘cspm’. ‘Damageshare’ is the percentage of damage caused by this player in the game compared to the entire team. And ‘cspm’ is the number of kills per minute. Because the main responsibility of a ‘bot’ in a game is to cause more damage under the protection of teammates, ‘bots’ naturally receive more resource bias, can kill more minions, and deal higher damage. Therefore, I think these two are important features.

At the beginning, I chose to use logistic regression as the baseline model. After adding these two features, we got an accuracy of 0.81. The improvement was not ideal, so I used GridSearchCV to perform hyperparameter tuning. After adjusting the hyperparameters, the performance of the model did not improve significantly (still 0.81). I think this may be due to the limited expressive power of logistic regression, and there is not much room for optimisation for the current problem. So I decided to try a zero-one model: random forest. In the end, I got a maximum tree depth of 10 and a minimum sample size of 2 for each split. 200 trees provided higher model stability and generalisation ability. The maximum accuracy was 0.82, a slight improvement over the 0.81 of logistic regression, which shows that random forests did perform better in this prediction.



# Fairness Analysis


Here, I want to assess a fairness issue: ‘Does my model perform equally well in predicting the position of players with a damageshare of less than 0.2 as it does for players with a damageshare of 0.2 or more?’ Some teams may not focus on the bot as their main tactic, or they may have a star player in another position, resulting in the bot's damage share being lower than that of other teams' bots. To test this, I conducted a permutation experiment. Group X represents players with a ‘damageshare’ of less than 0.2, and Group Y represents players with a ‘damageshare’ of 0.2 or greater. I still chose to use accuracy as the evaluation metric, because it directly measures the model's ability to predict the target variable, and this is a binary classification problem.

Hypothesis test
Null Hypothesis: The model's prediction accuracy for Group X and Group Y is the same, and any differences are due to randomness.
Alternative Hypothesis: There is a significant difference in the model's prediction accuracy for Group X and Group Y.
The test statistic is the absolute difference between the prediction accuracies of the two groups. The significance level is 0.05.

After the permutation test, we obtained a statistic of 0.2282 and a p-value of 0. This indicates that there is a significant difference in the model's prediction accuracy for lower and higher ‘damageshare’players, suggesting that the model may be unfair.

### Permutation Test Distribution

The following interactive plot shows the distribution of the permutation test statistics, along with the observed statistic highlighted in red:

<iframe
  src="assets/permutation_test_distribution.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>