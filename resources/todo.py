from flask import request
from flask_restful import Resource
from http import HTTPStatus

import models.todo
from models.todo import Todo, todo_list

class TodoListResource(Resource):
     def get(self):
          data=[]

          for todo in todo_list:
               data.append(todo.data)

          return {'data' : data}, HTTPStatus.OK

     def post(self):
          data = request.get_json()

          todo = Todo(
               betreff=data['betreff'],
               beschreibung=data['beschreibung'],
               termin=data['termin'],
               firma=data['firma'],
               projekt=data['projekt'],
               sammelaufgabe=data['sammelaufgabe'],
               status=data['status']
          )
          todo.save()
          return todo.data, HTTPStatus.CREATED

class TodoResource(Resource):
     def get(self, todo_id):
          todo = next((todo for todo in todo_list if todo.id == todo_id),None)

          if todo is None:
                return {'message' : 'Todo nicht gefunden !'}, HTTPStatus.NOT_FOUND

          return todo.data, HTTPStatus.OK

     def delete(self, todo_id):
          todo = next((todo for todo in todo_list if todo.id == todo_id), None)

          if todo is None:
               return {'message': 'Todo nicht gefunden !'}, HTTPStatus.NOT_FOUND

          todo_list.remove(todo)
          return {}, HTTPStatus.NO_CONTENT

     def post(self, todo_id):
          data = request.get_json()

          todo = next((todo for todo in todo_list if todo.id == todo_id), None)

          if todo is None:
               return {'message': 'Todo nicht gefunden !'}, HTTPStatus.NOT_FOUND

          todo.betreff = data['betreff']
          todo.beschreibung = data['beschreibung']
          todo.termin = data['termin']
          todo.firma = data['firma']
          todo.projekt = data['projekt']
          todo.sammelaufgabe = data['sammelaufgabe']

          return todo.data, HTTPStatus.OK

class TodoStatus_inArbeit(Resource):
     def put(self, todo_id):
          todo = next((todo for todo in todo_list if todo.id == todo_id), None)

          if todo is None:
               return {'message': 'Todo nicht gefunden !'}, HTTPStatus.NOT_FOUND

          todo.status = "in Arbeit"
          return {},HTTPStatus.OK

