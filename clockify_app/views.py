import datetime

from django.shortcuts import render
from clockify_app.models import Project, Task, User
import requests

import os
from dotenv import load_dotenv

load_dotenv()


def get_all_data(request):
    api_key = os.getenv('API_KEY')
    data_for_headers = {'x-api-key': api_key}
    response_workspace = requests.get('https://api.clockify.me/api/v1/workspaces', headers=data_for_headers)
    data_workspace = response_workspace.json()

    for i in range(len(data_workspace)):
        response_user = requests.get(f'https://api.clockify.me/api/v1/workspaces/{data_workspace[i]["id"]}/users',
                                     headers=data_for_headers)
        data_users = response_user.json()
        for j in range(len(data_users)):
            user_data = User(
                name=data_users[j]['name'],
                email=data_users[j]['email'],
                status=data_users[j]['status'],
                id=data_users[j]['id']
            )

            user_data.save()

        response_project = requests.get(
            f'https://api.clockify.me/api/v1/workspaces/{data_workspace[i]["id"]}/projects',
            headers=data_for_headers)
        data_projects = response_project.json()
        for j in range(len(data_projects)):
            response_task = requests.get(
                f'https://api.clockify.me/api/v1/workspaces/{data_workspace[i]["id"]}/projects/{data_projects[j]["id"]}/tasks',
                headers=data_for_headers)
            data_tasks = response_task.json()

            all_tasks = Task.objects.all()
            response_time = requests.get(
                f'https://api.clockify.me/api/v1/workspaces/{data_workspace[i]["id"]}/user/{data_users[j]["id"]}/time-entries',
                headers=data_for_headers)
            data_time = response_time.json()

            for k in range(len(data_tasks)):
                for t in range(len(data_time)):
                    if data_tasks[k]['id'] == data_time[t]['taskId']:
                        start_time = data_time[t]["timeInterval"]["start"]
                        print(str(start_time).split('T')[0])
                        print(type(str(start_time).split('T')[0]))
                        print(type(start_time))
                        start_date = str(start_time).split('T')[0]
                        end_time = data_time[t]["timeInterval"]["end"]
                        end_date = str(end_time).split('T')[0]
                        duration = str(datetime.datetime.strptime(end_time,
                                                                  '%Y-%m-%dT%H:%M:%SZ') - datetime.datetime.strptime(
                            start_time, '%Y-%m-%dT%H:%M:%SZ'))
                        project_id = data_time[t]['projectId']
                task_data = Task(
                    name=data_tasks[k]['name'],
                    status=data_tasks[k]['status'],
                    id=data_tasks[k]['id'],
                    duration=duration,
                    end_time=end_time,
                    start_time=start_time,
                    end_date=end_date,
                    start_date=start_date,
                    project_name=project_id
                )
                task_data.save()
                for l in data_tasks[k]['assigneeIds']:
                    task_data.assignees.add(User.objects.get(id=l))

        project_data = Project(
            name=data_projects[j]['name'],
            archived=data_projects[j]['archived'],
            public=data_projects[j]['public'],
            id=data_projects[j]['id']
        )
        project_data.save()

        all_tasks = Task.objects.all()
        for l in all_tasks:
            project_data.tasks.add(Task.objects.get(id=l))

        for p in range(len(data_projects)):
            tasks = Task.objects.all().filter(project_name=data_projects[p]['id'])
            for task in tasks:
                task.project_name = data_projects[p]['name']
                task.save()

