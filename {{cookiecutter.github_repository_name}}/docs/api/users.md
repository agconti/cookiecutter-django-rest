# Users
Supports registering, viewing, and updating user accounts.

## Register a new user account

**Request**:

`POST` `users/`

*Note:*

- *Not* **Authorization Protected**


**Response**:

```json
Content-Type application/json
201 Created

{
  "id": 1,
  "first_name": "Richard",
  "last_name": "Hendriks",
  "auth_token": "fFBGRNJru1FQd44AzqT3Zg",
  "email": "hendriks@piepiper.com"
}
```
## Get a user's profile information

**Request**:

`GET` `users/:id`

Parameters:

Name | Type | Description
---|---|---
id | integer | The id associated with the user object.


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": 1,
  "first_name": "Richard",
  "last_name": "Hendriks",
  "auth_token": "fFBGRNJru1FQd44AzqT3Zg",
  "email": "hendriks@piepiper.com"
}
```

## Get a user's profile information

**Request**:

`GET` `users/:id`

Parameters:

Name | Type | Description
---|---|---
id | integer | The id associated with the user object.


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": 1,
  "first_name": "Richard",
  "last_name": "Hendriks",
  "auth_token": "fFBGRNJru1FQd44AzqT3Zg",
  "email": "hendriks@piepiper.com"
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
email | string | The new email of the user object.


*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": 1,
  "first_name": "Richard",
  "last_name": "Hendriks",
  "auth_token": "fFBGRNJru1FQd44AzqT3Zg",
  "email": "hendriks@piepiper.com"
}
```
