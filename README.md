# HireDjango
A reverse job board for Django developers.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)

## Want To Contribute? => Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

**Working on your first Pull Request?** You can learn how from this *free* series [How to Contribute to an Open Source Project on GitHub](https://kcd.im/pull-request)

### Prerequisites & Installing

This is running on python 3.8 and Django 4. To get started create a virtual environment and install the packages from requirements.txt. Remember to migrate the db changes to your local machine

```
pip install -r requirements.txt
python manage.py migrate
```

Currently the local env uses sqlite db and the production app uses PostreSQL.

Email verification for new users is done locally within the terminal.

Static files are served in prod by Digital Ocean static sites

Media (user uploaded) files are served in prod by Digial Ocean Spaces (S3)

User auth is handled by the django-allauth package (email signup - new users req to verify email)

### Project & Apps

Config is the main project folder

Accounts handles the custom user model

Jobs handles the freelancer/business functionality


### Seeding data

When first starting you will want to create a superuser. and also some fake accounts for developers and businesses.

A custom user model is used. Each Freelancer or Business is tied to a user via a OneToOne relationship.

## Running the tests

Right now tests still need to be implemented..

## Production

The live site is deployed to Digital Ocean. Once a commit is made to Master it is auto deployed.

## Built With

* [Django](https://docs.djangoproject.com/) - The web framework used

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/vacchiano/HireDjango/blob/master/LICENSE) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Also create a free developer profile if you haven't yet!