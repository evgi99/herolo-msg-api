# herolo-msg-api

small project that demonstrate Dockerizing Flask with Postgres. 
The flask rest-api app connected to a postgres server running on the host. 
Our application had a two Docker containers that combined to one docker-compose.yml which define that flask server is depend on postgres db service.

## How to run:

1. `git clone` the project and cd to project file directory
2. Install [Docker](https://docs.docker.com/install/), if you don't already have it,
3. Build the image and once the image is built, run the container:
```
$ sudo docker-compose up -d 
```
4. check that two services up:
```
$ sudo docker ps 
```
5. create and init database table:
```
$ sudo docker-compose exec server python manage.py db upgrade 
```
6. go to your favorite api tester. (like postman)
i used [Talend API Tester](https://chrome.google.com/webstore/detail/talend-api-tester-free-ed/aejoelaoggembcahagimdiliamlcdmfm) - chrome extension

## supported APIs

### add message

``` [HTTP POST] http://localhost:8000/api/add_message```

with body like attached below 

```
{
  "subject":"msg subject",
  "sender":"corona",
  "receiver": "evgeni",
  "content":"conantent of msg"
}
```
will add this message to message db table with status 'unread' and return information that message added succsefuly and the msg_id

``` { "Response": "msg added. msg id=1" }```

### read message
```[HTTP GET] http://localhost:8000/api/get_message/1```

will mark message with id 1 as read and return all message info:

```
{
"msg":{
    "creation_date": "03/06/2020 11:54:10",
    "id": 1,
    "msg_content": "content of zero msg",
    "receiver": "evgeni",
    "sender": "eva",
    "subject": "msg_subject_to_pg25"
  }
}
```

### list all my messages
```[HTTP GET] http://localhost:8000/api/get_my_messages/evgeni```

will return list of all messages where the receiver are 'evgeni'
```
[
 {
  "creation_date": "03/06/2020 11:54:02",
  "id": 1,
  "content":"conantent of msg",
  "receiver": "evgeni",
  "sender": "corona",
  "subject": "msg_subject"
  },
  {
  "creation_date": "03/06/2020 11:54:10",
  "id": 2,
  "content":"conantent of msg",
  "receiver": "evgeni",
  "sender": "ronen",
  "subject": "msg_subject_2"
  }
]
```
### list all my unread messages
```[HTTP GET] http://localhost:8000/api/get_my_unread_messages/evgeni```

will return list of all messages where the receiver are 'evgeni' and thier status is 'unread'
```
[
  {
  "creation_date": "03/06/2020 11:54:10",
  "id": 2,
  "content":"conantent of msg",
  "receiver": "evgeni",
  "sender": "ronen",
  "subject": "msg_subject_2"
  }
]
```
### delete message
```[HTTP DELETE] http://localhost:8000/api/delete_message/1```

will delete message where id = '1' return information that message deleted succsefuly and the msg_id

``` { "Response": "msg added. msg id=1" }```

