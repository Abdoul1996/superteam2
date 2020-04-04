# Coffee Shop Community Library (CSCL)
## Getting Started
### Requirements:
- Python3
- pip3
- [Docker](https://docs.docker.com/install/)
- [docker-compose](https://docs.docker.com/compose/install/)

### Installation:
`pip3 install -r requirements.txt`  

If using a virtual development environment i.e. `virtualenv`:
```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Docker & Docker-Compose
Docker containers are used to facilitate local development. Using docker-compose you can run a local environment which contains a MongoDB database that is bootstrapped with 1,000 book records.

#### Commands
| Command | Description |
|:---|---|
| `docker-compose up` | Start the local development environment |
| `docker-compose down` | Stop the local development environment. Keeps the data volume so changes to the database persist. |
| `docker-compose down -v` | Stop the local development environment. Delete the database data volume. Useful when wanting to start from scratch. |
| `docker-compose exec mongo bash` | Start a bash shell within the running mongodb container. |

Once up and running, you can access your local api by going to http://127.0.0.1:5000.

#### Mongo
The development database is called `cscl`
The authentication information is:
- Username: `cscl`
- Password: `SuperSecret`
- Authentication Database: `cscl`

### Environment Variables
Environment variables allow you to configur your application environment. These values will be passed to the API and can be retrieved by using `os.get_env` (See `cscl_api/config.py` for an example).

| Variable | Description |
|---|---|
| FLASK_APP | Name of application that the Flask development server should start. This should be the name of your Python package relative to your current directory. i.e `cscl_api`|
| FLASK_ENV | Environment type that FLask should be running in. `development` enables Debug and should only be used for local development. `production` disables debug and is appropriate for a production build. |
| CSCL_MONGO_URL | URL to MongoDB server. Must start with `mongodb://` |
| CSCL_MONGO_USER | Username to use when authenticating MongoDB server.|
| CSCL_MONGO_PASS | Password to use when authentication with MongoDB server. |
| CSCL_CORS_DOMAINS | List of domains that can access the API. By default all sources are allowed. *Advanced Topic* |

## API
The CSCL API is a simple API which allows users (frontend clients), to interact with the data records stored within MongoDB
### Parameters
Below is a description of parameters that will be rerferenced in the [Endpoints](#Endpoints) section.
- `isbn`: Book ID which is passed in the request URI
- `title`: Book title
- `author`: First author of book
- `publication_year`: Year that book was published
- `image_url_s`: Link to small/thumbnail image of book
- `image_url_m`: Link to medium image of book
- `image_url_l`: Link to large image of

### Endpoints
#### /book/\<isbn\>
HTTP Method: GET  
Parameters: 
- `isbn`: Book ID which is passed in the request URI
Returns:
- A book record

example: 
```
<Request>
GET myapi.com/book/123456

<Response>
{
    "isbn": 123456,
    "title": "my little book",
    "author": "Me, Myself and I",
    "publication_year": 2009,
    "image_url_s": "someurl.com/1s",
    "image_url_m": "someurl.com/1m",
    "image_url_m": "someurl.com/1l",
}
```

#### /book/
HTTP Method: PUT  
Parameters (Body):
- `isbn`
- `title`
- `author`
- `publication_year`
- `image_url_s`
- `image_url_m`
- `image_url_l`


example:
```
<Request>
PUT myapi.com/book
{
    "isbn": 99999999,
    "title": "Newest Book",
    "author": "Orlando Miami",
    "publication_year": 2019,
    "image_url_s": "someurl.com/00000s",
    "image_url_m": "someurl.com/123232m",
    "image_url_m": "someurl.com/2ff2f31l",
}

<Response>
Created Ok
```

#### /books
HTTP Method: GET  
Url Parameters:
- p: Pagination page number
- c: Number of results to return per page

example:
```
<Request>
GET myapi.com/books?c=2&p=1

<Response>
[
    {
        "isbn": 000001,
        "title": "First book",
        "author": "Some author",
        "publication_year": 2005,
        "image_url_s": "someurl.com/000001s",
        "image_url_m": "someurl.com/000001m",
        "image_url_m": "someurl.com/000001l",
    },
    {
        "isbn": 000002,
        "title": "Another book",
        "author": "Same author",
        "publication_year": 2005,
        "image_url_s": "someurl.com/000002s",
        "image_url_m": "someurl.com/000002m",
        "image_url_m": "someurl.com/000002l",
    },

]
```