# Liaar

A simple tool to create a fake REST API


##How to use?

You should create directories as resources’ namespace and place JSON files inside them as API methods.

Suppose you have following directory structure:

```
apps
     |_ .
     |_ ..
     |_ blog
             |_ .
             |_ ..
             |_ setting.json
             |_ resources
                          |_ .
                          |_ ..
                          |_ users
                                   |_ .
                                   |_ ..
                                   |_ profile.json
```

And the url would be `http://127.0.0.1:1234/blog/v1/users/profile`. In next parts you can read more about resource and application setting JSON file's format.

##Schema

In order to run the application, you should define application’s setting and resources using JSON files.
This section shows you the schema of these JSON files.

###setting.json: Application setting

Using this file you can define global properties for the application. The `setting.json` can have following properties:

####Mandatory
- version {string} - Version number of application


###Application resources
Using this file you define application's resources. This JSON file can have as many as fields you need and each value can be either `string` or `object`. Following JSON file is an example of a resource:

          {
            "firstName": "first_name",
            "lastName": "last_name",
            "username": "user_name",
            "email": {
              "type": "list",
              "count": 3,
              "formatter": "email"
            }
          }


##Requirements

- Python v2.7
- Twisted v14.0
- Faker v0.4.0

##Thanks

##License
MIT
