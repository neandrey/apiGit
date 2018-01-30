import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


#создание вызовов API и сохранение ответов.
url = 'https://api.github.com/search/repositories?q=language:python &sort=star'
r = requests.get(url)
print("status code: ", r.status_code)

#Сохранение ответов API в переменной.
response_dict = r.json()
print(response_dict.keys())
print("Total repositories: ", response_dict['total_count'])

names, stars = [],[]
#анализ информации о репозиториях
repo_dicts = response_dict['items']

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#построение визуализации
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend = False)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')

# анализ первого репозитория
# repo_dict = repo_dicts[0]
# print("\nKeys: ", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
