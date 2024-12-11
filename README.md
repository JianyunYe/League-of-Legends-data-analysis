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


##