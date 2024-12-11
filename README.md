# **Statistical Analysis of the First Dragon in League of Legends**

## **Introduction**

### **Dataset Background**
League of Legends is a MOBA game developed by Riot Games. Its success in the professional scene has made it known as the best e-sports game. The dataset I used is a professional dataset developed by **Oracle Elixir**, containing match data from the entire 2024 professional competition.  

This dataset provides key game statistics and results for every professional match.

In League of Legends, the dragon appears in the lower jungle, refreshing **4 minutes** after the start of the game and again 4 minutes after being killed. When a team secures **four baby dragons**, they gain the **Dragon Soul buff**. After obtaining the Dragon Soul buff, the next dragon to spawn is the **Elder Dragon**, whose buff can heavily influence the game's outcome. Securing both the Dragon Soul and the Elder Dragon significantly increases a team's chances of winning. Even teams that fail to secure the Dragon Soul can still turn the game around by obtaining the Elder Dragon buff.

Given this context, we explore the question: **Does getting the first dragon have a significant impact on the course of the game?**  

### **Research Question**
Teams with strong early-game performance often aim to secure the **first dragon** to gain an advantage and maintain their dominance. Securing the first dragon accelerates the acquisition of Dragon Soul and Elder Dragon buffs, creating pressure on the opposing team.  

Conversely, teams with stronger mid-to-late game potential might still benefit from securing the first dragon. By strategically abandoning subsequent dragons after securing the first, they can delay their opponents' acquisition of the Dragon Soul by 4 minutes. This tactic is critical for teams weaker in the early game.  

Thus, the research question is:  
**What impact does securing the first dragon have on the team's overall performance, individual player statistics, and game outcomes?**  

Through data analysis, we aim to demonstrate the significant impact of securing the first dragon on various aspects of the game. Additionally, we build a predictive model to determine a player's position based on their performance metrics. This model helps us identify key metrics for each role without needing to watch the game or understand its intricacies.

---

## **Column Introduction**
The dataset includes the following columns relevant to our analysis:

- **gameid**: Unique identifier for each match, ensuring rows can be linked to the same game.  
- **league**: The league or tournament where the game took place (e.g., **LCK**, **LCS**, **MSI**).  
- **patch**: The game version used during the match (e.g., **13.24**).  
- **side**: The team's starting position on the map: **blue** or **red**.  
- **result**: Match outcome: **1** for a win, **0** for a loss.  
- **kills**: Total number of enemy champions eliminated by the team.  
- **deaths**: Total number of deaths experienced by the team.  
- **assists**: Total number of assists (helping to eliminate enemy champions) achieved by the team.  
- **firstdragon**: Indicates whether the team secured the **first dragon** (**1** for yes, **0** for no).  
- **dragons**: Total number of dragons secured by the team.  
- **opp_dragons**: Total number of dragons secured by the opposing team.  
- **elders**: Total number of Elder Dragons secured by the team.  
- **firstherald**: Indicates whether the team secured the **first Rift Herald** (**1** for yes, **0** for no).  
- **position**: The player's role within the game (e.g., **top**, **jungle**, **mid**, **bot**, **support**).  

This curated subset highlights essential team and player performance metrics needed to address the research question effectively.



# **Data Cleaning and Exploratory Data Analysis**

## **Data Cleaning**
As mentioned above, I only kept the relevant columns I think are potentially useful: **‘gameid’, ‘league’, ‘patch’, ‘side’, ‘result’ ,‘kills’, ‘deaths’, ‘assists’, ‘firstdragon’ ,‘dragons’, ‘opp_dragons’ ,‘elders’ ,‘firstherald’ ,‘position’**. In addition, each game uses **twelve lines**, which are **ten lines of player information** and **two lines of team information**. To facilitate data research, I have divided them into **‘team_data’** and **‘player_data’**.  
- **‘team_data’** is used to study the impact of obtaining the first dragon on the team.  
- **‘player_data’** is used to predict the position of the player through the data.  

In addition, since the game IDs are all duplicated with even numbers, we can assume that there are **17 games missing version numbers** and **1391 games that do not record the dragon**. It can also be assumed that neither team played the dragon in these 1391 games.  
We changed the value of the missing version number to **‘unknown’** and the value of the missing dragon record to **‘unknown’**. Apart from this, there are no missing values.

The following is the header of the **‘team_data’** datasets:

| **gameid**          | **league** | **patch** | **side** | **result** | **kills** | **deaths** | **assists** | **firstdragon** | **dragons** | **opp_dragons** | **elders**  | **firstherald** | **position** |
|---------------------|------------|-----------|----------|------------|-----------|------------|-------------|-----------------|-------------|-----------------|-------------|-----------------|--------------|
| 10660-10660_game_1 | DCup       | 13.24     | Blue     | False      | 3         | 16         | 7           | unknown         | 2           | 3               | unknown     | unknown         | team         |
| 10660-10660_game_1 | DCup       | 13.24     | Red      | True       | 16        | 3          | 43          | unknown         | 3           | 2               | unknown     | unknown         | team         |
| 10660-10660_game_2 | DCup       | 13.24     | Blue     | False      | 3         | 17         | 8           | unknown         | 0           | 4               | unknown     | unknown         | team         |
| 10660-10660_game_2 | DCup       | 13.24     | Red      | True       | 17        | 3          | 42          | unknown         | 4           | 0               | unknown     | unknown         | team         |
| 10660-10660_game_3 | DCup       | 13.24     | Blue     | True       | 21        | 3          | 32          | unknown         | 2           | 1               | unknown     | unknown         | team         |

---

## **Univariate Analysis**

I performed a univariate analysis of the homicide statistics in the dataset.

### **Team Kills Distribution**
<iframe
  src="assets/team_kills_distribution.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

The histogram shows that the team's kills are close to a **near-normal distribution**, slightly **skewed to the right**. This suggests that the distribution is logical and typical for professional League of Legends matches.

---

## **Bivariate Analysis**

### **Win/Loss Distribution for Teams that Got First Dragon**
<iframe
  src="assets/win_loss_distribution_first_dragon.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

It can be seen that the team that gets the **first dragon** has a **56.8% probability of winning**, which is already an impressive statistic given the large dataset. This shows that getting the first dragon is highly beneficial for winning the game.

---

## **Interesting Aggregates**

| **Firstdragon**   | **Result** | **Kills**   | **Deaths**  | **Assists** | **Dragons** | **Opp Dragons** |
|-------------------|------------|-------------|-------------|-------------|-------------|-----------------|
| False             | 3616       | 120256      | 135504      | 275586      | 12960       | 24063           |
| True              | 4740       | 135037      | 120334      | 308969      | 24063       | 12960           |
| Unknown           | 1390       | 38998       | 39071       | 92801       | 6244        | 6244            |

I grouped the dataset by teams that **got the first dragon** and those that **didn't**, and calculated the sum of all the data. The findings reveal that the team that got the **first dragon**:  
- Had **more total kills**  
- **Fewer deaths**  
- **More assists**  
- Secured **more dragons** overall  

These results strongly indicate that securing the **first dragon** plays a significant role in improving the team's overall stats.






# **Assessment of Missingness**

## **NMAR Analysis**
Among the data, I think the following missing values may be considered **NMAR**:

- **patch**: The missing version number may be due to incomplete or incorrect recording when entering the game data and is not related to other characteristics of the game (such as the game result, number of kills, etc.).
- **firstdragon** and **firstherald**: The missing values may exist because the game does not clearly record whether these events occurred. This could be related to the recording mechanism or entry rules.

Since the mechanism for generating missing values in these columns is more likely to be directly related to their own recording process rather than the characteristics of other columns, I believe that the missing values in these columns are **NMAR**.

If more information about the data generation and recording process can be obtained (e.g., the habit of not recording these in some competitions or what special circumstances occurred on certain days), this may help us change the missing values in these columns from **NMAR** to **MAR**.

---

## **Missingness Dependency**
I will test whether the **firstdragon** column does indeed depend on other columns. The other two columns I use are **‘league’** and **‘patch’**.  
The significance level I have chosen is **0.05**, and the test statistic is **TVD**.

---

### **Firstdragon vs League**
**Null Hypothesis**: The distribution of the **‘league’** column is the same when the **‘firstdragon’** column is missing as when it is not.  
**Alternative Hypothesis**: The distribution of the **‘league’** column is not the same when the **‘firstdragon’** column is missing as when it is not.

Below is a table of the **league** column distribution:

| **League**        | **fb_missing = True** | **fb_missing = False** |
|-------------------|-----------------------:|------------------------:|
| DCup             |           0.0129403   |              0         |
| LDL              |           0.406183    |              0         |
| LPL              |           0.515457    |              0         |
| MSI              |           0.0560748   |              0         |
| WLDs             |           0.00934579  |         0.0142396      |
| AC               |           0           |         0.00418811     |
| ...              |           ...          |         ...            |

After the permutation test:
- **Observed Statistic**: 0.0024468826290344773  
- **P-value**: 1  

The following figure shows the empirical **TVD** distribution for this test:

### **Permutation Test: TVD Distribution for Firstdragon vs League**
<iframe
  src="assets/firstdragon_vs_league_tvd.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

Since the p-value is much larger than 0.05, we **cannot reject the null hypothesis**, meaning the missing values of **firstdragon** do not depend on the **‘league’** column.

---

### **Firstdragon vs Patch**
**Null Hypothesis**: The distribution of the **‘patch’** column is the same when the **‘firstdragon’** column is missing as when it is not.  
**Alternative Hypothesis**: The distribution of the **‘patch’** column is not the same when the **‘firstdragon’** column is missing as when it is not.

Below is a table of the **patch** column distribution:

| **Patch**   | **fb_missing = True** | **fb_missing = False** |
|-------------|-----------------------:|------------------------:|
| 13.24       |            0.0129403  |             0          |
| 14.01       |            0.109993   |         0.0749073      |
| 14.02       |            0.136592   |         0.0630609      |
| 14.04       |            0.123652   |         0.0589925      |
| 14.05       |            0.0826743  |         0.0662917      |
| ...         |            ...         |         ...            |

After the permutation test:
- **Observed Statistic**: 0.2511157600695836  
- **P-value**: 0.0  

The following figure shows the empirical **TVD** distribution for this test:

### **Permutation Test: TVD Distribution for Firstdragon vs Patch**
<iframe
  src="assets/firstdragon_vs_patch_tvd.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

Since the p-value is much smaller than 0.05, we **reject the null hypothesis**, meaning the missing values of **firstdragon** depend on the **‘patch’** column.




# **Hypothesis Testing**

In this hypothesis test, I aim to assess whether there is a difference in the number of deaths between teams that won the first dragon and those that did not. Since the number of deaths is often an important measure of whether a team is at a disadvantage in professional competitions, this analysis helps evaluate whether the winning team faced a hard fight.

- **Significance Level**: 0.05  
- **Test Statistic**: Absolute mean death count difference between teams with and without the first dragon  

**Hypotheses**:  
- **Null Hypothesis**: The death count distribution of the winning team with the first dragon is the same as the death count distribution of the winning team without the first dragon.  
- **Alternative Hypothesis**: The death count distribution of the winning team with the first dragon is different from the death count distribution of the winning team without the first dragon.

### **Permutation Test Results**
The following histogram visualizes the distribution of the test statistics:

<iframe
  src="assets/deaths_difference_distribution.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

- **P-value**: 0.001  
Since the p-value is much smaller than 0.05, we reject the null hypothesis. This result indicates that there is indeed a difference in the death toll of teams that secure the first dragon compared to those that don't. Teams that obtain the first dragon tend to win more easily.

---

# **Framing a Prediction Problem**

My prediction problem is to determine whether a player is a ‘bot’ player or not. This is a **binary classification problem**, where the target variable is either:
- **True**: The player is in the ‘bot’ position.  
- **False**: The player is not in the ‘bot’ position.  

I encoded the `position` column into a one-hot encoded variable named `position_bot`. This response variable (`position_bot`) is derived from post-game data, showcasing the power of data analysis to make predictions without actually watching the game.  

- **Features**: `kills`, `assists`, `deaths`, and `dpm`  
- **Evaluation Metric**: Accuracy  
  - Chosen because it directly measures the correctness of the classification, which is crucial for a binary problem like this.

### **Example of the Processed Data**

| **Kills** | **Deaths** | **Assists** | **DPM**   | **Position Bot** |
|-----------|------------|-------------|-----------|------------------|
| 1         | 3          | 1           | 225.62    | False            |
| 0         | 4          | 3           | 234.178   | False            |
| 0         | 2          | 0           | 318.293   | False            |
| 2         | 4          | 0           | 346.511   | True             |
| 0         | 3          | 3           | 205.228   | False            |

---

# **Baseline Model**

I built a baseline model using **logistic regression**. To account for differences in game length, I normalized `kills`, `deaths`, and `assists` by the game duration. These quantitative features were standardized using `StandardScaler`.

- **Baseline Accuracy**: 80%  
This suggests the model can correctly predict whether a player is a bot in 80% of cases. While acceptable, there is room for improvement.

---

# **Final Model**

### **Feature Engineering**
I added two new features to the model:
- **`damageshare`**: The percentage of total team damage dealt by a player.  
- **`cspm`**: Creep Score per Minute, representing the number of minions killed by the player per minute.

Since bots are typically tasked with dealing more damage while being protected by teammates, these features are crucial for better prediction.

### **Model Selection and Performance**
Initially, I used logistic regression. After adding these two features:
- **Accuracy**: 81%  
Despite the slight improvement, I applied **GridSearchCV** for hyperparameter tuning. However, logistic regression's expressive power was limited, and the performance gain was negligible.

Next, I tried a **random forest model**:
- **Hyperparameters**:
  - Maximum tree depth: 10
  - Minimum sample size per split: 2
  - Number of trees: 200  
- **Final Accuracy**: 82%  

This demonstrates that random forests performed better in this task, albeit with a marginal improvement.

---

# **Fairness Analysis**

### **Question**
Does the model perform equally well in predicting the position of players with a `damageshare` of less than 0.2 compared to players with a `damageshare` of 0.2 or more?

### **Groups**:
- **Group X**: Players with a `damageshare` < 0.2  
- **Group Y**: Players with a `damageshare` ≥ 0.2  

### **Evaluation Metric**: Accuracy  
Chosen because it directly measures the model's prediction quality in this binary classification problem.

### **Hypotheses**:
- **Null Hypothesis**: The model's prediction accuracy for Group X and Group Y is the same, and any observed differences are due to random chance.  
- **Alternative Hypothesis**: The model's prediction accuracy for Group X and Group Y is significantly different.

### **Test Results**
- **Test Statistic**: 0.2282  
- **P-value**: 0.0  

Since the p-value is much smaller than 0.05, we reject the null hypothesis. This indicates that the model's prediction accuracy differs significantly between the two groups, suggesting potential unfairness in the model.

### **Permutation Test Distribution**
The following interactive plot visualizes the permutation test distribution and highlights the observed statistic:

<iframe
  src="assets/permutation_test_distribution.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>
