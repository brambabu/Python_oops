Q1 = "select avg(age) from player;"

Q2 = "select match_no,play_date from match where audience > 50000;"

Q3 = "select team_id ,count(win_lose) from MatchTeamDetails where win_lose = 'W' group by team_id order by count(win_lose) desc,team_id asc;"

Q4 = "select match_no,play_date from match where stop1_sec > (select avg(stop1_sec) from match) order by match_no desc,play_date desc;"

Q5 = "select match_no ,team.name,player.name from matchcaptain inner join team on team.team_id = matchcaptain.team_id inner join player on player_id = captain order by match_no,team.name"

Q6 = "select match_no,player.name,player.jersey_no from match inner join player on player_of_match = player_id order by match_no;"

Q7 = "select team.name,(select avg(age) from player where team.team_id = player.team_id) as avg_age from team where avg_age > 26 order by team.name asc;"

Q8 = "select player.name,player.jersey_no,player.age,count(goal_id) from player inner join goaldetails on goaldetails.player_id = player.player_id where player.age <=27 group by player.player_id order by count(goal_id) desc,player.name asc ;"

Q9 = "select team_id ,count(goal_id)*100.0/(select count(goal_id) from goaldetails) as pre_goal from goaldetails group by goaldetails.team_id;"

Q10 = "select avg(avg_goal) from  (select count(goal_id) as avg_goal from goaldetails group by goaldetails.team_id);"

Q11 = "select player_id,player.name,date_of_birth from player where not exists (select player_id from goaldetails where player.player_id = goaldetails.player_id group by player_id having count(goal_id) <> 0);"

Q12 = "select team.name, match.match_no,match.audience,match.audience-(select avg(audience) from matchteamdetails inner join match on match.match_no = matchteamdetails.match_no where team.team_id = matchteamdetails.team_id  group by matchteamdetails.team_id) from matchteamdetails inner join team on team.team_id = matchteamdetails.team_id inner join match on match.match_no = matchteamdetails.match_no; "
