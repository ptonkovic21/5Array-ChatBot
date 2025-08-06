# Dobrodošli

Na ovom repozitoriju se nalazi jednostavan robot za razgovor koji koristi RAG pristup kao primarni izvor informacija. Glavni model koji se koristi je deepseek-llm-7b-chat.

# Potrebne specifikacije

Bilo koji 8Gb GPU <br>
16Gb - RAM <br>
20Gb slobodnog prostora <br>

Moguće je pokrenuti na ovim specifikacijama:
gtx 1650 4Gb - GPU <br>
16Gb RAM <br>
Ryzen 5 4000 Series - CPU <br>
Ali performanse su jako spore i potrebno je do 4 min za odgovor.

# Dodatne informacije

Potrebni paketi i biblioteke koje se koriste u projektu su:

| Naziv biblioteke      | Dokumentacija                                                                                                                      |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| langchain_community   | [https://python.langchain.com/api_reference/community/index.html](https://python.langchain.com/api_reference/community/index.html) |
| transformers          | [https://huggingface.co/docs/transformers/en/index](https://huggingface.co/docs/transformers/en/index)                             |
| torch                 | [https://pypi.org/project/torch/](https://pypi.org/project/torch/)                                                                 |
| faiss-cpu             | [https://pypi.org/project/faiss-cpu/](https://pypi.org/project/faiss-cpu/)                                                         |
| faiss-gpu             | [https://pypi.org/project/faiss-gpu/#description](https://pypi.org/project/faiss-gpu/#description)                                 |
| sentence-transformers | [https://sbert.net/](https://sbert.net/)                                                                                           |
| accelerate            | [https://huggingface.co/docs/accelerate/en/index](https://huggingface.co/docs/accelerate/en/index)                                 |

Skupovi podataka su prošireni i generirani uz pomoć ChatGPT-a kako bi se ubrzao proces izgradnje aplikacije.

| Početni izgled podataka                                                                                                                                                                              | Izgled nakon proširenja uz ChatGPT                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Marko <br> --Birthday is on 9.01.2002 <br> --Favorite color is yellow <br> --Pet name is Bruice <br> --Favorite thing is playing games <br> --Favorite food is pasta <br> --Favorite drink is Sprite | Marko <br> Marko was born on January 9th, 2002. <br> His favorite color is yellow. <br> He has a pet named Bruice. <br> In his free time, Marko enjoys playing games. <br> He loves pasta and drinks Sprite as his favorite beverage. |
