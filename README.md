# Meme Generator (Flask + Docker)

Preprost spletni Meme Generator, ki omogoča:
- nalaganje slike
- dodajanje zgornjega in spodnjega teksta
- generiranje mema
- prikaz mema v brskalniku

## Tehnologije
- Python 3.12
- Flask
- Pillow
- Docker

## Docker zagon

### Build:
docker build -t meme-generator .

### Run:
docker run -p 5000:5000 meme-generator

Aplikacija bo dostopna na:
http://localhost:5000
