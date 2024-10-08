# evabird
WIP projects using Cornell University's [eBird APIs](https://documenter.getpostman.com/view/664302/S1ENwy59) for birdwatching data

## Local development

1. Clone this repo.
1. Optionally create a new Python virtual environment.
1. Run `pip install -r requirements.txt` to install dependencies.
1. Go to https://ebird.org/api/keygen and copy your eBird API key.
1. Run `export API_KEY=your-api-key-here` to set the key as an environment variable.
1. Run `flask --debug run` to start the application.

## Used in this project

* [Cornell eBird API 2.0](https://documenter.getpostman.com/view/664302/S1ENwy59)
* [Flask](https://github.com/pallets/flask)
* [Requests](https://requests.readthedocs.io/en/latest/)