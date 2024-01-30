# Casual

## Installation

1. Create a virtual environment and activate it.

       ❯ python3 -m venv venv
       ❯ . ./venv/bin/activate

2. Create the initial env files to run Casual.

       ❯ flask core init -d

3. Check and modify the three new files `dev_casual.conf`, `.env`, and `.flaskenv`.

   The most important one is `dev_casual.conf` where you should check the following keys:
  - `SECRET_KEY`
  - `ALCHEMICAL_DATABASE_URL`
  - `CASUAL_ADMINS` before you go to the next step!.
  - `MAIL_*` you will need this to safely create the user accounts and communicate with the users.
  - `CASUAL_*` in general.

4. Create the DB Migrations infrastructure, the first migration, and apply it.
   
       ❯ flask db init
       ❯ flask db migrate
       ❯ flask db upgrade

5. Create the Admin Accounts according to the `CASUAL_ADMIN` key in the conf file (see step 3).
   
       ❯ flask auth create-admins

6. Now you can run the development server and conform that you can log in + change the password from the default value of `Casual` to a more secure one.

   Each admin account will be forced to change the password on the first successful login.