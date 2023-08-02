SELECT h.hacker_id,h.name
FROM Hackers h,Difficulty d,Challenges c,Submissions s
WHERE h.hacker_id = s.hacker_id and d.score = s.score and c.challenge_id = s.challenge_id and d.difficulty_level = c.difficulty_level
GROUP BY h.hacker_id,h.name
HAVING COUNT(c.challenge_id)>1
ORDER BY COUNT(s.challenge_id) DESC,h.hacker_id ASC;
