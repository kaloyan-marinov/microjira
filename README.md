[![workflows_run-test-suite](https://github.com/kaloyan-marinov/rename/actions/workflows/run-test-suite.yml/badge.svg)](https://github.com/kaloyan-marinov/rename/actions/workflows/run-test-suite.yml)

# Common setup

There is nothing to set up.

# Options for serving the application and issuing requests to it

1. Using `localhost` (= the local network interface) to serve the Flask application:

    ```
    $ python3 --version
    Python 3.8.3

    $ python3 -m venv venv
    $ source venv/bin/activate
    (venv) $ pip install --upgrade pip
    (venv) $ pip install -r requirements.txt
    ```

    ```
    (venv) $ pytest \
        --cov=application \
        --cov-report=term-missing \
        --cov-branch \
        test*
    ```

    ```
    # Launch one terminal instance and, in it, start serving the application:

    (venv) $ FLASK_APP=application.py flask run
    ```

    ```
    # Launch a second terminal instance and, in it, issue requests to the application:

    $ curl localhost:5000/api/health-check | json_pp
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
    100    26  100    26    0     0   1018      0 --:--:-- --:--:-- --:--:--  3714
    {
      "health-check" : "passed"
    }
    ```

2. Using Docker to serve both the persistence layer and the Flask application:

    ```
    $ DB_ENGINE_HOSTNAME=container-mini-jira-mysql docker compose \
        --env-file .env \
        config
    
    $ DB_ENGINE_HOSTNAME=container-mini-jira-mysql docker compose \
        --env-file .env \
        build
    
    $ DB_ENGINE_HOSTNAME=container-mini-jira-mysql docker compose \
        --env-file .env \
        up
    ```

    ```
    $ curl localhost:5000/api/health-check | json_pp
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
    100    26  100    26    0     0    220      0 --:--:-- --:--:-- --:--:--   433
    {
      "health-check" : "passed"
    }

    $ curl localhost:5000/api/projects | json_pp
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
    100    16  100    16    0     0    139      0 --:--:-- --:--:-- --:--:--   177
    {
      "projects" : []
    }

    $ curl \
      -X POST \
      -H "Content-Type: application/json" \
      -d '{"name": "Build a basic web application using Flask"}' \
      localhost:5000/api/projects \
      | json_pp
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
    100   113  100    60  100    53    642    567 --:--:-- --:--:-- --:--:--  1793
    {
      "id" : 1,
      "name" : "Build a basic web application using Flask"
    }

    $ curl localhost:5000/api/projects | json_pp
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
    100    68  100    68    0     0    945      0 --:--:-- --:--:-- --:--:--  2720
    {
      "projects" : [
          {
            "id": 1,
            "name" : "Build a basic web application using Flask"
          }
      ]
    }
    ```
