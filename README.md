
# The Los Pollos Hermanos API

> "I am not in danger, Skyler. I am the danger. A guy opens his door and gets shot, and you think that of me? No. I am the one who knocks!"

And this API is the one that *answers*.

Welcome to the digital distribution center for the Heisenberg empire. This Go API is the backbone of the **Heisenberg Stack**, serving up piping hot data on every character, quote, and shady connection from the world of Breaking Bad.

Our product is 99.1% pure data, cooked up with the finest ingredients:

- **The Cook**: Go & 
- **The Formula**: A SQLite database
- **The Intel**: Scraped directly from the source with beautifulSoup

## The Special Offer: "Six Degrees of Saul Goodman"

Ever wonder how Jesse Pinkman is connected to Lydia Rodarte-Quayle? Our star feature lets you find out. Using a sophisticated graph algorithm (BFS), we can calculate the shortest chain of connections between any two characters. No more guessing—just pure, calculated chemistry.

## API Menu

All orders are placed at the `/api/v1` counter.

*   `GET /characters`
    **The Roster**: Get a list of every player in the game.

*   `GET /characters/:name`
    **The Dossier**: Get the detailed file on a specific individual.
    *Example: `/api/v1/characters/Gus%20Fring`*

*   `GET /quotes/random`
    **Words of Wisdom**: Get a random, memorable quote from the series.

*   `GET /connections?from=...&to=...`
    **Connect the Dots**: The main event. Find the path between two characters.
    *Example: `/api/v1/connections?from=Walter%20White&to=Gale%20Boetticher`*

## Fire Up the Lab

Ready to get cooking?

1.  **Get the Keys:**
    `git clone <your-repo-url> && cd breaking-bad-api`

2.  **Gather Supplies:**
    `go mod tidy`

3.  **Start the Business:**
    `go run ./cmd/api/main.go`

The server will be open for business at `http://localhost:8080`. Tread lightly.

