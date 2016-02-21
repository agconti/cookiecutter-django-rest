# Users
Supports registering, viewing, and updating user accounts.

## Register a new user account

**Request**:

`POST` `users/`

Parameters:

Name     | Type   | Description
---------|--------|---
username | string | The username for the new user.
password | string | The password for the new user (plaintext).

*Note:*

- *Not* **Authorization Protected**


**Response**:
If a User with given `username` doesn't exist, you'll get a 201:

```json
Content-Type application/json
201 Created

{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "username": "richard",
  "password": "pbkdf2_sha256$24000$aGozcCr6QXhv$WCgPt2voqVO+Nno2flVnNnLcfks6Yq8XJyxoadB/r50=",
  "auth_token": "132cf952e0165a274bf99e115ab483671b3d9ff6"
}
```

else if the `username` is already taken, you'll get a 400:

```json
Content-Type application/json
400 Bad Request

{
    "username": [
        "A user with that username already exists."
    ]
}
```


## Get a user's profile information

**Request**:

`GET` `users/:id`

Parameters:

Name | Type   | Description
-----|--------|---
id   | string | The id associated with the user object.


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "username": "richard",
  "first_name": "Richard",
  "last_name": "Hendriks"
}
```


## Update your profile information

**Request**:

`PUT/PATCH` `users/:id`

Parameters:

Name | Type | Description
---|---|---
first_name | string | The new first_name of the user object.
last_name | string | The new last_name of the user object.


*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "username": "richard",
  "first_name": "Richard",
  "last_name": "Hendriks"
}
```
