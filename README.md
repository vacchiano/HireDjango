# HireDjango
A reverse job board for Django developers.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites & Installing

This is running on python 3.8 and Django 4. To get started create a virtual environment and install the packages from requirements.txt. Remember to migrate the db changes to your local machine

```
pip install -r requirements.txt
python manage.py migrate
```

Currently the local env uses sqlite db and the production app uses PostreSQL.

### Seeding data

When first starting you will want to create a superuser. and also some fake accounts for developers and businesses.

## Running the tests

Right now tests still need to be implemented..

## Deployment

The live site is deployed to Digital Ocean. Once a commit is made to Master it is auto deployed.

## Built With

* [Django](http://www.dropwizard.io/1.0.2/docs/) - The web framework used

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Also create a free developer profile if you haven't yet!