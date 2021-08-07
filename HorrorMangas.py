from bs4 import BeautifulSoup
import requests

url = 'https://rehnwriter.com/book-recommendations/33-terrifying-horror-manga/'
response = requests.get(url)

markup = BeautifulSoup(response.text, "html.parser")
content = markup.find(class_='entry-content').find_all('h2')

for i in content:
    print(i.text)

''' 
Results:
TOP 33 HORROR MANGAS 
Scraped FROM 'https://rehnwriter.com/book-recommendations/33-terrifying-horror-manga/

33. God’s Left Hand, Devil’s Right Hand

32. The Kurosagi Corpse Delivery Service

31. Manhole

30. Pet Shop of Horrors

29. Domu: A Child’s Dream

28. Ajin

27. Hideout

26. Heads

25. I Am a Hero

24. Zashiki Onna

23. Ibitsu

22. The Promised Neverland

21. Shiga Hime

20. The Laughing Vampire

19. Mr. Arashi’s Amazing Freak Show

18. Lychee Light Club

17. Parasyte

16. Attack on Titan

15. Franken Fran

14. Mieruko-chan

13. Goth

12. Tokyo Ghoul

11. The Shadow Out of Time

10. Ichi the Killer

9. Fuan no Tane

8. Kouishou Rajio

7. Dorohedoro

6. Homunculus

5. Kamisama no Iutoori and Kamisama no Iutoori Ni

4.Gantz

3. Uzumaki

2. Blame!

1. Berserk
'''