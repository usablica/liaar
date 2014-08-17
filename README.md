# Liaar

Create fake REST API in a minute

<p align="center"><img src='http://usablica.github.io/liaar/images/pinocchio.jpg' /></p>


##Install

Issue following command:

     pip install liaar
     
or with `easy_install`:

     easy_install liaar

Above commands install all dependecies automatically. Then use following command to run the liaar:

    liaar

Then you should see the liaar picture.

##How to use

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

Following JSON file shows an example of `setting.json`:

     {
       "version": "1"
     }


###Application resources
Using this file you define application's resources. This JSON file can have as many as fields you need and each value can be either `string` or `object`. Following JSON file is an example of a resource:

          {
            "firstName": "first_name",
            "lastName": "last_name",
            "username": "user_name"
          }

The output of above resource file is:  

     {
       "firstName": "Polk",
       "lastName": "Nienow",
       "username": "kbogan"
     }


If you need a list of values instead of a single value, you can use nested object like following:

     {
       "firstName": "first_name",
       "lastName": "last_name",
       "username": "user_name",
       "email": {
         "liaar_type": "list",
         "liaar_count": 3,
         "liaar_formatter": "email"
       }
     }

And then the output of above JSON file would be:

     {
       "username": "kbogan",
       "lastName": "Nienow",
       "email": ["darcie.pfannerstill@mohr.com", "barton.elvira@haneoconnell.com", "imills@hotmail.com"],
       "firstName": "Polk"
     }


Liaar uses [Faker](http://www.joke2k.net/faker/) library to generate fake data for API methods. You can use all Faker's formatters to produce fake data. Following list shows current available formatters to use in Liaar:

**file**:

     mime_type                   # video/webm

**user_agent**:

     chrome                      # Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_4) AppleWebKit/5341 (KHTML, like Gecko) Chrome/13.0.803.0 Safari/5341
     firefox                     # Mozilla/5.0 (Windows 95; sl-SI; rv:1.9.1.20) Gecko/2012-01-06 22:35:05 Firefox/3.8
     internet_explorer           # Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.1)
     linux_platform_token        # X11; Linux x86_64
     linux_processor             # x86_64
     mac_platform_token          # Macintosh; U; PPC Mac OS X 10_7_6
     mac_processor               # U; PPC
     opera                       # Opera/9.41 (Windows CE; it-IT) Presto/2.9.168 Version/12.00
     safari                      # Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.34.4 (KHTML, like Gecko) Version/5.0 Safari/534.34.4
     user_agent                  # Mozilla/5.0 (iPod; U; CPU iPhone OS 3_2 like Mac OS X; en-US) AppleWebKit/531.15.3 (KHTML, like Gecko) Version/4.0.5 Mobile/8B119 Safari/6531.15.3
     windows_platform_token      # Windows 98; Win 9x 4.90


**phone_number**:

     phone_number                # (593)652-1880


**miscelleneous**:

     random_number               # 3438
     random_digit                # 3
     boolean                     # True
     country_code                # BB
     language_code               # fr
     locale                      # pt_GN
     md5                         # ab9d3552b5c6e68714c04c35725ba73c
     null_boolean                # True
     sha1                        # 3fc2ede28f2596050f9a94c15c59b800175409d0
     sha256                      # f06561a971d6b1306ecef60be336556d6de2540c2d0d2158f4d0ea3f212cd740


**internet**:

     company_email               # ggreenfelder@ortizmedhurst.com
     domain_name                 # mayer.com
     domain_word                 # gusikowski
     email                       # gbrakus@johns.net
     free_email                  # abbey60@yahoo.com
     free_email_domain           # hotmail.com
     ipv4                        # 81.132.249.71
     ipv6                        # 4c55:8c8b:54b5:746d:44ed:c7ab:486a:a50e
     safe_email                  # amalia49@example.com
     slug                        # TypeError
     tld                         # net
     uri                         # http://www.parker.com/
     uri_extension               # .asp
     uri_page                    # terms
     uri_path                    # explore/list/app
     url                         # http://dubuque.info/
     user_name                   # goodwin.edwin

**company**:

     bs                          # maximize end-to-end infrastructures
     catch_phrase                # Multi-tiered analyzing instructionset
     company                     # Stanton-Luettgen
     company_suffix              # Group

**date_time**:

     am_pm                       # AM
     century                     # IX
     date                        # 1985-02-17
     date_time                   # 1995-06-08 14:46:50
     date_time_ad                # 1927-12-17 23:08:46
     date_time_between           # 1999-08-22 22:49:52
     date_time_this_century      # 1999-07-24 23:35:49
     date_time_this_decade       # 2008-01-27 01:08:37
     date_time_this_month        # 2012-11-12 14:13:04
     date_time_this_year         # 2012-05-19 00:40:00
     day_of_month                # 23
     day_of_week                 # Friday
     iso8601                     # 2009-04-09T21:30:02
     month                       # 03
     month_name                  # April
     time                        # 06:16:50
     timezone                    # America/Noronha
     unix_time                   # 275630166
     year                        # 2002

**person**:

     first_name                  # Elton
     last_name                   # Schowalter
     name                        # Susan Pagac III
     prefix                      # Ms.
     suffix                      # V

**address**:

     address                     # 044 Watsica Brooks West Cedrickfort, SC 35023-5157
     building_number             # 319
     city                        # Kovacekfort
     city_prefix                 # New
     city_suffix                 # ville
     country                     # Monaco
     geo_coordinate              # 148.031951
     latitude                    # 154.248666
     longitude                   # 109.920335
     postcode                    # 82402-3206
     secondary_address           # Apt. 230
     state                       # Nevada
     state_abbr                  # NC
     street_address              # 793 Haskell Stravenue
     street_name                 # Arvilla Valley
     street_suffix               # Crescent

**lorem**

     paragraph                   # Itaque quia harum est autem inventore quisquam eaque. Facere mollitia repudiandae
                                          qui et voluptas. Consequatur sunt ullam blanditiis aliquam veniam illum voluptatem.
     paragraphs                  # ['Alias porro soluta eum voluptate. Iste consequatur qui non nam.',
                                             'Id eum sint eius earum veniam fugiat ipsum et. Et et occaecati at labore
                                             amet et. Rem velit inventore consequatur facilis. Eum consequatur consequatur
                                             quis nobis.', 'Harum autem autem totam ex rerum adipisci magnam adipisci.
                                             Qui modi eos eum vel quisquam. Tempora quas eos dolorum sint voluptatem
                                             tenetur cum. Recusandae ducimus deleniti magnam ullam adipisci ipsa.']
     sentence                    # Eum magni soluta unde minus nobis.
     sentences                   # ['Ipsam eius aut veritatis iusto.',
                                             'Occaecati libero a aut debitis sunt quas deserunt aut.',
                                             'Culpa dolor voluptatum laborum at et enim.']
     text                        # Dicta quo eius possimus quae eveniet cum nihil. Saepe sint non nostrum.
                                          Sequi est sit voluptate et eos eum et. Pariatur non sunt distinctio magnam.
     word                        # voluptas
     words                       # ['optio', 'et', 'voluptatem']



##Roadmap
- Allow cross-domain XHR request
- Better error handling
- Add URL format to `setting.json`


##Requirements

- Python v2.7
- Twisted v14.0
- Faker v0.4.0


##Thanks

 - [Mohammad Efazati](https://github.com/efazati)
 - [Amir Mohammad Said](https://github.com/amir)
 - http://investingcaffeine.com/ for Pinocchio picture


## Author
**Afshin Mehrabani**

- [Twitter](https://twitter.com/afshinmeh)
- [Github](https://github.com/afshinm)
- [Personal page](http://afshinm.name/)


##License
MIT
